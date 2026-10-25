# Skill catalog

Agent interpretations of pinned upstream sources. Selection aid only; downloading a skill does not install or invoke it. Human calibration is pending.

Qualified IDs identify the collection; they are catalog identities, not promises about host slash-command syntax.

## Matt · 38 skills

| ID | Role | Catalog status | Useful result |
| --- | --- | --- | --- |
| [matt/ask-matt](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md) | router | stable | Selects an entry skill and a route through Matt’s collection, including idea-to-build work, diagnosis, maintenance, and context handoffs. It distinguishes standalone tools from shared reference layers. |
| [matt/code-review](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md) | workflow | stable | Reviews a fixed-point diff in two independent tracks: repository standards and conformity to the originating spec. It reports each track separately, with repository rules taking precedence over heuristic code smells. |
| [matt/codebase-design](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md) | reference | stable | Provides a shared vocabulary for placing small public interfaces over substantial behavior. Supporting guides cover dependency-aware deepening and comparing alternative interface designs. |
| [matt/diagnosing-bugs](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md) | workflow | stable | Builds a tight feedback command that catches the exact failure, minimizes the reproduction, tests ranked hypotheses, and verifies a fix. It treats an inadequate testing seam as an architectural finding rather than manufacturing a misleading regression test. |
| [matt/domain-modeling](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md) | reference | stable | Sharpens a project’s domain terms against user scenarios and actual code, recording agreed language in glossaries. It offers short decision records only for meaningful, nonobvious, hard-to-reverse tradeoffs. |
| [matt/grill-with-docs](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) | workflow | stable | Combines a structured interview with persistent domain modeling so clarified decisions and vocabulary survive in the repository. |
| [matt/implement](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md) | workflow | stable | Builds a supplied specification or tickets with tests at agreed seams, regular focused checks, and a final two-axis review. It commits completed work to the current branch. |
| [matt/implement-spec](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement-spec/SKILL.md) | workflow | stable | Orchestrates a specified ticket dependency graph across implementer worktrees, merging ready work onto one integration branch. It performs a final integration review and resolves work through the configured tracker. |
| [matt/improve-codebase-architecture](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture/SKILL.md) | workflow | stable | Surveys recent areas of change for architectural friction and produces a visual report of deepening candidates. After the user chooses one, it interviews them about the design and records resolved domain decisions. |
| [matt/pr](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/pr/SKILL.md) | reference | stable | Shapes a concise pull request body around a small explanatory visual, concrete before/after evidence, and rollback difficulty plus blast radius. |
| [matt/prototype](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md) | workflow | stable | Answers a specific design question with either a shareable logic demo or several switchable UI variants. It captures the validated decision and preserves the exploratory artifact outside the main branch. |
| [matt/research](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/research/SKILL.md) | workflow | stable | Delegates a question to a background agent that follows claims to primary sources and leaves a cited Markdown research note. |
| [matt/retro](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/retro/SKILL.md) | workflow | stable | Examines a coding session for improvements to the agent’s environment, such as navigation, automated checks, review standards and information access. It presents prioritized candidates rather than directly prescribing feature changes. |
| [matt/setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md) | setup | stable | Configures the repository’s tracker, optional triage labels and domain-document conventions for Matt’s engineering workflows. It preserves existing steering files and allows local Markdown, GitHub, GitLab or a custom tracker. |
| [matt/tdd](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md) | workflow | stable | Implements behavior one failing test and minimal implementation at a time, using agreed public testing seams. Its current rules reserve refactoring for the later review stage. |
| [matt/to-spec](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-spec/SKILL.md) | workflow | stable | Synthesizes existing discussion into a detailed feature specification and publishes it to the configured tracker. It includes user stories, decisions, test strategy and explicit scope. |
| [matt/to-tickets](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md) | workflow | stable | Breaks an existing plan into independently verifiable vertical tickets with explicit blockers. It supports a local one-file-per-ticket tracker and remote native dependencies, with an expand–contract exception for wide refactors. |
| [matt/triage](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md) | workflow | stable | Classifies and verifies incoming requests, interviews the maintainer when needed, and applies a triage state with a durable agent brief. External PRs participate only when enabled or specifically named. |
| [matt/wayfinder](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md) | workflow | stable | Maps a very large uncertain effort as linked decision tickets, resolving one non-research ticket per session as the frontier becomes clear. By default it delivers decisions and a handoff to implementation planning. |
| [matt/wizard](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wizard/SKILL.md) | utility | stable | Authors a staged interactive Bash procedure for actions only the human can complete. The generated script guides browser steps, captures values and can persist local environment variables and GitHub settings. |
| [matt/chief-of-staff](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/chief-of-staff/SKILL.md) | workflow | experimental | Coordinates a long-running goal through background subagents while maintaining dated, source-linked knowledge in a durable wiki. It combines tactical delivery with improving the environment for later work. |
| [matt/claude-handoff](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/claude-handoff/SKILL.md) | utility | experimental | Writes a redacted temporary handoff and immediately seeds a named Claude background agent with it. This extends the portable handoff concept with a Claude-specific launch. |
| [matt/loop-me](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/loop-me/SKILL.md) | workflow | experimental | Interviews the user about recurring activities and turns selected loops into implementable workflow specifications. It maintains workspace notes and creates, edits or deletes specs as decisions settle. |
| [matt/setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/setup-ts-deep-modules/SKILL.md) | setup | experimental | Adds dependency-cruiser checks to enforce package entry points and private implementation folders in a TypeScript repository. It creates a copyable example and demonstrates enforcement with pass–fail–pass evidence. |
| [matt/writing-beats](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-beats/SKILL.md) | workflow | experimental | Shapes fixed raw material into an article through user-selected narrative beats, tracking which concepts the audience already understands. Each accepted beat is written before alternatives for the next move are offered. |
| [matt/writing-fragments](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-fragments/SKILL.md) | workflow | experimental | Interviews the author to collect unstructured fragments that could become future writing. It appends them to a single raw-material document without imposing an outline. |
| [matt/writing-shape](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-shape/SKILL.md) | workflow | experimental | Turns a fixed raw-material file into a separate article through user-agreed openings, paragraphs and format choices. It keeps track of conceptual prerequisites and preserves the input unchanged. |
| [matt/git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/git-guardrails-claude-code/SKILL.md) | setup | specialized | Installs a Claude Code PreToolUse hook that blocks configured risky Git command patterns before Bash execution. Project or global scope is chosen by the user. |
| [matt/migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/migrate-to-shoehorn/SKILL.md) | workflow | specialized | Replaces TypeScript test-data assertions with shoehorn helpers for partial or intentionally invalid inputs. It installs the helper package and verifies types after migration. |
| [matt/scaffold-exercises](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/scaffold-exercises/SKILL.md) | utility | specialized | Creates numbered course exercise directories with problem, solution or explainer stubs and validates them with the AI Hero course linter. It commits the completed structure. |
| [matt/setup-pre-commit](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/setup-pre-commit/SKILL.md) | setup | specialized | Installs Husky, lint-staged and Prettier to format staged files and run available typecheck/test scripts at commit time. It verifies the setup by committing through the new hook. |
| [matt/grill-me](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grill-me/SKILL.md) | workflow | stable | Runs the shared interview primitive to sharpen a plan or design without the repository-documentation wrapper. |
| [matt/grilling](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md) | workflow | stable | Interviews the user in rounds of currently answerable decisions, advancing a dependency-aware design tree. The agent researches facts while the user owns the choices. |
| [matt/handoff](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff/SKILL.md) | utility | stable | Writes a portable, redacted summary so another agent can resume the work, referencing existing artifacts instead of copying them. |
| [matt/teach](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md) | teaching | stable | Builds a persistent learning workspace with short HTML lessons, reference materials, sources and evidence of learning. It chooses practice relative to the learner’s mission and recorded progress. |
| [matt/to-questionnaire](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/to-questionnaire/SKILL.md) | utility | stable | Creates a discovery questionnaire for one external knowledge holder after clarifying who receives it and what the user needs back. It writes a local document for asynchronous completion or a meeting. |
| [matt/wait-what](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/wait-what/SKILL.md) | utility | stable | Re-explains the preceding message with missing context, simplified English and the project’s established vocabulary. |
| [matt/writing-for-agents](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md) | reference | stable | Guides the structure and wording of documents agents consume, using conditional pointers, explicit completion criteria and a single source for each meaning. A supporting guide explains skill invocation and router design. |

## Poteto · 58 skills

