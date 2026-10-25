#!/usr/bin/env python3
"""Package the public page and required attribution, excluding source/review archives."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
destination = ROOT / "dist"
if destination.exists():
    shutil.rmtree(destination)
destination.mkdir()
shutil.copyfile(ROOT / "index.html", destination / "index.html")
shutil.copyfile(ROOT / "THIRD_PARTY_NOTICES.md", destination / "THIRD_PARTY_NOTICES.md")
shutil.copytree(ROOT / "licenses", destination / "licenses")
(destination / ".nojekyll").touch()
print("Public website packaged in dist/.")
