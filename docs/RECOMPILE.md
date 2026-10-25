# Repeat the compilation

Maintenance is scheduled every 14 days through the original Codex chat, with standing user authorization to publish passing updates to GitHub Pages. Agent-led interpretation runs locally and requires the Mac and Codex app to be available. The public site remains available independently. See `maintenance.json` for the automation identifier.

## Inputs and ownership

The source repositories own skill behavior. `analysis/*.json` contains agent judgments. `catalog/routes.json` and `catalog/compatibility.json` contain curator decisions. `catalog/scenarios.json` owns the explicit expected routing examples. Generated `catalog/skills.json` and `docs/CATALOG.md` are derived artifacts.

Version 2 uses `catalog/navigation.json` for active goal-selection rules and `catalog/search-terms.json` for local keyword vocabulary. `catalog/navigation-cases.json` records regression examples. `tools/navigation-core.js` is the shared executable resolver/matcher for the browser and offline checks. Keep the original binary graph as a comparison baseline; update the active guide explicitly rather than silently substituting one for the other.

Use [the compilation contract](../analysis/CONTRACT.md) for record fields and [the agent prompt](COMPILATION-PROMPT.md) for the next interpretation run. Keep host authorization separate from every upstream autonomy statement.

## 1. Preserve the baseline and fetch a candidate

Create a fresh run directory such as `runs/2026-11-07/`. Copy the current `tools/` into that run's `tools/`. Copy the contract and scenario/route drafts as candidate inputs. Do not overwrite the accepted baseline or advance its source checkouts.

From the workspace root, download fresh snapshots:

```bash
python3 tools/fetch_sources.py --destination runs/2026-11-07/sources
python3 runs/2026-11-07/tools/catalog.py inventory
python3 tools/catalog.py diff --old catalog/source-inventory.json --new runs/2026-11-07/catalog/source-inventory.json
```

The downloader refuses an existing destination. It downloads Git data and selected source files only; it does not execute upstream scripts, install skills or invoke their procedures. Interrupted downloads can be retained for diagnosis; choose a new candidate directory on retry.

Completion criterion: both source commits are pinned, all primary files are discovered, the source working trees are clean and a complete candidate inventory exists.

## 2. Interpret the candidate sources

In version 1, any downloaded content change triggers a full reread of the primary skill files and re-evaluation of material shared references, routing and composition. This deliberately avoids a fragile dependency-invalidation shortcut. Record the new commits even when content is unchanged; identical content may reuse interpretations with refreshed provenance.

Split research into Matt, Poteto workflows and Poteto principles, then consolidate. Read the files rather than only the READMEs. Follow links when they define material behavior; record unknown requirements explicitly. Include new, removed, beta and misc files appropriately. Preserve qualified IDs and investigate renames instead of assuming same-name behavior is unchanged.

Completion criterion: one complete source-cited record per current primary SKILL.md; all source changes and relevant consumers considered; routing and comparison notes reconciled. Never claim every auxiliary file was audited unless it was.

## 3. Lock the new interpretation

Only after the reread and consolidation, write the candidate's `analysis/source-lock.json` with the inventory's exact commits/tree hashes and SHA-256 hashes of the three interpretation arrays, routes, compatibility notes and scenarios. Follow the baseline lock's shape. The lock is an audit and stale-input guard, not proof that source reading occurred.

Do not update the lock merely to make a failing compile pass. Source changes require interpretation; curation changes require checking the affected decisions and scenarios.

## 4. Compile, verify and render

Run these inside the candidate directory:

```bash
python3 tools/catalog.py compile
```

After compiling the candidate catalog, reconcile all active navigation IDs, recommendations, prerequisites, alternatives and search aliases with that catalog. Update the candidate's `analysis/navigation-lock.json` only after reviewing the curation. It binds the exact compiled catalog hash and the three navigation/search data artifacts. The HTML generator refuses stale curation inputs. Preserve pending human-calibration status.

Then run:

```bash
python3 tools/verify.py
python3 tools/render_catalog.py
```

Verification uses Node.js for the same resolver/matcher embedded in the generated page. Include the real module-isolation task, its analysis-only variant, settled specification writing, local search, lifecycle filters and no-match behavior. Recheck browser interactions when the UI changes.

Repeat compile/render without changing inputs and compare output bytes. Retain the detailed verification report after the last verification run. The restricted frontmatter reader handles the forms in the baseline sources and fails on unsupported forms; update and verify the reader when upstream introduces a new form.

Completion criterion: structural checks, all curated scenarios, negative cases, evidence checks and reproducibility pass. New skills and changed recommendation boundaries must have appropriate scenario coverage. A passing structural validator cannot certify a new interpretation's semantic correctness.

## 5. Calibrate and promote

For the initial strategy, have the user try five real scenarios. For later runs, inspect new/changed recommendations and preserve feedback as scenarios. Produce a short change report: added/removed skills, changed scope/approval/effects, changed questions, unresolved uncertainty and exact sources.

Keep the previous accepted snapshot intact until the candidate is accepted under the user's standing instructions. The user has authorized this recurring recompilation and publication. Commit and push only the verified project changes to `main`, then verify the Pages workflow and public HTML. Do not overwrite unrelated local changes. If sources are unchanged, preserve the published snapshot without a redundant commit. A failed fetch, unsupported metadata, missing interpretation, source drift or failed scenario leaves the previous accepted catalog available.

Completion criterion: the candidate's state is explicit (candidate, accepted, or blocked with a concrete reason); the previous accepted artifacts remain recoverable; future automation can rerun the same documented process.
