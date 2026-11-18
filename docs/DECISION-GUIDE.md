# Goal-first decision guide (version 2)

Choose the intended result before answering follow-up questions. The guide returns one source-grounded suggestion, its prerequisites, a next action, and conditional alternatives. Search the complete catalog when no goal fits. The original binary routes remain in catalog/routes.json as a comparison baseline.

## Goals

| Goal | Intended result | First question |
| --- | --- | --- |
| Understand or research | Explain behavior, recover design rationale, or investigate primary sources. | understand-focus |
| Plan tests or verify behavior | Choose testing strategy, write behavior checks, or build stronger verification. | test-intent |
| Clarify a plan or write a specification | Resolve open decisions, synthesize settled discussion, or split an agreed plan. | plan-state |
| Implement agreed work | Execute a bounded spec or its existing ticket graph. | implementation-size |
| Diagnose a failure or performance symptom | Choose a reproduce-and-fix loop or live diagnosis without a product fix. | diagnosis-result |
| Explore or improve a design | Get interface advice, test an idea cheaply, or design and implement the chosen shape. | design-depth |
| Review changes or prepare delivery | Separate review findings, PR communication, merge readiness, and actually landing changes. | review-result |
| Write clearly or learn something | Choose a conversational explanation, persistent learning workspace, or technical writing support. | writing-learning |
| Improve workflows or coordinate work | Triage requests, learn from a session, prevent recurring mistakes, sharpen prompts, or partition work. | improvement-target |
| Carry context into the next step | Prepare a portable handoff or catch up on an active chat, including software work. | context-action |

## Follow-up questions

### understand-focus: What do you need to understand?

Choose the evidence you need, rather than the author you prefer.

- How existing code works and where behavior belongs → `explain-system`
- Why an existing design or decision exists → `recover-rationale`
- Facts about a topic, API, or external technology → `research-topic`

### test-intent: What testing result do you want?

Planning how to test is a separate task from writing or running tests.

- Choose a strategy for testing a module → `module-execution`
- Write tests while building feature behavior → `feature-test-first`
- Capture and fix a known bug with a regression check → `bug-regression`
- Build or maintain checks that drive the real application → `app-check-state`
- Check a costly invariant beyond example-based tests → `formal-check`

### module-execution: What execution is allowed for the module checks?

Not starting the whole application is different from not executing any code.

- Isolated tests may run; the whole system must not start → `module-isolated-strategy`
- Analysis only; do not execute code → `module-analysis-strategy`

### app-check-state: Does the project already have a verification skill and feature map?

These checks launch and drive the real application. Use module strategy if full-system startup is forbidden.

- No; create a repeatable real-app verification workflow → `create-app-check`
- Yes; audit and update its source and live coverage → `maintain-app-check`

### plan-state: How settled is the plan?

A settled discussion should become a specification before implementation.

- Important product or design decisions are still open → `clarify-plan`
- Discussion is settled; write the specification → `write-spec`
- An agreed plan or spec needs verifiable tickets → `split-tickets`

### implementation-size: What is already specified?

Use planning first if the expected behavior is still unsettled.

- One bounded change, spec, or set of tickets → `implement-scoped`
- A whole spec with a dependency graph of tickets → `implement-ticket-graph`

### diagnosis-result: What diagnosis result do you need?

Live instrumentation and repository fixes have different action scopes.

- Reproduce a bug or regression, find its cause, and fix it → `diagnose-fix`
- Diagnose a live runtime symptom; do not implement a fix → `diagnose-live`

### design-depth: How far should design work go?

Choose shared design vocabulary, a throwaway experiment, or concrete architecture sketches before implementation.

- Advice on module interfaces and seams only → `design-reference`
- A throwaway prototype to answer a design question → `design-prototype`
- Compare concrete architecture sketches before implementation → `design-implement`

### review-result: What should happen after the review?

Reviewing, making a PR ready, and merging it are distinct tasks.

- Report code findings against standards and a spec → `review-standards-spec`
- Challenge a change with independent adversarial checks → `review-execution`
- Write the pull request description → `write-pr-body`
- Drive an existing PR to merge-ready; do not merge → `ready-pr`
- Independently verify and land authorized PRs → `ship-pr`

