# Skill catalog

Agent interpretations of pinned upstream sources. Selection aid only; downloading a skill does not install or invoke it. Human calibration is pending.

Qualified IDs identify the collection; they are catalog identities, not promises about host slash-command syntax.

## Matt · 39 skills

| ID | Role | Catalog status | Useful result |
| --- | --- | --- | --- |
| [matt/ask-matt](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md) | router | stable | Selects an entry skill and a route through idea clarification, specification, building, diagnosis, maintenance and context transitions. It distinguishes workflow sessions from shared vocabulary references. |
| [matt/code-review](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md) | workflow | stable | Reviews a fixed-point diff in independent Standards and Spec tracks, reporting each separately. Repository standards override the heuristic smell baseline. |
| [matt/codebase-design](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md) | reference | stable | Supplies shared language for small interfaces that hide substantial behavior. Supporting guides cover dependency-aware deepening and comparing radically different interface designs. |
| [matt/diagnosing-bugs](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md) | workflow | stable | Builds a runnable feedback command for the exact symptom, minimizes the reproduction, tests ranked hypotheses and verifies the fix. A missing adequate testing seam is recorded as an architectural finding. |
| [matt/domain-modeling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md) | reference | stable | Sharpens domain language against concrete scenarios and code, recording agreed terms as they settle. It offers small decision records for consequential, nonobvious tradeoffs. |
| [matt/grill-with-docs](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) | workflow | stable | Combines structured interviewing with domain modeling so agreed terms and qualifying decisions persist in the repository. |
| [matt/implement](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md) | workflow | stable | Builds specified work with tests at agreed seams, focused checks and a final two-axis review, then commits it on the current branch. |
| [matt/implement-spec](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md) | workflow | stable | Orchestrates a ticket dependency graph in separate implementer worktrees and merges completed work onto one integration branch. It finishes with an integration review and the tracker's completion procedure. |
| [matt/improve-codebase-architecture](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md) | workflow | stable | Surveys architecture friction in relevant or recently changed areas and produces a visual report of deepening candidates. After selection, it interviews the user and records settled domain decisions. |
| [matt/pr](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/SKILL.md) | reference | stable | Shapes a concise PR body around a small explanatory visual, concrete before/after evidence and rollback difficulty with blast radius. |
| [matt/prototype](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/SKILL.md) | workflow | stable | Answers one design question with a shareable state/logic demo or switchable UI variants. It captures the validated answer while preserving the exploratory artifact on a separate branch. |
| [matt/research](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/research/SKILL.md) | workflow | stable | Delegates a question to a fresh background agent that traces claims to primary sources and leaves a cited Markdown note in the repository. |
| [matt/retro](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md) | workflow | stable | Reviews a coding session for improvements to agent navigation, automated checks, review standards and information access. It presents prioritized environment recommendations. |
| [matt/setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md) | setup | stable | Configures repository tracker, optional triage labels and domain-document conventions. It also offers legacy glossary renames and wires a missing GitHub or GitLab remote before considering remote setup complete. |
| [matt/tdd](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md) | workflow | stable | Builds behavior one failing test and minimal implementation at a time at agreed public seams. Its loop explicitly defers refactoring to review. |
| [matt/to-spec](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md) | workflow | stable | Synthesizes existing discussion and codebase understanding into a published feature specification covering user stories, implementation decisions, tests and scope. |
| [matt/to-tickets](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md) | workflow | stable | Splits a plan into independently verifiable tickets with explicit blockers, locally or on a tracker. Wide mechanical refactors use an expand-contract sequence rather than forced vertical slices. |
| [matt/triage](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md) | workflow | stable | Classifies and verifies incoming requests, obtains maintainer decisions and applies triage state with a durable brief. External PR discovery participates only when configured; explicitly named PRs are handled regardless of author. |
| [matt/wayfinder](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wayfinder/SKILL.md) | workflow | stable | Maps a large uncertain effort as linked decision tickets and advances the frontier one non-research ticket per session. Planning is the default; execution is an explicit per-effort override. |
| [matt/wizard](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md) | utility | stable | Authors an interactive Bash procedure for human-only steps, guiding browser actions and captured values that may configure local environment files and GitHub settings. |
| [matt/chief-of-staff](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/chief-of-staff/SKILL.md) | workflow | experimental | Coordinates a sustained goal through background subagents and a dated, source-linked wiki. It now explicitly delegates large builds through specs and tickets, and selects and pursues improvements from periodic retrospectives. |
| [matt/claude-handoff](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/claude-handoff/SKILL.md) | utility | experimental | Writes a redacted temporary handoff and immediately launches a named background Claude agent seeded with it. |
| [matt/loop-me](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/loop-me/SKILL.md) | workflow | experimental | Interviews the user about recurring activities and writes implementable workflow specifications with workspace notes about their world. |
| [matt/setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/setup-ts-deep-modules/SKILL.md) | setup | experimental | Adds dependency-cruiser checks enforcing public package entry points and private subfolders in TypeScript, then proves enforcement with pass-fail-pass evidence. |
| [matt/software-factory](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/SKILL.md) | reference | experimental | Provides shared language and design questions for an agent system that moves tickets and PRs through disposable runs. It pairs problem-driven task examples with service-slot surveys, duplicate-work controls and gradual automation behind review gates. |
| [matt/writing-beats](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-beats/SKILL.md) | workflow | experimental | Shapes fixed raw material into an article through user-selected narrative beats, tracking conceptual prerequisites and writing only the chosen next move. |
| [matt/writing-fragments](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-fragments/SKILL.md) | workflow | experimental | Interviews the author to collect unstructured fragments for later writing, appending them to one raw-material file without imposing an outline. |
| [matt/writing-shape](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-shape/SKILL.md) | workflow | experimental | Turns fixed raw material into a separate article through selected openings, agreed blocks and explicit format choices while tracking the reader's conceptual prerequisites. |
| [matt/git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/SKILL.md) | setup | specialized | Installs a Claude Code hook that blocks configured risky Git command patterns before Bash execution, at project or global scope. |
| [matt/migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/migrate-to-shoehorn/SKILL.md) | workflow | specialized | Migrates TypeScript test fixtures from broad type assertions to shoehorn helpers for partial or intentionally invalid data, then verifies types. |
| [matt/scaffold-exercises](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/scaffold-exercises/SKILL.md) | utility | specialized | Creates numbered course exercise stubs following AI Hero conventions, validates them with the course linter and commits the structure. |
| [matt/setup-pre-commit](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md) | setup | specialized | Installs Husky, lint-staged and Prettier for commit-time formatting and available type/test scripts. A commit through the new hook verifies the setup. |
| [matt/grill-me](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grill-me/SKILL.md) | workflow | stable | Runs the shared interviewing primitive to sharpen a plan or design without adding repository documentation. |
| [matt/grilling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) | workflow | stable | Interviews the user in rounds of decisions whose prerequisites are already settled. The agent investigates environmental facts while the user owns the choices. |
| [matt/handoff](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/handoff/SKILL.md) | utility | stable | Writes a redacted portable handoff for another agent, referencing existing artifacts instead of duplicating them. |
| [matt/teach](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md) | teaching | stable | Builds a persistent learning workspace of short HTML lessons, reusable assets, references, trusted sources and evidence of understanding tied to the learner's mission. |
| [matt/to-questionnaire](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/to-questionnaire/SKILL.md) | utility | stable | Creates a discovery questionnaire for an external knowledge holder after clarifying the recipient and the decisions or facts needed back. |
| [matt/wait-what](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/wait-what/SKILL.md) | utility | stable | Re-explains the last message with missing context, simplified English and established project terms. |
| [matt/writing-for-agents](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md) | reference | stable | Guides documents consumed by agents through conditional context pointers, information hierarchy, explicit completion criteria and a single source for each meaning. A supporting guide covers skill invocation and routers. |

## Poteto · 58 skills

