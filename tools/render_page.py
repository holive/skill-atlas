#!/usr/bin/env python3
"""Build a standalone, offline decision-tree page from the shared catalog."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "catalog/skills.json").read_text())
routes_bytes = (ROOT / "catalog/routes.json").read_bytes()
routes = json.loads(routes_bytes)
navigation_bytes = (ROOT / "catalog/navigation.json").read_bytes()
navigation = json.loads(navigation_bytes)
lock = json.loads((ROOT / "analysis/navigation-lock.json").read_text())
assert lock["catalog_sha256"] == hashlib.sha256((ROOT / "catalog/skills.json").read_bytes()).hexdigest(), "Navigation needs review against the changed catalog"
for relative, expected in lock["artifacts"].items():
    assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected, f"Navigation curation changed after its review lock: {relative}"
notes = json.loads((ROOT / "catalog/compatibility.json").read_text())["notes"]
data = {
    "routes": routes,
    "navigation": navigation,
    "vocabulary": json.loads((ROOT / "catalog/search-terms.json").read_text()),
    "skills": {entry["id"]: {
        "id": entry["id"],
        "source_url": entry["facts"]["source_url"],
        "collection": entry["facts"]["collection"],
        "status": entry["facts"]["status"],
        "interpretation": entry["interpretation"],
    } for entry in catalog["skills"]},
    "notes": notes,
    "sources": catalog["sources"],
    "snapshot": {
        "source_commits": {author: source["commit"] for author, source in catalog["sources"].items()},
        "routes_sha256": hashlib.sha256(routes_bytes).hexdigest(),
        "navigation_sha256": hashlib.sha256(navigation_bytes).hexdigest(),
        "navigation_version": 2,
        "search_terms_sha256": hashlib.sha256((ROOT / "catalog/search-terms.json").read_bytes()).hexdigest(),
        "shared_logic_sha256": hashlib.sha256((ROOT / "tools/navigation-core.js").read_bytes()).hexdigest(),
        "skill_count": len(catalog["skills"]),
    },
}
template = (ROOT / "tools/page-template.html").read_text()
assert template.count("__ATLAS_DATA__") == 1, "Expected one embedded data slot"
assert template.count("__ATLAS_CORE__") == 1, "Expected one shared logic slot"
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
(ROOT / "index.html").write_text(template.replace("__ATLAS_DATA__", payload).replace("__ATLAS_CORE__", (ROOT / "tools/navigation-core.js").read_text()))
print("Rendered standalone index.html; no network or server required.")