### writing-learning: Which result would help you?

A short lesson and a persistent learning workspace have different scope.

- Learn through a conversational explanation now → `learn-conversation`
- Build a learning workspace across multiple sessions → `learn-workspace`
- Write or improve a technical document → `technical-document`

### improvement-target: What needs improvement?

Pick the change you want, since some of these workflows only report while others edit and commit.

- Turn incoming requests into verified, actionable briefs → `triage-requests`
- Find improvements after a coding session → `session-retrospective`
- Prevent the same agent mistakes from recurring → `prevent-mistakes`
- Improve a task prompt without widening scope → `sharpen-task`
- Coordinate bounded parallel coverage or candidates → `coordinate-workers`

### context-action: Who needs the context?

These routes also apply to coding projects; no software/non-software fork is required.

- A fresh agent or next session must continue the work → `portable-handoff`
- I need to catch up on this chat and its open decisions → `catch-up`

### review-execution: May reviewers create and run isolated reproductions?

Poteto interrogate now keeps only findings proved by a run. Source-only review uses Matt’s standards and specification reports.

- Yes; isolated worktrees and executable probes are allowed → `review-adversarial`
- Source and diff inspection only; do not run the product or create probes → `review-standards-spec`

## Recommendations

### explain-system: Explain existing behavior

**Suggested next:** poteto/how

It grounds an architectural explanation in code, ownership, and runtime flow.

**Do next:** Name one subsystem and ask for its entry points, data flow, owners, and important gotchas.

**Scope:** This is an explanation. It does not authorize implementing changes.

- Prerequisite: Access to the relevant code.
- Prerequisite: An agent host able to run or adapt one read-only explanation subagent.
- Alternative: poteto/teach — You want a conversational lesson that combines behavior and rationale.

### recover-rationale: Recover the reasons behind a design

**Suggested next:** poteto/why

It reads the commits and PR discussions that introduced and later changed the target, marks inference, and reports unanswered questions.

**Do next:** Name the design decision and collect code anchors, source-control history, and any available decision records.

**Scope:** Missing evidence stays a gap; plausible rationale is not a confirmed historical fact.

- Prerequisite: Access to relevant commits and PR discussions.
- Prerequisite: Additional evidence sources if the historical trail is thin.
- Alternative: poteto/how — The real question is what the code does today, rather than why it was chosen.

### research-topic: Research a bounded question

**Suggested next:** matt/research

It traces claims to primary sources and saves a cited research note.

**Do next:** State the question, the decision it informs, and where the research note belongs.

**Scope:** The deliverable is a research note, not an implementation or an unqualified recommendation.

- Prerequisite: A bounded research question.
- Prerequisite: Access to relevant primary sources and a writable notes destination.
- Prerequisite: A background research agent with a fresh context window, or a stated adaptation.
- Alternative: poteto/why — The question is specifically historical rationale for code already in your repository.

### module-isolated-strategy: Plan isolated module tests without starting the system

**Suggested next:** matt/codebase-design

This reference owns interface and seam design for testability. Its dependency guide distinguishes in-process work, local stand-ins, owned remote services, and external systems.

**Do next:** Produce a testability map: the public interface, dependency categories, available stand-ins, smallest isolated invocation, behaviors it catches, and integrations it leaves unverified.

**Scope:** Consult this as a reference, not a coordinator. Planning does not authorize refactoring or writing tests. An isolated pass cannot prove the real integrations work.

- Prerequisite: Identify the module and its callers.
- Prerequisite: Confirm which local processes, fixtures, stand-ins, and network calls an isolated check may use.
- Alternative: matt/tdd — You explicitly request writing tests, agree the seams first, and allow the required isolated execution.
- Conditional support: poteto/how — Use only if ownership or runtime flow must first be mapped from code.

### module-analysis-strategy: Analyze module testability without executing code

**Suggested next:** matt/codebase-design

This reference supplies the vocabulary for choosing the test interface and classifying dependencies before any test is run.

**Do next:** Write an analysis-only testability map with candidate seams, dependencies, hypothetical stand-ins, proposed checks, and every assumption that still needs execution evidence.