| ID | Role | Catalog status | Useful result |
| --- | --- | --- | --- |
| [poteto/architect](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/architect/SKILL.md) | workflow | stable | Traces every system a change touches, sketches two type and module shapes, and selects the one with clear state ownership and the least caller knowledge. Large or contested designs route to arena. |
| [poteto/arena](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md) | workflow | stable | Runs competing attempts at one shared brief, scores them against a task-specific rubric, and synthesizes one verified artifact. A cross-vendor judge is attempted under the configured pool and fallback rules. |
| [poteto/automate-me](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/automate-me/SKILL.md) | workflow | stable | Drafts or refreshes a personal mode skill from repeated preferences in workspace-scoped history and a direct interview. Existing mode skills are revised in place by default and delivered for review through a PR. |
| [poteto/benchmark-checklist](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/benchmark-checklist/SKILL.md) | workflow | stable | Checks whether a measured performance claim is meaningful, repeatable and about completed work. Produces a verdict with units, spread and the identified limiter. |
| [poteto/blast-radius](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/blast-radius/SKILL.md) | workflow | stable | Finds downstream breakage that a diff or caller list can miss and executes a small proof of the safety fact the change depends on. |
| [poteto/bro](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/bro/SKILL.md) | utility | stable | Restates the previous assistant message in simpler, shorter language without jargon. |
| [poteto/correct](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/correct/SKILL.md) | workflow | stable | Finds repeated agent mistake classes and changes repository structure or enforcement so they are harder to repeat. Demonstrates each new check on a real past mistake. |
| [poteto/create-formal-verification-skill](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-formal-verification-skill/SKILL.md) | workflow | stable | Verifies one costly property that tests rarely reach and leaves a reproducible project-local skill to check it again. The handoff states code coverage, assumptions, bounds and the synchronization commit, with a demonstrated failing variant. |
| [poteto/create-verification-skill](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/SKILL.md) | workflow | stable | Creates a repository-specific skill that launches, health-checks, drives and cleans up the real app. Seeds a user-facing feature map and executes one complete journey before handoff. |
| [poteto/figure-it-out](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/figure-it-out/SKILL.md) | workflow | stable | Designs a custom, auditable workflow when bundled playbooks do not fit or a change is ambitious. Runs small hypothesis-driven units against an explicit completion predicate. |
| [poteto/how](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/how/SKILL.md) | workflow | stable | Uses one read-only explainer to trace existing code and explain its architecture, runtime flow or ownership at a senior engineer’s level. The parent presents that explanation with only light edits. |
| [poteto/in-your-own-words](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/in-your-own-words/SKILL.md) | utility | stable | Restates the user's apparent goals and the underlying problem before work proceeds. |
| [poteto/interrogate](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/interrogate/SKILL.md) | workflow | stable | Has configured adversaries try to break a change or design with executable repros in isolated worktrees. The coordinator reruns each claim and reports all verified intent-breaking failures without applying fixes. |
| [poteto/ketchup](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup/SKILL.md) | utility | stable | Catches the user up on changes since their last message and lists every outstanding decision with enough context to act from the reply. |
| [poteto/ketchup-video](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup-video/SKILL.md) | utility | stable | Delivers the ketchup catch-up as a short silent slide video, with outstanding decisions retained as text under it. |
| [poteto/maintain-formal-verification-skill](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-formal-verification-skill/SKILL.md) | workflow | stable | Reconciles formal checks with code changes since their synchronization commit. Separates verification drift from real product bugs and proves updated checks can still fail. |
| [poteto/maintain-verification-skill](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-verification-skill/SKILL.md) | workflow | stable | Audits every mapped feature from source and drives every feature live. Ships at most one PR limited to proven verification documentation or harness corrections. |
| [poteto/make-bot-ui](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md) | workflow | stable | Builds a server-backed page whose buttons wake a Grok Bot through a webhook routine, then exposes the page on a Tailscale network. |
| [poteto/no-comments](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/no-comments/SKILL.md) | workflow | stable | Delegates a scoped comment pass to Comment Sicko, audits deletions and flags, then implements accepted root-cause fixes within the same fence. Claimed constraints can be offered an approved type, runtime, test or lint encoding. |
| [poteto/poteto-help](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md) | router | stable | Answers pstack help questions with one adapted prompt and a link to the owning source, without starting a help question’s work. An actual request to do work is explicitly handed to poteto-mode instead. |
| [poteto/poteto-mode](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md) | router | stable | Routes rigorous engineering work through 22 task-specific playbooks and companion skills, with explicit design, delegation, evidence and delivery rules. Read-only investigations, plan-only requests, PR readiness and authorized landing retain distinct scopes. |
| [poteto/principle-attack-the-premise](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-attack-the-premise/SKILL.md) | principle | stable | Interrupts fixes that repeatedly fail the same gate by writing down their common premise and testing it directly before another attempt. |
| [poteto/principle-boundary-discipline](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-boundary-discipline/SKILL.md) | principle | stable | Concentrates parsing, validation and error handling at system boundaries, leaving internal business logic expressed as typed pure functions. |
| [poteto/principle-build-the-lever](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-build-the-lever/SKILL.md) | principle | stable | Turns nontrivial work into a small rerunnable tool or an explicit delegate recipe, making the result reproducible for reviewers. |
| [poteto/principle-encode-lessons-in-structure](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) | principle | stable | Replaces repeated instructions or corrections with an enforceable structural rule where possible; judgment-heavy lessons receive a clearer instruction and failure example. |
| [poteto/principle-exhaust-the-design-space](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-exhaust-the-design-space/SKILL.md) | principle | stable | Resolves unfamiliar architecture or interaction choices by comparing a few competing prototypes before selecting an approach. |
| [poteto/principle-experience-first](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-experience-first/SKILL.md) | principle | stable | Prioritizes the experience of consumers and maintainers when deciding scope and polish, using prototypes to test design choices early. |
| [poteto/principle-explain-the-number](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-explain-the-number/SKILL.md) | principle | stable | Makes measurement decision-led by declaring the result that would change a choice, finding the observed limiter, and ruling out misleading alternative explanations before trusting a number. It stops when run-to-run spread exceeds the effect and retains the run evidence. |
| [poteto/principle-fix-root-causes](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-fix-root-causes/SKILL.md) | principle | stable | Traces a reproduced symptom to the first wrong decision and distinguishes legitimate states needing handling from impossible states that should never be produced. |
| [poteto/principle-foundational-thinking](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-foundational-thinking/SKILL.md) | principle | stable | Orders work around sound data structures and shared foundations so later increments remain simple and coherent. |
| [poteto/principle-guard-the-context-window](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-guard-the-context-window/SKILL.md) | principle | stable | Controls reasoning load by bounding phases and moving bulk reading to delegates while retaining summaries in the coordinating context. |
| [poteto/principle-laziness-protocol](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-laziness-protocol/SKILL.md) | principle | stable | Keeps refactors and additions small by consolidating repeated choices and avoiding unnecessary layers or abstractions. |
| [poteto/principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-make-operations-idempotent/SKILL.md) | principle | stable | Designs state-changing work to reconcile current state with the goal so retries and interrupted runs converge safely. |
| [poteto/principle-migrate-callers-then-delete-legacy-apis](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | principle | stable | Keeps an internal API simplification coherent by migrating callers and removing the old API in the same wave, with tests aligned to the new contract. |
| [poteto/principle-minimize-reader-load](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-minimize-reader-load/SKILL.md) | principle | stable | Evaluates maintainability through the indirections a reader must trace and the mutable state they must remember, then removes layers or narrows state. |
| [poteto/principle-model-the-domain](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-model-the-domain/SKILL.md) | principle | stable | Encodes domain invariants and access patterns in an appropriate structure rather than spreading lifecycle rules across conditionals and phases. |
| [poteto/principle-never-block-on-the-human](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-never-block-on-the-human/SKILL.md) | principle | stable | Lets reversible execution proceed with reasonable decisions and asynchronous supervision while retaining confirmation for irreversible actions and human control of product direction. |
| [poteto/principle-outcome-oriented-execution](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-outcome-oriented-execution/SKILL.md) | principle | stable | Allows explicitly scoped transitional breakage during a planned migration so work converges on the verified target architecture without accumulating compatibility scaffolding. |
| [poteto/principle-prove-it-works](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-prove-it-works/SKILL.md) | principle | stable | Verifies completion against the actual output and favors a deterministic repeatable check whose evidence a human can inspect. |
| [poteto/principle-redesign-from-first-principles](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-redesign-from-first-principles/SKILL.md) | principle | stable | Integrates a requirement by reconsidering the whole affected design as though the requirement had always existed, then delivering the redesign incrementally. |
| [poteto/principle-separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md) | principle | stable | Removes unnecessary shared write targets before introducing locks, and uses structural ownership or serialization when one canonical mutable object is unavoidable. |
| [poteto/principle-sequence-verifiable-units](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-sequence-verifiable-units/SKILL.md) | principle | stable | Sequences multi-step execution and delivery into small checked units whose order demonstrates correctness to a reviewer. |
| [poteto/principle-subtract-before-you-add](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-subtract-before-you-add/SKILL.md) | principle | stable | Simplifies the existing base before extending it by removing dead code, redundant rules and references without novel content. |
| [poteto/principle-test-behavior-not-implementation](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) | principle | stable | Judges a test by whether it catches broken observable behavior while surviving internal restructuring, then rewrites assertions around the consumer contract. |
| [poteto/principle-type-system-discipline](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-type-system-discipline/SKILL.md) | principle | stable | Uses types and authoritative schemas to prevent invalid states, semantic primitive mixups and unhandled variants before runtime. |
| [poteto/recall](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/recall/SKILL.md) | workflow | stable | Rebuilds recent work context across the user's scoped chat history, shared evidence and live PR state. Returns a compact current-state brief before work resumes. |
| [poteto/reflect](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/reflect/SKILL.md) | workflow | stable | Reads the active conversation for durable lessons and proposes edits to skills the session used, separating rejected ideas and enforceable backlog work. Approved edits go into a local copy of the skill rather than the installed plugin cache. |
| [poteto/setup-pstack](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/setup-pstack/SKILL.md) | setup | stable | Detects available host models, confirms a per-role model map and one of three reasoning budgets, then writes the rule used by new sessions. Recognized retired defaults migrate while other user choices remain. |
| [poteto/sharpen](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/sharpen/SKILL.md) | utility | stable | Rewrites a task prompt around expert practice, raw evidence, concrete methods and an independent correctness check. The rewritten prompt asks its future executor to prototype experimentally decidable choices and leaves only product or preference calls to the user. |
| [poteto/show-me-your-work](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/SKILL.md) | workflow | stable | Maintains one append-only TSV decision trail for long or unattended work, with explicit boundaries between runs sharing a log. Audits this run’s entries against its transcript and obtains a different-vendor review before handoff. |
| [poteto/statechart](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md) | workflow | stable | Checks a TLA+ model and renders a reader-labeled Mermaid statechart with per-rule bug paths and honest unchecked-rule limits. Code-backed bug paths must be replayed against real code before being treated as product bugs. |
| [poteto/swarm](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/swarm/SKILL.md) | workflow | stable | Fans workers out across slices or declared races and consolidates their terminal results into one evidence-backed report. Missing coverage is recorded rather than counted as a pass. |
| [poteto/tdd](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/tdd/SKILL.md) | workflow | stable | Fixes a bug with a focused failing-before, passing-after regression check when a practical local test path exists. Uses another executable proof when a new test would be brittle or disproportionate. |
| [poteto/teach](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/teach/SKILL.md) | teaching | stable | Combines code behavior and historical rationale into a plain, conversational explanation at the learner's pace. Builds diagrams incrementally when they help understanding. |
| [poteto/technical-writing](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/technical-writing/SKILL.md) | reference | stable | Applies a layered standard for technical documents, choosing a document purpose before refining sentences, instructions and unambiguous language. |
| [poteto/typescript-best-practices](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/typescript-best-practices/SKILL.md) | reference | stable | Applies TypeScript modeling and boundary rules to .ts/.tsx work, including verified brands, schema-owned validation and the simplest total type. The examples explain when to strengthen a representation and when a plain type is enough. |
| [poteto/unslop](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/unslop/SKILL.md) | utility | stable | Edits prose to remove recurring AI writing patterns while preserving meaning and intended tone. |
| [poteto/why](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/why/SKILL.md) | workflow | stable | Reconstructs why code took its present shape from introducing and subsequent commits and PR discussions. Cites the authors’ record, marks its own inferences, and states what the evidence does not answer. |

## Detailed cards

Use cases, boundaries and roles below are compiler interpretations. Evidence links point to exact upstream revisions. Effects are possible actions of the described workflow, not permissions granted by the catalog.

### matt/ask-matt

Selects an entry skill and a route through idea clarification, specification, building, diagnosis, maintenance and context transitions. It distinguishes workflow sessions from shared vocabulary references.

- **Role / status:** router / stable.
- **Use when:** Choose a Matt skill when you know the situation but not its name.; Choose between one-session implementation, ticket-by-ticket work and whole-spec orchestration.
- **Scope limits:** Catalog interpretation: Read the selected skill before acting; this router's summaries are orientation.
- **Result:** Recommended skill sequence; Context-transition recommendation
- **Requirements:** Read each recommended SKILL.md before explaining or skipping it.; Engineering flows assume setup-matt-pocock-skills configuration.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** matt/grill-with-docs, matt/handoff, matt/prototype, matt/to-spec, matt/to-tickets, matt/implement, matt/implement-spec, matt/tdd, matt/code-review, matt/pr, matt/retro, matt/triage, matt/diagnosing-bugs, matt/wayfinder, matt/improve-codebase-architecture, matt/domain-modeling, matt/codebase-design, matt/grill-me, matt/grilling, matt/research, matt/to-questionnaire, matt/wizard, matt/wait-what, matt/teach, matt/writing-for-agents, matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:11–13](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md#L11-L13) — Read full skills before recommending; router scope
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:19–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md#L19-L30) — Interview, prototype and implementation branches
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:46–60](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md#L46-L60) — Incoming requests, hard bugs, uncertain planning and upkeep
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:85–97](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md#L85-L97) — Standalone routes and setup prerequisite
- **Evidence:** [skills/engineering/ask-matt/PHASE-BOUNDARIES.md:19–38](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/PHASE-BOUNDARIES.md#L19-L38) — Ordered context-transition decision tree

### matt/code-review

Reviews a fixed-point diff in independent Standards and Spec tracks, reporting each separately. Repository standards override the heuristic smell baseline.

- **Role / status:** workflow / stable.
- **Use when:** Review committed changes since a known base.; Check both repository conventions and requested behavior.
- **Scope limits:** Catalog interpretation: Resolve a valid nonempty committed comparison first; its three-dot HEAD command does not include uncommitted edits.; Catalog interpretation: Report an unavailable spec as skipped rather than inventing one.
- **Result:** Separate Standards and Spec findings; Counts and worst finding within each axis
- **Requirements:** Git repository and resolvable fixed point; uses a merge-base three-dot diff.; Configured issue tracker, otherwise requests setup-matt-pocock-skills.; Parallel reviewers, each with a fresh context window and explicit diff/spec/standards inputs.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** Asks for the fixed point if absent and a spec source if discovery fails. If the user says no spec exists, skips that axis. No report-approval gate is stated.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/code-review/SKILL.md:6–13](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md#L6-L13) — Two axes, fresh reviewer contexts and tracker prerequisite
- **Evidence:** [skills/engineering/code-review/SKILL.md:19–32](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md#L19-L32) — Committed comparison and missing-input questions
- **Evidence:** [skills/engineering/code-review/SKILL.md:36–41](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md#L36-L41) — Repository precedence and heuristic rather than hard smell violations
- **Evidence:** [skills/engineering/code-review/SKILL.md:60–80](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md#L60-L80) — Foreground parallel prompts and separate reporting

### matt/codebase-design

Supplies shared language for small interfaces that hide substantial behavior. Supporting guides cover dependency-aware deepening and comparing radically different interface designs.

- **Role / status:** reference / stable.
- **Use when:** Choose a module interface or testing seam.; Compare alternative designs for a selected deepening candidate.
- **Scope limits:** Catalog interpretation: Reading design vocabulary does not itself request implementation.; Catalog interpretation: Avoid speculative seams without real variation.
- **Result:** Consistent architecture vocabulary; Interface and dependency strategy; Alternative designs and recommendation when requested
- **Requirements:** The optional Design It Twice branch uses 3+ parallel subagents with fresh context windows and separate technical briefs.
- **Possible effects:** read, delegate
- **Confirmation behavior:** For alternative designs, shows the problem space then immediately starts subagents without waiting; presents designs and its recommendation afterward.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:8–28](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md#L8-L28) — Purpose and shared vocabulary
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:62–65](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md#L62-L65) — Interface, test surface and real-adapter criterion
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:111–114](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md#L111-L114) — Conditional support branches
- **Evidence:** [skills/engineering/codebase-design/DESIGN-IT-TWICE.md:11–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/DESIGN-IT-TWICE.md#L11-L30) — Nonblocking presentation and fresh-context distinct design briefs
- **Evidence:** [skills/engineering/codebase-design/DEEPENING.md:9–35](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/DEEPENING.md#L9-L35) — Dependency-sensitive testing and replacement strategy

### matt/diagnosing-bugs

Builds a runnable feedback command for the exact symptom, minimizes the reproduction, tests ranked hypotheses and verifies the fix. A missing adequate testing seam is recorded as an architectural finding.

- **Role / status:** workflow / stable.
- **Use when:** Diagnose a resistant or intermittent bug.; Measure and isolate a performance regression.
- **Scope limits:** Catalog interpretation: Do not hypothesize before a tight red-capable feedback loop exists.; Catalog interpretation: Temporary production instrumentation needs the permission requested by this workflow.
- **Result:** Symptom-specific reproduction command; Ranked falsifiable hypotheses; Verified fix and regression test or documented missing seam; Cleaned instrumentation
- **Requirements:** Access to a reproducing environment or captured artifact.; Runnable tests, HTTP/CLI/browser harness or the structured human feedback template.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Shows hypotheses before testing but proceeds if the user is away. If no loop can be built, stops to request access, redacted evidence or permission for production instrumentation.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:14–16](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md#L14-L16) — Redact captured output
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:53–66](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md#L53-L66) — Hard feedback-loop precondition and escalation choices
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:90–98](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md#L90-L98) — Ranked predictions and nonblocking checkpoint
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:116–138](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md#L116-L138) — Regression seam, original scenario and cleanup
- **Evidence:** [skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh:9–16](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh#L9-L16) — Human fallback captures observations, not login secrets

### matt/domain-modeling

Sharpens domain language against concrete scenarios and code, recording agreed terms as they settle. It offers small decision records for consequential, nonobvious tradeoffs.

- **Role / status:** reference / stable.
- **Use when:** Resolve overloaded project terminology.; Update a glossary or qualifying architectural decision.
- **Scope limits:** Catalog interpretation: A glossary should not become a specification or implementation scratchpad.; Catalog interpretation: Routine decisions that fail the ADR criteria need no ADR.
- **Result:** Updated domain glossary; Optional numbered ADR
- **Requirements:** Working directory; follow GLOSSARY-MAP.md when present.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Surfaces contradictions for the user to resolve, then records settled terms inline. Offers ADRs only when all three qualifying criteria hold.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:8–8](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md#L8-L8) — Active model refinement, not vocabulary consumption alone
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:40–64](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md#L40-L64) — Lazy creation, contradictions, code check and immediate glossary updates
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:66–74](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md#L66-L74) — Three ADR criteria
- **Evidence:** [skills/engineering/domain-modeling/ADR-FORMAT.md:3–15](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/ADR-FORMAT.md#L3-L15) — Small sequential decision artifacts
- **Evidence:** [skills/engineering/domain-modeling/GLOSSARY-FORMAT.md:27–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md#L27-L30) — Project-specific canonical terms and concise definitions

### matt/grill-with-docs

Combines structured interviewing with domain modeling so agreed terms and qualifying decisions persist in the repository.

- **Role / status:** workflow / stable.
- **Use when:** Clarify a repository-backed idea while preserving its language and decisions.
- **Scope limits:** Catalog interpretation: For a stateless conversation without a working directory, the router recommends grill-me.
- **Result:** Confirmed shared understanding; Glossary updates and optional ADRs
- **Requirements:** Skill invocation support for grilling and domain-modeling, including fresh-context fact-finding when needed.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Inherits grilling's waits and final confirmation, while domain-modeling records already settled terminology inline.
- **Explicit companions/references:** matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/grill-with-docs/SKILL.md:7–7](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md#L7-L7) — Two explicit primitive calls
- **Evidence:** [skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L28-L30) — Facts delegated, decisions owned and confirmed by user
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:60–74](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md#L60-L74) — Inline glossary updates and conditional ADRs

### matt/implement

Builds specified work with tests at agreed seams, focused checks and a final two-axis review, then commits it on the current branch.

- **Role / status:** workflow / stable.
- **Use when:** Implement a scoped spec or ready ticket in the current session.
- **Scope limits:** Catalog interpretation: Resolve ambiguous ticket references first.; Catalog interpretation: Use implement-spec to coordinate a whole ticket graph.
- **Result:** Implemented code and tests; Review findings and commit on current branch
- **Requirements:** Spec or tickets and tracker access for references.; Project typecheck/test commands; companion TDD and parallel review capabilities.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Asks when a ticket reference is ambiguous; tests use pre-agreed seams. No extra confirmation before its specified commit is stated.
- **Explicit companions/references:** matt/tdd, matt/code-review
- **Evidence:** [skills/engineering/implement/SKILL.md:7–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md#L7-L17) — Ticket lookup, TDD, verification, review and commit
- **Evidence:** [skills/engineering/tdd/SKILL.md:22–24](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L22-L24) — Companion testing-seam agreement

### matt/implement-spec

Orchestrates a ticket dependency graph in separate implementer worktrees and merges completed work onto one integration branch. It finishes with an integration review and the tracker's completion procedure.

- **Role / status:** workflow / stable.
- **Use when:** Build a ready multi-ticket spec through parallel implementation.
- **Scope limits:** Catalog interpretation: Not a discovery or specification workflow.; Catalog interpretation: Requires subagent, branch and worktree coordination.
- **Result:** Implemented integration branch; Resolved tickets or review-ready PR; Removed implementer worktrees
- **Requirements:** Spec, tickets, blocking graph and configured tracker; otherwise requests setup-matt-pocock-skills.; Every subagent starts with fresh context; a fresh implementer per ticket and a fresh final-fix implementer.; Background agents, Git worktrees/branches and shared access to optional exploration notes outside the repository.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Draft PR creation depends on tracker workflow or user request. No extra general checkpoint is stated; the companion TDD seam confirmation still applies.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/tdd, matt/code-review
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:7–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md#L7-L19) — Task graph, integration goal and fresh-context coordination
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:23–32](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md#L23-L32) — Optional exploration, conditional draft PR and fresh ticket implementers
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:34–42](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md#L34-L42) — Mergers, final fresh fix agent, tracker completion and cleanup

### matt/improve-codebase-architecture

Surveys architecture friction in relevant or recently changed areas and produces a visual report of deepening candidates. After selection, it interviews the user and records settled domain decisions.

- **Role / status:** workflow / stable.
- **Use when:** Find architecture improvements grounded in observed maintenance or testing friction.
- **Scope limits:** Catalog interpretation: Wait for candidate selection before interface proposals.; Catalog interpretation: Purely hypothetical refactors without friction are weak candidates.
- **Result:** Temporary architecture-review HTML with before/after visuals; Ranked deepening candidates; Design decisions and conditional domain documentation
- **Requirements:** Codebase, optional history, glossary and relevant ADRs.; Fresh-context exploration subagent; report loads Tailwind and Mermaid from CDNs.; OS-specific file opener for report presentation.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Asks which candidate to explore before grilling. Offers an ADR for a rejection whose durable reason future reviews need.
- **Explicit companions/references:** matt/codebase-design, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:20–35](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md#L20-L35) — Focused survey, fresh-context exploration and friction criteria
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:39–60](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md#L39-L60) — Temporary report, CDNs and selection checkpoint
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:64–71](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md#L64-L71) — Interview, glossary updates and conditional alternative-interface branch
- **Evidence:** [skills/engineering/improve-codebase-architecture/HTML-REPORT.md:94–100](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/HTML-REPORT.md#L94-L100) — Static report with external rendering scripts

### matt/pr

Shapes a concise PR body around a small explanatory visual, concrete before/after evidence and rollback difficulty with blast radius.

- **Role / status:** reference / stable.
- **Use when:** Explain a concrete change in a pull request body.
- **Scope limits:** Catalog interpretation: This is a writing reference, not review execution or permission to merge.
- **Result:** PR body with Summary, Evidence and Merge Danger
- **Requirements:** Change details, before/after evidence and glossary vocabulary where available.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/pr/SKILL.md:12–37](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/SKILL.md#L12-L37) — Body template and concise glossary-based wording
- **Evidence:** [skills/engineering/pr/SKILL.md:154–170](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/SKILL.md#L154-L170) — Minimal visual, concrete evidence and merge-risk framing

### matt/prototype

Answers one design question with a shareable state/logic demo or switchable UI variants. It captures the validated answer while preserving the exploratory artifact on a separate branch.

- **Role / status:** workflow / stable.
- **Use when:** Try awkward state-model scenarios.; Compare structurally different UI directions.
- **Scope limits:** Catalog interpretation: Prototype constraints exclude tests and production hardening.; Catalog interpretation: Persistence is limited to scratch storage when it is explicitly the question being explored.
- **Result:** One-file logic HTML or UI variants; Decision and verdict; Preserved prototype branch and issue pointer
- **Requirements:** Specific design question and existing project conventions for UI.; Git branch and issue-context mechanism for capture.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** May ask to clarify the question when the user is available; otherwise states a context-based branch assumption. User feedback selects the answer.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/prototype/SKILL.md:12–26](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/SKILL.md#L12-L26) — Question-based branches, assumptions, constraints and capture
- **Evidence:** [skills/engineering/prototype/LOGIC.md:35–48](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/LOGIC.md#L35-L48) — Self-contained demo with domain-language walkthroughs
- **Evidence:** [skills/engineering/prototype/UI.md:18–28](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/UI.md#L18-L28) — Existing host page preferred over a new route
- **Evidence:** [skills/engineering/prototype/UI.md:98–112](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/UI.md#L98-L112) — Preserve variants outside main, stub mutations and rewrite production winner

### matt/research

Delegates a question to a fresh background agent that traces claims to primary sources and leaves a cited Markdown note in the repository.

- **Role / status:** workflow / stable.
- **Use when:** Gather official API facts or source-backed answers while other work continues.
- **Scope limits:** Catalog interpretation: Research informs design decisions rather than replacing them.
- **Result:** Single cited Markdown findings file following repository convention
- **Requirements:** Background-agent support with fresh context and access to relevant primary sources.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/research/SKILL.md:6–12](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/research/SKILL.md#L6-L12) — Fresh background research, source standard and repository output

### matt/retro

Reviews a coding session for improvements to agent navigation, automated checks, review standards and information access. It presents prioritized environment recommendations.

- **Role / status:** workflow / stable.
- **Use when:** A build went sideways or repeated mistakes suggest missing environment guardrails.
- **Scope limits:** Catalog interpretation: Not a product retrospective or general feature refactor.; Catalog interpretation: Inspect current checks before proposing replacements.
- **Result:** Severity-ordered environment improvement candidates
- **Requirements:** Current session context or accessible session logs.; Existing checks and steering documents.
- **Possible effects:** read
- **Confirmation behavior:** Presents candidates to the user; this skill does not specify a separate implementation step.
- **Explicit companions/references:** matt/writing-for-agents
- **Evidence:** [skills/engineering/retro/SKILL.md:7–13](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md#L7-L13) — Environment focus and source inspection
- **Evidence:** [skills/engineering/retro/SKILL.md:17–25](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md#L17-L25) — Improvement categories, existing checks and recommendation output

### matt/setup-matt-pocock-skills

Configures repository tracker, optional triage labels and domain-document conventions. It also offers legacy glossary renames and wires a missing GitHub or GitLab remote before considering remote setup complete.

- **Role / status:** setup / stable.
- **Use when:** Prepare a repository for the engineering workflows.; Intentionally switch its tracker.
- **Scope limits:** Catalog interpretation: Directly edit established configuration for small adjustments.; Catalog interpretation: Preserve existing steering files rather than creating a competing one.
- **Result:** docs/agents tracker/domain configuration and navigation block; Optional triage-label configuration and remote labels; Conditional glossary migration and Git remote setup
- **Requirements:** Repository inspection and user tracker choice.; Reachable remote repository and gh or glab for GitHub/GitLab; request URL if missing and verify repo view succeeds.; User-described workflow for other trackers.
- **Possible effects:** read, local_write, external_write, execute, configure
- **Confirmation behavior:** Offers legacy glossary renames, asks applicable tracker/label/layout questions, obtains a missing remote URL, and shows draft files before writing. Single-context layout defaults silently. GitHub template verifies the first issue target and asks if it is not the user's repository.
- **Explicit companions/references:** matt/triage
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:15–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md#L15-L30) — Explore and confirm, including offered legacy migration
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:42–63](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md#L42-L63) — Tracker choices, required reachable remote and conditional questions
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:65–84](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md#L65-L84) — Draft review and existing steering-file preservation
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:104–116](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md#L104-L116) — Conditional labels and seed templates
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md:19–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md#L19-L19) — Fork target verification before first issue creation
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:3–15](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md#L3-L15) — Local publication is file creation

### matt/tdd

Builds behavior one failing test and minimal implementation at a time at agreed public seams. Its loop explicitly defers refactoring to review.

- **Role / status:** workflow / stable.
- **Use when:** Implement a concrete behavior test-first.; Fix behavior with public-seam regression coverage.
- **Scope limits:** Catalog interpretation: Do not write tests at unconfirmed seams or couple them to internals.; Catalog interpretation: Avoid writing all tests ahead or adding speculative refactors to the loop.
- **Result:** Behavior-focused tests; Incremental passing implementation
- **Requirements:** User-confirmed test seams and runnable project tests.; Glossary and relevant ADR context when present.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Requires the user to confirm the proposed seams before any test is written.
- **Explicit companions/references:** matt/codebase-design, matt/code-review
- **Evidence:** [skills/engineering/tdd/SKILL.md:14–26](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L14-L26) — Behavior through public interfaces, seam confirmation and design vocabulary
- **Evidence:** [skills/engineering/tdd/SKILL.md:30–38](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L30-L38) — Anti-patterns, red-green slices and review-stage refactoring
- **Evidence:** [skills/engineering/tdd/mocking.md:3–14](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/mocking.md#L3-L14) — Mock external system boundaries rather than owned internals

### matt/to-spec

Synthesizes existing discussion and codebase understanding into a published feature specification covering user stories, implementation decisions, tests and scope.

- **Role / status:** workflow / stable.
- **Use when:** A discussed idea is ready to become a buildable specification.
- **Scope limits:** Catalog interpretation: This is synthesis rather than another requirements interview.
- **Result:** Published ready-for-agent spec; Agreed testing seams
- **Requirements:** Existing conversation context and codebase understanding.; Configured tracker and triage vocabulary; otherwise requests setup-matt-pocock-skills.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** Checks proposed testing seams with the user before writing and publishing. On GitHub, the configured template checks the first issue's repository target and asks if it is not the user's.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/to-spec/SKILL.md:7–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md#L7-L19) — Synthesis, tracker prerequisite, testing checkpoint and publication
- **Evidence:** [skills/engineering/to-spec/SKILL.md:43–69](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md#L43-L69) — Implementation/testing decisions, prototype-snippet exception and scope
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md:19–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md#L19-L19) — Conditional first-issue target confirmation

### matt/to-tickets

Splits a plan into independently verifiable tickets with explicit blockers, locally or on a tracker. Wide mechanical refactors use an expand-contract sequence rather than forced vertical slices.

- **Role / status:** workflow / stable.
- **Use when:** Break a ready spec into fresh-session tickets.; Sequence a wide refactor that cannot land as independent vertical slices.
- **Scope limits:** Catalog interpretation: Generated agent-ready tickets do not need intake triage.; Catalog interpretation: Publication must not modify or close the parent issue.
- **Result:** Approved ticket breakdown; Published tickets and blocking graph
- **Requirements:** Plan, spec or current discussion.; Configured tracker and label vocabulary; otherwise requests setup-matt-pocock-skills.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** Iterates until the user approves granularity and blocking edges, then publishes. GitHub configuration also checks the first issue target and asks if it is not the user's repository.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md#L9-L17) — Inputs and tracker requirements
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:31–40](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md#L31-L40) — Vertical slices and wide-refactor exception
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:44–67](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md#L44-L67) — Human approval, local/remote publishing and parent boundary
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md:10–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md#L10-L19) — Native blocking, open-blocker count and repository target guard

### matt/triage

Classifies and verifies incoming requests, obtains maintainer decisions and applies triage state with a durable brief. External PR discovery participates only when configured; explicitly named PRs are handled regardless of author.

- **Role / status:** workflow / stable.
- **Use when:** Raw bug reports or feature requests need verification and maintainer direction.; An external contribution needs a next-step brief.
- **Scope limits:** Catalog interpretation: Agent-ready tickets generated from a plan do not need intake triage.; Catalog interpretation: Conflicting state labels and unusual transitions need maintainer direction.
- **Result:** Category and triage state; Agent brief or needs-info notes; Conditional rejection record and closure
- **Requirements:** Configured tracker and role-to-label mapping.; Codebase access and runnable verification for claims; fresh-context fact-finding through grilling when needed.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Waits after recommending a state and asks on conflicting states or unusual transitions. Quick overrides confirm impending role/comment/close actions; configured GitHub issue creation checks its repository target.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/triage/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md#L9-L17) — Tracker scope and AI disclaimer
- **Evidence:** [skills/engineering/triage/SKILL.md:39–45](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md#L39-L45) — State invariants and approval
- **Evidence:** [skills/engineering/triage/SKILL.md:64–90](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md#L64-L90) — Discovery scope, verification, interview and outcome effects
- **Evidence:** [skills/engineering/triage/AGENT-BRIEF.md:3–5](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/AGENT-BRIEF.md#L3-L5) — Brief is the behavioral contract
- **Evidence:** [skills/engineering/triage/OUT-OF-SCOPE.md:84–97](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/OUT-OF-SCOPE.md#L84-L97) — Only rejected enhancements enter rejection memory
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md:19–29](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md#L19-L29) — Target safeguard and full PR body/comments/diff acquisition
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md:21–25](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md#L21-L25) — External MR list operation and filtering

### matt/wayfinder

Maps a large uncertain effort as linked decision tickets and advances the frontier one non-research ticket per session. Planning is the default; execution is an explicit per-effort override.

- **Role / status:** workflow / stable.
- **Use when:** A foggy greenfield project or huge feature exceeds one reasoning session.
- **Scope limits:** Catalog interpretation: A well-scoped build with a visible route needs no map.; Catalog interpretation: Decision tickets are not implementation tasks without the effort's explicit scope override.
- **Result:** Decision map and linked tickets; Resolution comments and updated frontier; Linked research/prototype assets
- **Requirements:** Tracker map/child/claim/blocking operations, with local Markdown fallback.; Fresh-context research subagents and branch/push access for research assets.; Tracker-specific native relationship support or documented fallback; GitLab template links children explicitly.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** HITL decisions require live human exchange. Stops to ask if charting finds no fog; charting ends after creating the map, tickets and research work. Configured GitHub issue creation checks the repository target.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/research, matt/prototype, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:11–25](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wayfinder/SKILL.md#L11-L25) — Planning default and tracker mechanics
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:65–80](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wayfinder/SKILL.md#L65-L80) — Claims, native blockers, ticket types and live-human ownership
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:105–126](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wayfinder/SKILL.md#L105-L126) — Session limit, charting, fresh research agents, pushes and resolution
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:23–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md#L23-L30) — Local map, claim and frontier
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md:10–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md#L10-L19) — Open blockers and issue-target safeguard
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md:41–46](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md#L41-L46) — Explicit child links and linked-child frontier discovery

### matt/wizard

Authors an interactive Bash procedure for human-only steps, guiding browser actions and captured values that may configure local environment files and GitHub settings.

- **Role / status:** utility / stable.
- **Use when:** Credentials, provisioning or cutovers require steps only the human can perform.
- **Scope limits:** Catalog interpretation: Let the agent perform steps it can already do.; Catalog interpretation: The authoring agent must not run the interactive script end-to-end.
- **Result:** Statically verified executable wizard; Human run instructions; Optional committed repeatable setup path
- **Requirements:** Bash, bundled template and optional shellcheck.; Browser opener when available; authenticated gh for GitHub writes, with manual fallback.
- **Possible effects:** read, local_write, external_write, execute, configure
- **Confirmation behavior:** Confirms ordered stages and value destinations before authoring. Generated stages confirm irreversible actions; the human runs the procedure.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/wizard/SKILL.md:8–12](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md#L8-L12) — Template purpose, effects and ephemeral default
- **Evidence:** [skills/engineering/wizard/SKILL.md:18–25](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md#L18-L25) — Procedure and destination confirmation
- **Evidence:** [skills/engineering/wizard/SKILL.md:35–44](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md#L35-L44) — Author stages, irreversible gates, static checks and handoff
- **Evidence:** [skills/engineering/wizard/template.sh:137–178](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/template.sh#L137-L178) — Actual environment and conditional GitHub secret/variable writes

### matt/chief-of-staff

Coordinates a sustained goal through background subagents and a dated, source-linked wiki. It now explicitly delegates large builds through specs and tickets, and selects and pursues improvements from periodic retrospectives.

- **Role / status:** workflow / experimental.
- **Use when:** A long-running goal needs strategic continuity and delegated delivery.
- **Scope limits:** Catalog interpretation: Experimental workflow outside the stable plugin.; Catalog interpretation: Its autonomous pursuit of retrospective candidates is broader than a recommendation-only retrospective.
- **Result:** Coordinated goal progress; Historical wiki; Published specs and tickets and implemented integration branch for large builds; Pursued environment improvements and schedule suggestions
- **Requirements:** Background subagents with fresh context windows and context-pointer communication.; Reuse an existing shared wiki and its conventions; agree a location only if none exists.; Installed retro, to-spec, to-tickets and implement-spec procedures and their tracker/build prerequisites; schedules depend on harness support.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Only asks for a wiki location if no shared wiki exists. Explicitly replaces retro's final presentation step with the coordinator's own selection and pursuit; large-build companions retain their seam and ticket-approval checkpoints. Schedules are suggested, not explicitly created.
- **Explicit companions/references:** matt/retro, matt/to-spec, matt/to-tickets, matt/implement-spec
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:7–24](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/chief-of-staff/SKILL.md#L7-L24) — Goal, schedules and fresh background delegation
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:28–38](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/chief-of-staff/SKILL.md#L28-L38) — Existing shared wiki first and its conventions
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:40–54](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/chief-of-staff/SKILL.md#L40-L54) — Dated historical knowledge and new procedure calls with autonomous retro pursuit
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:50–63](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md#L50-L63) — Companion approval before publishing
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:27–42](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md#L27-L42) — Coordinated implementation, PR and tracker effects

### matt/claude-handoff

Writes a redacted temporary handoff and immediately launches a named background Claude agent seeded with it.

- **Role / status:** utility / experimental.
- **Use when:** Continue current work immediately in a fresh Claude background session.
- **Scope limits:** Catalog interpretation: Experimental and dependent on the Claude CLI, rather than a portable launch mechanism.
- **Result:** Temporary handoff summary; Named background Claude agent
- **Requirements:** Claude CLI supporting --bg and --name, with claude agents for job management.; Writable OS temporary directory.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/claude-handoff/SKILL.md:8–10](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/claude-handoff/SKILL.md#L8-L10) — Temporary summary and immediate named launch
- **Evidence:** [skills/in-progress/claude-handoff/SKILL.md:12–18](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/claude-handoff/SKILL.md#L12-L18) — Suggested skills, pointers, redaction and tailored focus

### matt/loop-me

Interviews the user about recurring activities and writes implementable workflow specifications with workspace notes about their world.

- **Role / status:** workflow / experimental.
- **Use when:** Discover repeatable personal or work activities worth specifying.
- **Scope limits:** Catalog interpretation: Experimental specification workflow, not implementation or scheduling.; Catalog interpretation: AI, schedules and human checkpoints are optional design choices.
- **Result:** workflows/*.md specifications; NOTES.md about user context
- **Requirements:** Stateful working directory and shared grilling discipline.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Uses grilling's human decisions and confirmation. A workflow is complete when an implementer would need no further questions; resulting workflow checkpoints are not mandatory.
- **Explicit companions/references:** matt/grilling
- **Evidence:** [skills/in-progress/loop-me/SKILL.md:8–23](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/loop-me/SKILL.md#L8-L23) — Interview, spec writes and optional workflow structure
- **Evidence:** [skills/in-progress/loop-me/SKILL.md:25–32](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/loop-me/SKILL.md#L25-L32) — Implementability and workspace artifacts
- **Evidence:** [skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L28-L30) — Inherited fact delegation and confirmation

### matt/setup-ts-deep-modules

Adds dependency-cruiser checks enforcing public package entry points and private subfolders in TypeScript, then proves enforcement with pass-fail-pass evidence.

- **Role / status:** setup / experimental.
- **Use when:** Enforce imports through package root entry-point files.
- **Scope limits:** Catalog interpretation: Experimental convention, not a universal package architecture.; Catalog interpretation: Merge existing dependency-cruiser configuration rather than overwriting it.
- **Result:** Dependency-cruiser configuration and lint:boundaries wiring; Committed example package; Package README and steering pointer; Observed pass-fail-pass enforcement
- **Requirements:** TypeScript repository and package manager; installs dependency-cruiser as a dev dependency.; Flat package roots; template references tsconfig.json.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Confirms package root if the repository has a different obvious convention; otherwise follows the specified installation and enforcement proof.
- **Explicit companions/references:** matt/codebase-design
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:9–35](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/setup-ts-deep-modules/SKILL.md#L9-L35) — Architecture policy and vocabulary companion
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:41–65](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/setup-ts-deep-modules/SKILL.md#L41-L65) — Environment, confirmation, merge, install and checks
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:69–95](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/setup-ts-deep-modules/SKILL.md#L69-L95) — Example, enforcement proof and documentation
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs:88–93](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs#L88-L93) — Template resolver assumptions

### matt/software-factory

Provides shared language and design questions for an agent system that moves tickets and PRs through disposable runs. It pairs problem-driven task examples with service-slot surveys, duplicate-work controls and gradual automation behind review gates.

- **Role / status:** reference / experimental.
- **Use when:** Explicitly design a software factory's tasks, triggers and service responsibilities.; Compare service-slot needs while planning a gradual automation rollout.
- **Scope limits:** Catalog interpretation: Experimental and user-invoked; do not promote into default engineering routing.; Catalog interpretation: A design reference does not itself deploy, provision or run the factory.; Catalog interpretation: Dated product surveys need fresh primary-source research before product selection.
- **Result:** Service-slot design naming each product or deliberate absence of a separate observability platform; Task definitions covering triggers, reads/writes, next runs, human re-entry and duplicate-work prevention; Ticket-source deduplication plan and staged review gates
- **Requirements:** Conditional reading of task examples and the relevant service survey.; Current primary-source research when choosing a product; surveys explicitly date their orientation to 2026-10.
- **Possible effects:** read
- **Confirmation behavior:** The reference specifies no separate approval for producing a design. The factory being designed starts with human review on every PR, bounded run loops and human re-entry through tracker/git-host changes; runs end rather than waiting for a human.
- **Explicit companions/references:** matt/grilling
- **Evidence:** [skills/in-progress/software-factory/SKILL.md:7–23](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/SKILL.md#L7-L23) — Design-language scope, tasks, runs and disposable runners
- **Evidence:** [skills/in-progress/software-factory/SKILL.md:50–62](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/SKILL.md#L50-L62) — Problem-first examples and gradual automation with brakes
- **Evidence:** [skills/in-progress/software-factory/SKILL.md:77–98](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/SKILL.md#L77-L98) — Conditional current research and complete service/task/source questions
- **Evidence:** [skills/in-progress/software-factory/EXAMPLE-TASKS.md:21–31](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/EXAMPLE-TASKS.md#L21-L31) — Cold automated review, bounded rework and human merge
- **Evidence:** [skills/in-progress/software-factory/RUNNERS.md:67–83](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/RUNNERS.md#L67-L83) — Limits, cost, lifecycle and access questions for choosing runners
- **Evidence:** [skills/in-progress/software-factory/OBSERVABILITY-PLATFORMS.md:5–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/software-factory/OBSERVABILITY-PLATFORMS.md#L5-L17) — Optional platform and export-hook distinction
- **Evidence:** [skills/in-progress/README.md:17–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/README.md#L17-L17) — Explicit suggestion to use alongside grilling

### matt/writing-beats

Shapes fixed raw material into an article through user-selected narrative beats, tracking conceptual prerequisites and writing only the chosen next move.

- **Role / status:** workflow / experimental.
- **Use when:** Choose an article's path one beat at a time from existing material.
- **Scope limits:** Catalog interpretation: Experimental shaping workflow rather than fragment discovery.; Catalog interpretation: Do not write ahead of the user's chosen beat.
- **Result:** Separate article file; Selected beats and grounded conceptual progression
- **Requirements:** Markdown raw material and agreed article output path.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Settles audience prerequisites and offers 2-3 alternatives, waiting for the user's choice before writing each beat.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:9–19](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-beats/SKILL.md#L9-L19) — Fixed input, path and choice-before-write loop
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:27–38](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-beats/SKILL.md#L27-L38) — Conceptual prerequisites and grounding
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:62–65](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-beats/SKILL.md#L62-L65) — One beat at a time and preserving user edits

### matt/writing-fragments

Interviews the author to collect unstructured fragments for later writing, appending them to one raw-material file without imposing an outline.

- **Role / status:** workflow / experimental.
- **Use when:** Explore a subject before deciding an article's structure.
- **Scope limits:** Catalog interpretation: Experimental; article shaping and imposed structure are outside its scope.
- **Result:** Append-only Markdown fragment collection
- **Requirements:** Agreed output path, requested once if absent.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Asks for the file path once, then appends without per-fragment permission. Specific edits and cuts follow user requests.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-fragments/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-fragments/SKILL.md#L9-L17) — Exploration, immediate capture and output path
- **Evidence:** [skills/in-progress/writing-fragments/SKILL.md:69–77](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-fragments/SKILL.md#L69-L77) — Unstructured append rhythm and reread-before-write

### matt/writing-shape

Turns fixed raw material into a separate article through selected openings, agreed blocks and explicit format choices while tracking the reader's conceptual prerequisites.

- **Role / status:** workflow / experimental.
- **Use when:** Collaboratively shape a transcript or fragment pile paragraph by paragraph.
- **Scope limits:** Catalog interpretation: Experimental; excludes new-fragment discovery, editing the source material and publication.
- **Result:** Separate article file; Agreed argument, opening and grounded progression
- **Requirements:** Raw-material Markdown file read in full and agreed article path.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Settles audience prerequisites, requires a chosen opening and writes agreed blocks; the user decides when the article is done.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-shape/SKILL.md:9–26](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-shape/SKILL.md#L9-L26) — Read-only source, full read and user-led shaping loop
- **Evidence:** [skills/in-progress/writing-shape/SKILL.md:55–77](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/in-progress/writing-shape/SKILL.md#L55-L77) — Gap handling, format choices, preserving edits and exclusions

### matt/git-guardrails-claude-code

Installs a Claude Code hook that blocks configured risky Git command patterns before Bash execution, at project or global scope.

- **Role / status:** setup / specialized.
- **Use when:** Configure explicit Git command restrictions in Claude Code.
- **Scope limits:** Catalog interpretation: Claude-specific hooks are not a portable policy engine.; Catalog interpretation: Regex blocking is not complete command-security verification.
- **Result:** Executable copied hook; Merged Claude settings configuration
- **Requirements:** Claude Code Bash hooks, Bash and jq.; Writable project or global .claude configuration.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Asks project versus global scope and whether to customize the blocked patterns.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/git-guardrails-claude-code/SKILL.md:22–39](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/SKILL.md#L22-L39) — Scope choice and hook installation
- **Evidence:** [skills/misc/git-guardrails-claude-code/SKILL.md:81–95](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/SKILL.md#L81-L95) — Preserve settings, customize and test blocking
- **Evidence:** [skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh:3–21](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh#L3-L21) — jq parsing and regex matching mechanism

### matt/migrate-to-shoehorn

Migrates TypeScript test fixtures from broad type assertions to shoehorn helpers for partial or intentionally invalid data, then verifies types.

- **Role / status:** workflow / specialized.
- **Use when:** Test fixtures require cumbersome full objects or broad as assertions.
- **Scope limits:** Catalog interpretation: The source explicitly restricts shoehorn to tests.
- **Result:** Migrated fixtures; Installed @total-typescript/shoehorn dependency; Typecheck result
- **Requirements:** TypeScript tests and @total-typescript/shoehorn; source installation uses npm.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Asks which test files and data needs motivate migration before installation and edits.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/migrate-to-shoehorn/SKILL.md:10–12](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/migrate-to-shoehorn/SKILL.md#L10-L12) — Partial data and test-only scope
- **Evidence:** [skills/misc/migrate-to-shoehorn/SKILL.md:97–118](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/migrate-to-shoehorn/SKILL.md#L97-L118) — Helper choice, questions, installation, migration and typecheck

### matt/scaffold-exercises

Creates numbered course exercise stubs following AI Hero conventions, validates them with the course linter and commits the structure.

- **Role / status:** utility / specialized.
- **Use when:** Turn an AI Hero-style course plan into correctly named exercise directories.
- **Scope limits:** Catalog interpretation: Requires the course-specific convention and linter rather than serving as a generic course generator.
- **Result:** Numbered section/exercise directories; Variant readmes; Linted and committed scaffold
- **Requirements:** pnpm ai-hero-cli internal lint, Git repository and course plan.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:8–25](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/scaffold-exercises/SKILL.md#L8-L25) — Linter, commit and course directory conventions
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:29–50](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/scaffold-exercises/SKILL.md#L29-L50) — Files and scaffold verification
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:65–71](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/scaffold-exercises/SKILL.md#L65-L71) — History-preserving moves and relint

### matt/setup-pre-commit

Installs Husky, lint-staged and Prettier for commit-time formatting and available type/test scripts. A commit through the new hook verifies the setup.

- **Role / status:** setup / specialized.
- **Use when:** Add commit-time formatting and checks to a JavaScript repository.
- **Scope limits:** Catalog interpretation: This is a JavaScript/Husky recipe.; Catalog interpretation: Missing typecheck/test scripts are omitted and reported, not invented.
- **Result:** Husky hook and lint-staged config; Dependency/prepare updates and conditional Prettier config; Smoke-test commit
- **Requirements:** npm, pnpm, yarn or Bun; installs husky, lint-staged and prettier.; Recipe targets Husky v9+.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:19–35](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md#L19-L35) — Package manager and dependency setup
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:39–59](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md#L39-L59) — Checks, missing-script adaptation and formatting
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:73–85](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md#L73-L85) — Verification and commit through hook

### matt/grill-me

Runs the shared interviewing primitive to sharpen a plan or design without adding repository documentation.

- **Role / status:** workflow / stable.
- **Use when:** Stress-test an idea without a working directory.
- **Scope limits:** Catalog interpretation: Prefer grill-with-docs when persistent project language and decisions belong in a repository.
- **Result:** Confirmed shared understanding
- **Requirements:** Skill invocation support for grilling; fresh-context fact-finding subagents when needed.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Inherits grilling's rounds of user decisions and final confirmation before action.
- **Explicit companions/references:** matt/grilling
- **Evidence:** [skills/productivity/grill-me/SKILL.md:7–7](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grill-me/SKILL.md#L7-L7) — Wrapper invokes grilling
- **Evidence:** [skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L28-L30) — Fresh-context research and final user confirmation
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:85–86](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md#L85-L86) — Stateless route versus repository wrapper

### matt/grilling

Interviews the user in rounds of decisions whose prerequisites are already settled. The agent investigates environmental facts while the user owns the choices.

- **Role / status:** workflow / stable.
- **Use when:** Stress-test a plan, decision or idea until assumptions are explicit.
- **Scope limits:** Catalog interpretation: Do not ask the user facts the agent can investigate.; Catalog interpretation: Do not act on the plan before final shared-understanding confirmation.
- **Result:** Settled design tree; Confirmed shared understanding
- **Requirements:** Fresh-context subagents for environmental fact-finding when needed.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Waits after each round and requires final user confirmation before acting. Independent questions continue while factual exploration runs.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/grilling/SKILL.md:6–8](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L6-L8) — Design tree and decision frontier
- **Evidence:** [skills/productivity/grilling/SKILL.md:24–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L24-L30) — Recommendations, fresh-context fact research and human decision gates

### matt/handoff

Writes a redacted portable handoff for another agent, referencing existing artifacts instead of duplicating them.

- **Role / status:** utility / stable.
- **Use when:** Move work to another harness, directory or colleague.; Fork a side task while preserving the current discussion.
- **Scope limits:** Catalog interpretation: The document itself neither launches nor messages another agent.
- **Result:** Temporary Markdown handoff with suggested skills
- **Requirements:** Writable OS temporary directory.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/handoff/SKILL.md:8–16](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/handoff/SKILL.md#L8-L16) — Temporary artifact, suggested skills, pointers, redaction and focus

### matt/teach

Builds a persistent learning workspace of short HTML lessons, reusable assets, references, trusted sources and evidence of understanding tied to the learner's mission.

- **Role / status:** teaching / stable.
- **Use when:** Learn a topic over multiple sessions with cumulative practice and reference materials.
- **Scope limits:** Catalog interpretation: A quick explanation without a course workspace is a different scope.; Catalog interpretation: Material covered alone is not evidence of learning.
- **Result:** MISSION.md and curated RESOURCES.md; HTML lessons and reference sheets; Reusable assets, glossary and learning records
- **Requirements:** Current working directory becomes the teaching workspace.; Access to high-trust material; optional CLI opener for lessons.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Questions the user to establish a missing mission and confirms before changing it. Respects preferences about community participation.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/teach/SKILL.md:8–20](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md#L8-L20) — Persistent workspace and artifacts
- **Evidence:** [skills/productivity/teach/SKILL.md:49–69](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md#L49-L69) — Short lessons, opener and reusable assets
- **Evidence:** [skills/productivity/teach/SKILL.md:73–95](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md#L73-L95) — Mission confirmation and trusted source grounding
- **Evidence:** [skills/productivity/teach/SKILL.md:116–120](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md#L116-L120) — Community preference
- **Evidence:** [skills/productivity/teach/LEARNING-RECORD-FORMAT.md:29–42](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/LEARNING-RECORD-FORMAT.md#L29-L42) — Record understanding or prior knowledge rather than activity
- **Evidence:** [skills/productivity/teach/GLOSSARY-FORMAT.md:29–35](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/GLOSSARY-FORMAT.md#L29-L35) — Glossary records demonstrated understanding

### matt/to-questionnaire

Creates a discovery questionnaire for an external knowledge holder after clarifying the recipient and the decisions or facts needed back.

- **Role / status:** utility / stable.
- **Use when:** A decision depends on knowledge held by another person.
- **Scope limits:** Catalog interpretation: Interview the user about the send, not facts they cannot know.; Catalog interpretation: Writing the questionnaire does not send it.
- **Result:** Local to-questionnaire-<slug>.md with prioritized questions and answer stubs
- **Requirements:** User identifies recipient role/expertise and the required outcome.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Uses two exchanges about the recipient and required outcome before writing; no send operation is specified.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/to-questionnaire/SKILL.md:7–20](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/to-questionnaire/SKILL.md#L7-L20) — Discovery scope, two exchanges and local output
- **Evidence:** [skills/productivity/to-questionnaire/SKILL.md:34–52](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/to-questionnaire/SKILL.md#L34-L52) — Answer guidance, prioritized questions and closing catch-all

### matt/wait-what

Re-explains the last message with missing context, simplified English and established project terms.

- **Role / status:** utility / stable.
- **Use when:** The previous explanation did not land.
- **Scope limits:** Catalog interpretation: Clarifying a message need not restart its underlying workflow.
- **Result:** Clearer contextualized explanation
- **Requirements:** GLOSSARY.md or mapped glossary when present; source requests ASD-STE100 style.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/wait-what/SKILL.md:7–7](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/wait-what/SKILL.md#L7-L7) — Re-pitch context, simplified English and glossary vocabulary

### matt/writing-for-agents

Guides documents consumed by agents through conditional context pointers, information hierarchy, explicit completion criteria and a single source for each meaning. A supporting guide covers skill invocation and routers.

- **Role / status:** reference / stable.
- **Use when:** Create or edit skills, steering files or agent-facing references.
- **Scope limits:** Catalog interpretation: Not a general human-audience prose guide.; Catalog interpretation: Source invocation mechanics are host assumptions, not universal portability guarantees.
- **Result:** More predictable agent instructions; Sharper pointers and completion criteria
- **Requirements:** Read SKILL-MECHANICS.md when authoring a skill.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:6–18](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md#L6-L18) — Scope, supporting mechanics and pointer design
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:31–59](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md#L31-L59) — Hierarchy, co-location, completion and splitting
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:78–81](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md#L78-L81) — Single-source, environmental lookup and pruning
- **Evidence:** [skills/productivity/writing-for-agents/SKILL-MECHANICS.md:9–22](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL-MECHANICS.md#L9-L22) — Host-oriented invocation distinctions and non-executing router

### poteto/architect

Traces every system a change touches, sketches two type and module shapes, and selects the one with clear state ownership and the least caller knowledge. Large or contested designs route to arena.

- **Role / status:** workflow / stable.
- **Use when:** Settle types, signatures and module boundaries before writing boundary-crossing code.; Repeated workarounds suggest the current shape needs redesign.
- **Scope limits:** Catalog interpretation: This leaf supplies pre-code design guidance; it does not specify an implementation or shipping loop.; Catalog interpretation: For a large or contested design, follow its conditional arena route rather than interpreting it as a solo sketch.
- **Result:** Two alternative type, signature and module sketches; Selected shape with state ownership and caller-facing rationale
- **Requirements:** Read access to every system the change touches.; For the conditional arena branch, the arena subagent, model-role and isolated-output prerequisites.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill. The current leaf has no separate implementation phase or checkpoint policy.
- **Explicit companions/references:** poteto/arena
- **Evidence:** [pstack/skills/architect/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/architect/SKILL.md#L9-L11) — Tracing, two sketches, ownership criteria, redesign and conditional arena; no implementation stages.
- **Evidence:** [pstack/skills/arena/SKILL.md:13–18](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L13-L18) — Conditional arena branch brings model selection and isolated candidate outputs.

### poteto/arena

Runs competing attempts at one shared brief, scores them against a task-specific rubric, and synthesizes one verified artifact. A cross-vendor judge is attempted under the configured pool and fallback rules.

- **Role / status:** workflow / stable.
- **Use when:** One artifact admits several plausible designs.; You want a bakeoff rather than separate investigation slices.
- **Scope limits:** Catalog interpretation: Use swarm for partitioned coverage without synthesizing competing artifacts.; Catalog interpretation: Avoid for a settled, trivial shape where multiple full attempts add little.
- **Result:** Synthesized artifact; Synthesis note with selected base, grafts, rejected choices and verification
- **Requirements:** Cursor Task background subagents, todolist support and isolated candidate worktrees or scratch directories.; Role lines in ~/.cursor/rules/pstack-models.mdc override the stated panel defaults; aliases and model-slug fallback depend on the host.; The documented Claude Code adapter maps Task to Agent and worktree isolation; non-Claude seats inherit the session model there, so cross-vendor judging is not universally preserved.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/poteto-mode, poteto/principle-separate-before-serializing-shared-state, poteto/principle-redesign-from-first-principles, poteto/principle-prove-it-works
- **Evidence:** [pstack/skills/arena/SKILL.md:13–18](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L13-L18) — Shared brief, rubric, current runner families and isolated outputs.
- **Evidence:** [pstack/skills/arena/SKILL.md:22–28](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L22-L28) — Background candidates and conditional cross-vendor judging with explicit fallbacks.
- **Evidence:** [pstack/skills/arena/SKILL.md:32–44](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L32-L44) — Read all candidates, select, graft or reframe, then verify.
- **Evidence:** [pstack/skills/arena/SKILL.md:48–48](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L48-L48) — Required synthesis note including skipped judge, convergence, dropouts and verification.
- **Evidence:** [pstack/docs/harness/claude-code.md:19–38](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L19-L38) — Claude Code tool, isolation and model mappings.

### poteto/automate-me

Drafts or refreshes a personal mode skill from repeated preferences in workspace-scoped history and a direct interview. Existing mode skills are revised in place by default and delivered for review through a PR.

- **Role / status:** workflow / stable.
- **Use when:** Capture a recurring personal working style for agents.; Refresh an existing personal mode with recent evidence.
- **Scope limits:** Catalog interpretation: Use ordinary skill authoring for one narrow workflow.; Catalog interpretation: Do not mine unrelated projects to infer preferences.
- **Result:** Personal -mode SKILL.md; Worktree commit and pull request
- **Requirements:** Cursor built-in create-skill, AskQuestion, workspace agent-transcripts path and Cursor skill directories.; Git and pull-request workflow; user handle or chosen identifier.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Confirms whether to update an existing mode unless already requested, asks structured preference questions, and shows the draft for feedback. Ships through a PR rather than pushing directly to main.
- **Explicit companions/references:** poteto/unslop, poteto/poteto-mode
- **Evidence:** [pstack/skills/automate-me/SKILL.md:15–31](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/automate-me/SKILL.md#L15-L31) — Existing-mode intent, since-last-edit refresh and workspace-limited transcript mining.
- **Evidence:** [pstack/skills/automate-me/SKILL.md:40–46](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/automate-me/SKILL.md#L40-L46) — Cross-slice evidence and structured preference interview.
- **Evidence:** [pstack/skills/automate-me/SKILL.md:67–83](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/automate-me/SKILL.md#L67-L83) — Built-in authoring, destination, default invocation flag, user feedback and PR delivery.
- **Evidence:** [pstack/skills/automate-me/SKILL.md:100–103](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/automate-me/SKILL.md#L100-L103) — Narrow task-specific workflows use regular skill authoring instead.

### poteto/benchmark-checklist

Checks whether a measured performance claim is meaningful, repeatable and about completed work. Produces a verdict with units, spread and the identified limiter.

- **Role / status:** workflow / stable.
- **Use when:** Report a measured speedup or regression.; Choose between implementations or validate an optimization harness.
- **Scope limits:** Catalog interpretation: Do not select an option from an untuned comparison.; Catalog interpretation: Use the explicitly lighter path only for a requested ballpark.
- **Result:** Performance verdict; Primary measurement with run count, range and limiter evidence
- **Requirements:** A runnable benchmark and realistic workload.; Host commands uptime and nproc; profiling tools appropriate to the runtime or OS, with Linux-specific examples.
- **Possible effects:** read, execute, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:9–17](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/benchmark-checklist/SKILL.md#L9-L17) — Measured-claim scope, explicit ballpark exception and machine/script preflight.
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:21–27](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/benchmark-checklist/SKILL.md#L21-L27) — Limiter, production tuning, limits, errors, repeated runs, user relevance and completed work.
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:31–39](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/benchmark-checklist/SKILL.md#L31-L39) — Verdict rules, evidence and perf/hillclimb integration.

### poteto/blast-radius

Finds downstream breakage that a diff or caller list can miss and executes a small proof of the safety fact the change depends on.

- **Role / status:** workflow / stable.
- **Use when:** A small change has uncertain effects outside its immediate callers.; An integration or teardown change depends on library behavior.
- **Scope limits:** Catalog interpretation: Use how for a runtime walkthrough without a proposed change.; Catalog interpretation: Do not equate a persuasive writeup with an executed safety proof.
- **Result:** Safety fact proved or marked unproven; Confirmed risks, cleared cases and cheapest regression check
- **Requirements:** The proposed change and its PR/commits, pinned shipped library sources and local patches.; An executable script, test or real-app surface able to prove the load-bearing safety fact.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/arena, poteto/unslop
- **Evidence:** [pstack/skills/blast-radius/SKILL.md:11–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/blast-radius/SKILL.md#L11-L29) — How/why relationship and explicit proof ladder through real-code and real-app execution.
- **Evidence:** [pstack/skills/blast-radius/SKILL.md:33–38](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/blast-radius/SKILL.md#L33-L38) — Pinned library and downstream investigation, executable proof and optional arena.
- **Evidence:** [pstack/skills/blast-radius/SKILL.md:42–50](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/blast-radius/SKILL.md#L42-L50) — Risks, cleared cases, unproven safety facts, regression proof and unslop/privacy requirements.

### poteto/bro

Restates the previous assistant message in simpler, shorter language without jargon.

- **Role / status:** utility / stable.
- **Use when:** The last reply was hard to understand.
- **Scope limits:** Catalog interpretation: Use teach when the underlying topic needs fresh investigation.
- **Result:** Plain-language restatement
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/bro/SKILL.md:2–7](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/bro/SKILL.md#L2-L7) — Restates the last assistant message in concise plain language.

### poteto/correct

Finds repeated agent mistake classes and changes repository structure or enforcement so they are harder to repeat. Demonstrates each new check on a real past mistake.

- **Role / status:** workflow / stable.
- **Use when:** The same agent mistake has occurred at least twice.; A documented repository rule keeps being ignored.
- **Scope limits:** Catalog interpretation: Do not turn a one-off preference into a repeated mistake class without evidence.; Catalog interpretation: Prefer structural enforcement over adding more instructions alone.
- **Result:** One commit per addressed mistake class; Checks demonstrated failing on past mistakes; Rule-to-enforcement table and rationale
- **Requirements:** Repository commits, reverts, review comments and agent instruction files; local and CI check commands.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Exceptions require a reason, expiry date and human approval on the offending line. No general implementation checkpoint is specified.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/correct/SKILL.md:15–22](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/correct/SKILL.md#L15-L22) — Repeated-class threshold and ordered architecture/types/lint/tests/docs enforcement.
- **Evidence:** [pstack/skills/correct/SKILL.md:26–32](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/correct/SKILL.md#L26-L32) — One commit per class, failing real-past-mistake proof, human-approved exceptions and enforcement table.

### poteto/create-formal-verification-skill

Verifies one costly property that tests rarely reach and leaves a reproducible project-local skill to check it again. The handoff states code coverage, assumptions, bounds and the synchronization commit, with a demonstrated failing variant.

- **Role / status:** workflow / stable.
- **Use when:** Concurrency, retries or state-machine ordering threaten an important invariant.; Code needs bounded or stronger verification beyond example tests.
- **Scope limits:** Catalog interpretation: Do not claim a bounded model proves the whole system.; Catalog interpretation: Report product bugs rather than changing product code without a request.
- **Result:** Verification model or code-level harness; Project-local verify skill with coverage and sync commit; Broken-variant demonstration and plain-language findings
- **Requirements:** Access to the relevant real code and an installable reproducible verification tool suited to the property.; TLA+ is the default for bad-order/interleaving questions in any language; code-level questions use a code verifier, or generated tests against real code when none exists.; A TLA+ result is read through the statechart skill by name, without copying its machine-specific commands into the generated skill.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Asks only for facts not observable in the code. Product code changes require the user to ask.
- **Explicit companions/references:** poteto/statechart, poteto/maintain-formal-verification-skill
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:13–19](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-formal-verification-skill/SKILL.md#L13-L19) — Code-selected target and question-dependent verification choice; TLA+ default and generated-input fallback.
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:23–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-formal-verification-skill/SKILL.md#L23-L29) — Faithful atomic steps, failure demonstration, product-code boundary, bounds and sync commit.
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:33–39](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-formal-verification-skill/SKILL.md#L33-L39) — Generated skill ownership, statechart-by-name dependency and scratch break proof.
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:43–43](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-formal-verification-skill/SKILL.md#L43-L43) — Plain-language handoff and maintenance route.

### poteto/create-verification-skill

Creates a repository-specific skill that launches, health-checks, drives and cleans up the real app. Seeds a user-facing feature map and executes one complete journey before handoff.

- **Role / status:** workflow / stable.
- **Use when:** A project lacks a reliable way for agents to prove observable behavior.; An app needs a launch, doctor, drive and evidence recipe.
- **Scope limits:** Catalog interpretation: Do not generate untested steps against a broken startup base.; Catalog interpretation: Do not drive a shared user instance when isolation is unavailable.
- **Result:** Project-local verify-<app> skill with launch, doctor, drive, evidence, cleanup and documented helpers; Feature-map index and initial user-facing feature journey files; Executed full journey with proof artifacts confirmed to survive cleanup
- **Requirements:** A runnable app and repository launch commands.; An appropriate harness such as browser/CDP, existing Playwright/Cypress, HTTP or isolated PTY/tmux.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Asks the user only what cannot be observed from the repository. No general approval gate is specified.
- **Explicit companions/references:** poteto/maintain-verification-skill
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:13–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/SKILL.md#L13-L21) — Repository interview, existing harness first, isolation and working-base prerequisite.
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:25–32](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/SKILL.md#L25-L32) — Generated sections, usable launch, real-path/side-effect proof and evidence-preserving cleanup.
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:36–40](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/SKILL.md#L36-L40) — Feature map, all entry points, complete execution proof and stand-in limitations.
- **Evidence:** [pstack/skills/create-verification-skill/references/feature-map-example/README.md:35–42](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/references/feature-map-example/README.md#L35-L42) — Worked feature file shape and user-facing scope.
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:44–44](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/create-verification-skill/SKILL.md#L44-L44) — Offer maintenance without unsolicited scheduling.

### poteto/figure-it-out

Designs a custom, auditable workflow when bundled playbooks do not fit or a change is ambitious. Runs small hypothesis-driven units against an explicit completion predicate.

- **Role / status:** workflow / stable.
- **Use when:** A large migration needs a task-specific sequence of verifiable units.; A human will review a long run after stepping away.
- **Scope limits:** Catalog interpretation: Use a narrower playbook when one fits a routine focused change.; Catalog interpretation: Use Multi-phase plan when only a written plan is authorized; this workflow designs phases and then executes them.
- **Result:** Written bespoke phase list; Verified units and decision trail; Final predicate verdict with open gaps
- **Requirements:** Todo-list support, executable verification harness and isolated branches or worktrees for writers.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Presents framing and tradeoffs before a long commitment; explicitly says a multi-hour run earns one checkpoint, while reversible work proceeds.
- **Explicit companions/references:** poteto/poteto-mode, poteto/architect, poteto/arena, poteto/show-me-your-work, poteto/principle-prove-it-works, poteto/principle-never-block-on-the-human, poteto/principle-foundational-thinking, poteto/principle-separate-before-serializing-shared-state, poteto/principle-laziness-protocol, poteto/principle-sequence-verifiable-units, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:9–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/figure-it-out/SKILL.md#L9-L23) — Workflow-first deliverable, falsifiable predicate, rigor and multi-hour checkpoint.
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:27–34](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/figure-it-out/SKILL.md#L27-L34) — Small independently landable units, harness first, architectural design and isolated delegation.
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:38–46](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/figure-it-out/SKILL.md#L38-L46) — Experiment loop, worker/judge separation, honest verdicts and canonical decision trail.
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:50–52](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/figure-it-out/SKILL.md#L50-L52) — Real-product final proof and handoff.

### poteto/how

Uses one read-only explainer to trace existing code and explain its architecture, runtime flow or ownership at a senior engineer’s level. The parent presents that explanation with only light edits.

- **Role / status:** workflow / stable.
- **Use when:** Understand how a subsystem works before changing it.; Determine which module owns a behavior or where new code should live.
- **Scope limits:** Catalog interpretation: Use why for historical motivation rather than runtime mechanics.; Catalog interpretation: This explains existing code and ownership; implementation requires a separately scoped task.
- **Result:** Code-grounded architecture, runtime-flow or ownership explanation from one readonly explorer
- **Requirements:** Code read/search access and a Cursor generalPurpose readonly Task subagent.; The Claude Code adapter maps readonly to Explore, adds a no-edit brief and checks git status afterward.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/how/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/how/SKILL.md#L3-L3) — Architecture, runtime and placement/ownership scope.
- **Evidence:** [pstack/skills/how/SKILL.md:9–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/how/SKILL.md#L9-L21) — One read-only explainer, ambiguity handled by stating interpretation, lightly edited presentation.
- **Evidence:** [pstack/docs/harness/claude-code.md:19–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L19-L23) — Host-specific readonly mapping.

### poteto/in-your-own-words

Restates the user's apparent goals and the underlying problem before work proceeds.

- **Role / status:** utility / stable.
- **Use when:** Check whether the agent understood the requested outcome.
- **Scope limits:** Catalog interpretation: Use a planning or research workflow when the problem still needs investigation.
- **Result:** Restated goals and problem
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/in-your-own-words/SKILL.md:2–7](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/in-your-own-words/SKILL.md#L2-L7) — Restatement of apparent user goals and problem, without a larger workflow.

### poteto/interrogate

Has configured adversaries try to break a change or design with executable repros in isolated worktrees. The coordinator reruns each claim and reports all verified intent-breaking failures without applying fixes.

- **Role / status:** workflow / stable.
- **Use when:** Challenge a branch diff or supplied scope with independent attempts to make it fail.; Test a design or plan using a prototype or a probe against the current tree.
- **Scope limits:** Catalog interpretation: Use a source-only review when worktrees, repro writes or code execution are forbidden.; Catalog interpretation: Style claims and speculative future risks without an executed failure do not survive this workflow.
- **Result:** Intent restatement; Verified findings with exact commands, observed and required outputs and finding adversaries; Per-adversary counts and reasons for dropped findings
- **Requirements:** A supplied scope or branch merge-base diff through the working tree, with enough evidence to state intent.; Arena framing/fan-out tools, configured interrogate reviewers and isolated worktrees containing the scope’s uncommitted changes.; An executable real-code probe, failing test or prototype for each reported finding; coordinator must rerun it.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Asks the user when intent is unclear. Explicitly reports findings without applying fixes; repros remain in each adversary’s worktree.
- **Explicit companions/references:** poteto/in-your-own-words, poteto/arena
- **Evidence:** [pstack/skills/interrogate/SKILL.md:9–19](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/interrogate/SKILL.md#L9-L19) — No-fixes boundary, intent restatement, default scope, isolated adversaries and required runs.
- **Evidence:** [pstack/skills/interrogate/SKILL.md:23–31](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/interrogate/SKILL.md#L23-L31) — Parent reruns, deduplication, no judge/base/graft phases and full verified/dropped output.
- **Evidence:** [pstack/skills/arena/SKILL.md:17–22](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/arena/SKILL.md#L17-L22) — Imported runner configuration, isolated outputs and background fan-out.

### poteto/ketchup

Catches the user up on changes since their last message and lists every outstanding decision with enough context to act from the reply.

- **Role / status:** utility / stable.
- **Use when:** Return to a chat after autonomous work or agent results.; See what is done and which calls still belong to you.
- **Scope limits:** Catalog interpretation: Use recall for work spanning recent chats.; Catalog interpretation: Do not start jobs, change code or post externally while preparing this update.
- **Result:** Concise current-state update; Existing inline visuals; Complete, decidable action-item list
- **Requirements:** Read access to the current PR, check and agent state when this chat touched them.; Existing screenshots or recordings; Mermaid or visualize for suitable derived diagrams.
- **Possible effects:** read
- **Confirmation behavior:** Reports approvals and irreversible actions waiting on the human; does not take those actions during this read-only update.
- **Explicit companions/references:** poteto/bro
- **Evidence:** [pstack/skills/ketchup/SKILL.md:9–19](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup/SKILL.md#L9-L19) — Current-chat window, plain voice, read-only collection and every outstanding user-owned call.
- **Evidence:** [pstack/skills/ketchup/SKILL.md:23–33](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup/SKILL.md#L23-L33) — Self-contained decisions, evidence, per-item risks and no truncating item lists.
- **Evidence:** [pstack/skills/ketchup/SKILL.md:37–43](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup/SKILL.md#L37-L43) — Small factual diagrams and embedding existing screenshots/video without starting apps or inventing screens.

### poteto/ketchup-video

Delivers the ketchup catch-up as a short silent slide video, with outstanding decisions retained as text under it.

- **Role / status:** utility / stable.
- **Use when:** A visual catch-up is easier to follow as a short animated sequence.
- **Scope limits:** Catalog interpretation: Use ordinary ketchup when video production adds little.; Catalog interpretation: Use only existing work evidence rather than inventing screens.
- **Result:** Short silent landscape slide video with burned-in subtitles, checked at chat size; Text of outstanding user decisions and remaining agent-owned work
- **Requirements:** A video renderer and existing screenshots, recordings, diffs or data.; A scratch output location outside the repository.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/ketchup
- **Evidence:** [pstack/skills/ketchup-video/SKILL.md:9–19](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup-video/SKILL.md#L9-L19) — Ketchup inheritance, outside-repo render exception, window, real artifacts and failure fallback.
- **Evidence:** [pstack/skills/ketchup-video/SKILL.md:23–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/ketchup-video/SKILL.md#L23-L29) — Readable subtitle strip, word-based holds, measured timing and rendered-file verification.

### poteto/maintain-formal-verification-skill

Reconciles formal checks with code changes since their synchronization commit. Separates verification drift from real product bugs and proves updated checks can still fail.

- **Role / status:** workflow / stable.
- **Use when:** Merges or refactors changed verified code without rechecking its model.; An old passing formal check may describe stale behavior.
- **Scope limits:** Catalog interpretation: Use create-formal-verification-skill when no project check exists.; Catalog interpretation: Keep product fixes separate and do not weaken properties to obtain a pass.
- **Result:** Separate verification-only change and updated coverage/sync records; Per-check in sync, updated, bug or blocked outcome; Replayed counterexamples and evidence updated checks still fail on real scratch breaks
- **Requirements:** Existing project-local formal verification skill, its verifier command and git history.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Product code changes require a user request. Properties change only with cited evidence that the intended promise changed.
- **Explicit companions/references:** poteto/create-formal-verification-skill
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:9–24](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-formal-verification-skill/SKILL.md#L9-L24) — Drift maintenance, four outcomes and verification-only edit boundary.
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:28–38](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-formal-verification-skill/SKILL.md#L28-L38) — Locate sync base, baseline run, inspect covered changes and update from code rather than desired result.
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:40–44](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-formal-verification-skill/SKILL.md#L40-L44) — Demonstrate fail-capability, distinguish real-code bug from model error and do not advance blocked syncs.
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:50–58](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-formal-verification-skill/SKILL.md#L50-L58) — Plain-language per-check report and separate verification change.

### poteto/maintain-verification-skill

Audits every mapped feature from source and drives every feature live. Ships at most one PR limited to proven verification documentation or harness corrections.

- **Role / status:** workflow / stable.
- **Use when:** An existing app verification skill or feature map may have drifted.
- **Scope limits:** Catalog interpretation: Use create-verification-skill when no suitable skill exists.; Catalog interpretation: Do not repair product regressions inside the verification-maintenance change.
- **Result:** Clean, changed or blocked outcome; Feature coverage and drift notes in scratch storage; At most one PR of proven skill/map/harness corrections
- **Requirements:** Existing project-local verification skill with feature map and runnable drive harness.; Parallel readonly source-reader subagents; coordinator-owned serial live driving or isolated CLI sessions.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Asks which verification skill to target when several exist. Product-code edits are explicitly excluded.
- **Explicit companions/references:** poteto/create-verification-skill
- **Evidence:** [pstack/skills/maintain-verification-skill/SKILL.md:9–25](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-verification-skill/SKILL.md#L9-L25) — Feature-level scope, clean/changed/blocked outcomes, directory-only edits and target selection.
- **Evidence:** [pstack/skills/maintain-verification-skill/SKILL.md:29–35](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-verification-skill/SKILL.md#L29-L35) — Parallel read-only source readers; coordinator live driving, doctor/retry/reset, evidence preservation and product-gap separation.
- **Evidence:** [pstack/skills/maintain-verification-skill/SKILL.md:37–39](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/maintain-verification-skill/SKILL.md#L37-L39) — At most one proven-correction PR; scratch notes, no PR for clean or blocked.

### poteto/make-bot-ui

Builds a server-backed page whose buttons wake a Grok Bot through a webhook routine, then exposes the page on a Tailscale network.

- **Role / status:** workflow / stable.
- **Use when:** A custom dashboard or control page should wake a Grok Bot.
- **Scope limits:** Catalog interpretation: Do not select for a generic static website without a bot webhook.; Catalog interpretation: Treat Cursor routine and secret-request features as host requirements, not portable APIs.
- **Result:** Webhook routine; Local UI and server-side webhook forwarding; Tailnet URLs and verified harmless probe
- **Requirements:** Cursor/Grok Bot update_state routine creation and SendToUser secret-request cards.; User-provided webhook URL and sender key through the secret channel.; Local server and Tailscale; installation can require sudo and network access.
- **Possible effects:** read, local_write, external_write, execute, configure
- **Confirmation behavior:** Waits on any routine confirmation card. Stops after requesting the sender key through a secret card. Tailscale enrollment requires the user's browser approval.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:11–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md#L11-L23) — Server-side secret boundary and routine creation confirmation.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:27–51](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md#L27-L51) — Routine-panel URL, secret-request card and no secret in chat.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:55–73](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md#L55-L73) — Local server bind, authenticated one-try POST, harmless probe and fallback log.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:77–103](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md#L77-L103) — Existing-node reuse, optional Tailscale install and browser enrollment approval.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:107–115](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/make-bot-ui/SKILL.md#L107-L115) — Webhook body is untrusted data and shared field contract.
- **Evidence:** [pstack/docs/harness/claude-code.md:59–68](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L59-L68) — Automations and secret-request calls are Cursor-only and skipped in Claude Code.

### poteto/no-comments

Delegates a scoped comment pass to Comment Sicko, audits deletions and flags, then implements accepted root-cause fixes within the same fence. Claimed constraints can be offered an approved type, runtime, test or lint encoding.

- **Role / status:** workflow / stable.
- **Use when:** Clean comments and their accepted workaround causes in caller-supplied files or a base-branch diff before review.; Replace an in-scope claimed constraint with an explicit approved enforcement mechanism.
- **Scope limits:** Catalog interpretation: This is not report-only comment criticism; it deletes comments and implements accepted in-scope fixes.; Catalog interpretation: Do not use root-cause principles to authorize edits outside the supplied scope.; Catalog interpretation: A refusal to encode does not preserve an unprotected constraint comment; the source still deletes it and reports the constraint open.
- **Result:** Audited scoped comment deletions and any exception-supported restorations; Architect sketch when accepted flags need a design, followed by smallest in-scope fixes; Report of reruns, encoding offers/results, unenforced constraints and remaining work
- **Requirements:** Cursor Task comment-sicko agent, caller scope or base-branch diff including working tree; main is the fallback base.; The comment-sicko agent’s exact keep exceptions and suppression rules; symbol tracing or why for thin IMPORTANT/do-not-remove claims.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Constraint encodings wait for interactive approval; unattended/eval runs need caller pre-approval. The source says unapproved encodings still result in deleting the comment and reporting the constraint open.
- **Explicit companions/references:** poteto/poteto-mode, poteto/why, poteto/architect, poteto/principle-fix-root-causes, poteto/principle-redesign-from-first-principles
- **Evidence:** [pstack/skills/no-comments/SKILL.md:15–20](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/no-comments/SKILL.md#L15-L20) — Scope, fresh agent, report/diff audit, suppressions, ambiguity policy and one rerun before failure.
- **Evidence:** [pstack/skills/no-comments/SKILL.md:21–24](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/no-comments/SKILL.md#L21-L24) — Sketch-only architect, scoped implementation, approval for encodings and open-constraint deletion behavior.
- **Evidence:** [pstack/agents/comment-sicko.md:14–30](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/agents/comment-sicko.md#L14-L30) — Agent keep list, correctness suppressions, historical proof and no application-code edits by reviewer.

### poteto/poteto-help

Answers pstack help questions with one adapted prompt and a link to the owning source, without starting a help question’s work. An actual request to do work is explicitly handed to poteto-mode instead.

- **Role / status:** router / stable.
- **Use when:** Find the right pstack entry point without memorizing its skills.; Understand setup, cost, host support or why a run drifted.
- **Scope limits:** Catalog interpretation: Help questions should not start a token-consuming workflow.; Catalog interpretation: Read the destination skill before recommending its detailed behavior.
- **Result:** Direct answer with public source link; At most one tailored example prompt; Optional need-category question
- **Requirements:** Read access to installed pstack leaves, guide pages and setup/model/verification state relevant to the question.; Cursor setup and mode assumptions; the documented Claude Code adapter for that host, including unavailable-feature handling.
- **Possible effects:** read, local_write, external_write, execute, delegate, configure
- **Confirmation behavior:** Help questions return a prompt for the user to send rather than starting the workflow. May ask one need-category question and offer setup once; actual work requests route to poteto-mode and its task-specific gates.
- **Explicit companions/references:** poteto/setup-pstack, poteto/poteto-mode, poteto/in-your-own-words, poteto/sharpen, poteto/how, poteto/why, poteto/teach, poteto/recall, poteto/ketchup, poteto/ketchup-video, poteto/blast-radius, poteto/architect, poteto/arena, poteto/swarm, poteto/interrogate, poteto/tdd, poteto/typescript-best-practices, poteto/no-comments, poteto/unslop, poteto/technical-writing, poteto/bro, poteto/create-verification-skill, poteto/maintain-verification-skill, poteto/create-formal-verification-skill, poteto/maintain-formal-verification-skill, poteto/statechart, poteto/benchmark-checklist, poteto/figure-it-out, poteto/show-me-your-work, poteto/automate-me, poteto/reflect, poteto/correct, poteto/make-bot-ui
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:9–17](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md#L9-L17) — Help versus work-request branch and owning-file authority.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:25–48](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md#L25-L48) — Relevant setup/verification checks, optional setup, cost and host limitations.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:64–101](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md#L64-L101) — Direct skill routing including verification, design, catch-up and corrections.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:107–132](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md#L107-L132) — Close calls, external dependencies, playbooks, Babysit/Shipping and plan-only boundary.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:151–162](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-help/SKILL.md#L151-L162) — Personalization and concise prompt/source reply.

### poteto/poteto-mode

Routes rigorous engineering work through 22 task-specific playbooks and companion skills, with explicit design, delegation, evidence and delivery rules. Read-only investigations, plan-only requests, PR readiness and authorized landing retain distinct scopes.

- **Role / status:** router / stable.
- **Use when:** Coordinate a nontrivial feature, defect, refactor or measured optimization through the matching playbook.; Run a bounded investigation or plan with its explicit no-implementation boundary.; Manage PR readiness, authorized landing, or a specified autonomous queue under the corresponding playbook’s gates.
- **Scope limits:** Catalog interpretation: Prefer a narrow skill for a small self-contained explanation or rewrite.; Catalog interpretation: Do not infer implementation, babysitting or merging from an investigation, plan or PR-opening request.; Catalog interpretation: Adapt host-specific tools and external dependencies explicitly; plain Agent Skills format does not guarantee equivalent execution.
- **Result:** Matched playbook copied into todos, with goal-led task report and relevant evidence; Verified implementation or diagnosis/plan-only artifact according to the request; Where requested, ready PRs, scoped readiness report, or independently verified authorized merges
- **Requirements:** Cursor Task/poteto-agent, per-role model configuration and task-specific control tools; current defaults cap effort at xhigh, use Opus 5.5 fast slugs, and reserve Fable outside panels for named use or two failed Opus attempts.; cursor-team-kit deslop before commit and control-ui/control-cli for relevant live proof; Cursor built-in create-skill and /loop for applicable playbooks.; Git worktrees and GitHub CLI by default, or Origin CLI when it resolves the repository; Graphite is never required.; Bun runs the GitHub PR watcher; first use installs its frozen-lockfile dependencies in the bundled scripts directory.; Claude Code has a documented adapter for Agent, isolation, model rules, paths and transcripts; Cursor-only automation/cloud-only steps are skipped with a note rather than assumed portable.
- **Possible effects:** read, local_write, external_write, execute, delegate, configure
- **Confirmation behavior:** The source permits reversible work and some external actions without asking, and pauses for shared-branch force-push, deploys, data deletion and customer messages. Multi-phase plans await explicit go; Babysit never grants merging; Autopilot-stack stops at verified/green and prohibits later pushes without go; named operator gates and forge-enforced approvals remain binding.
- **Explicit companions/references:** poteto/why, poteto/architect, poteto/arena, poteto/swarm, poteto/interrogate, poteto/unslop, poteto/technical-writing, poteto/no-comments, poteto/benchmark-checklist, poteto/figure-it-out, poteto/show-me-your-work, poteto/setup-pstack, poteto/tdd, poteto/ketchup, poteto/principle-boundary-discipline, poteto/principle-model-the-domain, poteto/principle-fix-root-causes, poteto/principle-encode-lessons-in-structure, poteto/principle-guard-the-context-window, poteto/principle-subtract-before-you-add, poteto/principle-foundational-thinking, poteto/principle-build-the-lever, poteto/principle-make-operations-idempotent, poteto/principle-sequence-verifiable-units, poteto/principle-test-behavior-not-implementation, poteto/principle-explain-the-number, poteto/principle-outcome-oriented-execution, poteto/principle-never-block-on-the-human, poteto/principle-redesign-from-first-principles, poteto/principle-minimize-reader-load, poteto/principle-exhaust-the-design-space, poteto/principle-migrate-callers-then-delete-legacy-apis, poteto/principle-attack-the-premise, poteto/principle-laziness-protocol, poteto/principle-experience-first, poteto/principle-prove-it-works, poteto/principle-separate-before-serializing-shared-state, poteto/principle-type-system-discipline
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:19–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L19-L29) — Goal-first working triggers, skill routing, cleanup, proof and readiness versus shipping.
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:74–100](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L74-L100) — Autonomy, current role/default model policy, verification model and fresh-agent ownership.
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:106–110](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L106-L110) — Task-to-playbook selection and large-work route.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/investigation.md:5–12](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/investigation.md#L5-L12) — Investigation is read-only with no PR/babysit and explicit reroute before code.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:3–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L3-L9) — Written-plan deliverable, concrete proof boxes and explicit execution go.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/babysit.md:5–10](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/babysit.md#L5-L10) — Babysit drive/threads-only/check modes, watcher, conflict stop and no merge grant.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/shipping.md:5–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/shipping.md#L5-L9) — Independent verification, patch-aware receipts and bottom-up confirmed landing.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/autopilot-full.md:7–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/autopilot-full.md#L7-L23) — Queue scope, cloud owners, proof/CI gates, countersigns, stuck-agent audit and stop.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/autopilot-stack.md:3–8](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L3-L8) — No-merge autopilot variant and no-push handoff.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/opening-a-pr.md:5–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/playbooks/opening-a-pr.md#L5-L9) — Ready PR format and opening does not start babysitting.
- **Evidence:** [pstack/skills/poteto-mode/scripts/bootstrap.ts:25–43](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/scripts/bootstrap.ts#L25-L43) — Watcher bootstrap installs frozen dependencies.
- **Evidence:** [pstack/docs/harness/claude-code.md:19–38](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L19-L38) — Claude Code model/tool/isolation adaptation.
- **Evidence:** [pstack/docs/harness/claude-code.md:59–68](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L59-L68) — Unavailable Cursor-specific features and fallback scope.

### poteto/principle-attack-the-premise

Interrupts fixes that repeatedly fail the same gate by writing down their common premise and testing it directly before another attempt.

- **Role / status:** principle / stable.
- **Use when:** Two or more fixes based on the same premise fail the same check.; The distribution of failures suggests one part is consistently put at a disadvantage.
- **Scope limits:** Catalog interpretation: A new requirement calls for redesign rather than falsifying an assumed fact.
- **Result:** Written shared premise; Discriminating observation testing the premise; Next debugging direction grounded in what the failures share
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-attack-the-premise/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-attack-the-premise/SKILL.md#L9-L15) — Repeated-failure trigger, written premise, discriminating observation and evidence-led next direction.

### poteto/principle-boundary-discipline

Concentrates parsing, validation and error handling at system boundaries, leaving internal business logic expressed as typed pure functions.

- **Role / status:** principle / stable.
- **Use when:** Wiring a CLI, configuration parser, network adapter or external API.; Reviewing redundant checks buried inside domain logic.
- **Scope limits:** Catalog interpretation: The task needs a complete implementation workflow rather than a placement rule.; Catalog interpretation: The supposedly internal input has not actually been parsed into a trusted domain type.
- **Result:** Raw inputs parsed into domain types at system boundaries; Pure business functions with thin framework wiring
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-boundary-discipline/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-boundary-discipline/SKILL.md#L3-L3) — System-boundary and adapter scope.
- **Evidence:** [pstack/skills/principle-boundary-discipline/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-boundary-discipline/SKILL.md#L9-L11) — Boundary parsing, trusted internal types, pure business logic and thin shell; two placement tests.

### poteto/principle-build-the-lever

Turns nontrivial work into a small rerunnable tool or an explicit delegate recipe, making the result reproducible for reviewers.

- **Role / status:** principle / stable.
- **Use when:** A migration or analysis needs a repeatable transformation.; A one-off nontrivial task needs a check a reviewer can rerun.
- **Scope limits:** Catalog interpretation: The work is a couple of obvious trivial edits.; Catalog interpretation: A framework would cost more than the smallest script that does or proves the job.
- **Result:** Small rerunnable script, codemod, generator, check or protected delegate skill; Tool verified against a manually completed first unit
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-build-the-lever/SKILL.md:9–14](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-build-the-lever/SKILL.md#L9-L14) — Nontriviality threshold, first-unit proof, rerun safety, deterministic-tool preference, fenced delegates and persistent file artifact.

### poteto/principle-encode-lessons-in-structure

Replaces repeated instructions or corrections with an enforceable structural rule where possible; judgment-heavy lessons receive a clearer instruction and failure example.

- **Role / status:** principle / stable.
- **Use when:** An agent needs the same correction for a second time.; A recurring rule could become a lint, metadata flag or runtime check.
- **Scope limits:** Catalog interpretation: The instruction is novel and there is no recurring pattern yet.
- **Result:** Lint, metadata flag, runtime check or script; Clearer instruction with a failure example when enforcement is infeasible
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** local_write, configure
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-encode-lessons-in-structure/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L3-L3) — Repeated-instruction trigger and structural enforcement options.
- **Evidence:** [pstack/skills/principle-encode-lessons-in-structure/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L9-L11) — Judgment fallback and structural-only fix corollary.

### poteto/principle-exhaust-the-design-space

Resolves unfamiliar architecture or interaction choices by comparing a few competing prototypes before selecting an approach.

- **Role / status:** principle / stable.
- **Use when:** A novel UI interaction has no precedent in the codebase.; A product choice depends on how alternatives feel.
- **Scope limits:** Catalog interpretation: An established codebase pattern already settles the choice.; Catalog interpretation: The task is a straightforward implementation with no meaningful competing design.
- **Result:** Two or three competing prototypes; Side-by-side comparison informing a design commitment
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-exhaust-the-design-space/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-exhaust-the-design-space/SKILL.md#L3-L3) — Novel interaction or architecture without precedent; compare two or three prototypes.
- **Evidence:** [pstack/skills/principle-exhaust-the-design-space/SKILL.md:9–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-exhaust-the-design-space/SKILL.md#L9-L9) — Product choices whose experience depends on feel.

### poteto/principle-experience-first

Prioritizes the experience of consumers and maintainers when deciding scope and polish, using prototypes to test design choices early.

- **Role / status:** principle / stable.
- **Use when:** Feature scope must trade quantity against quality.; An API or UI design favors implementation convenience at a consumer's expense.
- **Scope limits:** Catalog interpretation: The question is work sequencing; this principle selects the target experience.
- **Result:** Justified feature scope; Prototype-informed design choice; Polished core workflow and feedback states
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-experience-first/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-experience-first/SKILL.md#L9-L15) — Justified scope, polish, prototype and core-loop criteria.
- **Evidence:** [pstack/skills/principle-experience-first/SKILL.md:17–19](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-experience-first/SKILL.md#L17-L19) — Consumers include maintainers and API users; experience target differs from foundation-first sequence.

### poteto/principle-explain-the-number

Makes measurement decision-led by declaring the result that would change a choice, finding the observed limiter, and ruling out misleading alternative explanations before trusting a number. It stops when run-to-run spread exceeds the effect and retains the run evidence.

- **Role / status:** principle / stable.
- **Use when:** Designing a measurement before running it: state the decision, a result that would change it and the noise floor.; Trusting or reporting a measured speedup, regression, throughput or latency.; Checking whether an evaluation result reflects completed, relevant work across trials and models.
- **Scope limits:** Catalog interpretation: No measurement is planned or available to interpret.; Catalog interpretation: The only question is whether an artifact exists or works at all; use direct verification before interpreting magnitude.
- **Result:** Predeclared decision, decision-changing result and noise floor; Limiter tied to a profile or counters and mapped to source; Run count, spread and evidence excluding alternative explanations
- **Requirements:** Limiter evidence from a profile or counters taken during a run, mapped to source; reading code alone is insufficient.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/benchmark-checklist
- **Evidence:** [pstack/skills/principle-explain-the-number/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-explain-the-number/SKILL.md#L3-L3) — Applies before measuring as well as before trusting or reporting results.
- **Evidence:** [pstack/skills/principle-explain-the-number/SKILL.md:9–12](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-explain-the-number/SKILL.md#L9-L12) — Predeclared decision threshold and noise floor, measured limiter, alternative explanations and retained run evidence.
- **Evidence:** [pstack/skills/principle-explain-the-number/SKILL.md:14–14](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-explain-the-number/SKILL.md#L14-L14) — Explicit benchmark-checklist route and evaluation-specific questions.

### poteto/principle-fix-root-causes

Traces a reproduced symptom to the first wrong decision and distinguishes legitimate states needing handling from impossible states that should never be produced.

- **Role / status:** principle / stable.
- **Use when:** A guard, retry, swallowed error or discarded state appears to hide a defect.; A reproduced symptom needs tracing to the first wrong decision.
- **Scope limits:** Catalog interpretation: The task needs a complete debugging phase workflow; this is a root-cause discipline within one.
- **Result:** Reproduction and root-cause trace; Pattern-wide fix that distinguishes legitimate from impossible states; Proposed cheap always-on signal when the deciding fact was hard to discover
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-fix-root-causes/SKILL.md:9–14](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-fix-root-causes/SKILL.md#L9-L14) — First wrong decision, reproduction and instrumentation, legitimate-state distinction, pattern-wide fix and proposed observability signal.

### poteto/principle-foundational-thinking

Orders work around sound data structures and shared foundations so later increments remain simple and coherent.

- **Role / status:** principle / stable.
- **Use when:** Choosing core types and dominant access patterns before logic.; Sequencing scaffolding and feature work or deciding what concurrent actors share.
- **Scope limits:** Catalog interpretation: An abstraction adds complexity without improving the data shape or downstream work.; Catalog interpretation: Scaffolding would preserve dead code that should be removed first.
- **Result:** Core data shape and access-pattern choices; Foundation-first sequence of coherent increments; Concurrent-state isolation decision
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-foundational-thinking/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-foundational-thinking/SKILL.md#L3-L3) — Core-type, scaffold sequencing and concurrent-state scope.
- **Evidence:** [pstack/skills/principle-foundational-thinking/SKILL.md:9–13](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-foundational-thinking/SKILL.md#L9-L13) — Dominant access patterns, structural reuse, concurrent isolation and scaffolding after dead-code removal.

### poteto/principle-guard-the-context-window

Controls reasoning load by bounding phases and moving bulk reading to delegates while retaining summaries in the coordinating context.

- **Role / status:** principle / stable.
- **Use when:** Long files or large outputs are filling the context.; Planning investigation fan-out without flooding the main thread.
- **Scope limits:** Catalog interpretation: The work is small enough that delegation adds overhead without reducing meaningful context pressure.
- **Result:** Bounded file scope and phase budgets; Delegated bulk work with coordinating summaries
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-guard-the-context-window/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-guard-the-context-window/SKILL.md#L3-L3) — Context-pressure triggers, bulk delegation and coordinating summaries.
- **Evidence:** [pstack/skills/principle-guard-the-context-window/SKILL.md:9–12](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-guard-the-context-window/SKILL.md#L9-L12) — Reason for the rule and file-scope, phase and turn-budget limits.

### poteto/principle-laziness-protocol

Keeps refactors and additions small by consolidating repeated choices and avoiding unnecessary layers or abstractions.

- **Role / status:** principle / stable.
- **Use when:** Sizing a refactor or evaluating an abstraction proposal.; The same decision is being threaded or repeated across callers.
- **Scope limits:** Catalog interpretation: Minimizing lines would fail to solve the actual problem or preserve duplicated decisions.
- **Result:** Minimal sufficient diff; One source of truth for a repeated decision
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-laziness-protocol/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-laziness-protocol/SKILL.md#L3-L3) — Refactor, diff-size and abstraction triggers.
- **Evidence:** [pstack/skills/principle-laziness-protocol/SKILL.md:9–10](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-laziness-protocol/SKILL.md#L9-L10) — Decision consolidation and smallest sufficient change.

### poteto/principle-make-operations-idempotent

Designs state-changing work to reconcile current state with the goal so retries and interrupted runs converge safely.

- **Role / status:** principle / stable.
- **Use when:** A command, processing loop or lifecycle action can be retried after a crash.; Temporary files, claimed jobs or stale locks survive partial execution.
- **Scope limits:** Catalog interpretation: The operation is purely observational and cannot leave partial state.
- **Result:** Current-state reconciliation steps; Stale artifacts identifiable after every possible interruption; Temporary-path writes renamed into place; Repeat-run and crash-point convergence checks
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-make-operations-idempotent/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-make-operations-idempotent/SKILL.md#L9-L11) — Converge state-changing work by reading present state and applying only the gap to the goal.
- **Evidence:** [pstack/skills/principle-make-operations-idempotent/SKILL.md:13–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-make-operations-idempotent/SKILL.md#L13-L15) — Crash-point-valid stale evidence, temporary-write then rename, repeat-run and interrupted-run tests.

### poteto/principle-migrate-callers-then-delete-legacy-apis

Keeps an internal API simplification coherent by migrating callers and removing the old API in the same wave, with tests aligned to the new contract.

- **Role / status:** principle / stable.
- **Use when:** Replacing an internal API as part of a simplification.
- **Scope limits:** Catalog interpretation: External consumers require backward compatibility.; Catalog interpretation: The project cannot coordinate a breaking change.
- **Result:** Migrated callers; Deleted legacy API; Tests for the new contract
- **Requirements:** No external users depend on backward compatibility; the project can absorb coordinated breaking changes as part of simplification or refactoring.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L3-L3) — Internal API migration and same-wave deletion.
- **Evidence:** [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md:9–14](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L9-L14) — Tests updated to new contract; no external compatibility dependence and coordinated breaking-change conditions.

### poteto/principle-minimize-reader-load

Evaluates maintainability through the indirections a reader must trace and the mutable state they must remember, then removes layers or narrows state.

- **Role / status:** principle / stable.
- **Use when:** A new maintainer cannot quickly trace a value's origin or mutations.; A wrapper or adapter adds a broad surface without hiding meaningful complexity.
- **Scope limits:** Catalog interpretation: A layer actually compresses meaningful decisions and reduces reader work.
- **Result:** Reduced pass-through layers; Narrower mutable-state scope and derived values; Invariant named once at the boundary; Traceability assessment for value origin and mutation
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-minimize-reader-load/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-minimize-reader-load/SKILL.md#L9-L15) — Independent layer and state axes; forwarding-layer collapse, narrower state, boundary invariant and 30-second traceability test.

### poteto/principle-model-the-domain

Encodes domain invariants and access patterns in an appropriate structure rather than spreading lifecycle rules across conditionals and phases.

- **Role / status:** principle / stable.
- **Use when:** Stateful logic keeps adding booleans or branches.; Several files repeat the same shape assumption or domain invariant.
- **Scope limits:** Catalog interpretation: The current shape is clear, local and unlikely to grow.; Catalog interpretation: An abstraction adds indirection without removing branches, duplicated rules or invalid states.
- **Result:** Domain-aligned state machine, typed model, registry or module boundary; Explicit invariant and access-pattern design
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-model-the-domain/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-model-the-domain/SKILL.md#L9-L11) — Domain encoding and concrete state-machine, typed-model, registry, reducer and collection alternatives.
- **Evidence:** [pstack/skills/principle-model-the-domain/SKILL.md:13–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-model-the-domain/SKILL.md#L13-L15) — Restraint for clear local shapes and warning signs of scattering or coupled booleans.

### poteto/principle-never-block-on-the-human

Lets reversible execution proceed with reasonable decisions and asynchronous supervision while retaining confirmation for irreversible actions and human control of product direction.

- **Role / status:** principle / stable.
- **Use when:** An agent is about to ask permission for a reversible code or note edit.
- **Scope limits:** Catalog interpretation: An action is irreversible, such as force-push, deleting production data or sending external messages.; Catalog interpretation: The unresolved choice is product direction owned by the human.
- **Result:** Completed reversible work with an explanation; Confirmation boundary for irreversible actions
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** The leaf says reversible code, note and task edits proceed without blocking, while force-pushes, production-data deletion and external messages require confirmation; product direction remains human-owned. The surrounding router has different external-action wording, so these leaf boundaries must stay visible.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-never-block-on-the-human/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-never-block-on-the-human/SKILL.md#L9-L15) — Asynchronous supervision, reversible execution, irreversible confirmation and human product ownership.
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:74–80](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L74-L80) — Surrounding router permits team chat, ticket updates and eval launches without asking, but pauses for irreversible writes including customer messages; this differs from the leaf external-message rule.

### poteto/principle-outcome-oriented-execution

Allows explicitly scoped transitional breakage during a planned migration so work converges on the verified target architecture without accumulating compatibility scaffolding.

- **Role / status:** principle / stable.
- **Use when:** A planned rewrite has explicit phase and verification boundaries.
- **Scope limits:** Catalog interpretation: Intermediate breakage is unplanned, unscoped or irreversible.; Catalog interpretation: No explicit verification boundary or full static/runtime completion gate exists.; Catalog interpretation: A green-per-step workflow is already chosen; reconcile phase and unit boundaries before combining this principle with it.
- **Result:** Declared temporary-breakage boundaries; Target architecture without throwaway compatibility code; High-signal phase checks and full completion verification
- **Requirements:** A planned rewrite or migration with explicit phase boundaries; declared acceptable breakage and full static/runtime verification at completion.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-outcome-oriented-execution/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L9-L15) — End-state integrity and only planned, scoped, reversible transitional breakage.
- **Evidence:** [pstack/skills/principle-outcome-oriented-execution/SKILL.md:17–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L17-L21) — Explicit migration phases, declared breakage, active-area checks and full completion verification.

### poteto/principle-prove-it-works

Verifies completion against the actual output and favors a deterministic repeatable check whose evidence a human can inspect.

- **Role / status:** principle / stable.
- **Use when:** An agent is about to declare a task complete.; A claim relies on freshness, cached output or a delegate's self-report.
- **Scope limits:** Catalog interpretation: The question is measurement magnitude or validity of a speedup rather than output reality.
- **Result:** Direct observation of the real output; Rerunnable check when feasible and human-visible evidence
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-prove-it-works/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-prove-it-works/SKILL.md#L3-L3) — Completion trigger and checking the actual artifact instead of compilation or self-report.
- **Evidence:** [pstack/skills/principle-prove-it-works/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-prove-it-works/SKILL.md#L9-L11) — Direct observations, checking the observation method, deterministic reruns and visible evidence; commit only for later auditability.

### poteto/principle-redesign-from-first-principles

Integrates a requirement by reconsidering the whole affected design as though the requirement had always existed, then delivering the redesign incrementally.

- **Role / status:** principle / stable.
- **Use when:** A new requirement would otherwise be bolted onto an existing architecture.
- **Scope limits:** Catalog interpretation: Repeated failed fixes require testing an assumed fact rather than accommodating a new requirement.
- **Result:** Requirement-informed target design; Updated affected types, documentation, examples and rationale; Incremental delivery sequence
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-redesign-from-first-principles/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-redesign-from-first-principles/SKILL.md#L3-L3) — New-requirement integration scope.
- **Evidence:** [pstack/skills/principle-redesign-from-first-principles/SKILL.md:9–16](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-redesign-from-first-principles/SKILL.md#L9-L16) — Affected-file reading, whole-design reconsideration, propagation through references and incremental delivery.

### poteto/principle-separate-before-serializing-shared-state

Removes unnecessary shared write targets before introducing locks, and uses structural ownership or serialization when one canonical mutable object is unavoidable.

- **Role / status:** principle / stable.
- **Use when:** Two workers may update the same state file, branch or key.; A proposed lock may be avoidable through independent owned outputs.
- **Scope limits:** Catalog interpretation: There are no concurrent mutable writers.
- **Result:** Shared-state ownership map; Independent write targets merged at the reporting boundary; Structural single-writer or atomic coordination where required
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md#L3-L3) — Concurrent mutable-writer scope.
- **Evidence:** [pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md#L9-L11) — Independent fact outputs, merge-on-read, shared-field race and structural serialization only for a real invariant.

### poteto/principle-sequence-verifiable-units

Sequences multi-step execution and delivery into small checked units whose order demonstrates correctness to a reviewer.

- **Role / status:** principle / stable.
- **Use when:** A migration or sweep applies many similar changes.; Commits or PRs need a replayable proof order, such as failing test before fix.
- **Scope limits:** Catalog interpretation: A migration deliberately permits scoped transitional breakage; reconcile the verification unit with that declared boundary before combining principles.
- **Result:** Small known-good/change/check units with passing gates; Commit or PR order that demonstrates the change
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-sequence-verifiable-units/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L9-L11) — Known-good bracket, one change, green check before next; applies even when tooling makes edits.
- **Evidence:** [pstack/skills/principle-sequence-verifiable-units/SKILL.md:13–13](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L13-L13) — Proof-ordered delivery and independently landing commits.

### poteto/principle-subtract-before-you-add

Simplifies the existing base before extending it by removing dead code, redundant rules and references without novel content.

- **Role / status:** principle / stable.
- **Use when:** Sequencing an addition, refactor or rewrite with existing dead weight.; Agent prompts or reference files repeat content without adding meaning.
- **Scope limits:** Catalog interpretation: Removal would discard required behavior or an observed use rather than speculative complexity.
- **Result:** Subtraction-first work sequence; Smaller code or instruction surface ready for extension
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-subtract-before-you-add/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-subtract-before-you-add/SKILL.md#L9-L11) — Continuous subtraction-first simplification with the same or smaller surface.
- **Evidence:** [pstack/skills/principle-subtract-before-you-add/SKILL.md:13–18](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-subtract-before-you-add/SKILL.md#L13-L18) — Remove before building, observed scope, no speculative guards and deletion of redundant prompt/reference content.

### poteto/principle-test-behavior-not-implementation

Judges a test by whether it catches broken observable behavior while surviving internal restructuring, then rewrites assertions around the consumer contract.

- **Role / status:** principle / stable.
- **Use when:** Writing or reviewing regression tests.; Tests assert private helpers, internal call order or test-constructed data.; An internal refactor breaks tests while consumer-visible behavior stays the same.
- **Scope limits:** Catalog interpretation: The task needs test-harness setup or a complete testing strategy rather than a rule for judging assertions against an observable consumer contract.
- **Result:** Contract-derived test cases through the public interface; Assertions that catch behavioral regressions and survive internal refactors; Positive counterpart cases and caller-relevant error-type assertions
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L3-L3) — Applies when writing, changing or keeping tests.
- **Evidence:** [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:9–14](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L9-L14) — Observable interface/effects contract and behavior-break versus internal-refactor test-quality checks.
- **Evidence:** [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:16–16](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L16-L16) — Rewrite/delete failing test designs, independent expected values, external effects, positive counterparts and caller-used error types.

### poteto/principle-type-system-discipline

Uses types and authoritative schemas to prevent invalid states, semantic primitive mixups and unhandled variants before runtime.

- **Role / status:** principle / stable.
- **Use when:** Designing signatures in a statically typed language.; External data or parallel hand-maintained types need a trusted parsing boundary or authoritative schema.
- **Scope limits:** Catalog interpretation: The environment has no static type system for the proposed compile-time guarantees.; Catalog interpretation: The question is TypeScript syntax; consult the dedicated TypeScript skill alongside this general rule.
- **Result:** Semantically distinct primitive types; Parsed boundary domain model; Schema-derived authoritative types
- **Requirements:** A statically typed language for compiler-enforced guarantees; TypeScript-specific syntax is delegated to typescript-best-practices.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/typescript-best-practices
- **Evidence:** [pstack/skills/principle-type-system-discipline/SKILL.md:3–3](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-type-system-discipline/SKILL.md#L3-L3) — Any statically typed language; impossible states, semantic primitives, boundaries and exhaustiveness.
- **Evidence:** [pstack/skills/principle-type-system-discipline/SKILL.md:9–13](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-type-system-discipline/SKILL.md#L9-L13) — Compiler guarantees, validated brands, parsed external data including database rows and schema-derived types.
- **Evidence:** [pstack/skills/principle-type-system-discipline/SKILL.md:15–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-type-system-discipline/SKILL.md#L15-L15) — Explicit TypeScript syntax companion.

### poteto/recall

Rebuilds recent work context across the user's scoped chat history, shared evidence and live PR state. Returns a compact current-state brief before work resumes.

- **Role / status:** workflow / stable.
- **Use when:** Find where work on a named feature stands across recent chats.; Recover decisions, failed approaches and the most useful next move.
- **Scope limits:** Catalog interpretation: Use the mode Session pickup playbook for one specific prior chat.; Catalog interpretation: Use automate-me to turn habits into lasting agent instructions.
- **Result:** Capsule and status-tagged threads; Recurring problems and one next action
- **Requirements:** Workspace-scoped Cursor JSONL transcripts or the documented Claude Code transcript path adaptation.; git and gh for surfaced live PR/branch checks; available connected shared-record sources for a named feature, subsystem, file, area or bug.; Parallel history miners and per-source agent-mode investigators for wider scopes; one or two chats are searched directly.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** States the search window/topic/workspace. Never reads another project's transcripts without being asked.
- **Explicit companions/references:** poteto/automate-me, poteto/unslop, poteto/poteto-mode
- **Evidence:** [pstack/skills/recall/SKILL.md:9–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/recall/SKILL.md#L9-L21) — Narrow scope, supplied-capsule skip, history mining, mandatory named-topic shared-record sweep and live verification.
- **Evidence:** [pstack/skills/recall/SKILL.md:26–35](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/recall/SKILL.md#L26-L35) — Capsule, exact thread tags, problems, next move and source/privacy discipline.
- **Evidence:** [pstack/docs/harness/claude-code.md:53–57](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L53-L57) — Claude Code paths and workspace-only transcripts.

### poteto/reflect

Reads the active conversation for durable lessons and proposes edits to skills the session used, separating rejected ideas and enforceable backlog work. Approved edits go into a local copy of the skill rather than the installed plugin cache.

- **Role / status:** workflow / stable.
- **Use when:** A completed session exposed repeatable instructions, missed checks or skill-trigger problems.; Capture improvements to used skills while keeping enforceable rules in a separate backlog.
- **Scope limits:** Catalog interpretation: Use correct for repeated repository mistake classes that need structural enforcement.; Catalog interpretation: Do not turn one-off details or drifting versions, hashes and counts into lasting skill rules.
- **Result:** Accepted proposals with problem, change and destination skill; Rejected ideas with reasons and an enforcement backlog; After approval, edited project/user copy of the skill folder
- **Requirements:** The full active transcript and the relevant skills used in that session.; Writable .cursor/skills/<skill>/ or ~/.cursor/skills/<skill>/ destination shown before approval; never edit plugins/cache/.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Presents Accepted, Rejected and Backlog and waits for approval before any skill edit. Shows the destination first, then copies and edits there; never opens a PR or pushes.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/reflect/SKILL.md:9–17](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/reflect/SKILL.md#L9-L17) — Full transcript as data, durable used-skill routing, rejected drift, backlog, explicit approval and local-copy-only edits.

### poteto/setup-pstack

Detects available host models, confirms a per-role model map and one of three reasoning budgets, then writes the rule used by new sessions. Recognized retired defaults migrate while other user choices remain.

- **Role / status:** setup / stable.
- **Use when:** Choose a smaller budget or adjust the models used for each pstack role.; Configure a new pstack installation.
- **Scope limits:** Catalog interpretation: Do not write unconfirmed real model slugs.; Catalog interpretation: Do not assume a Cursor .mdc rule is loaded by another host.
- **Result:** ~/.cursor/rules/pstack-models.mdc; Validated role/model table and budget; Optional offered verification setup
- **Requirements:** Cursor Task model availability or user-supplied available slugs, AskQuestion and a writable user rules directory.; The Claude Code adapter instead uses Agent schema model/effort values and ~/.claude/rules/pstack-models.md without frontmatter.
- **Possible effects:** read, local_write, configure
- **Confirmation behavior:** Asks for a budget and confirmation of every role/model table before writing. Verification generators are invoked only if the user accepts each optional offer.
- **Explicit companions/references:** poteto/arena, poteto/poteto-mode, poteto/create-verification-skill, poteto/create-formal-verification-skill
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:14–26](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/setup-pstack/SKILL.md#L14-L26) — Detect actual available models, remove retired roles and migrate recognized legacy defaults only.
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:30–42](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/setup-pstack/SKILL.md#L30-L42) — Three budgets, capped effort, host-detected slugs, family preservation and explicit role-table approval.
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:46–70](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/setup-pstack/SKILL.md#L46-L70) — Always-applied defaults:3 rule shape and future-session effect.
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:72–78](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/setup-pstack/SKILL.md#L72-L78) — Independent optional app and formal verification offers.
- **Evidence:** [pstack/docs/harness/claude-code.md:41–47](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L41-L47) — Claude Code detection/defaults and alternate rule destination.

### poteto/sharpen

Rewrites a task prompt around expert practice, raw evidence, concrete methods and an independent correctness check. The rewritten prompt asks its future executor to prototype experimentally decidable choices and leaves only product or preference calls to the user.

- **Role / status:** utility / stable.
- **Use when:** Strengthen an existing prompt’s evidence and methods without expanding its goal.; Make the future task test uncertain choices rather than handing empirical forks back to the user.
- **Scope limits:** Catalog interpretation: The deliverable here is a rewritten prompt, not execution of its experiments or implementation.; Catalog interpretation: Use an interactive clarification workflow when the underlying product goals themselves are unsettled.
- **Result:** Four expert-method and evidence considerations; Rewritten prompt with experimental choice-setting and human preference boundaries
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read
- **Confirmation behavior:** The rewritten task leaves product or preference choices that experiments cannot settle for the user. This skill does not specify an approval step before returning the prompt.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/sharpen/SKILL.md:7–16](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/sharpen/SKILL.md#L7-L16) — Four preparatory considerations, scope-preserving rewrite and experimental-versus-preference distinction.
- **Evidence:** [pstack/docs/guide/02-poteto-mode.md:69–75](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/guide/02-poteto-mode.md#L69-L75) — Current guide explicitly says sharpening does not do the rewritten task.

### poteto/show-me-your-work

Maintains one append-only TSV decision trail for long or unattended work, with explicit boundaries between runs sharing a log. Audits this run’s entries against its transcript and obtains a different-vendor review before handoff.

- **Role / status:** workflow / stable.
- **Use when:** A reviewer must trust a long run after stepping away.; Track hypotheses, pivots and verification results as a run proceeds.
- **Scope limits:** Catalog interpretation: Do not log every trivial action or silently rewrite earlier rows.; Catalog interpretation: Keep the log local unless the work warrants committing an audit artifact.
- **Result:** Canonical append-only TSV with evidence pointers and superseding corrections; Transcript-checked decision trail with explicit run start boundaries; Attention section naming the reviewing model and specific flags or no flags
- **Requirements:** Writable log destination and this run’s full transcript under the active workspace’s transcript directory.; Optional bundled log.sh helper, or append logic with equivalent single-line and spreadsheet-formula safeguards.; A subagent on a different vendor’s model for trail review; the mode’s role and reasoning rules apply.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/unslop, poteto/poteto-mode, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:13–22](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/SKILL.md#L13-L22) — Canonical TSV columns with single-line cells and evidence pointers.
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:36–48](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/SKILL.md#L36-L48) — Safe helper, decision granularity, interleaved-run starts and local-by-default placement.
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:52–63](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/SKILL.md#L52-L63) — Append-only corrections and transcript audit limited to this run’s stretches.
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:67–74](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/SKILL.md#L67-L74) — Different-vendor review and required Attention section.
- **Evidence:** [pstack/skills/show-me-your-work/scripts/log.sh:25–42](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/show-me-your-work/scripts/log.sh#L25-L42) — Bundled helper timestamps, sanitizes formula-leading cells and appends.

### poteto/statechart

Checks a TLA+ model and renders a reader-labeled Mermaid statechart with per-rule bug paths and honest unchecked-rule limits. Code-backed bug paths must be replayed against real code before being treated as product bugs.

- **Role / status:** workflow / stable.
- **Use when:** Show a behavior owner a checked product flow, protocol or service state model.; Present the shortest path to rule-breaking states in reader-facing terms.; Read TLA+ results produced by a project-local formal verification skill.
- **Scope limits:** Catalog interpretation: This is not a chart-to-spec conversion workflow; it starts from a TLA+ spec and config.; Catalog interpretation: A model pass is scoped to its rules and bounds, and unchecked rules remain unknown.; Catalog interpretation: Large models may produce bug-path-only charts or no chart when no rule breaks.
- **Result:** TLA+ spec/config and optional view module in scratch space; report.md, TLC output and chart.mmd where model size permits; Reader-facing bug paths, model omissions and reproducible command; SVG via Pele when rendering
- **Requirements:** Scratch workspace outside the repo and a new or empty output directory.; A runtime able to execute the bundled TypeScript; wrapper supports Node 22.18–22.x or 23.6+, Bun 1.1.5+, or Deno 2+.; TLC and Java via mise with network on first install, or TLA2TOOLS plus JAVA/existing Java 11+ as documented by the implementation.; View module exports state(vars), optionally step(action, from, to), group(vars), colors and title; state returns a string, hierarchy array or region object.; Pele npm package 1.9.0 installed outside the repo for SVG rendering; another renderer only on user request.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** The reader decides whether the modeled behavior is right, and agreed rules become invariants. No general execution checkpoint is specified; using a different chart renderer requires the user to ask.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/statechart/SKILL.md:9–27](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md#L9-L27) — Reader ownership, scratch TLA+ invocation, runtime/bootstrap and never weakening agreed rules.
- **Evidence:** [pstack/skills/statechart/SKILL.md:31–51](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md#L31-L51) — Current view-module interface, state shapes, labels, optional exports and purity.
- **Evidence:** [pstack/skills/statechart/SKILL.md:53–60](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md#L53-L60) — Aggregation and hidden-edge constraints and disclosure.
- **Evidence:** [pstack/skills/statechart/SKILL.md:64–70](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md#L64-L70) — Break/mayBreak meanings, constraints, repeated checks and unchecked-rule bounds.
- **Evidence:** [pstack/skills/statechart/SKILL.md:74–82](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/SKILL.md#L74-L82) — 500-state display budget, Pele, plain-language handoff and real-code replay.
- **Evidence:** [pstack/skills/statechart/references/render.md:3–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/references/render.md#L3-L9) — Pele 1.9.0 SVG outputs, renderer options and mark styling.
- **Evidence:** [pstack/skills/statechart/scripts/statechart:18–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/scripts/statechart#L18-L29) — Supported runtime versions in wrapper.
- **Evidence:** [pstack/skills/statechart/scripts/statechart.ts:9–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/scripts/statechart.ts#L9-L23) — CLI output contract, new/empty output and exit codes.
- **Evidence:** [pstack/skills/statechart/scripts/run.ts:194–207](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/statechart/scripts/run.ts#L194-L207) — Existing TLC/Java environment overrides or mise installation.

### poteto/swarm

Fans workers out across slices or declared races and consolidates their terminal results into one evidence-backed report. Missing coverage is recorded rather than counted as a pass.

- **Role / status:** workflow / stable.
- **Use when:** Cover a matrix of independent checks.; Race workers or partition exploration over a large target.
- **Scope limits:** Catalog interpretation: Use arena when competing artifacts need base selection and grafting.; Catalog interpretation: Do not accept measurement results without the exact requested commits and method.
- **Result:** Consolidated result table; Issues, coverage gaps and dropouts; Declared race outcome
- **Requirements:** Cursor background generalPurpose Task workers with cloud environments by default; local only for resources on the user’s machine.; Optional ~/.cursor/rules/pstack-models.mdc swarm-workers choice; default Opus 5.5 high fast with alias and invalid-slug handling.; Separate writable outputs, exact commit SHAs for verification/measurement, and a declared sampling method for measurements.; Claude Code adapter maps cloud to worktree isolation; cloud-machine/dashboard-only steps are unavailable there.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/poteto-mode
- **Evidence:** [pstack/skills/swarm/SKILL.md:20–23](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/swarm/SKILL.md#L20-L23) — Predicate, declared slice/race rule, current model selection, exact SHAs and measurement method.
- **Evidence:** [pstack/skills/swarm/SKILL.md:27–33](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/swarm/SKILL.md#L27-L33) — Cloud/local fields, branch base, standalone briefs and terminal status evidence.
- **Evidence:** [pstack/skills/swarm/SKILL.md:37–41](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/swarm/SKILL.md#L37-L41) — Invalid receipts get one retry, gaps never pass, all required slices and consolidated output.
- **Evidence:** [pstack/docs/harness/claude-code.md:19–27](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L19-L27) — Claude Code worktree/environment adaptation.

### poteto/tdd

Fixes a bug with a focused failing-before, passing-after regression check when a practical local test path exists. Uses another executable proof when a new test would be brittle or disproportionate.

- **Role / status:** workflow / stable.
- **Use when:** A bug has an obvious cheap regression test.; The user explicitly asks for a failing test or TDD.
- **Scope limits:** Catalog interpretation: Do not build broad new infrastructure solely to satisfy the cadence.; Catalog interpretation: Do not use implementation-mirroring tests or weaken assertions to match wrong behavior.
- **Result:** Focused regression test or closest executable check; Small production fix; Failing-before and passing-after evidence
- **Requirements:** Existing practical test target or another executable reproduction surface.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/tdd/SKILL.md:3–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/tdd/SKILL.md#L3-L11) — Explicit request or cheap local bug path, with no forced brittle test harness.
- **Evidence:** [pstack/skills/tdd/SKILL.md:15–26](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/tdd/SKILL.md#L15-L26) — Narrow focused red-before-fix/green-after loop and practical executable alternatives.
- **Evidence:** [pstack/skills/tdd/SKILL.md:30–42](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/tdd/SKILL.md#L30-L42) — Behavior guardrails and honest failure/passing evidence.

### poteto/teach

Combines code behavior and historical rationale into a plain, conversational explanation at the learner's pace. Builds diagrams incrementally when they help understanding.

- **Role / status:** teaching / stable.
- **Use when:** Understand a change or unfamiliar subsystem rather than modify it.
- **Scope limits:** Catalog interpretation: Do not use as an implementation workflow or a quiz-based course generator.; Catalog interpretation: Avoid a full historical sweep when a narrow question suffices.
- **Result:** Layered plain-language explanation; Incremental diagrams or generated spatial illustrations when useful
- **Requirements:** How’s readonly explorer and why’s historical records, used for the relevant scope.; An image-generation tool for spatial explanations; Mermaid for flows and structure, and source/diff/debugger access when useful.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Adapts depth from the conversation, starts with a small complete explanation and waits for the learner’s lead. No implementation approval workflow is specified; the stated goal is understanding rather than changing the code.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/unslop
- **Evidence:** [pstack/skills/teach/SKILL.md:9–16](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/teach/SKILL.md#L9-L16) — Understanding-only purpose, real how/why invocations, preserved historical confidence and conversational pacing.
- **Evidence:** [pstack/skills/teach/SKILL.md:17–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/teach/SKILL.md#L17-L21) — Incrementally built diagrams/images, spatial image generation, unslop and explanation-only reply.

### poteto/technical-writing

Applies a layered standard for technical documents, choosing a document purpose before refining sentences, instructions and unambiguous language.

- **Role / status:** reference / stable.
- **Use when:** Write or review documentation, an RFC, README, PR description or commit message.
- **Scope limits:** Catalog interpretation: Use product copy guidelines for UI strings.; Catalog interpretation: Do not force a rule that makes a sentence worse.
- **Result:** Rewritten or newly written technical prose; Clear tutorial, how-to, reference or explanation structure
- **Requirements:** Real repository terminology and commands when documenting code.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/unslop
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:9–30](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/technical-writing/SKILL.md#L9-L30) — Precise plain writing and one Diátaxis document mode.
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:34–63](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/technical-writing/SKILL.md#L34-L63) — Developer, instruction and Global English clarity rules.
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:67–70](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/technical-writing/SKILL.md#L67-L70) — Unslop dependency, PR/commit briefing limits, product-copy boundary and regenerable factual claims.

### poteto/typescript-best-practices

Applies TypeScript modeling and boundary rules to .ts/.tsx work, including verified brands, schema-owned validation and the simplest total type. The examples explain when to strengthen a representation and when a plain type is enough.

- **Role / status:** reference / stable.
- **Use when:** Read or edit .ts or .tsx code.
- **Scope limits:** Catalog interpretation: Do not route non-TypeScript work to this language-specific rule set.; Catalog interpretation: Avoid treating stylistic advice as an independent task plan.
- **Result:** TypeScript changes or review guidance aligned with stated rules
- **Requirements:** TypeScript code; repository schema library and framework test primitives where present.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/principle-type-system-discipline, poteto/principle-boundary-discipline
- **Evidence:** [pstack/skills/typescript-best-practices/SKILL.md:10–29](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/typescript-best-practices/SKILL.md#L10-L29) — Required principles, schema-first validation, constructive/total types, exhaustiveness and real behavior checks.
- **Evidence:** [pstack/skills/typescript-best-practices/references/patterns.md:90–112](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/typescript-best-practices/references/patterns.md#L90-L112) — Strengthen only when loose arrays force partial operations; weaker total outputs can also work.
- **Evidence:** [pstack/skills/typescript-best-practices/references/patterns.md:134–153](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/typescript-best-practices/references/patterns.md#L134-L153) — Reuse existing runtime schema system instead of duplicate guards/types or a new dependency.

### poteto/unslop

Edits prose to remove recurring AI writing patterns while preserving meaning and intended tone.

- **Role / status:** utility / stable.
- **Use when:** Clean generated prose, documentation or agent replies.
- **Scope limits:** Catalog interpretation: Do not remove meaningful uncertainty just because hedging can be overused.; Catalog interpretation: Use a technical-document structure workflow when the document's purpose is unclear.
- **Result:** Plain, more concrete prose preserving intended meaning
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/unslop/SKILL.md:9–22](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/unslop/SKILL.md#L9-L22) — Preserve meaning/tone while removing recurring attribution, vocabulary and punctuation patterns.
- **Evidence:** [pstack/skills/unslop/SKILL.md:23–40](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/unslop/SKILL.md#L23-L40) — Concrete, whole, active sentences and removal of filler and formatting tells.

### poteto/why

Reconstructs why code took its present shape from introducing and subsequent commits and PR discussions. Cites the authors’ record, marks its own inferences, and states what the evidence does not answer.

- **Role / status:** workflow / stable.
- **Use when:** Find why a design, defensive check or threshold exists.; Recover regression history or planning constraints before changing behavior.
- **Scope limits:** Catalog interpretation: Use how for current runtime mechanics.; Catalog interpretation: Do not infer author intent solely from code or promote an unsupported rationale into a fact.
- **Result:** Cited historical rationale and tradeoffs; Explicitly labeled inferences and unanswered questions
- **Requirements:** Access to the commits and PR discussions introducing the target and each later change; other relevant records when that trail is thin.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/why/SKILL.md:3–9](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/why/SKILL.md#L3-L9) — Historical rationale, regressions, thresholds, primary-record method, inference labeling and unanswered gaps.
