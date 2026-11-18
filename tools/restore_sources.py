#!/usr/bin/env python3
"""Restore exact reviewed snapshots for a clean checkout; never follow upstream HEAD."""
import argparse
import json
import re
import subprocess
from pathlib import Path
import catalog

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--destination", type=Path, default=ROOT / "sources")
args = parser.parse_args()
destination = args.destination.resolve()
expected = catalog.read(ROOT / "catalog/source-inventory.json")
for author, config in catalog.COLLECTIONS.items():
    source = expected["sources"][author]
    if source["repository"] != config["repository"] or not re.fullmatch(r"[0-9a-f]{40}", source["commit"]):
        raise ValueError("Unexpected source repository or revision")
    target = destination / author
    if target.exists():
        if catalog.git(target, "rev-parse", "HEAD") != source["commit"]:
            raise ValueError(f"Existing source has another revision: {author}; preserve it and use a new destination")
        continue
    target.mkdir(parents=True)
    def git(*arguments):
        subprocess.run(["git", "-C", str(target), *arguments], check=True)
    git("init", "--quiet")
    git("remote", "add", "origin", config["repository"] + ".git")
    if author == "poteto":
        git("sparse-checkout", "init", "--cone")
        git("sparse-checkout", "set", "pstack", "cursor-team-kit")
    git("fetch", "--depth", "1", "origin", source["commit"])
    git("checkout", "--detach", "FETCH_HEAD")
actual = catalog.inventory(destination)
if actual != expected:
    differences = {"sources": {}, "skills": []}
    for author in expected["sources"]:
        before, after = expected["sources"][author], actual["sources"][author]
        old_files = {item["path"]: item for item in before["files"]}
        new_files = {item["path"]: item for item in after["files"]}
        changes = {key: {"expected": before[key], "actual": after.get(key)} for key in before if key != "files" and before[key] != after.get(key)}
        changes["missing_files"] = sorted(old_files.keys() - new_files.keys())[:10]
        changes["extra_files"] = sorted(new_files.keys() - old_files.keys())[:10]
        changes["changed_files"] = [path for path in old_files.keys() & new_files.keys() if old_files[path] != new_files[path]][:10]
        differences["sources"][author] = changes
    old_skills = {item["id"]: item for item in expected["skills"]}
    new_skills = {item["id"]: item for item in actual["skills"]}
    for sid in sorted(old_skills.keys() | new_skills.keys()):
        before, after = old_skills.get(sid, {}), new_skills.get(sid, {})
        if before != after:
            differences["skills"].append({"id": sid, "fields": {key: {"expected": before.get(key), "actual": after.get(key)} for key in before.keys() | after.keys() if before.get(key) != after.get(key)}})
    print(json.dumps(differences, indent=2))
    raise ValueError("Restored source inventory differs from the reviewed snapshot")
print("Restored exact reviewed sources; no upstream code was executed.")
