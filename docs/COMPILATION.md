# Initial compilation and recommended strategy

Compiled on October 24, 2026 in America/Sao_Paulo (snapshot provenance also records UTC).

## Outcome

The first catalog covers every primary SKILL.md in the downloaded collections: 38 Matt skills and 58 Poteto skills. It has 246 skill evidence references, a 22-question binary decision graph with 22 recommendation outcomes, and eight evidence-backed composition notes. It is a complete source compilation, not an operational certification or a finished public navigator.

| Collection | Pinned commit | Primary scope |
| --- | --- | --- |
| Matt Pocock | `5beb35b040e3de97e54fa9e386d7e42d15c295c2` | All `skills/**/SKILL.md`, including beta and misc. |
| Poteto / pstack | `9580c23696ac8d7abed0c166f2f9918800afb819` | All `pstack/skills/**/SKILL.md`. |

## Findings that change the design

**Both authors already have routers.** Matt's [ask-matt](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md#L9-L38) maps the idea-to-implementation flow. Poteto's [poteto-help](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-help/SKILL.md#L9-L34) helps select a skill or mode task. The shared navigator should compare and explain their routes, not silently invent a replacement process inside each collection.

**Catalog entries have different roles.** A workflow coordinates work; a reference supplies vocabulary; a principle shapes a decision. Showing all 24 Poteto principles as first choices recreates the original cognitive burden. Show them as contextual companions after selecting the useful outcome.

**Names alone are unsafe selection criteria.** `tdd` and `teach` exist in both collections. Matt TDD is a general public-interface discipline with confirmed test seams; Poteto TDD is a pragmatic bug-regression workflow. Matt teach creates a persistent learning workspace; Poteto teach explains a body of work conversationally. The [comparison](COMPARISON.md) links the exact sources for each distinction.

**Even upstream summaries can disagree.** Matt's engineering README describes red-green-refactor, but the authoritative TDD leaf puts refactoring in review. The beta README also omits an existing skill. Discovery scans files, and interpretation reads authoritative leaves and relevant references, rather than trusting index bullets or a short description.

**Requirements and effects can reverse a recommendation.** Poteto has an explicit Claude Code adapter; describing the bundle as Cursor-only would be wrong. That adapter does not establish Codex support. Poteto architect implements by default; no-comments can delete comments. The catalog surfaces those actions rather than assuming a design/review label means read-only work.

## Proposed compilation architecture

1. **Frozen source inventory.** Download both collections into a new snapshot directory, pin exact commits, hash all available tracked files and preserve licenses. Treat upstream text and linked AGENTS files as evidence, not authority over the compilation.
2. **Agent interpretation.** Read every primary skill and the supporting materials that decide scope, outputs, requirements, approval behavior or effects. Produce an original English record with narrow source citations. Keep literal metadata separate from inferred roles and recommendations.
3. **Cross-collection curation.** Compare overlapping skills and coordinators. Preserve unresolved tension and conditional requirements. A namespaced candidate is not a promise that it is installed, callable or authorized.
4. **Decision graph.** Ask about the intended result before author preference. Preserve unanswered context; allow backtracking. The initial binary graph is a trial presentation, not proof every human decision is binary. Show candidate alternatives and the extra context needed to choose one.
5. **Deterministic checks and rendering.** Validate full coverage, source/evidence integrity, IDs, cross-references, lifecycle eligibility, graph reachability, cycles and scenario expectations. Generate readable documents from the same data a website could consume.
6. **Human calibration.** Try real situations, record useful/misleading recommendations and adjust discriminating questions. Preserve expected decisions as scenario regressions.

There is no embedding step in version 1. A small explicit catalog and graph can serve guided navigation directly. Free-text retrieval can be added later if it solves observed failures; retrieval would still be filtered by source-specific scope and requirements.

## Lifecycle labels

`stable` is the catalog label for Matt's promoted engineering/productivity buckets and pstack's normal skill directory. It does not certify quality. `experimental` follows Matt's in-progress bucket. `specialized` identifies Matt's misc/unpromoted bucket and makes no claim that it is deprecated. These are deterministic catalog labels derived from upstream placement, not quoted frontmatter attributes. The default graph recommends stable entries only; all 96 remain discoverable in the full catalog.

## Verification performed

- 96 of 96 primary source files have one interpreted record each.
- All 246 skill evidence references point to existing files and valid line ranges in the locked source snapshot.
- 22 curated routing scenarios cover all 22 recommendation outcomes.
- Eight composition notes have 18 additional evidence ranges.
- Invalid coverage, unknown companions, invalid citation ranges, cycles, experimental defaults and stale interpretation snapshots are rejected.
- Missing answers remain questions; reference-only changes invalidate the analysis even when skill bodies are unchanged.
- Offline regeneration is checked for deterministic output.

These checks validate artifacts and explicit expectations. They do not prove the interpretation is correct, measure user success, or execute the downloaded workflows. Human calibration remains pending.

## What to do next

Try five situations from the user's own work: an unclear feature idea, a reproducible bug, an architectural choice, an existing diff to review, and a topic to learn. Follow the graph and compare the result with the full cards. Record whether the questions were understandable, the alternatives were actually discriminated, and the recommended result fit the request.

If this works, build the static interface over `catalog/skills.json`, `catalog/routes.json` and `catalog/compatibility.json`. Schedule this same interpretation process every 14 days. GitHub can validate and publish the result after updates; the agent remains responsible for source interpretation.

No GitHub repository was created, no site was published, no skill was installed and no automation was scheduled during this compilation.
