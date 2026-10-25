# Matt collection: compilation findings

This report interprets the downloaded source snapshot. It does not install or execute the collection. All paths below are relative to the Matt repository root; every `avoid_when` entry in `matt.json` is labeled as a catalog interpretation.

## Coverage and lifecycle

- **38 SKILL.md inputs, 38 interpretation records, 114 evidence ranges**. Every input was read in full; supporting material was read for material branching, output, approval and host assumptions. Evidence paths and line bounds were checked locally.
- **27 promoted plugin skills**: 20 engineering and 7 productivity. The plugin manifest explicitly lists those directories: `.claude-plugin/plugin.json:21–48`; category positioning is in `skills/engineering/README.md:1–7` and `skills/productivity/README.md:1–7`.
- **7 beta skills** under `skills/in-progress/`: chief-of-staff, claude-handoff, loop-me, setup-ts-deep-modules, writing-beats, writing-fragments and writing-shape. Upstream explicitly says this bucket is excluded from the plugin and can change or disappear: `skills/in-progress/README.md:1–9`. Its bullet inventory omits chief-of-staff, which exists as a full SKILL.md; discover files, not README bullet counts.
- **4 misc skills**, unpromoted rather than explicitly deprecated: git-guardrails-claude-code, migrate-to-shoehorn, scaffold-exercises and setup-pre-commit. `skills/misc/README.md:1–8`.

## Existing routing worth preserving

`ask-matt` already exists precisely because people cannot remember every skill (`skills/engineering/ask-matt/SKILL.md:2–13`). It is a substantive upstream router, not just a directory index. Its recommended primary route is:

1. In a working directory: grill-with-docs. Without one: grill-me.
2. If a design needs a runnable answer: prototype, with a portable handoff when moving sessions/directories.
3. If a build spans sessions: to-spec → to-tickets → implement per ticket, or implement-spec for parallel orchestration. Small work can proceed directly to implement in context.
4. TDD is the building discipline; code-review is the final Standards + Spec check; pr supplies the body format; retro improves the next run’s environment.

Evidence: `skills/engineering/ask-matt/SKILL.md:15–38`, `:81–97`. The shared catalog should expose and compare this route against Poteto’s approach, rather than silently substituting a new Matt workflow.

The same router distinguishes incoming raw requests (triage), hard bugs (diagnosing-bugs), huge foggy planning (wayfinder), and maintenance surveys (improve-codebase-architecture): `skills/engineering/ask-matt/SKILL.md:42–60`. Wayfinder is normally about decisions, not implementation; its resulting map should collapse into a spec before ticket implementation: `:52–54` and `skills/engineering/wayfinder/SKILL.md:11–13`.

There is already an ordered binary decision tree for context transitions: continue → clear → portable handoff → AFK subagent → compact, first applicable answer wins. Evidence: `skills/engineering/ask-matt/PHASE-BOUNDARIES.md:19–38`. This is a useful example for the proposed interface, but it answers a different question from “which skill fits this task?”

## Important distinctions for the shared catalog