**Scope:** Read and reason only. Do not run code or call the proposed checks verified. Treat this skill as a reference, not an execution workflow.

- Prerequisite: Access to module source, callers, and existing test examples.
- Prerequisite: A clear no-execution constraint.
- Alternative: matt/tdd — Later, you request writing tests, agree the seams, and explicitly allow execution; until then it is not the next action.
- Conditional support: poteto/how — Consult if an explanation of the existing code is needed to identify the seam.

### feature-test-first: Build feature behavior one failing test at a time

**Suggested next:** matt/tdd

It targets observable behavior through agreed public seams, with one red-to-green slice at a time.

**Do next:** List the proposed seams with what each catches and misses, confirm them, then write one independently expected failing test.

**Scope:** Do not write tests at unconfirmed seams. Its current loop excludes refactoring, which belongs to the later review stage.

- Prerequisite: Requested test-first feature work.
- Prerequisite: User agreement on testing seams before writing tests.
- Prerequisite: A runnable focused test command and permission for implementation changes.
- Alternative: poteto/tdd — You are fixing a specific known bug with a cheap local regression target, rather than building feature behavior.
- Conditional support: matt/codebase-design — Reference when the interface or testing seam itself needs design.

### bug-regression: Lock down a known bug with a focused regression

**Suggested next:** poteto/tdd

It requires failing-before and passing-after evidence on a practical local bug path.

**Do next:** Identify intended and broken behavior; choose the smallest existing executable check and show it fail before changing production code.

**Scope:** Do not build a broad brittle harness merely to add a test. If a failing test is impractical, report the closest executable proof and its limits.

- Prerequisite: A specific bug and expected behavior.
- Prerequisite: An inexpensive local test target, or an explicitly requested regression check.
- Prerequisite: Permission to fix the bug and execute the check.
- Alternative: matt/diagnosing-bugs — The failure is hard to reproduce or its cause is unknown; build a reliable feedback loop before choosing the fix.

### create-app-check: Create a repeatable real-app verification workflow

**Suggested next:** poteto/create-verification-skill

It builds launch, health, drive, evidence, cleanup, and feature-map instructions grounded in the actual repository.

**Do next:** Identify the primary user surface and existing harness, then generate the workflow and run one complete mapped journey.

**Scope:** This starts and drives the application and writes a project-local skill. A generated workflow that was never executed remains a draft.

- Prerequisite: Permission and prerequisites to start the real application.
- Prerequisite: A safe test instance, required configuration, and controllable user surface.
- Alternative: matt/codebase-design — The full application must not run; consult the reference to plan isolated module checks instead.

### maintain-app-check: Audit an existing app verification workflow

**Suggested next:** poteto/maintain-verification-skill

It compares each feature map entry with source and live behavior, then corrects proven harness or documentation drift.

**Do next:** Locate the existing verification skill and map, cover every mapped feature from source and live execution, and report gaps.

**Scope:** Edits belong to the verification skill and harness. Product regressions are reported, not hidden by weakening the map.

- Prerequisite: An existing project-local verification skill and feature map.
- Prerequisite: Permission and environment to drive every reachable feature live.
- Alternative: poteto/create-verification-skill — No verification skill or feature map exists yet.

### formal-check: Create a scoped invariant verification workflow

**Suggested next:** poteto/create-formal-verification-skill

It chooses a tool for one costly invariant, ties the model to real code, and demonstrates that the check can fail.

**Do next:** State the invariant and harm. Use TLA+ for bad-order or interleaving questions, and a code verifier or real-code generated-input checks for input properties. Record bounds and prove a broken variant fails.

**Scope:** A pass covers only stated scope and assumptions. Report real product violations without changing product code unless requested.

- Prerequisite: Relevant source code and a meaningful invariant.
- Prerequisite: Permission to create local verification artifacts and run the chosen tool.
- Alternative: poteto/maintain-formal-verification-skill — A formal workflow already exists and must be reconciled with changed code.
- Conditional support: poteto/statechart — Use for readable TLA+ states and counterexample paths when a TLA+ model is chosen.

### clarify-plan: Clarify decisions and preserve the domain language

**Suggested next:** matt/grill-with-docs

It combines a decision interview with domain modeling so decisions and terminology persist.

