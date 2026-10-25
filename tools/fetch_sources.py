#!/usr/bin/env python3
"""Download fresh upstream snapshots into a new directory; never update a baseline."""
import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--destination", type=Path, required=True)
args = parser.parse_args()
destination = args.destination.resolve()
if destination.exists():
    parser.error("Destination already exists. Choose a fresh snapshot directory.")
destination.mkdir(parents=True)
subprocess.run(["git", "clone", "--depth", "1", "https://github.com/mattpocock/skills.git", str(destination / "matt")], check=True)
subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", "https://github.com/cursor/plugins.git", str(destination / "poteto")], check=True)
subprocess.run(["git", "-C", str(destination / "poteto"), "sparse-checkout", "set", "pstack", "cursor-team-kit"], check=True)
print(f"Downloaded source snapshots into {destination}. No upstream code was executed.")
