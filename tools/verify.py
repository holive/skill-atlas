#!/usr/bin/env python3
"""Run offline source, routing and stale-input regression checks."""
import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path

import catalog

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--sources-dir", type=Path, default=ROOT / "sources")
args = parser.parse_args()
cat = catalog.read(ROOT / "catalog/skills.json")
inv = catalog.read(ROOT / "catalog/source-inventory.json")
routes = catalog.read(ROOT / "catalog/routes.json")
index = {entry["id"]: entry for entry in cat["skills"]}
result = catalog.validate(cat, inv, routes, args.sources_dir)
assert catalog.inventory(args.sources_dir) == inv, "Source snapshot drifted"

# Newer Git renders a zero UTC offset as Z; both spellings must restore identical facts.
original_git = catalog.git
def git_with_zulu_time(source, *arguments):
    value = original_git(source, *arguments)
    if arguments == ("show", "-s", "--format=%cI", "HEAD") and value.endswith("+00:00"):
        return value[:-6] + "Z"
    return value
try:
    catalog.git = git_with_zulu_time
    assert catalog.inventory(args.sources_dir) == inv, "Equivalent UTC timestamps changed the source inventory"
finally:
    catalog.git = original_git

scenarios = catalog.read(ROOT / "catalog/scenarios.json")["scenarios"]
outcomes_seen = set()
for case in scenarios:
    outcome = catalog.route(routes, case["answers"])
    assert outcome.get("outcome_id") == case["expected_outcome"], case["scenario"]
    assert set(case["required_candidates"]) <= set(outcome["candidates"]), case["scenario"]
    outcomes_seen.add(outcome["outcome_id"])
assert outcomes_seen == set(routes["outcomes"]), "A recommendation has no scenario coverage"
assert catalog.route(routes, {})["question_id"] == "software", "Missing context became an answer"
assert routes["outcomes"]["course"]["candidates"] == ["matt/teach"]
assert routes["outcomes"]["plain_teaching"]["candidates"] == ["poteto/teach"]
assert "Not explicitly specified" not in index["matt/tdd"]["interpretation"]["confirmation"]
assert set(cat["duplicate_names"]) == {"tdd", "teach"}, "Revisit duplicate-name decisions"

notes = catalog.read(ROOT / "catalog/compatibility.json")["notes"]
compatibility_evidence = 0
for note in notes:
    assert all(sid in index for sid in note["skills"]), note["id"]
    assert note["evidence"], note["id"]
    for evidence in note["evidence"]:
        path = args.sources_dir / evidence["collection"] / evidence["path"]
        assert path.is_file(), evidence
        assert 1 <= evidence["start_line"] <= evidence["end_line"] <= len(path.read_text().splitlines()), evidence
        compatibility_evidence += 1


def rejects(call, name):
    try:
        call()
    except ValueError:
        return name
    raise AssertionError(f"Invalid input was accepted: {name}")


negative = []
bad = copy.deepcopy(cat)
bad["skills"].pop()
negative.append(rejects(lambda: catalog.validate(bad, inv, routes, args.sources_dir), "missing skill"))
bad = copy.deepcopy(cat)
bad["skills"][0]["interpretation"]["companions"].append("matt/nonexistent")
negative.append(rejects(lambda: catalog.validate(bad, inv, routes, args.sources_dir), "unknown companion"))
bad = copy.deepcopy(cat)
bad["skills"][0]["interpretation"]["evidence"][0]["start_line"] = 0
negative.append(rejects(lambda: catalog.validate(bad, inv, routes, args.sources_dir), "invalid evidence range"))
bad_routes = copy.deepcopy(routes)
bad_routes["questions"]["software"]["answers"]["yes"] = "software"
negative.append(rejects(lambda: catalog.validate_routes(bad_routes, index), "cyclic decision graph"))
bad_routes = copy.deepcopy(routes)
bad_routes["outcomes"]["course"]["candidates"] = ["matt/chief-of-staff"]
negative.append(rejects(lambda: catalog.validate_routes(bad_routes, index), "experimental default recommendation"))
bad_inv = copy.deepcopy(inv)
bad_inv["sources"]["matt"]["commit"] = "0" * 40
negative.append(rejects(lambda: catalog.validate_interpretation_lock(bad_inv), "stale interpretation source"))

same = catalog.changes(inv, inv)
assert not same["requires_full_reinterpretation"]
assert not same["added"] and not same["removed"]
changed = copy.deepcopy(inv)
changed["sources"]["matt"]["files"].append({"path": "shared-policy.md", "sha256": "new reference", "bytes": 10, "type": "file"})
diff = catalog.changes(inv, changed)
assert not diff["changed_skill_files"], "Reference-only change was misclassified"
assert diff["requires_full_reinterpretation"], "Reference-only change failed to invalidate interpretations"
assert "shared-policy.md" in diff["changed_source_files"]["matt"]

analyses = [ROOT / "analysis" / name for name in ["matt.json", "poteto-workflows.json", "poteto-principles.json"]]
assert catalog.compile_catalog(inv, analyses) == cat, "Catalog does not rebuild exactly from locked inputs"
render_command = [sys.executable, str(ROOT / "tools/render_catalog.py")]
subprocess.run(render_command, check=True, capture_output=True, text=True)
rendered_paths = [ROOT / "docs" / name for name in ["CATALOG.md", "DECISION-GUIDE.md", "COMPARISON.md"]]
rendered_paths.append(ROOT / "index.html")
first_render = {p.name: catalog.digest(p.read_bytes()) for p in rendered_paths}
subprocess.run(render_command, check=True, capture_output=True, text=True)
assert first_render == {p.name: catalog.digest(p.read_bytes()) for p in rendered_paths}, "Rendering is not reproducible"
subprocess.run(["node", str(ROOT / "tools/verify_navigation.js")], check=True)

report = {
    **result, "scenario_checks": len(scenarios), "outcomes_covered": len(outcomes_seen),
    "compatibility_notes": len(notes), "compatibility_evidence": compatibility_evidence,
    "rejected_invalid_inputs": negative, "missing_context_preserved": True,
    "reference_only_change_invalidates_analysis": True, "unchanged_snapshot_is_noop": True,
    "deterministic_catalog_rebuild": True, "canonical_utc_commit_dates": True, "deterministic_rendered_documents": 3,
    "deterministic_html_page": True,
    "goal_navigation": catalog.read(ROOT / "catalog/navigation-validation.json"),
    "human_calibration": "pending; these checks do not establish subjective recommendation quality or host execution compatibility",
}
catalog.write(ROOT / "catalog/validation.json", report)
print(json.dumps(report, indent=2))
