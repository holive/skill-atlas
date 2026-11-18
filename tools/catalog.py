#!/usr/bin/env python3
"""Inventory frozen sources, join agent interpretations, and validate a catalog offline."""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    "matt": {"repository": "https://github.com/mattpocock/skills", "scope": "skills", "license": "LICENSE"},
    "poteto": {"repository": "https://github.com/cursor/plugins", "scope": "pstack/skills", "license": "pstack/LICENSE"},
}
KINDS = {"router", "workflow", "reference", "principle", "setup", "utility", "teaching"}
INTENTS = {"clarify", "plan", "implement", "debug", "review", "research", "design", "test", "write", "learn", "handoff", "operate", "improve", "setup"}
EFFECTS = {"read", "local_write", "external_write", "execute", "delegate", "configure"}


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_bytes(path):
    return os.readlink(path).encode() if path.is_symlink() else path.read_bytes()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def scalar(value):
    # Parse only the scalar forms used by the frozen collections; reject new forms.
    value = value.strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'"):
        if not value.endswith("'"):
            raise ValueError("Unterminated single-quoted metadata")
        return value[1:-1].replace("''", "'")
    if value in {"true", "false"}:
        return value == "true"
    if value in {"|", ">", "|-", ">-"}:
        raise ValueError("Multiline metadata needs explicit parser support before compiling")
    return value


def metadata(path):
    text = path.read_text()
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter: {path}")
    result = {}
    lines = match[1].splitlines()
    for offset, line in enumerate(lines):
        field = re.match(r"^(name|description|disable-model-invocation):\s*(.*)$", line)
        if field:
            if field[2] in {">-", "|-"}:
                block = []
                for continuation in lines[offset + 1:]:
                    if not continuation.startswith("  "):
                        break
                    assert_true(continuation.strip(), f"Multiline paragraph metadata needs parser support: {path}")
                    block.append(continuation[2:])
                assert_true(block, f"Empty multiline metadata: {path}")
                result[field[1]] = (" " if field[2] == ">-" else "\n").join(block)
            else:
                result[field[1]] = scalar(field[2])
    if not all(isinstance(result.get(k), str) and result[k] for k in ["name", "description"]):
        raise ValueError(f"Missing name/description: {path}")
    if "disable-model-invocation" in result and not isinstance(result["disable-model-invocation"], bool):
        raise ValueError(f"Invalid invocation flag: {path}")
    return result


def inventory(sources):
    source_records, skills = {}, []
    for author, config in COLLECTIONS.items():
        root = sources / author
        if git(root, "status", "--porcelain"):
            raise ValueError(f"Downloaded source has modifications: {author}")
        commit = git(root, "rev-parse", "HEAD")
        files = []
        # Hash every tracked file available in the downloaded scope, including references.
        tracked = subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"]).decode().split("\0")
        for rel in sorted(filter(None, tracked)):
            p = root / rel
            if not p.exists() and not p.is_symlink():
                continue
            if p.is_symlink() or p.is_file():
                data = source_bytes(p)
                files.append({"path": rel, "sha256": digest(data), "bytes": len(data), "type": "symlink" if p.is_symlink() else "file"})
        source_records[author] = {
            **config, "commit": commit, "commit_time": datetime.fromisoformat(git(root, "show", "-s", "--format=%cI", "HEAD").replace("Z", "+00:00")).isoformat(timespec="seconds"),
            "snapshot_tree_sha256": digest(json.dumps(files, sort_keys=True).encode()),
            "downloaded_scopes": ["entire repository"] if author == "matt" else ["pstack", "cursor-team-kit", "repository root files"],
            "supporting_collection": None if author == "matt" else "cursor-team-kit (dependency context, not a primary catalog collection)",
            "files": files,
        }
        for path in sorted((root / config["scope"]).rglob("SKILL.md")):
            meta = metadata(path)
            rel = path.relative_to(root).as_posix()
            group = path.relative_to(root / config["scope"]).parts[0] if author == "matt" else "pstack"
            status = "experimental" if group == "in-progress" else "specialized" if group == "misc" else "deprecated" if group == "deprecated" else "stable"
            own_files = sorted(p for p in path.parent.rglob("*") if p.is_file())
            own_hashes = [{"path": p.relative_to(root).as_posix(), "sha256": digest(source_bytes(p))} for p in own_files]
            skills.append({
                "id": f"{author}/{meta['name']}", "collection": author, "name": meta["name"],
                "description": meta["description"], "declared_disable_model_invocation": meta.get("disable-model-invocation"),
                "upstream_group": group, "status": status, "path": rel,
                "source_url": f"{config['repository']}/blob/{commit}/{rel}",
                "skill_sha256": digest(path.read_bytes()), "bundle_sha256": digest(json.dumps(own_hashes, sort_keys=True).encode()),
                "line_count": len(path.read_text().splitlines()),
                "snapshot_commit": commit,
            })
    ids = [s["id"] for s in skills]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate names within a collection need an identity migration")
    return {"schema_version": 1, "sources": source_records, "skills": skills}