**Do next:** Bring the proposal and constraints; identify answerable decisions and record agreed terms and significant tradeoffs.

**Scope:** This sharpens a plan and writes relevant domain documentation; it is not an instruction to start implementation.

- Prerequisite: A plan or design to interrogate.
- Prerequisite: Willingness to answer product decisions and a destination for domain documents.
- Alternative: matt/grill-me — You want the interview without the persistent glossary and decision-document wrapper.

### write-spec: Turn settled discussion into a specification

**Suggested next:** matt/to-spec

It synthesizes what is already discussed into user stories, decisions, scope, and a test strategy.

**Do next:** Read the settled discussion, sketch the testing seams for confirmation, and publish the synthesized specification to the configured tracker.

**Scope:** This creates a specification and tracker entry, not implementation. It avoids restarting the product interview but still checks proposed testing seams.

- Prerequisite: Enough settled discussion to synthesize.
- Prerequisite: Configured issue-tracker and triage conventions.
- Prerequisite: Agreement on testing seams and authorization for the selected publication destination.
- Alternative: matt/grill-with-docs — Material product or design decisions are still unresolved.
- Conditional support: matt/setup-matt-pocock-skills — Configure the repository first if tracker conventions are missing.

### split-tickets: Split an agreed plan into verifiable work

**Suggested next:** matt/to-tickets

It makes vertical, independently verifiable slices with explicit blocking edges.

**Do next:** Read the plan and create demoable tickets with acceptance evidence and dependency relationships.

**Scope:** Ticket publication changes the configured tracker. Tickets are a work graph, not a substitute for implementing or verifying the feature.

- Prerequisite: An existing plan, spec, or sufficiently settled discussion.
- Prerequisite: Configured tracker and authorization to publish tickets.
- Alternative: matt/to-spec — The discussion is settled but still needs a coherent specification before slicing.

### implement-scoped: Implement a bounded specification

**Suggested next:** matt/implement

It implements supplied work with agreed test seams, focused checks, final review, and a commit.

**Do next:** Supply the spec or exact ticket reference, confirm testing seams, then implement and verify the bounded change.

**Scope:** This writes and commits code on the current branch. A recommendation does not establish that the source workflow is installed or compatible.

- Prerequisite: A supplied spec or unambiguous tickets.
- Prerequisite: Permission to edit and commit in the intended checkout.
- Prerequisite: Agreed testing seams and repository checks.
- Alternative: poteto/architect — The interface shape still needs competing sketches before implementation can begin.

### implement-ticket-graph: Implement a specification across its ticket graph

**Suggested next:** matt/implement-spec

It dispatches each ready ticket to a fresh implementer in its own worktree and integrates the results before final review.

**Do next:** Read the spec and blocking relationships, create the integration branch, and execute the ready frontier with bounded implementer worktrees.

**Scope:** This creates branches and worktrees, merges implementation, and resolves work through the configured tracker. It is a wider orchestration commitment.

- Prerequisite: An existing spec with associated dependency-linked tickets.
- Prerequisite: Configured tracker, worktree support, and fresh parallel agents with separate context windows.
- Prerequisite: Authorization for code, commits, integration merges, and relevant tracker updates.
- Alternative: matt/implement — The work is a single bounded change that does not need graph orchestration.

### diagnose-fix: Diagnose and fix a reproducible failure

**Suggested next:** matt/diagnosing-bugs

Its core is a fast red-capable feedback command, followed by minimization and ranked hypothesis checks.

**Do next:** Start by building and running one command that detects the exact reported symptom; then minimize it before testing theories.

**Scope:** It needs executable failure evidence. Do not claim a cause from source speculation when no meaningful feedback loop is possible.

- Prerequisite: The observed symptom and expected behavior.
- Prerequisite: Access to a reproducing environment or redacted artifact.
- Prerequisite: Permission to run the feedback loop and make the eventual fix.
- Alternative: poteto/tdd — A cheap local reproduction and narrow bug target are already obvious.

### diagnose-live: Diagnose a live runtime symptom

**Suggested next:** poteto/poteto-mode

The Runtime forensics playbook captures a real live signal and maps a proved mechanism to source.

