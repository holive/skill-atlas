# Routing findings from the initial compilation

This is a catalog design interpretation of the downloaded snapshots, not an upstream compatibility guarantee. Repository prefixes below identify the two source roots. The recommendations should retain those source identities, commit pins and evidence links.

## Make the user's desired result the entry point

Do not begin with “Matt or Poteto?” or present all 24 Poteto principles as peer workflows. A person asking for a bug fix usually wants reproduction and a fix, not to choose among root causes, premise testing, boundary discipline and proof. Those principles refine a workflow after its purpose and context are known.

Poteto explicitly describes the standalone principle files as short references that other skills can consult and indexes them inside its mode (`poteto/pstack/README.md:223–225`). The mode says to read the full leaf for any principle applied and gives each a contextual trigger (`poteto/pstack/skills/poteto-mode/SKILL.md:38–79`). Its native help routes nontrivial work to the mode and recommends a particular skill when more or less than the playbook is wanted (`poteto/pstack/skills/poteto-help/SKILL.md:62–66`). Matt similarly separates an idea-to-ship flow, on-ramps, standalone skills and vocabulary underneath (`matt/skills/engineering/ask-matt/SKILL.md:13–34,42–67`).

Show a result as one primary workflow, optional companions and a justified alternative. Explain the meaningful tradeoff and give a copyable invocation only after the full authoritative leaf has been read. Matt's router explicitly warns that its own summaries are orientation, not enough to recommend skipping or characterize a skill (`matt/skills/engineering/ask-matt/SKILL.md:9–11`). Poteto's help gives the same ownership rule for its linked files (`poteto/pstack/skills/poteto-help/SKILL.md:9–13`).

Examples of contextual companions:

- A repeated failed bug fix can add `poteto/principle-attack-the-premise` only after two or more attempts share an assumption and fail the same gate. It requires an explicit discriminating test before another fix, and distinguishes itself from redesign for a new requirement (`poteto/pstack/skills/principle-attack-the-premise/SKILL.md:9–21`).
- A measurement claim adds `poteto/principle-explain-the-number`; it requires a named observed limiter, run count and spread, and routes performance measurement to `benchmark-checklist`. Merely verifying that an artifact exists is a different question (`poteto/pstack/skills/principle-explain-the-number/SKILL.md:9–17`).
- Concurrent writes add `poteto/principle-separate-before-serializing-shared-state`, which asks whether independent owned outputs can remove sharing before recommending a lock (`poteto/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md:9–16`).

## Context that actually changes the recommendation

Collect only facts that discriminate the current candidates. These are not mandatory questions on every route.

| Context | Why it changes the route | Snapshot evidence |
| --- | --- | --- |
| Deliverable: explanation, diagnosis, implementation, review, or decision | Read-only investigation, runnable changes and learning are different outcomes even when their vocabulary overlaps. | Poteto mode `SKILL.md:127–145`; Matt `ask-matt/SKILL.md:46–67,85–93`. |
| Question about current behavior versus historical rationale | Poteto `how` and `why` address different evidence; `teach` combines explanation for understanding. | Poteto help `SKILL.md:105–109`. |
| A known failing behavior and practical local regression path | Poteto TDD is bug-oriented and deliberately allows a cheaper executable check when test infrastructure is impractical. Matt's TDD is a general public-seam discipline with user confirmation before writing tests. | Poteto `tdd/SKILL.md:9–26`; Matt `tdd/SKILL.md:18–26`. |
| Conversation can settle uncertainty versus runnable evidence is required | Matt routes empirical state/UI questions through a prototype and handoffs. | Matt `ask-matt/SKILL.md:19–23`. |
| Scope fits one session versus a buildable multi-session spec versus a foggy large destination | These select direct implementation, spec/ticket workflow, or wayfinding respectively. | Matt `ask-matt/SKILL.md:24–30,52–54`. |
| A working directory and existing setup | Matt distinguishes persistent domain-document interviewing from stateless interviewing and requires configuration before engineering flows. | Matt `ask-matt/SKILL.md:19,85–86,95–97`. |
| Harness and available models/tools | pstack assumes Cursor subagents, role models and features; Claude has an adapter, while other hosts may only be able to read the format. Verification and formal-verification harness presence also changes advice. | Poteto help `SKILL.md:25–48`. |
| Review scope | Diff correctness/quality and effects outside the diff are distinct needs; do not route solely on the word “review.” | Poteto help `SKILL.md:105–110`. |
| Delegation topology | Same brief with competing attempts differs from partitioned coverage or a race. | Poteto help `SKILL.md:108–108`. |
| Effects and approval expectations | A read-only explanation, local edits and landing a stack need different permission context. Source autonomy policies cannot supersede the user's host or explicit authorization. | Poteto mode `SKILL.md:81–87`; Poteto principle-never-block-on-the-human `SKILL.md:9–15`; Matt TDD `SKILL.md:22–24`. |

