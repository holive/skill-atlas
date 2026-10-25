#!/usr/bin/env python3
"""Restore exact reviewed snapshots for a clean checkout; never follow upstream HEAD."""
import argparse
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
if catalog.inventory(destination) != expected:
    raise ValueError("Restored source inventory differs from the reviewed snapshot")
print("Restored exact reviewed sources; no upstream code was executed.")