def compile_catalog(inv, analyses):
    validate_interpretation_lock(inv)
    interpreted = []
    for path in analyses:
        interpreted.extend(read(path))
    ids = [x["id"] for x in interpreted]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate interpretation IDs")
    index = {x["id"]: x for x in interpreted}
    wanted = {x["id"] for x in inv["skills"]}
    if set(index) != wanted:
        raise ValueError(f"Coverage mismatch: missing={wanted - set(index)}, extra={set(index) - wanted}")
    records = []
    for facts in inv["skills"]:
        interpretation = dict(index[facts["id"]])
        interpretation.pop("id")
        interpretation["provenance"] = "Agent interpretation of the pinned source, not an upstream-authored classification."
        interpretation["review_status"] = "source-grounded; human calibration pending"
        records.append({"id": facts["id"], "facts": facts, "interpretation": interpretation})
    names = collections.defaultdict(list)
    for record in records:
        names[record["facts"]["name"]].append(record["id"])
    return {
        "schema_version": 1, "language": "en", "compilation_status": "initial compilation; structurally validated; human calibration pending",
        "cadence": {"interval_days": 14, "schedule_reference": "maintenance.json"},
        "installation": "Source download only. This catalog does not install or invoke skills.",
        "sources": {author: {k: v for k, v in config.items() if k != "files"} for author, config in inv["sources"].items()},
        "duplicate_names": {k: v for k, v in names.items() if len(v) > 1},
        "skills": records,
    }


def validate_interpretation_lock(inv):
    lock = read(ROOT / "analysis/source-lock.json")
    expected = {author: {key: source[key] for key in ["commit", "snapshot_tree_sha256"]} for author, source in inv["sources"].items()}
    assert_true(lock["sources"] == expected, "Interpretations belong to another source snapshot; reread changed sources before updating the analysis lock")
    required = {"analysis/matt.json", "analysis/poteto-workflows.json", "analysis/poteto-principles.json", "catalog/routes.json", "catalog/compatibility.json", "catalog/scenarios.json"}
    assert_true(set(lock["artifacts"]) == required, "Interpretation lock omits a required artifact")
    for rel, expected_hash in lock["artifacts"].items():
        assert_true(digest((ROOT / rel).read_bytes()) == expected_hash, f"Interpretation changed since its source lock: {rel}")


def assert_true(value, message):
    if not value:
        raise ValueError(message)


def validate(cat, inv, routes, sources):
    validate_interpretation_lock(inv)
    index = {x["id"]: x for x in cat["skills"]}
    assert_true(set(index) == {x["id"] for x in inv["skills"]}, "Catalog does not cover the inventory")
    assert_true(len(index) == len(cat["skills"]), "Duplicate catalog IDs")
    for entry in cat["skills"]:
        sid, facts, interp = entry["id"], entry["facts"], entry["interpretation"]
        assert_true(facts in inv["skills"], f"Extracted facts changed for {sid}")
        assert_true(interp["kind"] in KINDS, f"Unknown kind: {sid}")
        assert_true(interp["intents"] and set(interp["intents"]) <= INTENTS, f"Invalid intents: {sid}")
        assert_true(set(interp["effects"]) <= EFFECTS, f"Invalid effects: {sid}")
        for field in ["when_to_use", "avoid_when", "outputs"]:
            assert_true(isinstance(interp[field], list) and interp[field] and all(isinstance(x, str) and x for x in interp[field]), f"Missing {field}: {sid}")
        for field in ["summary", "confirmation"]:
            assert_true(isinstance(interp[field], str) and interp[field], f"Missing {field}: {sid}")
        for companion in interp["companions"]:
            assert_true(companion in index, f"Unknown companion {companion}: {sid}")
        assert_true(interp["evidence"], f"Missing evidence: {sid}")
        assert_true(any(e["path"] == facts["path"] for e in interp["evidence"]), f"Missing own source citation: {sid}")
        for evidence in interp["evidence"]:
            rel = Path(evidence["path"])
            assert_true(not rel.is_absolute() and ".." not in rel.parts, f"Unsafe evidence path: {sid}")
            path = sources / facts["collection"] / rel
            assert_true(path.is_file(), f"Missing evidence file: {sid}: {path}")
            count = len(path.read_text().splitlines())
            assert_true(1 <= evidence["start_line"] <= evidence["end_line"] <= count, f"Invalid evidence lines: {sid}: {evidence}")
            assert_true(evidence.get("supports"), f"Evidence purpose missing: {sid}")
            expected = next((f["sha256"] for f in inv["sources"][facts["collection"]]["files"] if f["path"] == rel.as_posix()), None)
            assert_true(expected == digest(path.read_bytes()), f"Evidence source changed: {sid}: {rel}")
    validate_routes(routes, index)
    return {"status": "pass", "skills": len(index), "collections": dict(collections.Counter(x["facts"]["collection"] for x in index.values())), "evidence_references": sum(len(x["interpretation"]["evidence"]) for x in index.values()), "route_outcomes": len(routes["outcomes"]), "limits": ["Checks source coverage, integrity, line ranges and graph structure, not semantic truth.", "Scenario regression checks are separate from human calibration."]}


