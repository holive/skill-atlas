#!/usr/bin/env python3
"""Render the reviewed JSON data as a readable English Markdown catalog."""
import collections
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
(ROOT / "docs").mkdir(exist_ok=True)
catalog = json.loads((ROOT / "catalog/skills.json").read_text())
routes = json.loads((ROOT / "catalog/routes.json").read_text())


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


parts = ["# Skill catalog", "", "Agent interpretations of pinned upstream sources. Selection aid only; downloading a skill does not install or invoke it. Human calibration is pending.", "", "Qualified IDs identify the collection; they are catalog identities, not promises about host slash-command syntax.", ""]
for author in ["matt", "poteto"]:
    entries = [entry for entry in catalog["skills"] if entry["facts"]["collection"] == author]
    parts += [f"## {author.title()} · {len(entries)} skills", "", "| ID | Role | Catalog status | Useful result |", "| --- | --- | --- | --- |"]
    for entry in entries:
        f, i = entry["facts"], entry["interpretation"]
        parts.append(f"| [{entry['id']}]({f['source_url']}) | {i['kind']} | {f['status']} | {cell(i['summary'])} |")
    parts.append("")
parts += ["## Detailed cards", "", "Use cases, boundaries and roles below are compiler interpretations. Evidence links point to exact upstream revisions. Effects are possible actions of the described workflow, not permissions granted by the catalog.", ""]
for entry in catalog["skills"]:
    f, i = entry["facts"], entry["interpretation"]
    parts += [f"### {entry['id']}", "", i["summary"], "", f"- **Role / status:** {i['kind']} / {f['status']}.", f"- **Use when:** {'; '.join(i['when_to_use'])}", f"- **Scope limits:** {'; '.join(i['avoid_when'])}", f"- **Result:** {'; '.join(i['outputs'])}", f"- **Requirements:** {'; '.join(i['requirements']) or 'None explicitly stated in the interpreted source.'}", f"- **Possible effects:** {', '.join(i['effects']) or 'None classified.'}", f"- **Confirmation behavior:** {i['confirmation']}", f"- **Explicit companions/references:** {', '.join(i['companions']) or 'None recorded.'}"]
    for evidence in i["evidence"]:
        url = f"{catalog['sources'][f['collection']]['repository']}/blob/{f['snapshot_commit']}/{evidence['path']}#L{evidence['start_line']}-L{evidence['end_line']}"
        parts.append(f"- **Evidence:** [{evidence['path']}:{evidence['start_line']}–{evidence['end_line']}]({url}) — {evidence['supports']}")
    parts.append("")
(ROOT / "docs/CATALOG.md").write_text("\n".join(parts))
navigation = json.loads((ROOT / "catalog/navigation.json").read_text())
guide = ["# Goal-first decision guide (version 2)", "", "Choose the intended result before answering follow-up questions. The guide returns one source-grounded suggestion, its prerequisites, a next action, and conditional alternatives. Search the complete catalog when no goal fits. The original binary routes remain in catalog/routes.json as a comparison baseline.", "", "## Goals", "", "| Goal | Intended result | First question |", "| --- | --- | --- |"]
for goal in navigation["goals"]:
    guide.append(f"| {cell(goal['label'])} | {cell(goal['description'])} | {goal['start']} |")
guide += ["", "## Follow-up questions", ""]
for qid, question in navigation["questions"].items():
    guide += [f"### {qid}: {question['question']}", "", question["hint"], ""]
    guide += [f"- {choice['label']} → `{choice['next']}`" for choice in question["choices"]]
    guide.append("")
guide += ["## Recommendations", ""]
for oid, result in navigation["outcomes"].items():
    guide += [f"### {oid}: {result['title']}", "", f"**Suggested next:** {result['primary']}", "", result["why"], "", f"**Do next:** {result['next_step']}", "", f"**Scope:** {result['boundary']}", ""]
    guide += [f"- Prerequisite: {item}" for item in result["prerequisites"]]
    if result["alternative"]:
        guide += [f"- Alternative: {result['alternative']['id']} — {result['alternative']['when']}"]
    if result["playbook"]:
        guide += [f"- Poteto mode playbook: {result['playbook']}"]
    guide += [f"- Conditional support: {item['id']} — {item['when']}" for item in result["support"]]
    guide.append("")
(ROOT / "docs/DECISION-GUIDE.md").write_text("\n".join(guide))
notes = json.loads((ROOT / "catalog/compatibility.json").read_text())
comparison = ["# Composition and differences", "", notes["status"], ""]
for note in notes["notes"]:
    comparison += [f"## {note['id']}", "", f"**Compare:** {', '.join(note['skills'])}", "", note["interpretation"], ""]
    for evidence in note["evidence"]:
        source = catalog["sources"][evidence["collection"]]
        url = f"{source['repository']}/blob/{source['commit']}/{evidence['path']}#L{evidence['start_line']}-L{evidence['end_line']}"
        comparison += [f"- [{evidence['collection']}/{evidence['path']}:{evidence['start_line']}–{evidence['end_line']}]({url}): {evidence['supports']}"]
    comparison.append("")
(ROOT / "docs/COMPARISON.md").write_text("\n".join(comparison))
subprocess.run([sys.executable, str(ROOT / "tools/render_page.py")], check=True)
print(f"Rendered {len(catalog['skills'])} skill cards and {len(routes['outcomes'])} decision outcomes.")