**Do next:** Capture the matching CPU, heap, or UI artifact; reduce it and confirm the suspected mechanism with targeted instrumentation.

**Scope:** The deliverable is a diagnosis, not a product fix. Instrumentation can affect a live process, so use an appropriate permitted instance.

- Prerequisite: Access and permission to instrument the target live process.
- Prerequisite: A matching runtime control or profiling tool available in the host.
- Alternative: matt/diagnosing-bugs — You want a reproducible feedback loop and an implemented fix rather than diagnosis alone.
- Poteto mode playbook: Runtime forensics

### design-reference: Use a reference for interface and seam design

**Suggested next:** matt/codebase-design

It supplies the shared module, interface, seam, adapter, depth, and locality vocabulary.

**Do next:** Map callers and dependencies, compare a few interface shapes, and state the test surface and tradeoffs without editing code.

**Scope:** This is a reference for reasoning, not an autonomous coordinator. Advice alone does not authorize refactoring.

- Prerequisite: The module’s current or proposed callers and responsibilities.
- Alternative: matt/improve-codebase-architecture — You want a broader survey of recent change areas and a visual report of architectural improvement candidates.

### design-prototype: Prototype to answer one design question

**Suggested next:** matt/prototype

It builds throwaway logic demos or switchable UI variants whose shape follows a specific uncertainty.

**Do next:** Name the decision and the observable result that would settle it; build the smallest exploratory artifact that answers it.

**Scope:** The artifact is exploratory. Do not treat a plausible prototype as production-ready code or a validated integration.

- Prerequisite: A specific behavioral or interface question.
- Prerequisite: Permission to create throwaway artifacts in a suitable location.
- Alternative: poteto/architect — You need concrete architectural sketches rather than an executable throwaway experiment.

### design-implement: Compare architecture sketches before implementation

**Suggested next:** poteto/architect

The current skill traces affected systems, compares two interface and ownership shapes, and uses arena for a large or contested design.

**Do next:** Trace the affected systems, sketch two different shapes, and choose the smallest interface with clear state ownership. Agree the implementation scope afterward.

**Scope:** Use it for pre-code sketches. A large or contested design can invoke arena, which creates and runs candidate artifacts; agree that scope first. The current leaf no longer specifies automatic implementation or a named checkpoint.

- Prerequisite: Access to the surrounding systems and caller constraints.
- Prerequisite: Arena capability or an explicit adaptation only when the design is large or contested.
- Alternative: matt/codebase-design — You need shared module and seam vocabulary rather than concrete architectural sketches.
- Conditional support: matt/implement — After the design is settled, you explicitly request implementation and agree the testing seams.

### review-standards-spec: Report standards and specification findings

**Suggested next:** matt/code-review

It pins a diff and reviews repository standards and spec compliance on separate axes.

**Do next:** Supply a resolving fixed point, the exact change, relevant standards, and the originating spec or an explicit absence.

**Scope:** The output is review findings. Missing specification coverage is reported, and review does not itself authorize code fixes or merging.

- Prerequisite: A nonempty committed comparison from a valid fixed point to HEAD; separately freeze any uncommitted work before expecting it in this diff.
- Prerequisite: Repository standards and the spec source, if available.
- Prerequisite: Separate standards/specification reviewers with fresh context windows.
- Alternative: poteto/interrogate — You permit isolated executable reproductions and want independent adversaries to prove failures rather than report standards/specification findings.

### review-adversarial: Prove adversarial findings with executable reproductions

**Suggested next:** poteto/interrogate

Independent adversaries try to break the change, and the coordinator reruns each reported reproduction before keeping it.

**Do next:** State the intent and exact scope, isolate each adversary in a worktree, run focused reproductions, and independently rerun the findings that survive.

**Scope:** Reviewers may write and run isolated repros. The workflow reports verified failures and does not apply product fixes; unrun speculation is dropped.

- Prerequisite: A clear intent, exact scope, and the relevant working-tree changes.
- Prerequisite: Permission and an environment for isolated worktrees and executable probes against real code.
- Prerequisite: Suitable independent model reviewers or an explicit host adaptation.
- Alternative: matt/code-review — You need source-and-diff review without executing product reproductions.