- **Selection is not execution.** Upstream treats user-invoked skills as explicit user choices; router skills hint rather than invoke them. `skills/productivity/writing-for-agents/SKILL-MECHANICS.md:9–22`. Keep the catalog’s recommendation and copyable invocation separate from permission to run a whole flow. Actual host behavior remains an environment-specific capability, not a compatibility promise.
- **Some entries are references, not sessions.** codebase-design and writing-for-agents principally supply a shared vocabulary or rules; codebase-design conditionally delegates 3+ alternative interface designs. `skills/engineering/codebase-design/SKILL.md:8–28`, `:111–114`; `skills/engineering/codebase-design/DESIGN-IT-TWICE.md:11–23`. Avoid giving every catalog entry the same “start full workflow” behavior.
- **Approval friction is real and explicit.** grilling waits for user decisions and final shared understanding; tdd requires confirmed testing seams before any test; to-tickets requires approval before publishing. `skills/productivity/grilling/SKILL.md:28–30`; `skills/engineering/tdd/SKILL.md:22–24`; `skills/engineering/to-tickets/SKILL.md:42–63`. The chooser should surface these checkpoints when comparing workflows.
- **A recommendation can imply consequential writes.** implement commits; implement-spec creates branches/worktrees and conditionally a PR, resolves tickets and cleans up; wayfinder writes tracker state and pushes research branches. `skills/engineering/implement/SKILL.md:11–17`; `skills/engineering/implement-spec/SKILL.md:25–40`; `skills/engineering/wayfinder/SKILL.md:113–126`. Do not flatten these into generic “coding” tags.
- **Remote effects are conditional.** A configured tracker can be local Markdown; “publish” can mean create a file, not post online. `skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:3–15`. JSON effect lists express possible workflow effects, not unconditional actions on every run.
- **Teaching differs from explaining.** teach intentionally creates a stateful course workspace with lessons, reusable assets and learning evidence. `skills/productivity/teach/SKILL.md:8–20`, `:49–69`; `skills/productivity/teach/LEARNING-RECORD-FORMAT.md:29–42`. wait-what only repairs an explanation: `skills/productivity/wait-what/SKILL.md:7`.
- **Human-only setup is separate from agent setup.** wizard writes a procedure for the human and statically verifies it, rather than running it end-to-end. It can later write .env values and GitHub secrets/variables. `skills/engineering/wizard/SKILL.md:18–44`; `skills/engineering/wizard/template.sh:137–178`.
- **Host and domain assumptions matter.** claude-handoff requires the Claude CLI background-agent command; git-guardrails-claude-code uses Claude hooks plus Bash/jq; scaffold-exercises expects the AI Hero linter; setup-pre-commit is a JS/Husky recipe. `skills/in-progress/claude-handoff/SKILL.md:8–10`; `skills/misc/git-guardrails-claude-code/SKILL.md:22–39` and `scripts/block-dangerous-git.sh:3–21`; `skills/misc/scaffold-exercises/SKILL.md:8`; `skills/misc/setup-pre-commit/SKILL.md:17–47`.

## Recommended entry questions (catalog interpretation)

1. What needs to change: your understanding, a decision/plan, implementation, an existing failure, a review, a learning process, or the working environment?
2. For decisions: can the live user answer, is knowledge held by someone else, is research needed, or must a runnable artifact settle it? Route toward grilling/grill-with-docs, to-questionnaire, research or prototype respectively.
3. For building: is the work already specified, and does it fit one session? This separates discovery, to-spec/to-tickets, implement and implement-spec.
4. For very large uncertain work: is the route itself unresolved across sessions? Consider wayfinder only then.
5. Before presenting the set: show stable/beta/misc status, host requirements, approval checkpoints and possible effects. A beta entry should be discoverable but clearly distinguished from the stable plugin.

The useful unit is a primary workflow plus its references and follow-on steps. Distinguish “calls/consults,” “suggested next,” and “alternative route”; the current contract’s companions list records explicit internal references, not a promise that every such entry is directly invocable by another skill.

## Source tensions and uncertainty to carry forward

- engineering README describes TDD as red-green-refactor (`skills/engineering/README.md:29`), while the executable skill explicitly excludes refactoring from its loop and puts it in review (`skills/engineering/tdd/SKILL.md:34–38`). This compilation follows the full SKILL.md. Changes in referenced files must trigger reinterpretation even if a short description is unchanged.
- setup-ts-deep-modules describes four conceptual rules (`skills/in-progress/setup-ts-deep-modules/SKILL.md:26–31`), while its template has five named forbidden rules, including private fixture protection (`skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs:28–74`). The record describes the policy rather than falsely equating the counts.
- Upstream can demand a shared Skill tool, background agents, worktrees or host-specific CLI behavior. This research did not execute workflows and therefore makes no claim that those capabilities work unchanged in the user’s installed Codex or Claude environment.
- Confirmation text reports explicit checkpoints, not a complete authorization analysis. “Not explicitly specified” means exactly that; it does not mean permission is unnecessary under a host’s rules.
- Beta is a bucket-level lifecycle statement. The present snapshot’s seven beta files are included even when a bucket README’s list is incomplete.