def validate_routes(routes, index):
    nodes, outcomes = routes["questions"], routes["outcomes"]
    assert_true(not (set(nodes) & set(outcomes)), "Question/outcome IDs overlap")
    for rid, result in outcomes.items():
        assert_true(result["candidates"], f"Empty recommendation: {rid}")
        for sid in result["candidates"] + result.get("support", []):
            assert_true(sid in index, f"Unknown route skill {sid}")
            assert_true(index[sid]["facts"]["status"] == "stable", f"Non-stable default recommendation: {sid}")
        assert_true(result.get("rationale") and result.get("constraints"), f"Unexplained route: {rid}")
    seen, active = set(), set()
    def visit(nid):
        assert_true(nid not in active, f"Cycle in decision graph at {nid}")
        assert_true(nid in nodes or nid in outcomes, f"Unknown node {nid}")
        if nid in seen:
            return
        seen.add(nid)
        if nid in outcomes:
            return
        active.add(nid)
        node = nodes[nid]
        assert_true(set(node["answers"]) == {"yes", "no"}, f"Non-binary question {nid}")
        for target in node["answers"].values():
            visit(target)
        active.remove(nid)
    visit(routes["start"])
    assert_true(seen == set(nodes) | set(outcomes), "Unreachable decision nodes")


def route(routes, answers):
    nid, trace = routes["start"], []
    while nid in routes["questions"]:
        node = routes["questions"][nid]
        if nid not in answers:
            return {"question_id": nid, "question": node["question"], "trace": trace}
        answer = answers[nid]
        assert_true(answer in {"yes", "no"}, f"Answer must be yes/no: {nid}")
        trace.append({"question_id": nid, "answer": answer})
        nid = node["answers"][answer]
    return {"outcome_id": nid, **routes["outcomes"][nid], "trace": trace}


def changes(old, new):
    a, b = {x["id"]: x for x in old["skills"]}, {x["id"]: x for x in new["skills"]}
    changed_files = {}
    for author in COLLECTIONS:
        before = {f["path"]: f["sha256"] for f in old["sources"][author]["files"]}
        after = {f["path"]: f["sha256"] for f in new["sources"][author]["files"]}
        changed_files[author] = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
    return {
        "added": sorted(b.keys() - a.keys()), "removed": sorted(a.keys() - b.keys()),
        "changed_skill_files": sorted(k for k in a.keys() & b.keys() if a[k]["skill_sha256"] != b[k]["skill_sha256"]),
        "changed_skill_bundles": sorted(k for k in a.keys() & b.keys() if a[k]["bundle_sha256"] != b[k]["bundle_sha256"]),
        "changed_source_files": changed_files,
        "requires_full_reinterpretation": any(changed_files.values()),
        "interpretation_policy": "Version 1 recompiles the full interpretation when any downloaded source content changes, including shared references, manifests and host adapters. Identical content may reuse judgments with refreshed provenance.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inventory", "compile", "validate", "route", "diff"])
    parser.add_argument("--sources-dir", type=Path, default=ROOT / "sources")
    parser.add_argument("--answers", default="{}")
    parser.add_argument("--old", type=Path)
    parser.add_argument("--new", type=Path)
    args = parser.parse_args()
    inv_path, cat_path, routes_path = ROOT / "catalog/source-inventory.json", ROOT / "catalog/skills.json", ROOT / "catalog/routes.json"
    if args.command == "inventory":
        inv = inventory(args.sources_dir)
        write(inv_path, inv)
        print(json.dumps({"skills": len(inv["skills"]), "commits": {k: v["commit"] for k, v in inv["sources"].items()}}))
    elif args.command == "compile":
        inv = read(inv_path)
        cat = compile_catalog(inv, [ROOT / "analysis" / name for name in ["matt.json", "poteto-workflows.json", "poteto-principles.json"]])
        result = validate(cat, inv, read(routes_path), args.sources_dir)
        write(cat_path, cat)
        write(ROOT / "catalog/validation.json", result)
        print(json.dumps(result))
    elif args.command == "validate":
        result = validate(read(cat_path), read(inv_path), read(routes_path), args.sources_dir)
        assert_true(inventory(args.sources_dir) == read(inv_path), "Snapshot inventory differs from downloaded sources")
        print(json.dumps(result))
    elif args.command == "route":
        print(json.dumps(route(read(routes_path), json.loads(args.answers)), indent=2))
    else:
        assert_true(args.old and args.new, "diff requires --old and --new inventory paths")
        print(json.dumps(changes(read(args.old), read(args.new)), indent=2))


if __name__ == "__main__":
    main()