| ID | Role | Catalog status | Useful result |
| --- | --- | --- | --- |
| [poteto/architect](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/architect/SKILL.md) | workflow | stable | Explores competing type and module designs, synthesizes a usage-first sketch, then implements against it. The human design checkpoint is opt-in. |
| [poteto/arena](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/arena/SKILL.md) | workflow | stable | Runs several candidates on the same brief, compares them using a rubric and an independent judge, and combines selected strengths into one verified artifact. |
| [poteto/automate-me](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/automate-me/SKILL.md) | workflow | stable | Turns recurring working preferences into a personal mode skill using workspace-scoped history and direct questions. Revises an existing mode instead of starting over by default. |
| [poteto/benchmark-checklist](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/benchmark-checklist/SKILL.md) | workflow | stable | Checks whether a measured performance claim is meaningful, repeatable and about completed work. Produces a verdict with units, spread and the identified limiter. |
| [poteto/blast-radius](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/blast-radius/SKILL.md) | workflow | stable | Finds downstream breakage that a diff or caller list can miss and executes a small proof of the safety fact the change depends on. |
| [poteto/bro](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/bro/SKILL.md) | utility | stable | Restates the previous assistant message in simpler, shorter language without jargon. |
| [poteto/correct](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/correct/SKILL.md) | workflow | stable | Finds repeated agent mistake classes and changes repository structure or enforcement so they are harder to repeat. Demonstrates each new check on a real past mistake. |
| [poteto/create-formal-verification-skill](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-formal-verification-skill/SKILL.md) | workflow | stable | Builds and proves a project-local formal verification workflow for a costly invariant tests seldom reach. Records model scope, assumptions and the code synchronization commit. |
| [poteto/create-verification-skill](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-verification-skill/SKILL.md) | workflow | stable | Creates a repository-specific skill that launches, health-checks, drives and cleans up the real app. Seeds a user-facing feature map and executes one complete journey before handoff. |
| [poteto/figure-it-out](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/figure-it-out/SKILL.md) | workflow | stable | Designs a custom, auditable workflow when bundled playbooks do not fit or a change is ambitious. Runs small hypothesis-driven units against an explicit completion predicate. |
| [poteto/how](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/how/SKILL.md) | workflow | stable | Explains a subsystem's architecture, runtime flow and ownership using code-grounded exploration. Scales from one explainer to several explorers and a synthesizer. |
| [poteto/in-your-own-words](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/in-your-own-words/SKILL.md) | utility | stable | Restates the user's apparent goals and the underlying problem before work proceeds. |
| [poteto/interrogate](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/SKILL.md) | workflow | stable | Obtains independent adversarial reviews from configured models and produces a lead judgment rather than automatically fixing the findings. |
| [poteto/ketchup](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup/SKILL.md) | utility | stable | Catches the user up on changes since their last message and lists every outstanding decision with enough context to act from the reply. |
| [poteto/ketchup-video](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup-video/SKILL.md) | utility | stable | Delivers the ketchup catch-up as a short silent slide video, with outstanding decisions retained as text under it. |
| [poteto/maintain-formal-verification-skill](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-formal-verification-skill/SKILL.md) | workflow | stable | Reconciles formal checks with code changes since their synchronization commit. Separates verification drift from real product bugs and proves updated checks can still fail. |
| [poteto/maintain-verification-skill](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-verification-skill/SKILL.md) | workflow | stable | Audits every mapped feature from source and drives every feature live. Ships at most one PR limited to proven verification documentation or harness corrections. |
| [poteto/make-bot-ui](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/make-bot-ui/SKILL.md) | workflow | stable | Builds a server-backed page whose buttons wake a Grok Bot through a webhook routine, then exposes the page on a Tailscale network. |
| [poteto/no-comments](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/no-comments/SKILL.md) | workflow | stable | Runs a specialized comment-removal agent, validates its findings and fixes accepted in-scope code workarounds. Can propose structural replacements for claimed constraints. |
| [poteto/poteto-help](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-help/SKILL.md) | router | stable | Helps choose a pstack setup path, skill, playbook or principle and returns an example prompt with a source link. It distinguishes help from an actual request to execute work. |
| [poteto/poteto-mode](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md) | router | stable | Coordinates pstack's working style and task-specific playbooks, selecting companion skills for grounding, design, delegation, verification and delivery. Its scope ranges from read-only investigation to autonomous PR programs. |
| [poteto/principle-attack-the-premise](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-attack-the-premise/SKILL.md) | principle | stable | Interrupts repeated failed fixes by making their shared assumption explicit and testing it before another attempt. |
| [poteto/principle-boundary-discipline](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-boundary-discipline/SKILL.md) | principle | stable | Concentrates parsing, validation and error handling at system boundaries, leaving internal business logic expressed as typed pure functions. |
| [poteto/principle-build-the-lever](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-build-the-lever/SKILL.md) | principle | stable | Turns nontrivial work into a small rerunnable tool or an explicit delegate recipe, making the result reproducible for reviewers. |
| [poteto/principle-encode-lessons-in-structure](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) | principle | stable | Replaces repeated instructions or corrections with an enforceable structural rule where possible; judgment-heavy lessons receive a clearer instruction and failure example. |
| [poteto/principle-exhaust-the-design-space](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-exhaust-the-design-space/SKILL.md) | principle | stable | Resolves unfamiliar architecture or interaction choices by comparing a few competing prototypes before selecting an approach. |
| [poteto/principle-experience-first](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-experience-first/SKILL.md) | principle | stable | Prioritizes the experience of consumers and maintainers when deciding scope and polish, using prototypes to test design choices early. |
| [poteto/principle-explain-the-number](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-explain-the-number/SKILL.md) | principle | stable | Qualifies a measured performance or evaluation result by identifying its limiter, testing alternative explanations and retaining run evidence. |
| [poteto/principle-fix-root-causes](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-fix-root-causes/SKILL.md) | principle | stable | Traces a reproduced symptom to the first wrong decision and distinguishes legitimate states needing handling from impossible states that should never be produced. |
| [poteto/principle-foundational-thinking](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-foundational-thinking/SKILL.md) | principle | stable | Orders work around sound data structures and shared foundations so later increments remain simple and coherent. |
| [poteto/principle-guard-the-context-window](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-guard-the-context-window/SKILL.md) | principle | stable | Controls reasoning load by bounding phases and moving bulk reading to delegates while retaining summaries in the coordinating context. |
| [poteto/principle-laziness-protocol](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-laziness-protocol/SKILL.md) | principle | stable | Keeps refactors and additions small by consolidating repeated choices and avoiding unnecessary layers or abstractions. |
| [poteto/principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-make-operations-idempotent/SKILL.md) | principle | stable | Designs state-changing work to reconcile current state with the goal so retries and interrupted runs converge safely. |
| [poteto/principle-migrate-callers-then-delete-legacy-apis](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | principle | stable | Keeps an internal API simplification coherent by migrating callers and removing the old API in the same wave, with tests aligned to the new contract. |
| [poteto/principle-minimize-reader-load](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-minimize-reader-load/SKILL.md) | principle | stable | Evaluates maintainability through the indirections a reader must trace and the mutable state they must remember, then removes layers or narrows state. |
| [poteto/principle-model-the-domain](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-model-the-domain/SKILL.md) | principle | stable | Encodes domain invariants and access patterns in an appropriate structure rather than spreading lifecycle rules across conditionals and phases. |
| [poteto/principle-never-block-on-the-human](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-never-block-on-the-human/SKILL.md) | principle | stable | Lets reversible execution proceed with reasonable decisions and asynchronous supervision while retaining confirmation for irreversible actions and human control of product direction. |
| [poteto/principle-outcome-oriented-execution](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-outcome-oriented-execution/SKILL.md) | principle | stable | Allows explicitly scoped transitional breakage during a planned migration so work converges on the verified target architecture without accumulating compatibility scaffolding. |
| [poteto/principle-prove-it-works](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-prove-it-works/SKILL.md) | principle | stable | Checks task outputs against the actual artifact and, where feasible, keeps a deterministic verification script and evidence for reviewers. |
| [poteto/principle-redesign-from-first-principles](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-redesign-from-first-principles/SKILL.md) | principle | stable | Integrates a requirement by reconsidering the whole affected design as though the requirement had always existed, then delivering the redesign incrementally. |
| [poteto/principle-separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md) | principle | stable | Removes unnecessary shared write targets before introducing locks, and uses structural ownership or serialization when one canonical mutable object is unavoidable. |
| [poteto/principle-sequence-verifiable-units](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-sequence-verifiable-units/SKILL.md) | principle | stable | Sequences multi-step execution and delivery into small checked units whose order demonstrates correctness to a reviewer. |
| [poteto/principle-subtract-before-you-add](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-subtract-before-you-add/SKILL.md) | principle | stable | Simplifies the existing base before extending it by removing dead code, redundant rules and references without novel content. |
| [poteto/principle-test-behavior-not-implementation](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) | principle | stable | Judges a test by whether it catches broken observable behavior while surviving internal restructuring, then rewrites assertions around the consumer contract. |
| [poteto/principle-type-system-discipline](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-type-system-discipline/SKILL.md) | principle | stable | Uses types and authoritative schemas to prevent invalid states, semantic primitive mixups and unhandled variants before runtime. |
| [poteto/recall](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/recall/SKILL.md) | workflow | stable | Rebuilds recent work context across the user's scoped chat history, shared evidence and live PR state. Returns a compact current-state brief before work resumes. |
| [poteto/reflect](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/reflect/SKILL.md) | workflow | stable | Extracts durable lessons from the current session through three reviewer lenses and a synthesizer. Proposes concrete skill edits and separates structural enforcement work into backlog items. |
| [poteto/setup-pstack](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/setup-pstack/SKILL.md) | setup | stable | Configures pstack's per-role models and reasoning budget using models the current host actually exposes. Writes an always-applied rule for future sessions. |
| [poteto/sharpen](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/sharpen/SKILL.md) | utility | stable | Rewrites a task prompt to seek deeper expertise, rawer evidence, concrete methods and an independent correctness check without expanding its scope. |
| [poteto/show-me-your-work](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/show-me-your-work/SKILL.md) | workflow | stable | Maintains an append-only TSV decision trail for long or unattended work. Audits it against the run transcript and obtains a different-model review before handoff. |
| [poteto/statechart](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/statechart/SKILL.md) | workflow | stable | Turns a TLA+ model into reader-labeled statecharts and numbered bug paths, or converts an agreed chart into a TLA+ starting point. Reports model scope and whether code-backed counterexamples reproduce. |
| [poteto/swarm](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/swarm/SKILL.md) | workflow | stable | Fans workers out across slices or declared races and consolidates their terminal results into one evidence-backed report. Missing coverage is recorded rather than counted as a pass. |
| [poteto/tdd](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/tdd/SKILL.md) | workflow | stable | Fixes a bug with a focused failing-before, passing-after regression check when a practical local test path exists. Uses another executable proof when a new test would be brittle or disproportionate. |
| [poteto/teach](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/teach/SKILL.md) | teaching | stable | Combines code behavior and historical rationale into a plain, conversational explanation at the learner's pace. Builds diagrams incrementally when they help understanding. |
| [poteto/technical-writing](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/technical-writing/SKILL.md) | reference | stable | Applies a layered standard for technical documents, choosing a document purpose before refining sentences, instructions and unambiguous language. |
| [poteto/typescript-best-practices](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/typescript-best-practices/SKILL.md) | reference | stable | Provides TypeScript-specific type modeling and boundary rules, emphasizing explicit variants, verified brands, schema-derived types and behavior checks. |
| [poteto/unslop](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/unslop/SKILL.md) | utility | stable | Edits prose to remove recurring AI writing patterns while preserving meaning and intended tone. |
| [poteto/why](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/why/SKILL.md) | workflow | stable | Investigates the historical reasons and constraints behind code across source control and available connected evidence categories. Separates explicit findings, inference, hypotheses and unresolved gaps. |

## Detailed cards

Use cases, boundaries and roles below are compiler interpretations. Evidence links point to exact upstream revisions. Effects are possible actions of the described workflow, not permissions granted by the catalog.

### matt/ask-matt

Selects an entry skill and a route through Matt’s collection, including idea-to-build work, diagnosis, maintenance, and context handoffs. It distinguishes standalone tools from shared reference layers.

- **Role / status:** router / stable.
- **Use when:** You know your situation but cannot remember which Matt skill fits.; You need to choose a multi-session build flow or a context transition.
- **Scope limits:** Catalog interpretation: Use the chosen skill’s full instructions before acting; this is orientation, not a substitute.
- **Result:** Recommended skill or skill sequence; Context-transition recommendation
- **Requirements:** Read each recommended SKILL.md before explaining or skipping it.; Engineering flows assume setup-matt-pocock-skills configuration.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** matt/grill-with-docs, matt/handoff, matt/prototype, matt/to-spec, matt/to-tickets, matt/implement, matt/implement-spec, matt/tdd, matt/code-review, matt/pr, matt/retro, matt/triage, matt/diagnosing-bugs, matt/wayfinder, matt/improve-codebase-architecture, matt/domain-modeling, matt/codebase-design, matt/grill-me, matt/grilling, matt/research, matt/to-questionnaire, matt/wizard, matt/wait-what, matt/teach, matt/writing-for-agents, matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:11–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md#L11-L30) — Router, idea flow and build-size branch
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:42–67](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md#L42-L67) — Diagnosis, incoming work, large planning and reference layers
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:81–97](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md#L81-L97) — Standalone routes and setup prerequisite
- **Evidence:** [skills/engineering/ask-matt/PHASE-BOUNDARIES.md:19–38](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/PHASE-BOUNDARIES.md#L19-L38) — Ordered continue, clear, handoff, subagent, compact decision tree

### matt/code-review

Reviews a fixed-point diff in two independent tracks: repository standards and conformity to the originating spec. It reports each track separately, with repository rules taking precedence over heuristic code smells.

- **Role / status:** workflow / stable.
- **Use when:** Review a branch or committed work since a known base.; Check whether a change matches both the requested behavior and repository conventions.
- **Scope limits:** Catalog interpretation: Resolve a valid nonempty comparison first.; Catalog interpretation: A missing spec can be reported as skipped rather than invented.
- **Result:** Separate Standards and Spec findings; Counts and worst finding within each axis
- **Requirements:** Git repository and a fixed point; source uses a merge-base three-dot diff.; Configured issue tracker; otherwise requests setup-matt-pocock-skills.; Parallel subagents.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** Asks for the fixed point if absent and for a spec source if none can be found. No approval gate for reporting is stated.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/code-review/SKILL.md:6–23](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md#L6-L23) — Two axes, delegation, fixed point and diff preconditions
- **Evidence:** [skills/engineering/code-review/SKILL.md:25–41](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md#L25-L41) — Spec discovery and repository precedence
- **Evidence:** [skills/engineering/code-review/SKILL.md:58–80](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md#L58-L80) — Subagent reporting and separate aggregation

### matt/codebase-design

Provides a shared vocabulary for placing small public interfaces over substantial behavior. Supporting guides cover dependency-aware deepening and comparing alternative interface designs.

- **Role / status:** reference / stable.
- **Use when:** Choose a module interface or testing seam.; Compare ways to consolidate architectural friction.
- **Scope limits:** Catalog interpretation: Do not treat this reference as an automatic implementation request.; Catalog interpretation: Avoid adding speculative seams when nothing actually varies.
- **Result:** Consistent design vocabulary; Interface and dependency strategy; Compared alternative designs when requested
- **Requirements:** Parallel subagents for the optional Design It Twice branch.
- **Possible effects:** read, delegate
- **Confirmation behavior:** The alternative-design branch shows the problem space to the user, then starts subagents without waiting; it later presents a recommendation.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:8–28](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md#L8-L28) — Deep-module vocabulary and intended result
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:60–65](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md#L60-L65) — Interface-oriented principles and seam criterion
- **Evidence:** [skills/engineering/codebase-design/SKILL.md:111–114](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md#L111-L114) — Conditional supporting guides
- **Evidence:** [skills/engineering/codebase-design/DESIGN-IT-TWICE.md:11–23](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/DESIGN-IT-TWICE.md#L11-L23) — User-facing framing and 3+ parallel designs
- **Evidence:** [skills/engineering/codebase-design/DEEPENING.md:9–35](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/DEEPENING.md#L9-L35) — Dependency-specific testing and replacement strategy

### matt/diagnosing-bugs

Builds a tight feedback command that catches the exact failure, minimizes the reproduction, tests ranked hypotheses, and verifies a fix. It treats an inadequate testing seam as an architectural finding rather than manufacturing a misleading regression test.

- **Role / status:** workflow / stable.
- **Use when:** A bug resists a first inspection or is intermittent.; A performance regression needs measurement and isolation.
- **Scope limits:** Catalog interpretation: Do not recommend hypothesizing before a red-capable feedback command exists.; Catalog interpretation: Production instrumentation requires the permission requested by this workflow.
- **Result:** Runnable symptom-specific reproduction; Ranked falsifiable hypotheses; Fix and regression test, or documented missing seam; Cleaned instrumentation and verified original scenario
- **Requirements:** Access to an environment or artifact that reproduces the symptom.; A runnable test, HTTP/CLI/browser harness, or structured human feedback loop.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Shows hypotheses before testing but does not block if the user is away. If no loop can be built, stops to request access, captured evidence, or permission for temporary production instrumentation.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:14–16](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md#L14-L16) — Redaction and sensitive-output handling
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:24–35](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md#L24-L35) — Feedback-loop options
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:53–66](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md#L53-L66) — Hard loop precondition and request for access or instrumentation
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:90–98](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md#L90-L98) — Hypothesis checkpoint does not block
- **Evidence:** [skills/engineering/diagnosing-bugs/SKILL.md:114–138](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md#L114-L138) — Regression seam, fix, original-loop verification and cleanup

### matt/domain-modeling

Sharpens a project’s domain terms against user scenarios and actual code, recording agreed language in glossaries. It offers short decision records only for meaningful, nonobvious, hard-to-reverse tradeoffs.

- **Role / status:** reference / stable.
- **Use when:** An overloaded term is causing design ambiguity.; A domain glossary or qualifying architectural decision needs recording.
- **Scope limits:** Catalog interpretation: Do not use a domain glossary as a specification or implementation scratchpad.; Catalog interpretation: Routine decisions that fail the ADR criteria do not need an ADR.
- **Result:** Updated GLOSSARY.md or context glossary; Optional numbered ADR
- **Requirements:** Working directory; follows GLOSSARY-MAP.md when present.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Surfaces contradictions for the user to resolve; captures terms when resolved. Offers ADRs sparingly after all three criteria hold.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:8–8](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md#L8-L8) — Active modeling rather than only reading vocabulary
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:24–40](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md#L24-L40) — Context layout and lazy file creation
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:44–74](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md#L44-L74) — Resolve terms, cross-check code, write inline and qualify ADRs
- **Evidence:** [skills/engineering/domain-modeling/ADR-FORMAT.md:3–15](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/ADR-FORMAT.md#L3-L15) — Small numbered local decision records

### matt/grill-with-docs

Combines a structured interview with persistent domain modeling so clarified decisions and vocabulary survive in the repository.

- **Role / status:** workflow / stable.
- **Use when:** Sharpen an idea in a repository while maintaining shared language.
- **Scope limits:** Catalog interpretation: For a conversation with no working directory, grill-me is the upstream router’s alternative.
- **Result:** Shared understanding; Glossary updates and qualifying ADRs
- **Requirements:** Skill invocation support for grilling and domain-modeling.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Inherits grilling’s wait for decisions and final confirmation, plus domain-modeling’s inline agreed documentation.
- **Explicit companions/references:** matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/grill-with-docs/SKILL.md:2–7](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md#L2-L7) — Wrapper invokes both primitive skills
- **Evidence:** [skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md#L28-L30) — User owns decisions and confirms understanding
- **Evidence:** [skills/engineering/domain-modeling/SKILL.md:60–74](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md#L60-L74) — Persistent glossary and conditional ADR writes

### matt/implement

Builds a supplied specification or tickets with tests at agreed seams, regular focused checks, and a final two-axis review. It commits completed work to the current branch.

- **Role / status:** workflow / stable.
- **Use when:** A scoped piece of work already has a spec or tickets.; Implement one ready ticket in a fresh context.
- **Scope limits:** Catalog interpretation: Clarify an ambiguous ticket reference before implementation.; Catalog interpretation: For orchestration of an entire ticket graph, implement-spec is the separate route.
- **Result:** Implemented code and tests; Review results; Commit on the current branch
- **Requirements:** Spec or tickets; issue-tracker access for ticket references.; Project typecheck and test commands.; Companion TDD and review capabilities, including parallel reviewers.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Asks when a ticket reference is ambiguous; TDD requires pre-agreed testing seams. No extra commit confirmation is specified.
- **Explicit companions/references:** matt/tdd, matt/code-review
- **Evidence:** [skills/engineering/implement/SKILL.md:7–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md#L7-L17) — Fetch ticket, TDD, checks, review and commit
- **Evidence:** [skills/engineering/tdd/SKILL.md:22–24](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L22-L24) — Mandatory human seam agreement

### matt/implement-spec

Orchestrates a specified ticket dependency graph across implementer worktrees, merging ready work onto one integration branch. It performs a final integration review and resolves work through the configured tracker.

- **Role / status:** workflow / stable.
- **Use when:** A multi-ticket spec is ready and you want parallel implementation.
- **Scope limits:** Catalog interpretation: Not an initial discovery or specification workflow.; Catalog interpretation: Requires coordination support for branches, worktrees and subagents.
- **Result:** Implemented integration branch; Completed tickets or review-ready PR; Removed implementer worktrees
- **Requirements:** Spec with tickets and blocking relationships.; Configured issue tracker; otherwise requests setup-matt-pocock-skills.; Background subagents, Git branches and worktrees; shared file access for optional exploration notes.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Conditional draft PR creation depends on tracker workflow or user request. It otherwise proceeds through implementation and ticket resolution; TDD seam confirmation remains part of the companion skill.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/tdd, matt/code-review
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:7–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement-spec/SKILL.md#L7-L17) — Spec graph and coordination assumptions
- **Evidence:** [skills/engineering/implement-spec/SKILL.md:21–40](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement-spec/SKILL.md#L21-L40) — Integration branch, worktrees, draft/ready PR, review, resolution and cleanup

### matt/improve-codebase-architecture

Surveys recent areas of change for architectural friction and produces a visual report of deepening candidates. After the user chooses one, it interviews them about the design and records resolved domain decisions.

- **Role / status:** workflow / stable.
- **Use when:** You want architectural improvement candidates grounded in real maintenance friction.
- **Scope limits:** Catalog interpretation: Do not jump to interface proposals before the user chooses a candidate.; Catalog interpretation: Purely theoretical refactors without observed friction are weak fits.
- **Result:** Temporary self-contained architecture-review HTML; Ranked before/after candidates; Follow-up design decisions and optional domain docs
- **Requirements:** Codebase and optional Git history, glossary and ADRs.; Subagent exploration; HTML uses Tailwind and Mermaid CDNs.; OS-specific file opener for the generated report.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Asks which candidate to explore before the grilling loop. Offers an ADR for a load-bearing rejection reason.
- **Explicit companions/references:** matt/codebase-design, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:13–27](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture/SKILL.md#L13-L27) — Vocabulary, domain context, hot spots and delegated scan
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:37–60](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture/SKILL.md#L37-L60) — Visual temporary report and candidate selection gate
- **Evidence:** [skills/engineering/improve-codebase-architecture/SKILL.md:62–71](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture/SKILL.md#L62-L71) — Grilling, inline docs and offered ADR

### matt/pr

Shapes a concise pull request body around a small explanatory visual, concrete before/after evidence, and rollback difficulty plus blast radius.

- **Role / status:** reference / stable.
- **Use when:** A pull request body needs to explain a concrete change.
- **Scope limits:** Catalog interpretation: Not a review process or a merge instruction.
- **Result:** PR body with Summary, Evidence and Merge Danger
- **Requirements:** Change details and concrete before/after evidence.; GLOSSARY.md vocabulary when available.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/pr/SKILL.md:12–37](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/pr/SKILL.md#L12-L37) — PR body template and writing scope
- **Evidence:** [skills/engineering/pr/SKILL.md:154–170](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/pr/SKILL.md#L154-L170) — Small visuals, evidence and merge-risk framing

### matt/prototype

Answers a specific design question with either a shareable logic demo or several switchable UI variants. It captures the validated decision and preserves the exploratory artifact outside the main branch.

- **Role / status:** workflow / stable.
- **Use when:** Test whether a state model handles awkward cases.; Compare structurally different UI directions.
- **Scope limits:** Catalog interpretation: Avoid using prototype constraints as the standard for production code.; Catalog interpretation: Prototype code excludes tests and production hardening; use scratch persistence only when the question explicitly concerns a database.
- **Result:** One-file HTML logic demo or UI variants; Decision and verdict; Preserved prototype branch and issue pointer
- **Requirements:** A specific design question; existing project conventions for UI work.; Git branch and issue-context mechanism for final capture.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** May ask to identify the question if the user is present; if unreachable, makes and states a context-based branch assumption. UI selection and demo feedback drive the answer.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/prototype/SKILL.md:8–26](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md#L8-L26) — Question branches, runnable artifacts, limits and capture
- **Evidence:** [skills/engineering/prototype/LOGIC.md:35–48](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/LOGIC.md#L35-L48) — Shareable one-file state exploration
- **Evidence:** [skills/engineering/prototype/UI.md:18–28](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/UI.md#L18-L28) — Prefer existing page over a new throwaway route
- **Evidence:** [skills/engineering/prototype/UI.md:98–112](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/UI.md#L98-L112) — Fold decision in and retain prototype separately; no real mutations
- **Evidence:** [skills/engineering/prototype/SKILL.md:23–24](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md#L23-L24) — Scratch-persistence exception is separate from the no-tests prototype constraint

### matt/research

Delegates a question to a background agent that follows claims to primary sources and leaves a cited Markdown research note.

- **Role / status:** workflow / stable.
- **Use when:** Gather official API facts or source-backed answers while other work continues.
- **Scope limits:** Catalog interpretation: Not a replacement for deciding how findings affect the design.
- **Result:** Cited Markdown findings in the repository
- **Requirements:** Background-agent support and access to the relevant primary sources.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/research/SKILL.md:6–12](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/research/SKILL.md#L6-L12) — Background research, source standard and local artifact

### matt/retro

Examines a coding session for improvements to the agent’s environment, such as navigation, automated checks, review standards and information access. It presents prioritized candidates rather than directly prescribing feature changes.

- **Role / status:** workflow / stable.
- **Use when:** A build went sideways or recurring mistakes suggest missing guardrails.
- **Scope limits:** Catalog interpretation: Not a retrospective on product functionality or a generic code refactor.; Catalog interpretation: Inspect existing checks before proposing new ones.
- **Result:** Severity-ordered environment improvement recommendations
- **Requirements:** Primary session context or accessible logs.; Existing repository check configuration and steering documents.
- **Possible effects:** read
- **Confirmation behavior:** Presents candidates to the user; no separate approval or implementation step is specified.
- **Explicit companions/references:** matt/writing-for-agents
- **Evidence:** [skills/engineering/retro/SKILL.md:7–25](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/retro/SKILL.md#L7-L25) — Environment focus, companion reference, source inspection and recommendations

### matt/setup-matt-pocock-skills

Configures the repository’s tracker, optional triage labels and domain-document conventions for Matt’s engineering workflows. It preserves existing steering files and allows local Markdown, GitHub, GitLab or a custom tracker.

- **Role / status:** setup / stable.
- **Use when:** Prepare a repository before using the engineering flows.; Intentionally switch the configured issue tracker.
- **Scope limits:** Catalog interpretation: Avoid recreating configuration that only needs a direct edit.; Catalog interpretation: Do not create a second steering file when one already exists.
- **Result:** docs/agents tracker/domain configuration; Optional triage-label configuration and created labels; Agent skills navigation block
- **Requirements:** Repository inspection; gh for GitHub or glab for GitLab operations.; User-provided workflow for other trackers.
- **Possible effects:** read, local_write, external_write, execute, configure
- **Confirmation behavior:** Presents findings, asks tracker and applicable layout/label questions, then shows draft files for edits before writing. Single-context docs default without a question.
- **Explicit companions/references:** matt/triage
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:9–15](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md#L9-L15) — Setup scope and confirm-before-write posture
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:38–61](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md#L38-L61) — Tracker variants and conditional questions
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:63–82](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md#L63-L82) — Draft review and steering-file preservation
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/SKILL.md:102–118](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md#L102-L118) — Optional remote labels and configuration output
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:3–15](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md#L3-L15) — Local tracker publication is file creation, not necessarily a remote write

### matt/tdd

Implements behavior one failing test and minimal implementation at a time, using agreed public testing seams. Its current rules reserve refactoring for the later review stage.

- **Role / status:** workflow / stable.
- **Use when:** Build a concrete behavior test-first.; Fix a behavior with regression coverage at a public seam.
- **Scope limits:** Catalog interpretation: Avoid unconfirmed seams and tests coupled to internal collaborators.; Catalog interpretation: Do not batch all tests before implementation or fold speculative refactoring into the loop.
- **Result:** Behavior-focused tests; Incremental passing implementation
- **Requirements:** User agreement on testing seams before writing tests.; Runnable project testing environment; glossary and ADR context when present.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Requires the user to confirm the seams before any test is written.
- **Explicit companions/references:** matt/codebase-design, matt/code-review
- **Evidence:** [skills/engineering/tdd/SKILL.md:8–16](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L8-L16) — Behavioral test reference
- **Evidence:** [skills/engineering/tdd/SKILL.md:18–26](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L18-L26) — Mandatory agreed seams and design vocabulary
- **Evidence:** [skills/engineering/tdd/SKILL.md:28–38](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L28-L38) — Anti-patterns, red-green slices and review-stage refactoring
- **Evidence:** [skills/engineering/tdd/mocking.md:3–14](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/mocking.md#L3-L14) — Mocks at system boundaries rather than owned internals

### matt/to-spec

Synthesizes existing discussion into a detailed feature specification and publishes it to the configured tracker. It includes user stories, decisions, test strategy and explicit scope.

- **Role / status:** workflow / stable.
- **Use when:** An idea has already been discussed and is ready to become a buildable spec.
- **Scope limits:** Catalog interpretation: Not an interview to discover unresolved requirements.
- **Result:** Published spec marked ready-for-agent; Agreed test seams
- **Requirements:** Conversation context and codebase understanding.; Configured tracker and triage-label vocabulary; otherwise requests setup-matt-pocock-skills.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** Checks proposed test seams with the user before writing and publishing the spec; it explicitly avoids a new requirements interview.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/to-spec/SKILL.md:7–19](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-spec/SKILL.md#L7-L19) — Synthesis-only scope, setup and test seam checkpoint
- **Evidence:** [skills/engineering/to-spec/SKILL.md:23–69](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-spec/SKILL.md#L23-L69) — Spec outputs, user stories, decisions and scope

### matt/to-tickets

Breaks an existing plan into independently verifiable vertical tickets with explicit blockers. It supports a local one-file-per-ticket tracker and remote native dependencies, with an expand–contract exception for wide refactors.

- **Role / status:** workflow / stable.
- **Use when:** Split a ready spec into fresh-session implementation tickets.; Sequence a mechanical refactor that cannot safely land as vertical slices.
- **Scope limits:** Catalog interpretation: Do not triage generated tickets again; they are agent-ready by construction.; Catalog interpretation: Do not modify or close a parent issue as part of ticket publication.
- **Result:** Approved ticket breakdown; Published tickets and blocking graph
- **Requirements:** Plan, spec or current discussion.; Configured tracker and label vocabulary; otherwise requests setup-matt-pocock-skills.
- **Possible effects:** read, local_write, external_write, execute
- **Confirmation behavior:** Iterates on granularity and blocking edges until the user approves the breakdown, then publishes.
- **Explicit companions/references:** matt/setup-matt-pocock-skills
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md#L9-L17) — Inputs and configuration
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:25–40](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md#L25-L40) — Vertical slicing and wide-refactor exception
- **Evidence:** [skills/engineering/to-tickets/SKILL.md:42–67](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md#L42-L67) — Human approval before local or remote publication; parent remains untouched

### matt/triage

Classifies and verifies incoming requests, interviews the maintainer when needed, and applies a triage state with a durable agent brief. External PRs participate only when enabled or specifically named.

- **Role / status:** workflow / stable.
- **Use when:** Raw bug reports or feature requests need maintainer decisions.; An external contribution needs verification and a next-step brief.
- **Scope limits:** Catalog interpretation: Generated agent-ready implementation tickets do not need this intake process.; Catalog interpretation: Conflicting roles or unusual transitions require maintainer direction.
- **Result:** Category and triage state; Agent brief or needs-info notes; Conditional rejection knowledge-base entry and closure
- **Requirements:** Configured issue tracker and role-to-label mapping.; Codebase access and runnable verification for claims.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Waits for direction after recommending a state. Asks on conflicting states or unusual transitions; quick overrides confirm impending role/comment/close changes before acting.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/triage/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md#L9-L17) — Tracker workflow and AI disclaimer
- **Evidence:** [skills/engineering/triage/SKILL.md:39–45](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md#L39-L45) — Role invariants and unusual-transition approval
- **Evidence:** [skills/engineering/triage/SKILL.md:64–90](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md#L64-L90) — PR scope, verify, interview, writes, closure and checkpoints
- **Evidence:** [skills/engineering/triage/AGENT-BRIEF.md:3–5](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/AGENT-BRIEF.md#L3-L5) — Brief is the authoritative behavioral contract
- **Evidence:** [skills/engineering/triage/OUT-OF-SCOPE.md:84–97](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/OUT-OF-SCOPE.md#L84-L97) — Only rejected enhancements enter rejection memory

### matt/wayfinder

Maps a very large uncertain effort as linked decision tickets, resolving one non-research ticket per session as the frontier becomes clear. By default it delivers decisions and a handoff to implementation planning.

- **Role / status:** workflow / stable.
- **Use when:** A greenfield project or large feature exceeds a single reasoning session.
- **Scope limits:** Catalog interpretation: A well-scoped build with a visible route does not need a map.; Catalog interpretation: Do not confuse decision tickets with implementation tasks unless the effort explicitly overrides the planning default.
- **Result:** Decision map and linked tickets; Resolution comments and updated frontier; Research or prototype assets linked from tickets
- **Requirements:** Configured tracker supporting maps, children, claims and blockers; local Markdown fallback.; Subagents for research; branch/push access for research artifacts.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** HITL decisions must come from live human exchange. If charting finds no fog, stops to ask how to proceed; charting itself stops after creating the map and research work.
- **Explicit companions/references:** matt/setup-matt-pocock-skills, matt/research, matt/prototype, matt/grilling, matt/domain-modeling
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:11–25](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md#L11-L25) — Planning default and configured tracker
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:65–80](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md#L65-L80) — Decision-ticket types, claims and human ownership
- **Evidence:** [skills/engineering/wayfinder/SKILL.md:103–128](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wayfinder/SKILL.md#L103-L128) — Session limit, charting and resolution operations
- **Evidence:** [skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:21–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md#L21-L30) — Local map and claim mechanics

### matt/wizard

Authors a staged interactive Bash procedure for actions only the human can complete. The generated script guides browser steps, captures values and can persist local environment variables and GitHub settings.

- **Role / status:** utility / stable.
- **Use when:** Credentials, provisioning or a cutover is blocked on human-only steps.
- **Scope limits:** Catalog interpretation: If the agent can perform the step itself, this is the wrong route.; Catalog interpretation: The authoring agent should not run the full interactive script itself.
- **Result:** Verified executable wizard script; Instructions for the human to run it; Optional documented repeatable setup path
- **Requirements:** Bash; optional shellcheck.; Bundled template; a browser opener where available.; Authenticated gh for GitHub writes, with documented manual fallback.
- **Possible effects:** read, local_write, external_write, execute, configure
- **Confirmation behavior:** Confirms stage order and captured-value destinations before authoring. Generated stages confirm before irreversible actions; the human runs the procedure.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/engineering/wizard/SKILL.md:8–12](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wizard/SKILL.md#L8-L12) — Wizard result, supported effects and ephemeral default
- **Evidence:** [skills/engineering/wizard/SKILL.md:18–25](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wizard/SKILL.md#L18-L25) — Stage-scope confirmation
- **Evidence:** [skills/engineering/wizard/SKILL.md:33–44](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wizard/SKILL.md#L33-L44) — Template use, irreversible gates, static validation and handoff
- **Evidence:** [skills/engineering/wizard/template.sh:137–178](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/wizard/template.sh#L137-L178) — Actual .env and conditional GitHub secret/variable mutations

### matt/chief-of-staff

Coordinates a long-running goal through background subagents while maintaining dated, source-linked knowledge in a durable wiki. It combines tactical delivery with improving the environment for later work.

- **Role / status:** workflow / experimental.
- **Use when:** A sustained goal requires strategic continuity and multiple delegated tasks.
- **Scope limits:** Catalog interpretation: Beta workflow; do not present it as part of the stable plugin.; Catalog interpretation: Requires an explicit shared wiki location before new durable memory writes.
- **Result:** Coordinated task progress; Interlinked historical wiki; Suggested recurring schedules and environment improvements
- **Requirements:** Background subagents.; Agreed wiki location; scheduling only where the harness supports it.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Agrees wiki location before the first write if none exists. Suggests schedules; automatic creation is not specified.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:7–28](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/chief-of-staff/SKILL.md#L7-L28) — Long-running coordination, schedules, delegation and wiki agreement
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:30–47](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/chief-of-staff/SKILL.md#L30-L47) — Historical, dated, source-linked wiki operations
- **Evidence:** [skills/in-progress/chief-of-staff/SKILL.md:49–68](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/chief-of-staff/SKILL.md#L49-L68) — Environmental improvement mandate

### matt/claude-handoff

Writes a redacted temporary handoff and immediately seeds a named Claude background agent with it. This extends the portable handoff concept with a Claude-specific launch.

- **Role / status:** utility / experimental.
- **Use when:** Resume current work in a fresh background Claude session.
- **Scope limits:** Catalog interpretation: Beta and Claude-specific; not a portable launch command for all agents.
- **Result:** Temporary handoff summary; Named background Claude agent
- **Requirements:** Claude CLI supporting --bg and --name; user manages launched jobs with claude agents.; Writable OS temporary directory.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/claude-handoff/SKILL.md:8–18](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/claude-handoff/SKILL.md#L8-L18) — Background command, descriptive name, pointers and redaction

### matt/loop-me

Interviews the user about recurring activities and turns selected loops into implementable workflow specifications. It maintains workspace notes and creates, edits or deletes specs as decisions settle.

- **Role / status:** workflow / experimental.
- **Use when:** Discover repeatable personal or work activities worth specifying.
- **Scope limits:** Catalog interpretation: Beta; not the implementation or scheduling of a workflow.; Catalog interpretation: Do not require AI, schedules or human checkpoints when the design does not need them.
- **Result:** workflows/*.md specifications; NOTES.md about the user’s world
- **Requirements:** Stateful working directory.; Shared grilling discipline.
- **Possible effects:** read, local_write, delegate
- **Confirmation behavior:** Runs grilling with user decisions; completion requires an implementer to need no further questions. Checkpoints in the resulting workflow are design choices, not mandatory.
- **Explicit companions/references:** matt/grilling
- **Evidence:** [skills/in-progress/loop-me/SKILL.md:8–22](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/loop-me/SKILL.md#L8-L22) — Grilling, loop/workflow distinction and optional structure
- **Evidence:** [skills/in-progress/loop-me/SKILL.md:25–32](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/loop-me/SKILL.md#L25-L32) — Implementability criterion and workspace files

### matt/setup-ts-deep-modules

Adds dependency-cruiser checks to enforce package entry points and private implementation folders in a TypeScript repository. It creates a copyable example and demonstrates enforcement with pass–fail–pass evidence.

- **Role / status:** setup / experimental.
- **Use when:** Enforce package-level imports through public root files.
- **Scope limits:** Catalog interpretation: Beta; the package layout is a deliberate convention, not a universal architecture rule.; Catalog interpretation: Existing dependency-cruiser configuration must be merged rather than overwritten.
- **Result:** Dependency-cruiser configuration and lint:boundaries check; Example package; Package README and steering-file pointer; Observed pass–fail–pass boundary check
- **Requirements:** TypeScript repository with a package manager.; Installs dependency-cruiser as a dev dependency.; Flat package roots; template references tsconfig.json.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Confirms package root if an obvious different convention already exists. It otherwise follows the prescribed setup and validates enforcement.
- **Explicit companions/references:** matt/codebase-design
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:9–35](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/setup-ts-deep-modules/SKILL.md#L9-L35) — Enforced public/private shape and scope
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:39–65](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/setup-ts-deep-modules/SKILL.md#L39-L65) — Environment detection, config merge, installation and wiring
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/SKILL.md:67–95](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/setup-ts-deep-modules/SKILL.md#L67-L95) — Example, enforcement proof and docs
- **Evidence:** [skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs:88–93](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs#L88-L93) — Template TypeScript resolver assumptions

### matt/writing-beats

Shapes fixed raw material into an article through user-selected narrative beats, tracking which concepts the audience already understands. Each accepted beat is written before alternatives for the next move are offered.

- **Role / status:** workflow / experimental.
- **Use when:** You have raw material and want to choose an article’s path one beat at a time.
- **Scope limits:** Catalog interpretation: Beta; this is shaping fixed material rather than gathering new fragments.; Catalog interpretation: Do not write ahead of the selected beat.
- **Result:** Separate article document; A progression of selected beats and grounded concepts
- **Requirements:** Markdown raw-material file and an agreed article output path.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Settles audience prerequisites, offers 2–3 choices and waits for the user to select each beat before writing.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:9–19](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-beats/SKILL.md#L9-L19) — Fixed-input shaping and per-beat selection
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:27–38](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-beats/SKILL.md#L27-L38) — Concept prerequisites and grounding
- **Evidence:** [skills/in-progress/writing-beats/SKILL.md:60–65](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-beats/SKILL.md#L60-L65) — One write at a time and preserve edits

### matt/writing-fragments

Interviews the author to collect unstructured fragments that could become future writing. It appends them to a single raw-material document without imposing an outline.

- **Role / status:** workflow / experimental.
- **Use when:** Explore a subject before deciding what article to write.
- **Scope limits:** Catalog interpretation: Beta; structure and article shaping are outside this skill.
- **Result:** Append-only Markdown fragment collection
- **Requirements:** Agreed output path; prompts if absent.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Asks for the path once; then appends fragments without requesting approval for each save. Specific edits or cuts follow user requests.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-fragments/SKILL.md:9–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-fragments/SKILL.md#L9-L17) — Exploration only, immediate capture and path question
- **Evidence:** [skills/in-progress/writing-fragments/SKILL.md:69–77](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-fragments/SKILL.md#L69-L77) — No imposed order, silent appends and reread-before-write

### matt/writing-shape

Turns a fixed raw-material file into a separate article through user-agreed openings, paragraphs and format choices. It keeps track of conceptual prerequisites and preserves the input unchanged.

- **Role / status:** workflow / experimental.
- **Use when:** You have a transcript or fragment pile and want collaborative paragraph-level shaping.
- **Scope limits:** Catalog interpretation: Beta; not new-fragment discovery, publication or editing the source material.
- **Result:** Separate article document; Agreed argument, opening and grounded progression
- **Requirements:** Raw-material Markdown file read in full.; Agreed article output path.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Settles reader prerequisites, requires a chosen opening, writes agreed blocks and leaves completion to the user.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/in-progress/writing-shape/SKILL.md:9–26](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-shape/SKILL.md#L9-L26) — Read-only source and user-led shaping loop
- **Evidence:** [skills/in-progress/writing-shape/SKILL.md:53–71](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-shape/SKILL.md#L53-L71) — Gap handling, format choices and preserving article edits
- **Evidence:** [skills/in-progress/writing-shape/SKILL.md:73–77](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/writing-shape/SKILL.md#L73-L77) — Scope exclusions

### matt/git-guardrails-claude-code

Installs a Claude Code PreToolUse hook that blocks configured risky Git command patterns before Bash execution. Project or global scope is chosen by the user.

- **Role / status:** setup / specialized.
- **Use when:** Configure explicit Git command restrictions for Claude Code.
- **Scope limits:** Catalog interpretation: Claude-specific hook; do not treat it as a portable policy engine.; Catalog interpretation: Pattern blocking should not be described as complete command-security verification.
- **Result:** Copied executable Git hook; Merged Claude settings hook configuration
- **Requirements:** Claude Code Bash hooks; Bash and jq in the bundled script.; Writable project or global .claude configuration, depending on scope.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Asks project versus global scope, then asks about adding or removing blocked patterns.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/git-guardrails-claude-code/SKILL.md:8–24](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/git-guardrails-claude-code/SKILL.md#L8-L24) — Hook purpose and scope question
- **Evidence:** [skills/misc/git-guardrails-claude-code/SKILL.md:26–39](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/git-guardrails-claude-code/SKILL.md#L26-L39) — Copy and configure hook
- **Evidence:** [skills/misc/git-guardrails-claude-code/SKILL.md:81–95](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/git-guardrails-claude-code/SKILL.md#L81-L95) — Merge settings, customization question and verification
- **Evidence:** [skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh:3–21](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh#L3-L21) — jq input parsing and regex-based command blocking

### matt/migrate-to-shoehorn

Replaces TypeScript test-data assertions with shoehorn helpers for partial or intentionally invalid inputs. It installs the helper package and verifies types after migration.

- **Role / status:** workflow / specialized.
- **Use when:** Test fixtures rely on broad as assertions or unwieldy full objects.
- **Scope limits:** Catalog interpretation: Test code only; the source excludes production use.
- **Result:** Migrated test fixtures; Installed @total-typescript/shoehorn dependency; Typecheck result
- **Requirements:** TypeScript test files; source installation command uses npm.; @total-typescript/shoehorn.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Asks which test files and data needs motivate the migration before installing and changing tests.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/migrate-to-shoehorn/SKILL.md:10–12](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/migrate-to-shoehorn/SKILL.md#L10-L12) — Partial data and test-only scope
- **Evidence:** [skills/misc/migrate-to-shoehorn/SKILL.md:97–118](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/migrate-to-shoehorn/SKILL.md#L97-L118) — Helper selection, questions, install, migration and typecheck

### matt/scaffold-exercises

Creates numbered course exercise directories with problem, solution or explainer stubs and validates them with the AI Hero course linter. It commits the completed structure.

- **Role / status:** utility / specialized.
- **Use when:** An AI Hero-style course plan needs correctly named exercise stubs.
- **Scope limits:** Catalog interpretation: Host-course convention and linter must be available; not a generic course generator.
- **Result:** Numbered section and exercise folders; Nonempty variant readmes; Linted and committed scaffold
- **Requirements:** pnpm ai-hero-cli internal lint.; Git repository and course-plan input.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:8–25](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/scaffold-exercises/SKILL.md#L8-L25) — Course linter, commit and structure
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:29–50](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/scaffold-exercises/SKILL.md#L29-L50) — Required files and scaffold workflow
- **Evidence:** [skills/misc/scaffold-exercises/SKILL.md:65–71](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/scaffold-exercises/SKILL.md#L65-L71) — History-preserving moves and rerun lint

### matt/setup-pre-commit

Installs Husky, lint-staged and Prettier to format staged files and run available typecheck/test scripts at commit time. It verifies the setup by committing through the new hook.

- **Role / status:** setup / specialized.
- **Use when:** A JavaScript repository needs commit-time formatting and checks.
- **Scope limits:** Catalog interpretation: Not a language-independent hook recipe.; Catalog interpretation: Missing typecheck or test scripts are reported and omitted rather than invented.
- **Result:** Husky hook and lint-staged configuration; Optional new Prettier configuration; Dependency and prepare-script updates; Smoke-test commit
- **Requirements:** JavaScript package manager; detects npm, pnpm, yarn or Bun.; Installs husky, lint-staged and prettier; recipe targets Husky v9+.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:8–35](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/setup-pre-commit/SKILL.md#L8-L35) — Setup components, package manager and initialization
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:37–59](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/setup-pre-commit/SKILL.md#L37-L59) — Hook steps and config behavior
- **Evidence:** [skills/misc/setup-pre-commit/SKILL.md:73–91](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/misc/setup-pre-commit/SKILL.md#L73-L91) — Verification, explicit commit and hook smoke test

### matt/grill-me

Runs the shared interview primitive to sharpen a plan or design without the repository-documentation wrapper.

- **Role / status:** workflow / stable.
- **Use when:** Stress-test an idea when no working directory is available.
- **Scope limits:** Catalog interpretation: For persistent project vocabulary and decisions in a repository, use grill-with-docs.
- **Result:** Confirmed shared understanding
- **Requirements:** Skill invocation for grilling.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Inherits grilling’s wait for user decisions and final confirmation of shared understanding.
- **Explicit companions/references:** matt/grilling
- **Evidence:** [skills/productivity/grill-me/SKILL.md:2–7](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grill-me/SKILL.md#L2-L7) — Interview wrapper invokes grilling
- **Evidence:** [skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md#L28-L30) — Fact-finding delegation and final human confirmation
- **Evidence:** [skills/engineering/ask-matt/SKILL.md:85–86](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/ask-matt/SKILL.md#L85-L86) — Stateless wrapper and repository alternative

### matt/grilling

Interviews the user in rounds of currently answerable decisions, advancing a dependency-aware design tree. The agent researches facts while the user owns the choices.

- **Role / status:** workflow / stable.
- **Use when:** Stress-test an idea, design or decision until assumptions are explicit.
- **Scope limits:** Catalog interpretation: Do not ask the user factual questions the agent can investigate.; Catalog interpretation: Do not act on the plan before shared understanding is confirmed.
- **Result:** Settled design tree; Confirmed shared understanding
- **Requirements:** Subagents for environmental fact-finding when needed.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Waits after each frontier of questions and requires final user confirmation before acting.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/grilling/SKILL.md:6–8](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md#L6-L8) — Round-based design-tree interview
- **Evidence:** [skills/productivity/grilling/SKILL.md:24–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md#L24-L30) — Recommended answers, facts versus decisions and final gate

### matt/handoff

Writes a portable, redacted summary so another agent can resume the work, referencing existing artifacts instead of copying them.

- **Role / status:** utility / stable.
- **Use when:** Move work to another harness, directory or colleague.; Fork a side task while preserving the current discussion.
- **Scope limits:** Catalog interpretation: The file does not itself launch or message a new agent.
- **Result:** Temporary Markdown handoff with suggested skills
- **Requirements:** Writable OS temporary directory.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/handoff/SKILL.md:8–16](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff/SKILL.md#L8-L16) — Temporary artifact, skill suggestions, pointers and redaction

### matt/teach

Builds a persistent learning workspace with short HTML lessons, reference materials, sources and evidence of learning. It chooses practice relative to the learner’s mission and recorded progress.

- **Role / status:** teaching / stable.
- **Use when:** Learn a topic across multiple sessions with cumulative exercises and references.
- **Scope limits:** Catalog interpretation: A quick explanation without a learning workspace is a different scope.; Catalog interpretation: Do not confuse coverage with demonstrated learning.
- **Result:** MISSION.md and curated RESOURCES.md; HTML lessons and reference sheets; Reusable assets and learning records
- **Requirements:** Current working directory becomes the teaching workspace.; Access to high-trust source material; optional OS opener for lessons.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Questions the user to establish a missing mission and confirms before changing it. User community preferences must be respected.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/teach/SKILL.md:8–20](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md#L8-L20) — Persistent workspace and artifacts
- **Evidence:** [skills/productivity/teach/SKILL.md:49–69](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md#L49-L69) — Short lessons and reusable components
- **Evidence:** [skills/productivity/teach/SKILL.md:73–95](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md#L73-L95) — Mission, explicit change confirmation and trusted sources
- **Evidence:** [skills/productivity/teach/SKILL.md:116–120](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md#L116-L120) — Community preference
- **Evidence:** [skills/productivity/teach/LEARNING-RECORD-FORMAT.md:29–42](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/LEARNING-RECORD-FORMAT.md#L29-L42) — Records require evidence or durable prior knowledge, not activity logs

### matt/to-questionnaire

Creates a discovery questionnaire for one external knowledge holder after clarifying who receives it and what the user needs back. It writes a local document for asynchronous completion or a meeting.

- **Role / status:** utility / stable.
- **Use when:** A decision depends on facts held by another person.
- **Scope limits:** Catalog interpretation: Not an interview of the user about a subject they cannot answer.; Catalog interpretation: Writing the questionnaire does not authorize sending it.
- **Result:** to-questionnaire-<slug>.md with context, prioritized questions and answer stubs
- **Requirements:** User identifies the recipient’s role and needed decisions or facts.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Asks two exchanges about the recipient and required outcome before writing. No send operation is specified.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/to-questionnaire/SKILL.md:7–20](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/to-questionnaire/SKILL.md#L7-L20) — Gap-directed discovery, two exchanges and local write
- **Evidence:** [skills/productivity/to-questionnaire/SKILL.md:24–52](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/to-questionnaire/SKILL.md#L24-L52) — Document form

### matt/wait-what

Re-explains the preceding message with missing context, simplified English and the project’s established vocabulary.

- **Role / status:** utility / stable.
- **Use when:** The last explanation did not land and needs a clearer pitch.
- **Scope limits:** Catalog interpretation: Not a request to restart the whole underlying workflow.
- **Result:** Clearer contextualized explanation
- **Requirements:** GLOSSARY.md or GLOSSARY-MAP.md when present; ASD-STE100 style reference in the request.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/wait-what/SKILL.md:2–7](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/wait-what/SKILL.md#L2-L7) — Re-pitch instruction and vocabulary requirement

### matt/writing-for-agents

Guides the structure and wording of documents agents consume, using conditional pointers, explicit completion criteria and a single source for each meaning. A supporting guide explains skill invocation and router design.

- **Role / status:** reference / stable.
- **Use when:** Create or edit a skill, steering file or agent-facing reference.
- **Scope limits:** Catalog interpretation: Not a general prose style guide for a human audience.; Catalog interpretation: Do not assume its documented invocation mechanics are universal across hosts.
- **Result:** More predictable agent-facing instructions; Sharper context pointers and completion criteria
- **Requirements:** Read supporting SKILL-MECHANICS.md when authoring a skill.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:6–18](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md#L6-L18) — Scope and conditional context pointers
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:29–59](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md#L29-L59) — Information hierarchy, completion criteria and splitting
- **Evidence:** [skills/productivity/writing-for-agents/SKILL.md:76–81](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md#L76-L81) — Single source, relevance and pruning
- **Evidence:** [skills/productivity/writing-for-agents/SKILL-MECHANICS.md:9–22](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL-MECHANICS.md#L9-L22) — Host-oriented invocation distinctions and router guidance

### poteto/architect

Explores competing type and module designs, synthesizes a usage-first sketch, then implements against it. The human design checkpoint is opt-in.

- **Role / status:** workflow / stable.
- **Use when:** A nontrivial change could lock in the wrong module boundary.; A requirement changes ownership or layering.
- **Scope limits:** Catalog interpretation: Use a read-only explanation workflow when implementation is unwanted.; Catalog interpretation: Request with checkpoint when the sketch must be reviewed before implementation.
- **Result:** Usage sketch and type signatures; Module map and design rationale; Implementation against the selected sketch
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Todo-list support and isolated candidate output directories or git worktrees.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Proceeds to implementation by default. Stops for sign-off only when the invoker explicitly asks for a checkpoint.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/arena, poteto/interrogate, poteto/principle-exhaust-the-design-space, poteto/principle-foundational-thinking, poteto/principle-outcome-oriented-execution, poteto/principle-redesign-from-first-principles, poteto/principle-fix-root-causes, poteto/principle-subtract-before-you-add
- **Evidence:** [pstack/skills/architect/SKILL.md:21–47](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/architect/SKILL.md#L21-L47) — Grounding, parallel designs, opt-in checkpoint and implementation default.
- **Evidence:** [pstack/skills/architect/SKILL.md:51–79](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/architect/SKILL.md#L51-L79) — Implementation, redesign triggers and outputs.
- **Evidence:** [pstack/skills/architect/references/runner-prompt.md:9–18](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/architect/references/runner-prompt.md#L9-L18) — Usage-first signatures, boundaries and type invariants.

### poteto/arena

Runs several candidates on the same brief, compares them using a rubric and an independent judge, and combines selected strengths into one verified artifact.

- **Role / status:** workflow / stable.
- **Use when:** One artifact admits several plausible designs.; You want a bakeoff rather than separate investigation slices.
- **Scope limits:** Catalog interpretation: Use swarm for partitioned coverage without synthesizing competing artifacts.; Catalog interpretation: Avoid for a settled, trivial shape where multiple full attempts add little.
- **Result:** Synthesized artifact; Synthesis note with selected base, grafts, rejected choices and verification
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Task background spawning; isolated per-candidate worktree or scratch output.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/poteto-mode, poteto/principle-separate-before-serializing-shared-state, poteto/principle-redesign-from-first-principles, poteto/principle-prove-it-works
- **Evidence:** [pstack/skills/arena/SKILL.md:13–28](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/arena/SKILL.md#L13-L28) — Shared brief, models, isolated outputs and cross-judge.
- **Evidence:** [pstack/skills/arena/SKILL.md:30–48](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/arena/SKILL.md#L30-L48) — Rubric selection, grafting, verification and deliverable.

### poteto/automate-me

Turns recurring working preferences into a personal mode skill using workspace-scoped history and direct questions. Revises an existing mode instead of starting over by default.

- **Role / status:** workflow / stable.
- **Use when:** Capture a recurring personal working style for agents.; Refresh an existing personal mode with recent evidence.
- **Scope limits:** Catalog interpretation: Use ordinary skill authoring for one narrow workflow.; Catalog interpretation: Do not mine unrelated projects to infer preferences.
- **Result:** Personal -mode SKILL.md; Worktree commit and pull request
- **Requirements:** Cursor built-in create-skill, AskQuestion, workspace agent-transcripts path and Cursor skill directories.; Git and pull-request workflow; user handle or chosen identifier.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Confirms whether to update an existing mode unless already requested, asks structured preference questions, and shows the draft for feedback. Ships through a PR rather than pushing directly to main.
- **Explicit companions/references:** poteto/unslop, poteto/poteto-mode
- **Evidence:** [pstack/skills/automate-me/SKILL.md:15–46](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/automate-me/SKILL.md#L15-L46) — Existing-mode intent check, workspace-scoped mining and direct interview.
- **Evidence:** [pstack/skills/automate-me/SKILL.md:65–83](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/automate-me/SKILL.md#L65-L83) — Authoring, draft feedback and PR delivery.
- **Evidence:** [pstack/skills/automate-me/SKILL.md:100–103](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/automate-me/SKILL.md#L100-L103) — Narrow workflow exclusions.

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
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:9–17](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/benchmark-checklist/SKILL.md#L9-L17) — Ballpark exception and machine/script preflight.
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:21–27](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/benchmark-checklist/SKILL.md#L21-L27) — Limiter, tuning, physical limits, errors, repeated runs and completed work.
- **Evidence:** [pstack/skills/benchmark-checklist/SKILL.md:29–39](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/benchmark-checklist/SKILL.md#L29-L39) — Reporting and mode playbook links.

### poteto/blast-radius

Finds downstream breakage that a diff or caller list can miss and executes a small proof of the safety fact the change depends on.

- **Role / status:** workflow / stable.
- **Use when:** A small change has uncertain effects outside its immediate callers.; An integration or teardown change depends on library behavior.
- **Scope limits:** Catalog interpretation: Use how for a runtime walkthrough without a proposed change.; Catalog interpretation: Do not equate a persuasive writeup with an executed safety proof.
- **Result:** Safety fact proved or marked unproven; Confirmed risks, cleared cases and cheapest regression check
- **Requirements:** Access to the real shipped library/code and an executable check; git and PR history through why.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/arena, poteto/unslop
- **Evidence:** [pstack/skills/blast-radius/SKILL.md:15–29](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/blast-radius/SKILL.md#L15-L29) — Proof ladder and executable checks.
- **Evidence:** [pstack/skills/blast-radius/SKILL.md:31–48](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/blast-radius/SKILL.md#L31-L48) — Diff, library and downstream investigation; synthesis and output.

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
- **Evidence:** [pstack/skills/bro/SKILL.md:2–7](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/bro/SKILL.md#L2-L7) — Restatement scope and style.

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
- **Evidence:** [pstack/skills/correct/SKILL.md:13–26](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/correct/SKILL.md#L13-L26) — Repeated-class threshold, enforcement order and proof.
- **Evidence:** [pstack/skills/correct/SKILL.md:28–32](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/correct/SKILL.md#L28-L32) — Agent rule table and reporting.

### poteto/create-formal-verification-skill

Builds and proves a project-local formal verification workflow for a costly invariant tests seldom reach. Records model scope, assumptions and the code synchronization commit.

- **Role / status:** workflow / stable.
- **Use when:** Concurrency, retries or state-machine ordering threaten an important invariant.; Code needs bounded or stronger verification beyond example tests.
- **Scope limits:** Catalog interpretation: Do not claim a bounded model proves the whole system.; Catalog interpretation: Report product bugs rather than changing product code without a request.
- **Result:** Verification model or code-level harness; Project-local verify skill with coverage and sync commit; Broken-variant demonstration and plain-language findings
- **Requirements:** An installable, reproducible verifier fitting the code and property; TLA+ is the stated default for interleavings.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Asks only for facts not observable in the code. Product code changes require the user to ask.
- **Explicit companions/references:** poteto/statechart, poteto/maintain-formal-verification-skill
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:13–29](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-formal-verification-skill/SKILL.md#L13-L29) — Target choice, tool choice, product-code boundary and scope.
- **Evidence:** [pstack/skills/create-formal-verification-skill/SKILL.md:31–43](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-formal-verification-skill/SKILL.md#L31-L43) — Generated skill, statechart link, deliberate-failure validation and handoff.

### poteto/create-verification-skill

Creates a repository-specific skill that launches, health-checks, drives and cleans up the real app. Seeds a user-facing feature map and executes one complete journey before handoff.

- **Role / status:** workflow / stable.
- **Use when:** A project lacks a reliable way for agents to prove observable behavior.; An app needs a launch, doctor, drive and evidence recipe.
- **Scope limits:** Catalog interpretation: Do not generate untested steps against a broken startup base.; Catalog interpretation: Do not drive a shared user instance when isolation is unavailable.
- **Result:** .cursor/skills/verify-<app>/SKILL.md and helpers; Feature README and initial feature journey files; Evidence from an end-to-end proof with cleanup
- **Requirements:** A runnable app and repository launch commands.; An appropriate harness such as browser/CDP, existing Playwright/Cypress, HTTP or isolated PTY/tmux.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Asks the user only what cannot be observed from the repository. No general approval gate is specified.
- **Explicit companions/references:** poteto/maintain-verification-skill
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:11–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-verification-skill/SKILL.md#L11-L21) — Repo interview, harness selection and startup precondition.
- **Evidence:** [pstack/skills/create-verification-skill/SKILL.md:23–40](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/create-verification-skill/SKILL.md#L23-L40) — Generated sections, observable evidence, feature map and execution proof.

### poteto/figure-it-out

Designs a custom, auditable workflow when bundled playbooks do not fit or a change is ambitious. Runs small hypothesis-driven units against an explicit completion predicate.

- **Role / status:** workflow / stable.
- **Use when:** A large migration needs a task-specific sequence of verifiable units.; A human will review a long run after stepping away.
- **Scope limits:** Catalog interpretation: Use a narrower playbook for a routine focused change.; Catalog interpretation: Use the mode Orchestrate playbook for a standing multiday program.
- **Result:** Written bespoke phase list; Verified units and decision trail; Final predicate verdict with open gaps
- **Requirements:** Todo-list support, executable verification harness and isolated branches or worktrees for writers.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Presents framing and tradeoffs before a long commitment; explicitly says a multi-hour run earns one checkpoint, while reversible work proceeds.
- **Explicit companions/references:** poteto/poteto-mode, poteto/architect, poteto/arena, poteto/show-me-your-work, poteto/principle-prove-it-works, poteto/principle-never-block-on-the-human, poteto/principle-foundational-thinking, poteto/principle-separate-before-serializing-shared-state, poteto/principle-laziness-protocol, poteto/principle-sequence-verifiable-units, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:9–32](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/figure-it-out/SKILL.md#L9-L32) — Workflow-first deliverable, framing checkpoint and decomposition.
- **Evidence:** [pstack/skills/figure-it-out/SKILL.md:34–52](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/figure-it-out/SKILL.md#L34-L52) — Execution loop, audit trail and final proof.

### poteto/how

Explains a subsystem's architecture, runtime flow and ownership using code-grounded exploration. Scales from one explainer to several explorers and a synthesizer.

- **Role / status:** workflow / stable.
- **Use when:** Understand how a subsystem works before changing it.; Determine which module owns a behavior or where new code should live.
- **Scope limits:** Catalog interpretation: Use why for historical motivation rather than runtime mechanics.; Catalog interpretation: Take the single-explainer route for narrow questions.
- **Result:** Architectural explanation with applicable overview, concepts, flow, file map and gotchas
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Cursor generalPurpose readonly Task subagents and code read/search access.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/poteto-mode
- **Evidence:** [pstack/skills/how/SKILL.md:9–28](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/how/SKILL.md#L9-L28) — Host-specific agents and complexity-based exploration.
- **Evidence:** [pstack/skills/how/SKILL.md:30–36](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/how/SKILL.md#L30-L36) — Presentation and output shape.
- **Evidence:** [pstack/skills/how/references/explainer-prompt.md:19–46](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/how/references/explainer-prompt.md#L19-L46) — Grounded synthesis and optional diagrams.

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
- **Evidence:** [pstack/skills/in-your-own-words/SKILL.md:2–7](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/in-your-own-words/SKILL.md#L2-L7) — Understanding-check scope.

### poteto/interrogate

Obtains independent adversarial reviews from configured models and produces a lead judgment rather than automatically fixing the findings.

- **Role / status:** workflow / stable.
- **Use when:** Stress-test a change for correctness, security and design weaknesses.; Get a diverse review panel for a contested implementation.
- **Scope limits:** Catalog interpretation: Do not treat this as permission to apply suggested changes.; Catalog interpretation: It challenges execution against stated intent rather than deciding whether the goal is right.
- **Result:** Intent statement; Act on, Consider, Noted and Dismissed findings; Model agreement map
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Cursor readonly generalPurpose Task reviewers and git diff or supplied scope.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** Asks the user when the change's intent is uncertain. Explicitly does not auto-apply review changes.
- **Explicit companions/references:** poteto/poteto-mode
- **Evidence:** [pstack/skills/interrogate/SKILL.md:9–38](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/SKILL.md#L9-L38) — Review-only delivery, intent clarification and model roster.
- **Evidence:** [pstack/skills/interrogate/SKILL.md:40–74](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/SKILL.md#L40-L74) — Synthesis and decision buckets.
- **Evidence:** [pstack/skills/interrogate/references/reviewer-prompt.md:11–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/references/reviewer-prompt.md#L11-L15) — Reviews execution, not the correctness of intent.
- **Evidence:** [pstack/skills/interrogate/references/lead-judgment.md:7–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/references/lead-judgment.md#L7-L19) — Rejects unsupported and preference-only findings.
- **Evidence:** [pstack/skills/interrogate/SKILL.md:13–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/SKILL.md#L13-L19) — Feature-branch scope explicitly executes git diff before read-only reviewer delegation.

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
- **Evidence:** [pstack/skills/ketchup/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup/SKILL.md#L9-L19) — Time window, style, read-only scope and action-item definition.
- **Evidence:** [pstack/skills/ketchup/SKILL.md:23–43](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup/SKILL.md#L23-L43) — Reply structure, risks, options and evidence-backed visuals.

### poteto/ketchup-video

Delivers the ketchup catch-up as a short silent slide video, with outstanding decisions retained as text under it.

- **Role / status:** utility / stable.
- **Use when:** A visual catch-up is easier to follow as a short animated sequence.
- **Scope limits:** Catalog interpretation: Use ordinary ketchup when video production adds little.; Catalog interpretation: Use only existing work evidence rather than inventing screens.
- **Result:** Silent landscape video; Text action items and remaining work
- **Requirements:** A video renderer and existing screenshots, recordings, diffs or data.; A scratch output location outside the repository.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/ketchup
- **Evidence:** [pstack/skills/ketchup-video/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup-video/SKILL.md#L9-L19) — Ketchup inheritance, read-only exception, slide evidence and limits.
- **Evidence:** [pstack/skills/ketchup-video/SKILL.md:21–23](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/ketchup-video/SKILL.md#L21-L23) — Rendering, timing and frame inspection.

### poteto/maintain-formal-verification-skill

Reconciles formal checks with code changes since their synchronization commit. Separates verification drift from real product bugs and proves updated checks can still fail.

- **Role / status:** workflow / stable.
- **Use when:** Merges or refactors changed verified code without rechecking its model.; An old passing formal check may describe stale behavior.
- **Scope limits:** Catalog interpretation: Use create-formal-verification-skill when no project check exists.; Catalog interpretation: Keep product fixes separate and do not weaken properties to obtain a pass.
- **Result:** Per-check in sync, updated, bug or blocked verdict; Verification-only updates and synchronized coverage records; Counterexample or deliberate-break evidence
- **Requirements:** Existing project-local formal verification skill, its verifier command and git history.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Product code changes require a user request. Properties change only with cited evidence that the intended promise changed.
- **Explicit companions/references:** poteto/create-formal-verification-skill
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:9–28](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-formal-verification-skill/SKILL.md#L9-L28) — Scope, outcome types and missing-skill route.
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:30–44](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-formal-verification-skill/SKILL.md#L30-L44) — Baseline, history reconciliation, rerun and sync commit.
- **Evidence:** [pstack/skills/maintain-formal-verification-skill/SKILL.md:46–58](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-formal-verification-skill/SKILL.md#L46-L58) — Evidence reporting and separate verification change.

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
- **Evidence:** [pstack/skills/maintain-verification-skill/SKILL.md:9–25](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-verification-skill/SKILL.md#L9-L25) — Feature-level coverage, limited edit scope and target selection.
- **Evidence:** [pstack/skills/maintain-verification-skill/SKILL.md:27–39](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/maintain-verification-skill/SKILL.md#L27-L39) — Source wave, mandatory live pass, proof preservation and PR rules.

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
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:11–51](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/make-bot-ui/SKILL.md#L11-L51) — Routine creation, confirmation card and user-only secret provisioning.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:53–73](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/make-bot-ui/SKILL.md#L53-L73) — Server forwarding, key placement and probes.
- **Evidence:** [pstack/skills/make-bot-ui/SKILL.md:75–103](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/make-bot-ui/SKILL.md#L75-L103) — Tailnet hosting and user machine approval.

### poteto/no-comments

Runs a specialized comment-removal agent, validates its findings and fixes accepted in-scope code workarounds. Can propose structural replacements for claimed constraints.

- **Role / status:** workflow / stable.
- **Use when:** Prepare a scoped diff for review under pstack's strict comment policy.; Replace workaround explanations with code that makes the behavior clear.
- **Scope limits:** Catalog interpretation: Do not select when the task is to preserve or merely proofread comments.; Catalog interpretation: Do not allow a root-cause argument to expand the caller's file boundary.
- **Result:** Scoped comment deletions; Accepted root-cause fixes and optional architect sketch; Report of encodings, unenforced constraints and open work
- **Requirements:** Cursor Task subagent_type comment-sicko and caller files/diff or base-branch diff.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Constraint encodings wait for interactive approval; unattended/eval runs need caller pre-approval. The source says unapproved encodings still result in deleting the comment and reporting the constraint open.
- **Explicit companions/references:** poteto/poteto-mode, poteto/how, poteto/why, poteto/architect, poteto/principle-fix-root-causes, poteto/principle-redesign-from-first-principles
- **Evidence:** [pstack/skills/no-comments/SKILL.md:13–24](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/no-comments/SKILL.md#L13-L24) — Scoped delegation, rejections, fixes, approval and report.
- **Evidence:** [pstack/agents/comment-sicko.md:14–30](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/agents/comment-sicko.md#L14-L30) — Narrow keep exceptions, suppressions and comment-only delegate edits.

### poteto/poteto-help

Helps choose a pstack setup path, skill, playbook or principle and returns an example prompt with a source link. It distinguishes help from an actual request to execute work.

- **Role / status:** router / stable.
- **Use when:** Find the right pstack entry point without memorizing its skills.; Understand setup, cost, host support or why a run drifted.
- **Scope limits:** Catalog interpretation: Help questions should not start a token-consuming workflow.; Catalog interpretation: Read the destination skill before recommending its detailed behavior.
- **Result:** Direct answer with public source link; At most one tailored example prompt; Optional need-category question
- **Requirements:** Read access to the installed pstack files and relevant guide pages.; Cursor-specific setup and model state checks; Claude Code adapter for that host.
- **Possible effects:** read
- **Confirmation behavior:** May ask one need-category question and offer setup once. A help answer returns a prompt for the user to invoke rather than starting the workflow.
- **Explicit companions/references:** poteto/setup-pstack, poteto/poteto-mode, poteto/in-your-own-words, poteto/sharpen, poteto/how, poteto/why, poteto/teach, poteto/recall, poteto/ketchup, poteto/ketchup-video, poteto/blast-radius, poteto/architect, poteto/arena, poteto/swarm, poteto/interrogate, poteto/tdd, poteto/typescript-best-practices, poteto/no-comments, poteto/unslop, poteto/technical-writing, poteto/bro, poteto/create-verification-skill, poteto/maintain-verification-skill, poteto/create-formal-verification-skill, poteto/maintain-formal-verification-skill, poteto/statechart, poteto/benchmark-checklist, poteto/figure-it-out, poteto/show-me-your-work, poteto/automate-me, poteto/reflect, poteto/correct, poteto/make-bot-ui
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:9–34](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-help/SKILL.md#L9-L34) — Help/execution distinction, question categories and setup checks.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:38–60](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-help/SKILL.md#L38-L60) — Native onboarding, Cursor and Claude Code support and mode persistence.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:62–118](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-help/SKILL.md#L62-L118) — Skill routing table, close calls and external dependencies.
- **Evidence:** [pstack/skills/poteto-help/SKILL.md:120–135](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-help/SKILL.md#L120-L135) — Playbooks, planning and principle entry points.

### poteto/poteto-mode

Coordinates pstack's working style and task-specific playbooks, selecting companion skills for grounding, design, delegation, verification and delivery. Its scope ranges from read-only investigation to autonomous PR programs.

- **Role / status:** router / stable.
- **Use when:** Run a nontrivial task with an explicit goal and a completion check.; Route a bug, feature, performance effort, PR lifecycle or multistage program through a playbook.
- **Scope limits:** Catalog interpretation: Use a narrow skill directly when the full workflow overhead is unnecessary.; Catalog interpretation: Do not interpret a read-only investigation as permission to implement.; Catalog interpretation: Review host support and approval rules before transferring this orchestration to another agent environment.
- **Result:** Playbook todo list; Task-specific verified artifacts or cited answers; PRs, plans, prototypes or audit trails as selected by the playbook
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Cursor Task poteto-agent and comment-sicko; built-in create-skill and loop.; cursor-team-kit deslop, control-ui and control-cli for relevant tasks.; Git worktrees and GitHub CLI by default; optional Origin CLI.; Bun for orchestrate bookkeeping and the GitHub watcher, whose first use can install frozen dependencies; Node for plan validation; app-specific live-control and verification tools.
- **Possible effects:** read, local_write, external_write, execute, delegate, configure
- **Confirmation behavior:** Source permits reversible work and external actions such as team chat or ticket updates without asking, but pauses for force-push to shared branches, deploys, data deletion and customer messages. Playbooks add explicit gates: plans wait for go, Babysit does not authorize merging, Autopilot-stack reserves landing for the human, and named operator gates remain binding.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/architect, poteto/arena, poteto/swarm, poteto/interrogate, poteto/unslop, poteto/technical-writing, poteto/no-comments, poteto/benchmark-checklist, poteto/figure-it-out, poteto/show-me-your-work, poteto/setup-pstack, poteto/tdd, poteto/ketchup, poteto/principle-boundary-discipline, poteto/principle-model-the-domain, poteto/principle-fix-root-causes, poteto/principle-encode-lessons-in-structure, poteto/principle-guard-the-context-window, poteto/principle-subtract-before-you-add, poteto/principle-foundational-thinking, poteto/principle-build-the-lever, poteto/principle-make-operations-idempotent, poteto/principle-sequence-verifiable-units, poteto/principle-test-behavior-not-implementation, poteto/principle-explain-the-number, poteto/principle-outcome-oriented-execution, poteto/principle-never-block-on-the-human, poteto/principle-redesign-from-first-principles, poteto/principle-minimize-reader-load, poteto/principle-exhaust-the-design-space, poteto/principle-migrate-callers-then-delete-legacy-apis, poteto/principle-attack-the-premise, poteto/principle-laziness-protocol, poteto/principle-experience-first, poteto/principle-prove-it-works, poteto/principle-separate-before-serializing-shared-state, poteto/principle-type-system-discipline
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:19–36](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L19-L36) — Routing triggers and companion workflows.
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:81–101](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L81-L101) — Autonomy and host-specific subagent policy.
- **Evidence:** [pstack/skills/poteto-mode/SKILL.md:121–149](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L121-L149) — Playbook categories and task routing.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/investigation.md:5–12](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/investigation.md#L5-L12) — Read-only investigation does not create PRs or implement.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:3–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L3-L15) — Plan-only output, explicit execution go and high verification requirements.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/autopilot-stack.md:3–10](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L3-L10) — Stacked delivery reserves landing for the operator.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/opening-a-pr.md:24–34](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/opening-a-pr.md#L24-L34) — Forge/tool precedence, ready PR default and babysit separation.
- **Evidence:** [pstack/skills/poteto-mode/playbooks/shipping.md:5–10](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/shipping.md#L5-L10) — Independent per-PR verification and controlled bottom-up landing.
- **Evidence:** [pstack/skills/poteto-mode/scripts/bootstrap.ts:25–38](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/scripts/bootstrap.ts#L25-L38) — Missing or outdated dependency installations run bun install --frozen-lockfile before the CLI continues.
- **Evidence:** [pstack/skills/poteto-mode/scripts/watch-pr/watch-pr:1–5](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/scripts/watch-pr/watch-pr#L1-L5) — The GitHub watcher is a Bun entry point and invokes dependency bootstrap before loading its CLI.

### poteto/principle-attack-the-premise

Interrupts repeated failed fixes by making their shared assumption explicit and testing it before another attempt.

- **Role / status:** principle / stable.
- **Use when:** Two fixes based on the same explanation fail the same check.
- **Scope limits:** Catalog interpretation: A new requirement calls for redesign rather than falsifying an assumed fact.
- **Result:** Written shared premise; Rerunnable discriminating observation; Evidence-based next debugging direction
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/principle-build-the-lever, poteto/principle-fix-root-causes, poteto/principle-laziness-protocol
- **Evidence:** [pstack/skills/principle-attack-the-premise/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-attack-the-premise/SKILL.md#L9-L19) — Trigger, premise test, rerunnable check, root-cause continuation and stop condition.
- **Evidence:** [pstack/skills/principle-attack-the-premise/SKILL.md:21–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-attack-the-premise/SKILL.md#L21-L21) — Distinction from redesign around a new requirement.

### poteto/principle-boundary-discipline

Concentrates parsing, validation and error handling at system boundaries, leaving internal business logic expressed as typed pure functions.

- **Role / status:** principle / stable.
- **Use when:** Wiring a CLI, configuration parser, network adapter or external API.; Reviewing redundant checks buried inside domain logic.
- **Scope limits:** Catalog interpretation: The task needs a complete implementation workflow rather than a placement rule.; Catalog interpretation: The supposedly internal input has not actually been parsed into a trusted domain type.
- **Result:** Boundary parsing and validation policy; Pure domain functions with thin framework wiring
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-boundary-discipline/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-boundary-discipline/SKILL.md#L9-L16) — Boundary guards, typed internals, pure logic and public domain concepts.
- **Evidence:** [pstack/skills/principle-boundary-discipline/SKILL.md:20–34](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-boundary-discipline/SKILL.md#L20-L34) — Concrete validation and organization applications and review questions.

### poteto/principle-build-the-lever

Turns nontrivial work into a small rerunnable tool or an explicit delegate recipe, making the result reproducible for reviewers.

- **Role / status:** principle / stable.
- **Use when:** A migration or analysis needs a repeatable transformation.; A one-off nontrivial task needs a check a reviewer can rerun.
- **Scope limits:** Catalog interpretation: The work is a couple of obvious trivial edits.; Catalog interpretation: A framework would cost more than the smallest script that does or proves the job.
- **Result:** Codemod, script, generator or protected delegate recipe; Comparison against a manually completed first unit
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/principle-laziness-protocol, poteto/principle-prove-it-works
- **Evidence:** [pstack/skills/principle-build-the-lever/SKILL.md:8–18](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-build-the-lever/SKILL.md#L8-L18) — Triviality threshold, first-unit proof, deterministic tools and optional delegate contract.
- **Evidence:** [pstack/skills/principle-build-the-lever/SKILL.md:19–23](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-build-the-lever/SKILL.md#L19-L23) — Commit condition, minimal tooling and verification companion.

### poteto/principle-encode-lessons-in-structure

Replaces repeated instructions or corrections with an enforceable structural rule where possible; judgment-heavy lessons receive a clearer instruction and failure example.

- **Role / status:** principle / stable.
- **Use when:** An agent needs the same correction for a second time.; A recurring rule could become a lint, metadata flag or runtime check.
- **Scope limits:** Catalog interpretation: The instruction is novel and there is no recurring pattern yet.; Catalog interpretation: The lesson requires judgment that cannot be encoded; improve its explanation and example instead.
- **Result:** Lint, metadata flag, runtime check or script; Clearer instruction with a failure example when enforcement is infeasible
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** local_write, configure
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-encode-lessons-in-structure/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L2-L3) — Recurring-instruction trigger and structural enforcement choices.
- **Evidence:** [pstack/skills/principle-encode-lessons-in-structure/SKILL.md:9–11](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L9-L11) — Judgment fallback and structural-fix-only corollary.

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
- **Evidence:** [pstack/skills/principle-exhaust-the-design-space/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-exhaust-the-design-space/SKILL.md#L2-L3) — Novelty, absence of precedent, multiple prototypes and comparison.
- **Evidence:** [pstack/skills/principle-exhaust-the-design-space/SKILL.md:9–9](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-exhaust-the-design-space/SKILL.md#L9-L9) — Product decisions whose experience depends on feel.

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
- **Evidence:** [pstack/skills/principle-experience-first/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-experience-first/SKILL.md#L9-L15) — Scope, polish, prototype and core-loop criteria.
- **Evidence:** [pstack/skills/principle-experience-first/SKILL.md:17–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-experience-first/SKILL.md#L17-L19) — Consumers include maintainers and API users; target versus sequence distinction.

### poteto/principle-explain-the-number

Qualifies a measured performance or evaluation result by identifying its limiter, testing alternative explanations and retaining run evidence.

- **Role / status:** principle / stable.
- **Use when:** Reporting a measured speedup, regression or latency.; Deciding whether an evaluation score reflects the intended task.
- **Scope limits:** Catalog interpretation: There is no measured number to interpret.; Catalog interpretation: The only question is whether a produced artifact exists or works at all.
- **Result:** Named limiter tied to profiles or counters and source; Run count, spread and alternative-explanation evidence
- **Requirements:** Limiter evidence from profiling or system counters during a run, mapped to source; code-reading guesses are insufficient.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/benchmark-checklist
- **Evidence:** [pstack/skills/principle-explain-the-number/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-explain-the-number/SKILL.md#L9-L15) — Measurement procedure, evidence retention and benchmark/eval routing.
- **Evidence:** [pstack/skills/principle-explain-the-number/SKILL.md:17–17](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-explain-the-number/SKILL.md#L17-L17) — Distinction from checking output reality.

### poteto/principle-fix-root-causes

Traces a reproduced symptom to the first wrong decision and distinguishes legitimate states needing handling from impossible states that should never be produced.

- **Role / status:** principle / stable.
- **Use when:** A defensive guard or retry appears to hide a defect.; A failure after restart may originate in persisted state.
- **Scope limits:** Catalog interpretation: The task needs a complete debugging phase workflow; this is a root-cause discipline within one.
- **Result:** Reproduced fault and root-cause trace; Fix across all instances of the faulty pattern; Proposed cheap observability signal when diagnosis was difficult
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-fix-root-causes/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-fix-root-causes/SKILL.md#L9-L19) — Definition of root cause, reproduce/instrument loop, state legitimacy and pattern-wide fixes.
- **Evidence:** [pstack/skills/principle-fix-root-causes/SKILL.md:20–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-fix-root-causes/SKILL.md#L20-L21) — Reject workaround comments and propose a cheap persistent signal.

### poteto/principle-foundational-thinking

Orders work around sound data structures and shared foundations so later increments remain simple and coherent.

- **Role / status:** principle / stable.
- **Use when:** Choosing core types and dominant access patterns before logic.; Sequencing scaffolding and feature work or deciding what concurrent actors share.
- **Scope limits:** Catalog interpretation: A new abstraction adds cleverness without improving data structure or downstream work.; Catalog interpretation: Scaffolding would preserve dead code that should be removed first.
- **Result:** Core data shape and access-pattern choices; Foundation-first sequence of coherent increments; Concurrent-state isolation decision
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-foundational-thinking/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-foundational-thinking/SKILL.md#L9-L19) — Structural option value, data shapes, abstraction restraint, concurrent isolation and scaffold sequence.
- **Evidence:** [pstack/skills/principle-foundational-thinking/SKILL.md:21–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-foundational-thinking/SKILL.md#L21-L21) — Subtraction precedes scaffolding.

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
- **Evidence:** [pstack/skills/principle-guard-the-context-window/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-guard-the-context-window/SKILL.md#L2-L3) — Context-pressure triggers, bulk delegation and summary strategy.
- **Evidence:** [pstack/skills/principle-guard-the-context-window/SKILL.md:9–12](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-guard-the-context-window/SKILL.md#L9-L12) — Reason for the rule and scope/turn-budget controls.

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
- **Evidence:** [pstack/skills/principle-laziness-protocol/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-laziness-protocol/SKILL.md#L2-L3) — Refactor, diff-size and abstraction triggers.
- **Evidence:** [pstack/skills/principle-laziness-protocol/SKILL.md:9–10](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-laziness-protocol/SKILL.md#L9-L10) — Decision consolidation and smallest sufficient change.

### poteto/principle-make-operations-idempotent

Designs state-changing work to reconcile current state with the goal so retries and interrupted runs converge safely.

- **Role / status:** principle / stable.
- **Use when:** A command, processing loop or lifecycle action can be retried after a crash.; Temporary files, claimed jobs or stale locks survive partial execution.
- **Scope limits:** Catalog interpretation: The operation is purely observational and cannot leave partial state.
- **Result:** Current-state reconciliation steps; Recognizable stale artifacts; Repeat-run and crash-point convergence checks
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-make-operations-idempotent/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-make-operations-idempotent/SKILL.md#L9-L15) — Retry convergence, goal comparison and stale artifact design.
- **Evidence:** [pstack/skills/principle-make-operations-idempotent/SKILL.md:17–22](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-make-operations-idempotent/SKILL.md#L17-L22) — Repeated-run and every-crash-point review tests.

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
- **Evidence:** [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L2-L3) — Internal API migration and same-wave deletion.
- **Evidence:** [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md:9–14](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L9-L14) — Contract-test changes and explicit applicability conditions.

### poteto/principle-minimize-reader-load

Evaluates maintainability through the indirections a reader must trace and the mutable state they must remember, then removes layers or narrows state.

- **Role / status:** principle / stable.
- **Use when:** A new maintainer cannot quickly trace a value's origin or mutations.; A wrapper or adapter adds a broad surface without hiding meaningful complexity.
- **Scope limits:** Catalog interpretation: A layer actually compresses meaningful decisions and reduces reader work.
- **Result:** Reduced pass-through layers; Narrower state scope and derived values; Interface compression and traceability assessment
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-minimize-reader-load/SKILL.md:9–18](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-minimize-reader-load/SKILL.md#L9-L18) — Two reader-load axes, layer and state changes, interface compression and traceability test.

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
- **Evidence:** [pstack/skills/principle-model-the-domain/SKILL.md:9–20](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-model-the-domain/SKILL.md#L9-L20) — Domain encoding and concrete structural alternatives.
- **Evidence:** [pstack/skills/principle-model-the-domain/SKILL.md:22–24](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-model-the-domain/SKILL.md#L22-L24) — Abstraction restraint and signs of scattered lifecycle knowledge.

### poteto/principle-never-block-on-the-human

Lets reversible execution proceed with reasonable decisions and asynchronous supervision while retaining confirmation for irreversible actions and human control of product direction.

- **Role / status:** principle / stable.
- **Use when:** An agent is about to ask permission for a reversible code or note edit.
- **Scope limits:** Catalog interpretation: An action is irreversible, such as force-push, deleting production data or sending external messages.; Catalog interpretation: The unresolved choice is product direction owned by the human.
- **Result:** Completed reversible work with an explanation; Confirmation boundary for irreversible actions
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Proceed on reversible work without blocking; irreversible actions such as force-push, production-data deletion and external messages require confirmation. Product direction remains with the human.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-never-block-on-the-human/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-never-block-on-the-human/SKILL.md#L9-L15) — Asynchronous supervision, reversible action examples, irreversible confirmation and product ownership.

### poteto/principle-outcome-oriented-execution

Allows explicitly scoped transitional breakage during a planned migration so work converges on the verified target architecture without accumulating compatibility scaffolding.

- **Role / status:** principle / stable.
- **Use when:** A planned rewrite has explicit phase and verification boundaries.
- **Scope limits:** Catalog interpretation: Intermediate breakage is unplanned, unscoped or not reversible.; Catalog interpretation: The task lacks a completion gate for full static and runtime verification.
- **Result:** Declared temporary-breakage boundaries; Target architecture without throwaway compatibility code; High-signal phase checks and full completion verification
- **Requirements:** A planned rewrite or migration with explicit phase boundaries; declared acceptable breakage and full static/runtime verification at completion.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-outcome-oriented-execution/SKILL.md:9–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L9-L21) — End-state priority, planned reversible breakage and verification guardrails.

### poteto/principle-prove-it-works

Checks task outputs against the actual artifact and, where feasible, keeps a deterministic verification script and evidence for reviewers.

- **Role / status:** principle / stable.
- **Use when:** An agent is about to declare a task complete.; A claim relies on freshness, cached output or a delegate's self-report.
- **Scope limits:** Catalog interpretation: The question is measurement magnitude or validity of a speedup rather than output reality.
- **Result:** Direct observation of the real output; Rerunnable comparison script and visible evidence artifact
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/show-me-your-work
- **Evidence:** [pstack/skills/principle-prove-it-works/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-prove-it-works/SKILL.md#L9-L16) — Direct reality checks and rejection of proxy evidence.
- **Evidence:** [pstack/skills/principle-prove-it-works/SKILL.md:18–22](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-prove-it-works/SKILL.md#L18-L22) — Scripted checks, visible artifact and audit-trail companion.

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
- **Evidence:** [pstack/skills/principle-redesign-from-first-principles/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-redesign-from-first-principles/SKILL.md#L9-L16) — Whole-design reconsideration, affected-reference propagation and incremental delivery.

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
- **Evidence:** [pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md#L9-L16) — Eliminate sharing first, race rationale, ownership partitioning and structural serialization.

### poteto/principle-sequence-verifiable-units

Sequences multi-step execution and delivery into small checked units whose order demonstrates correctness to a reviewer.

- **Role / status:** principle / stable.
- **Use when:** A migration or sweep applies many similar changes.; Commits or PRs need a replayable proof order, such as failing test before fix.
- **Scope limits:** Catalog interpretation: A migration deliberately permits scoped transitional breakage; reconcile the verification unit with that declared boundary before combining principles.
- **Result:** Small before/after units with passing checks; Commit or PR sequence that demonstrates the change
- **Requirements:** The source asks for rebasing onto clean trunk before per-unit checks so they measure the real baseline.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/principle-prove-it-works, poteto/principle-build-the-lever
- **Evidence:** [pstack/skills/principle-sequence-verifiable-units/SKILL.md:9–17](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L9-L17) — Per-unit green gates, clean-trunk baseline, delivery proof order and verification companions.

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
- **Evidence:** [pstack/skills/principle-subtract-before-you-add/SKILL.md:9–18](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-subtract-before-you-add/SKILL.md#L9-L18) — Continual simplification, removal order, observed scope and redundant-reference deletion.

### poteto/principle-test-behavior-not-implementation

Judges a test by whether it catches broken observable behavior while surviving internal restructuring, then rewrites assertions around the consumer contract.

- **Role / status:** principle / stable.
- **Use when:** Writing or reviewing regression tests.; A refactor repeatedly breaks tests despite identical consumer-visible behavior.
- **Scope limits:** Catalog interpretation: The task needs test-harness setup or a complete testing strategy rather than a rule for judging assertions against an observable consumer contract.
- **Result:** Contract-driven test cases; Assertions that catch behavioral regressions and survive internal refactors
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L9-L16) — Observable behavior definition, two-edit test-quality check and requirement-derived expectations.
- **Evidence:** [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:18–20](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L18-L20) — External effects, precise contract-dependent assertions and invariants.

### poteto/principle-type-system-discipline

Uses types and authoritative schemas to prevent invalid states, semantic primitive mixups and unhandled variants before runtime.

- **Role / status:** principle / stable.
- **Use when:** Designing signatures in a statically typed language.; External data or parallel hand-maintained types need a trusted parsing boundary or authoritative schema.
- **Scope limits:** Catalog interpretation: The environment has no static type system for the proposed compile-time guarantees.; Catalog interpretation: The question is TypeScript syntax; consult the dedicated TypeScript skill alongside this general rule.
- **Result:** Semantically distinct primitive types; Parsed boundary domain model; Schema-derived authoritative types
- **Requirements:** A statically typed language for compiler-enforced guarantees; TypeScript-specific syntax is delegated to typescript-best-practices.
- **Possible effects:** read, local_write
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/typescript-best-practices, poteto/principle-boundary-discipline, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/principle-type-system-discipline/SKILL.md:2–3](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-type-system-discipline/SKILL.md#L2-L3) — Static-language scope and core type-system applications.
- **Evidence:** [pstack/skills/principle-type-system-discipline/SKILL.md:9–13](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-type-system-discipline/SKILL.md#L9-L13) — Semantic branding, external parsing, schema derivation and explicit companions.

### poteto/recall

Rebuilds recent work context across the user's scoped chat history, shared evidence and live PR state. Returns a compact current-state brief before work resumes.

- **Role / status:** workflow / stable.
- **Use when:** Find where work on a named feature stands across recent chats.; Recover decisions, failed approaches and the most useful next move.
- **Scope limits:** Catalog interpretation: Use the mode Session pickup playbook for one specific prior chat.; Catalog interpretation: Use automate-me to turn habits into lasting agent instructions.
- **Result:** Capsule and status-tagged threads; Recurring problems and one next action
- **Requirements:** Workspace-scoped Cursor JSONL transcripts.; git and gh for live checks; available MCP evidence sources through why.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** States the search window/topic/workspace. Never reads another project's transcripts without being asked.
- **Explicit companions/references:** poteto/why, poteto/automate-me, poteto/unslop, poteto/poteto-mode
- **Evidence:** [pstack/skills/recall/SKILL.md:13–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/recall/SKILL.md#L13-L21) — Scoped transcripts, default seven-day window, shared record and live verification.
- **Evidence:** [pstack/skills/recall/SKILL.md:24–35](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/recall/SKILL.md#L24-L35) — Brief output and privacy boundary.

### poteto/reflect

Extracts durable lessons from the current session through three reviewer lenses and a synthesizer. Proposes concrete skill edits and separates structural enforcement work into backlog items.

- **Role / status:** workflow / stable.
- **Use when:** A substantial finished session exposed recurring process or skill gaps.
- **Scope limits:** Catalog interpretation: Skip trivial sessions or lessons already covered by correctly followed instructions.; Catalog interpretation: Do not edit plugin cache copies or treat every one-off as a durable rule.
- **Result:** Accepted, Rejected and Backlog findings; User-approved skill-copy edits; Filed backlog items and applied-edit summary
- **Requirements:** Active workspace transcript or fallback session digest.; Cursor generalPurpose agent-mode Task subagents with MCP access; built-in create-skill for substantive authoring.; A team devex/backlog tracker for backlog filing.
- **Possible effects:** read, local_write, external_write, execute, delegate
- **Confirmation behavior:** Waits for explicit approval of a chosen subset before editing skills and shows the destination first. Backlog tracker filing proceeds without waiting; never opens a PR or pushes.
- **Explicit companions/references:** poteto/poteto-mode, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/reflect/SKILL.md:9–27](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/reflect/SKILL.md#L9-L27) — Trigger, scoped transcript discovery and reviewer host assumptions.
- **Evidence:** [pstack/skills/reflect/SKILL.md:37–60](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/reflect/SKILL.md#L37-L60) — Synthesis, structural check, approval, automatic backlog filing and safe destination.
- **Evidence:** [pstack/skills/reflect/references/judgment-reviewer.md:3–5](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/reflect/references/judgment-reviewer.md#L3-L5) — Reviewers are forbidden to modify state and constrain lookups to cited context.

### poteto/setup-pstack

Configures pstack's per-role models and reasoning budget using models the current host actually exposes. Writes an always-applied rule for future sessions.

- **Role / status:** setup / stable.
- **Use when:** Choose a smaller budget or adjust the models used for each pstack role.; Configure a new pstack installation.
- **Scope limits:** Catalog interpretation: Do not write unconfirmed real model slugs.; Catalog interpretation: Do not assume a Cursor .mdc rule is loaded by another host.
- **Result:** ~/.cursor/rules/pstack-models.mdc; Validated role/model table and budget; Optional offered verification setup
- **Requirements:** Cursor Task model availability, AskQuestion and writable user rules directory.; Claude Code uses the documented adapter and a different rules path.
- **Possible effects:** read, local_write, configure
- **Confirmation behavior:** Asks for a budget and confirmation of every role/model table before writing. Verification generators are invoked only if the user accepts each optional offer.
- **Explicit companions/references:** poteto/create-verification-skill, poteto/create-formal-verification-skill
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:8–18](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/setup-pstack/SKILL.md#L8-L18) — Configuration destination and model detection.
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:20–39](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/setup-pstack/SKILL.md#L20-L39) — Budget, explicit table confirmation, validation and overwrite.
- **Evidence:** [pstack/skills/setup-pstack/SKILL.md:68–78](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/setup-pstack/SKILL.md#L68-L78) — New-session activation and opt-in verification offers.
- **Evidence:** [pstack/docs/harness/claude-code.md:40–46](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/docs/harness/claude-code.md#L40-L46) — Claude Code-specific setup mapping.

### poteto/sharpen

Rewrites a task prompt to seek deeper expertise, rawer evidence, concrete methods and an independent correctness check without expanding its scope.

- **Role / status:** utility / stable.
- **Use when:** Improve a prompt before sending it to an agent.
- **Scope limits:** Catalog interpretation: Do not execute the rewritten task or decide choices that belong to the user.
- **Result:** Four-part depth assessment; Rewritten prompt
- **Requirements:** None explicitly stated in the interpreted source.
- **Possible effects:** read
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/sharpen/SKILL.md:7–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/sharpen/SKILL.md#L7-L16) — Depth questions, rewrite-only outcome and user-owned choices.

### poteto/show-me-your-work

Maintains an append-only TSV decision trail for long or unattended work. Audits it against the run transcript and obtains a different-model review before handoff.

- **Role / status:** workflow / stable.
- **Use when:** A reviewer must trust a long run after stepping away.; Track hypotheses, pivots and verification results as a run proceeds.
- **Scope limits:** Catalog interpretation: Do not log every trivial action or silently rewrite earlier rows.; Catalog interpretation: Keep the log local unless the work warrants committing an audit artifact.
- **Result:** Canonical decision TSV; Transcript audit with superseding corrections; Cross-model Attention flags
- **Requirements:** Writable local work area, optional bundled log.sh helper and workspace transcript.; A subagent on a different model family for trail review.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/unslop, poteto/poteto-mode, poteto/principle-encode-lessons-in-structure
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:13–22](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/show-me-your-work/SKILL.md#L13-L22) — Decision trail schema.
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:36–52](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/show-me-your-work/SKILL.md#L36-L52) — Helper, per-run boundaries, local default and append-only rule.
- **Evidence:** [pstack/skills/show-me-your-work/SKILL.md:55–74](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/show-me-your-work/SKILL.md#L55-L74) — Transcript audit and mandatory cross-model review.

### poteto/statechart

Turns a TLA+ model into reader-labeled statecharts and numbered bug paths, or converts an agreed chart into a TLA+ starting point. Reports model scope and whether code-backed counterexamples reproduce.

- **Role / status:** workflow / stable.
- **Use when:** Explain a modeled race or invariant violation as observable steps.; Agree on a behavior chart before implementation or audit code against an existing spec.
- **Scope limits:** Catalog interpretation: Do not claim model traces alone prove code behavior without replay.; Catalog interpretation: Use a simple ordinary diagram when formal checking adds no useful evidence.
- **Result:** PNG and Mermaid charts; Bug stories and summary.json; TLA+ skeleton or model comparison and regeneration command
- **Requirements:** Node and bundled statechart.mjs.; TLC and Java; first run downloads about 305 MB through mise unless existing tools are configured.; Scratch folder outside the repository and PNG inspection capability.; npm for first PNG rendering, which installs Pele and resvg into a user cache.
- **Possible effects:** read, local_write, execute, configure
- **Confirmation behavior:** Reader/behavior owners agree on chart-to-spec behavior. Design bugs and code/chart differences are taken back to those people for a decision.
- **Explicit companions/references:** None recorded.
- **Evidence:** [pstack/skills/statechart/SKILL.md:9–17](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/statechart/SKILL.md#L9-L17) — Reader labels, installation/network assumptions and direction selection.
- **Evidence:** [pstack/skills/statechart/SKILL.md:21–26](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/statechart/SKILL.md#L21-L26) — Invariants, bug paths, rendering and replay against code.
- **Evidence:** [pstack/skills/statechart/SKILL.md:28–36](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/statechart/SKILL.md#L28-L36) — Chart agreement, reader decisions and outputs.
- **Evidence:** [pstack/skills/statechart/scripts/statechart-help.mjs:119–126](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/statechart/scripts/statechart-help.mjs#L119-L126) — PNG rendering has a separate npm-installed Pele/resvg dependency cache and can fail when installation is unavailable.

### poteto/swarm

Fans workers out across slices or declared races and consolidates their terminal results into one evidence-backed report. Missing coverage is recorded rather than counted as a pass.

- **Role / status:** workflow / stable.
- **Use when:** Cover a matrix of independent checks.; Race workers or partition exploration over a large target.
- **Scope limits:** Catalog interpretation: Use arena when competing artifacts need base selection and grafting.; Catalog interpretation: Do not accept measurement results without the exact requested commits and method.
- **Result:** Consolidated result table; Issues, coverage gaps and dropouts; Declared race outcome
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Cursor cloud Task agents by default; local workers only for resources on the user's computer.
- **Possible effects:** read, local_write, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/poteto-mode
- **Evidence:** [pstack/skills/swarm/SKILL.md:18–31](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/swarm/SKILL.md#L18-L31) — Done predicate, race rules, model, isolation and cloud default.
- **Evidence:** [pstack/skills/swarm/SKILL.md:33–41](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/swarm/SKILL.md#L33-L41) — Dropouts, SHA/method validation and reporting.

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
- **Evidence:** [pstack/skills/tdd/SKILL.md:3–11](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/tdd/SKILL.md#L3-L11) — Bug-fix trigger and impractical-test exclusion.
- **Evidence:** [pstack/skills/tdd/SKILL.md:15–26](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/tdd/SKILL.md#L15-L26) — Fail-first cadence and alternative executable checks.
- **Evidence:** [pstack/skills/tdd/SKILL.md:28–42](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/tdd/SKILL.md#L28-L42) — Guardrails and evidence reporting.

### poteto/teach

Combines code behavior and historical rationale into a plain, conversational explanation at the learner's pace. Builds diagrams incrementally when they help understanding.

- **Role / status:** teaching / stable.
- **Use when:** Understand a change or unfamiliar subsystem rather than modify it.
- **Scope limits:** Catalog interpretation: Do not use as an implementation workflow or a quiz-based course generator.; Catalog interpretation: Avoid a full historical sweep when a narrow question suffices.
- **Result:** Layered plain-language explanation; Incremental diagrams or generated spatial illustrations when useful
- **Requirements:** how and why dependencies, including host-specific subagents and relevant source access.; Image-generation tool for spatial explanations; Mermaid for structured flows.
- **Possible effects:** read, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/how, poteto/why, poteto/unslop
- **Evidence:** [pstack/skills/teach/SKILL.md:9–16](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/teach/SKILL.md#L9-L16) — Explanation-only scope, actual how/why invocations and conversational pace.
- **Evidence:** [pstack/skills/teach/SKILL.md:17–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/teach/SKILL.md#L17-L21) — Progressive visuals, tool choice and final output.

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
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:9–19](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/technical-writing/SKILL.md#L9-L19) — Plain language, repo vocabulary and non-destructive rule escape.
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:30–49](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/technical-writing/SKILL.md#L30-L49) — Diataxis document modes.
- **Evidence:** [pstack/skills/technical-writing/SKILL.md:91–96](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/technical-writing/SKILL.md#L91-L96) — Unslop companion, PR applicability and product UI exclusion.

### poteto/typescript-best-practices

Provides TypeScript-specific type modeling and boundary rules, emphasizing explicit variants, verified brands, schema-derived types and behavior checks.

- **Role / status:** reference / stable.
- **Use when:** Read or edit .ts or .tsx code.
- **Scope limits:** Catalog interpretation: Do not route non-TypeScript work to this language-specific rule set.; Catalog interpretation: Avoid treating stylistic advice as an independent task plan.
- **Result:** TypeScript changes or review guidance aligned with stated rules
- **Requirements:** TypeScript code; repository schema library and framework test primitives where present.
- **Possible effects:** read, local_write, execute
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/principle-type-system-discipline, poteto/principle-boundary-discipline
- **Evidence:** [pstack/skills/typescript-best-practices/SKILL.md:3–10](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/typescript-best-practices/SKILL.md#L3-L10) — TypeScript scope and initial principle.
- **Evidence:** [pstack/skills/typescript-best-practices/SKILL.md:14–31](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/typescript-best-practices/SKILL.md#L14-L31) — Modeling, narrowing, boundaries, real tests and structured telemetry.

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
- **Evidence:** [pstack/skills/unslop/SKILL.md:9–13](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/unslop/SKILL.md#L9-L13) — Editing scope and stable pattern identifiers.
- **Evidence:** [pstack/skills/unslop/SKILL.md:17–37](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/unslop/SKILL.md#L17-L37) — Content, vocabulary and formatting patterns.
- **Evidence:** [pstack/skills/unslop/SKILL.md:41–62](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/unslop/SKILL.md#L41-L62) — Communication, filler, jargon and plain-language rules.

### poteto/why

Investigates the historical reasons and constraints behind code across source control and available connected evidence categories. Separates explicit findings, inference, hypotheses and unresolved gaps.

- **Role / status:** workflow / stable.
- **Use when:** Find why a design, defensive check or threshold exists.; Recover regression history or planning constraints before changing behavior.
- **Scope limits:** Catalog interpretation: Use how for current runtime mechanics.; Catalog interpretation: Do not infer author intent solely from code or hide unavailable evidence categories.
- **Result:** Cited, confidence-separated rationale; Sources consulted and explicit gaps; Preserve/Change/Avoid/Risk constraints when a change follows
- **Requirements:** Cursor Task subagents and pstack-models.mdc role configuration; fallback model slugs and alias handling are host-specific.; Cursor generalPurpose agent-mode Task subagents to retain MCP access.; git and gh for source history; available MCPs for tickets, docs, chat, observability, errors and analytics.
- **Possible effects:** read, execute, delegate
- **Confirmation behavior:** Not explicitly specified in this skill.
- **Explicit companions/references:** poteto/how, poteto/poteto-mode
- **Evidence:** [pstack/skills/why/SKILL.md:9–27](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/why/SKILL.md#L9-L27) — Read-only investigation purpose, host modes and git/PR anchors.
- **Evidence:** [pstack/skills/why/SKILL.md:31–75](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/why/SKILL.md#L31-L75) — Parallel evidence categories and documented skip rules.
- **Evidence:** [pstack/skills/why/SKILL.md:77–94](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/why/SKILL.md#L77-L94) — Synthesis, confidence language, outputs and planning constraints.
- **Evidence:** [pstack/skills/why/references/synthesizer-prompt.md:29–45](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/why/references/synthesizer-prompt.md#L29-L45) — Confidence tiers and explicit prohibition on writes.