### write-pr-body: Write an evidence-backed PR description

**Suggested next:** matt/pr

It structures the body around a small explanatory view, before/after evidence, and merge risk.

**Do next:** Bring the finished diff, concrete validation evidence, and rollback implications; draft the body from those facts.

**Scope:** This is a writing template. It does not make the PR merge-ready, open it, or merge it by itself.

- Prerequisite: A concrete change and actual before/after evidence.
- Prerequisite: Known scope and rollback implications.
- Alternative: poteto/technical-writing — You need a general technical-document structure rather than Matt’s specific PR-body format.

### ready-pr: Make an existing PR ready for a merge decision

**Suggested next:** poteto/poteto-mode

The Babysit playbook manages the merge frontier, review threads, and CI until the forge says it is merge-ready.

**Do next:** Declare drive, threads-only, or check mode. Stop on a conflict or stale base and name the owner’s rebase and drift sweep; otherwise resolve the selected frontier blockers.

**Scope:** Babysitting never authorizes merging, rebasing, retargeting, or force-pushing. Opening a PR does not itself start babysitting.

- Prerequisite: An existing PR or ordered stack.
- Prerequisite: Forge CLI access, relevant watcher capability, and permission for scoped fixes and thread replies.
- Prerequisite: A single responsible babysitter for the stack.
- Alternative: matt/code-review — You only need findings, without CI watching or external changes.
- Poteto mode playbook: Babysit

### ship-pr: Verify and land an explicitly authorized PR run

**Suggested next:** poteto/poteto-mode

The Shipping playbook requires independent per-PR runtime verdicts and lands only the contiguous verified run from the bottom.

**Do next:** Identify the authorized PR run and ceiling, obtain independent non-author live verdicts, check that each verdict still covers the current patch, and land only the contiguous verified run bottom-up.

**Scope:** This merges code and can retarget or move dependent branches. A green CI check alone is not its runtime verification verdict.

- Prerequisite: Explicit authorization to land the selected PRs.
- Prerequisite: Merge-ready PRs and independent live verdicts for the current patches, with patch-id or build-equivalence receipts when relying on an older verdict.
- Prerequisite: Forge CLI and independent runtime-verification capability, with environment adaptation checked.
- Alternative: poteto/poteto-mode — Use the Babysit playbook instead if the request ends at merge readiness.
- Poteto mode playbook: Shipping

### learn-conversation: Learn through a code-grounded conversation

**Suggested next:** poteto/teach

It combines how code behaves with why it was shaped that way and builds the explanation at the learner’s pace.

**Do next:** Name the topic and what you already understand; start with one small complete explanation and expand as needed.

**Scope:** This teaches through conversation. It is not the persistent lesson-and-progress workspace of Matt’s teach skill.

- Prerequisite: A topic and, for code explanations, relevant source or evidence access.
- Alternative: matt/teach — You want saved lessons, resources, and evidence of progress across sessions.

### learn-workspace: Create a persistent learning workspace

**Suggested next:** matt/teach

It maintains a mission, sourced resources, HTML lessons, reference materials, and learning records across sessions.

**Do next:** Choose the learning mission and a workspace destination, then ground the first bounded lesson in high-quality resources.

**Scope:** This writes multiple persistent learning artifacts in the selected workspace. It has more setup than a single explanation.

- Prerequisite: An ongoing learning goal and writable teaching workspace.
- Prerequisite: Access to suitable learning sources.
- Alternative: poteto/teach — You want a conversational explanation now rather than a long-lived learning workspace.

### technical-document: Structure and clarify technical writing

**Suggested next:** poteto/technical-writing

It chooses tutorial, how-to, reference, or explanation before refining precision and readability.

**Do next:** Identify the reader’s task and choose one document mode, then revise the draft using real repository terms and verifiable claims.

**Scope:** It improves document structure and language; it does not verify product behavior or justify invented evidence.

- Prerequisite: A target audience and document purpose.
- Prerequisite: A draft or concrete source material.
- Alternative: matt/writing-for-agents — The document is steering instructions or a skill intended primarily for agents.

### triage-requests: Triage requests into actionable work

**Suggested next:** matt/triage

