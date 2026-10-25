# Skill Atlas

An English, source-grounded catalog for choosing between Matt Pocock's skills and Poteto's pstack workflows.

Live site: **[Skill Atlas](https://holive.github.io/skill-atlas/)**. This source-grounded compilation remains open to human calibration. No skills are installed or executed by the catalog.

## Start here

Open [the interactive guide and local search](index.html) directly in a browser. It is a self-contained HTML file with basic styling and no server or network requirement. Choose one of 10 goals and answer up to two discriminating follow-ups. Results explain one suggested next skill or reference, a concrete next step, prerequisites, scope, and a conditional alternative. Backtracking preserves test notes and unfinished feedback.

Search names, tasks and expected results locally, with related English and Portuguese terms and collection/lifecycle filters. All 96 entries are browsable; experimental/specialized entries and principles are explicit opt-ins. Keyword matches are candidates, not execution authorization. Feedback records the skill the user would choose (or none), stays in this browser, and can be downloaded as JSON.

The interface and catalog are in English. `catalog/navigation.json` owns goal-selection rules. `catalog/search-terms.json` owns the curated search vocabulary. The shared resolver and keyword matcher live in `tools/navigation-core.js`, used by both the page and offline checks. `tools/page-template.html` owns the interface; `tools/render_page.py` embeds the shared data and logic into `index.html`. Normal catalog rendering rebuilds the page too. The original binary routes remain an archived comparison baseline, not the active UI rules.

| Read | Purpose |
| --- | --- |
| [Compilation report](docs/COMPILATION.md) | Findings, scope, strategy and what still needs calibration. |
| [Decision guide](docs/DECISION-GUIDE.md) | Goal-first selection with 35 explained recommendations. |
| [Version 2 notes](docs/V2.md) | Changes, module-testing case, verification and limits. |
| [Complete catalog](docs/CATALOG.md) | All 96 source-grounded skill cards, requirements, effects and evidence. |
| [Composition and differences](docs/COMPARISON.md) | Eight material distinctions and conditional composition notes. |
| [Recompilation procedure](docs/RECOMPILE.md) | How to repeat this process every 14 days after validation. |

## Snapshot

- **Matt:** 38 skills, of which 27 are in the promoted engineering/productivity buckets, 7 are beta and 4 are misc/unpromoted.
- **Poteto:** 58 pstack skills, comprising 34 workflows/routers/utilities and 24 principles.
- **Supporting material:** full Matt repository; pstack and cursor-team-kit directories plus repository root files from cursor/plugins. Cursor-team-kit is dependency context, not a third primary collection.
- Exact source commits, source-file hashes and interpreted-artifact hashes are preserved in [the inventory](catalog/source-inventory.json) and [the analysis lock](analysis/source-lock.json).
- All primary SKILL.md files were read. All 23 Poteto mode playbooks and selected references informed interpretation. Supporting scripts were not executed or exhaustively audited.

## Working model

The agent interprets sources into a persisted catalog. Local tools inventory files, join those interpretations, validate structural integrity and render readable documents. Tools do not infer intent or replace the source-reading phase.

Start with the desired outcome. Narrow by context, scope and host requirements. Compare a primary workflow with an explained alternative; attach principles and references only where relevant. Names such as `matt/tdd` are catalog identities, not host command syntax.

English JSON is the common data source for the static page and local keyword search. Embeddings remain deferred until real situations show that they would improve discovery.

## Verify offline

Verification requires Python 3.10+, Node.js and Git. The generated HTML itself needs only a browser. No package installation or AI API is needed.

```bash
python3 tools/catalog.py validate
python3 tools/verify.py
python3 tools/render_catalog.py
```

`compile` joins the agent-authored interpretations with the inventory and refuses an outdated interpretation lock. It does not generate new interpretations.

```bash
python3 tools/catalog.py compile
```

The [validation report](catalog/validation.json) retains 22 baseline routing checks and adds 35 version 2 goal scenarios and seven search checks, plus source integrity, evidence bounds, compatibility notes, missing-context handling, stale-source rejection and deterministic rendering. Browser checks cover all 35 guided outcomes, local search, filters, changed answers, notes and feedback saving. These checks do not establish semantic truth, improved real-user selection success or host execution compatibility.

## Provenance and attribution

Sources: [mattpocock/skills](https://github.com/mattpocock/skills) and [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack). Both downloaded collections carry MIT licenses. Copyright and license texts are preserved under `sources/` and `licenses/`; see [third-party notices](THIRD_PARTY_NOTICES.md).

Maintenance is active **every 14 days**, through a Codex scheduled follow-up in the original chat. The agent reads changed upstream sources, reinterprets and verifies the catalog, then pushes passing updates. The local Mac and Codex app must be available for that maintenance run. GitHub Pages serves the published snapshot independently of the local computer. See [maintenance configuration](maintenance.json) and [the rebuild procedure](docs/RECOMPILE.md).

## Hosting and clean-checkout verification

The public repository is [holive/skill-atlas](https://github.com/holive/skill-atlas). Pushing `main` or manually running the Pages workflow restores the exact reviewed source revisions, runs the complete checks, and publishes only the HTML and attribution files. The workflow never interprets new upstream content; that is the scheduled agent's job. Failed checks leave the previous deployment available.

```bash
python3 tools/restore_sources.py
python3 tools/verify.py
python3 tools/package_site.py
```

`restore_sources.py` preserves existing source directories and refuses mismatched revisions or inventories. `fetch_sources.py` is the separate tool for fetching new upstream candidates. Source clones, candidate runs and archived internal reviews are excluded from Git.