Avoid collecting irrelevant preferences such as favorite author when current deliverable, setup, scope and workflow style already select a useful path. Author preference can be a later filter or tie-breaker. Distinguish factual prerequisites from user workflow preferences, and unknown from false.

## Why a strict binary tree and embeddings are insufficient

A binary tree is a useful presentation metaphor but a brittle underlying model. One task can be implementation plus an empirical design detour, and several principles can apply together. A graph or declarative rule set can share a question across branches, attach contextual companions and let the user revise an answer without rebuilding a duplicated subtree. Display two choices when the real decision is binary; allow three or more, “not sure,” and backward navigation when appropriate.

Compile the graph from explicit facts such as intent, desired artifact, workflow scope, setup, host assumptions, effects and declared gating. Each recommendation needs a trace: matched conditions, excluded candidates, evidence and any unanswered question that could reverse it. Preserve sources and interpretation separately so upstream changes can invalidate only affected judgments.

Embeddings can later retrieve plausible candidates from free text. They do not prove that a skill is eligible, installed, callable on this host or compatible with a workflow. Same-named TDD skills are semantically close but differ materially in test scope and confirmation. The current Matt TDD also explicitly excludes refactoring from its red→green loop, placing it in review (`matt/skills/engineering/tdd/SKILL.md:34–38`), so the catalog must not silently inherit an older red-green-refactor summary.

Principles can also create tensions that a semantic nearest-neighbor list hides. Poteto's outcome-oriented execution allows planned scoped reversible intermediate breakage with full verification at completion (`principle-outcome-oriented-execution/SKILL.md:13–21`), while sequence-verifiable-units says to check each unit green before the next (`principle-sequence-verifiable-units/SKILL.md:9–15`). These can be reconciled by carefully choosing phase/unit boundaries, but the compiler must not declare them unconditionally compatible. Record a conditional composition note with both citations rather than inventing a global precedence rule.

No embeddings are needed to validate the first guided version. Use them only if free-text retrieval demonstrably misses scenarios that explicit metadata cannot conveniently cover.

## Small scenario acceptance suite

These are initial expected routing properties. For routes outside the fully read principle and TDD leaves, the owning compiler should verify the authoritative workflow leaf before making exact invocation promises.

1. **“A pure function returns the wrong value; there is an existing fast test. I want a regression fix.”** Return bug-regression candidates including Poteto TDD; explain Matt's user-confirmed seam distinction if offered as an alternative. Attach behavior and proof principles rather than listing all principles. Do not promise broad harness construction as Poteto's default.
2. **“I want integration tests for a new feature, and I want to agree the public boundaries first.”** Prefer Matt's TDD discipline over Poteto's cheap-bug-regression workflow. Preserve the confirmation gate. Do not describe the current Matt loop as red-green-refactor.
3. **“Two attempted fixes based on the same cache assumption failed the same check.”** Attach premise testing and root-cause discipline; require a written premise and a discriminating rerunnable observation before another implementation attempt. A single failed fix should not automatically satisfy the repeated-premise trigger.
4. **“Tell me why this code was designed this way. Do not change it.”** Select explanation/history-oriented routes. Keep implementation, setup writes and autonomous full-mode execution out of the promised action. State evidence limitations if historical sources are unavailable.
5. **“The new internal API has no external users; migrate its callers and delete the old interface.”** Enable the same-wave internal-migration principle. Changing the scenario to “public API with external customers” must remove that recommendation or surface its applicability mismatch.
6. **“Two workers update independent counters inside the same state file.”** Recommend examining separate owned outputs before adding a lock. Changing the scenario to one real canonical shared object must allow structural serialization.
7. **“The benchmark got 2x faster; write the result.”** Attach measurement-validity review, require run count, spread and observed limiter, and route to the performance checklist. A green build alone must not satisfy this evidence requirement.
8. **“A planned migration can temporarily break an intermediate phase; every completed phase must verify.”** Surface the outcome-oriented and per-unit verification scopes explicitly. Do not present temporary breakage and universally green microsteps as simultaneous unconditional requirements.
9. **“I use Codex, have no Cursor tools, and want Poteto's entire workflow unchanged.”** Explain host assumptions and missing capabilities before promising portability. Keep catalog inclusion distinct from installation and operational readiness.
10. **“I have an idea, no repository, and need to think it through.”** Favor the stateless interview route over persistent glossary/ADR setup. Adding a working directory should change the persistent-versus-stateless comparison, while the author choice remains secondary.

For every check assert stable namespaced IDs, at least one evidence citation for each decisive rule, a clear next step, and no invented guarantee that a downloaded skill is installed or executable. Also test that missing setup is a visible prerequisite rather than silently installing it.