It classifies and verifies requests, gathers missing decisions, and records a durable agent-ready brief.

**Do next:** Select a narrow issue set and configured triage roles; verify each request before assigning a state.

**Scope:** This changes tracker state and may post AI-labeled comments. External PR triage depends on the repository’s configuration.

- Prerequisite: Configured tracker and triage vocabulary.
- Prerequisite: Authorization for the selected issue reads, writes, and comments.
- Alternative: matt/to-tickets — A plan is already agreed and simply needs a graph of implementation tickets.

### session-retrospective: Find improvements to the agent’s working environment

**Suggested next:** matt/retro

It inspects an actual coding session for navigation, checks, standards, tooling, and information-access improvements.

**Do next:** Choose the session and review its primary records; return prioritized environment improvements backed by observed friction.

**Scope:** The first deliverable is prioritized candidates, not automatic feature changes or silent edits to global instructions.

- Prerequisite: Access to the selected session records and repository check configuration.
- Alternative: poteto/reflect — You want the complete active transcript mined for durable, approval-gated edits to locally copied skills.

### prevent-mistakes: Prevent recurring classes of agent mistakes

**Suggested next:** poteto/correct

It requires evidence of repetition and prefers structural enforcement over another instruction.

**Do next:** Find a mistake class that occurred at least twice, choose architecture, types, lint, or tests, and prove the check catches a real past mistake.

**Scope:** This edits the repository and commits fixes by mistake class. It is not a report-only retrospective.

- Prerequisite: Evidence of repeated mistakes.
- Prerequisite: Permission for repository changes, checks, and commits.
- Alternative: matt/retro — You want prioritized improvement candidates before authorizing structural changes.

### sharpen-task: Improve the prompt without expanding the task

**Suggested next:** poteto/sharpen

It rewrites the task around expert methods, raw evidence, independent checks, and prototypes for choices an experiment can settle.

**Do next:** Supply the task prompt; ask the rewrite to include experimental prototypes for observable choices while leaving product and preference decisions to you.

**Scope:** The output is a revised prompt. It does not execute the rewritten task or add unrelated scope.

- Prerequisite: An existing task prompt and its intended scope.
- Alternative: matt/grill-me — The underlying decisions need an interactive interview rather than a prompt rewrite.

### coordinate-workers: Coordinate parallel coverage or candidate work

**Suggested next:** poteto/swarm

It declares a completion rule, bounded slices or race arms, and consolidates terminal evidence while retaining coverage gaps.

**Do next:** Define the artifact and done predicate, give each worker its own output, and declare how candidates or slices will be judged.

**Scope:** Worker agreement is not proof, and missing coverage is never a pass. Runtime, cloud, and model assumptions require host adaptation.

- Prerequisite: A partitionable bounded task or explicit candidate race.
- Prerequisite: Parallel-worker support and a declared selection or coverage rule.
- Prerequisite: Separate writable outputs where workers write.
- Alternative: poteto/figure-it-out — The task first needs a custom auditable workflow because ordinary playbooks do not fit.

### portable-handoff: Prepare a portable handoff for the next session

**Suggested next:** matt/handoff

It summarizes the current work for another agent, references existing artifacts, and redacts sensitive details.

**Do next:** State what the next session is for; save a concise handoff in the OS temporary directory with artifact pointers and suggested skills.

**Scope:** This writes a temporary handoff. It does not automatically message or launch another agent, or copy secrets into the summary.

- Prerequisite: The current conversation or reliable work context.
- Prerequisite: A next-session focus and writable OS temporary directory.
- Alternative: poteto/recall — You need to reconstruct context across prior scoped chats before making the handoff.

### catch-up: Catch up on this chat and outstanding decisions

**Suggested next:** poteto/ketchup

It reads changes since your last message and gives enough context to resolve every outstanding user-owned call.

**Do next:** Identify your last message, inspect current touched work and PR state, and summarize changes plus the decisions that still need you.

**Scope:** This is read-only catch-up. Do not start an app, edit code, or invent an action item to fill the reply.

- Prerequisite: Access to the current chat and state of any touched work.
- Alternative: poteto/recall — The needed context spans earlier chats or workspaces rather than the current chat interval.
