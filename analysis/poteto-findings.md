# Poteto workflow compilation findings

This is a descriptive, agent-interpreted compilation of downloaded upstream text. It does not activate pstack or grant any workflow permission. All evidence paths below are relative to the downloaded `cursor/plugins` root.

## Coverage

- 34 non-principle SKILL.md records, including routers, setup, utilities and workflows.
- All 34 assigned SKILL.md files were read in full. All 23 poteto-mode playbooks and the Claude Code adapter informed interpretation. Selected material reference prompts, agent definitions and help recipes were also read.
- 91 evidence ranges were checked for existing paths and valid line bounds. Every record cites its own SKILL.md. All companion IDs resolve to downloaded skills.
- Supporting playbooks and agent definitions are dependencies, not extra skill records.

## Native entry flow

The requested navigator has an upstream precedent. `/poteto-help` already categorizes needs into setup, starting a mode task, picking a skill, fixing a run, or personalizing pstack. It asks one multiple-choice question only when context cannot resolve the need. Help returns an answer and a prompt; it does not start the work. Actual requests to do work route to mode. Evidence: `pstack/skills/poteto-help/SKILL.md:9-34`.

The default setup sequence is `/setup-pstack`, `/create-verification-skill` unless a harness exists, then `/poteto-mode` with a goal and a pass/fail done check. Model setup is optional; without it, role defaults apply. Evidence: `pstack/skills/poteto-help/SKILL.md:36-48`.

`poteto-help` says default to mode for nontrivial work and choose individual skills when the user wants more or less of a particular workflow. It explicitly discourages manually listing a skill sequence because that can drop or reorder playbook steps. Evidence: `pstack/skills/poteto-help/SKILL.md:50-64`; `pstack/skills/poteto-help/references/prompting.md:3-17`.

A catalog should distinguish entry points from dependencies. Mode is a router, playbooks are internal step lists with no slash command, and principles are leaf rules normally read through mode rather than primary user destinations. There is no pstack `/orchestrate` skill and no standalone planning skill. Planning is a mode playbook. Evidence: `pstack/skills/poteto-help/SKILL.md:114-135`.

## Material workflow distinctions

- `architect` is design **and implementation** by default. A human design checkpoint must be requested. Its candidates start from caller usage and two or three realistic call sites. Evidence: `pstack/skills/architect/SKILL.md:41-53`; `pstack/skills/architect/references/runner-prompt.md:9-18`.
- `arena` produces competing artifacts from the same brief, selects a base and grafts chosen strengths. `swarm` partitions coverage or runs declared races and returns one report. Evidence: `pstack/skills/arena/SKILL.md:13-48`; `pstack/skills/swarm/SKILL.md:20-41`.
- `interrogate` is review-only and does not auto-apply findings. The review challenges implementation against the intent, not the intent itself. `blast-radius` instead executes a proof of a load-bearing safety fact beyond the diff. Evidence: `pstack/skills/interrogate/SKILL.md:9-23`; `pstack/skills/interrogate/references/reviewer-prompt.md:11-15`; `pstack/skills/blast-radius/SKILL.md:31-48`.
- `how` explains mechanics, `why` seeks historical motivations, and `teach` orchestrates one or both for conversational understanding. `why` requires explicit coverage gaps and preserves confidence tiers. Evidence: `pstack/skills/how/SKILL.md:9-36`; `pstack/skills/why/SKILL.md:29-94`; `pstack/skills/teach/SKILL.md:9-21`.
- `tdd` is primarily a pragmatic bug-regression workflow. It skips disproportionate or unclear new tests and can use another executable check. Evidence: `pstack/skills/tdd/SKILL.md:3-26`.
- Verification generation and maintenance are separate from product repair. Formal generation proves a broken variant is caught and preserves bounded-scope caveats. Maintenance distinguishes model drift from product bugs and does not weaken a property to pass. Evidence: `pstack/skills/create-formal-verification-skill/SKILL.md:23-39`; `pstack/skills/maintain-formal-verification-skill/SKILL.md:22-44`.
- Mode investigation is read-only with no PR or implementation. Multi-phase planning is plan-only and waits for an explicit execution go. Runtime forensics can instrument a live process despite describing its final deliverable as a diagnosis; record effects according to actions, not only headings. Evidence: `pstack/skills/poteto-mode/playbooks/investigation.md:5-12`; `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:3-15`; `pstack/skills/poteto-mode/playbooks/runtime-forensics.md:3-11`.

## Host requirements and portability

pstack is designed for Cursor, but it explicitly supports Claude Code through an adapter. Therefore “Cursor-only” is too broad a label for the bundle. The adapter maps Task to Agent, rule paths and skill paths, cloud workers to worktree isolation, and unsupported model families to the parent model. Evidence: `pstack/skills/poteto-help/SKILL.md:46-48`; `pstack/docs/harness/claude-code.md:3-46`.

That mapping does not establish Codex support. Cursor role slugs, Task fields, Custom Modes, `/loop`, routines, secret-request cards and transcript locations are host assumptions. Claude Code skips unsupported Cursor features and loses cross-family model diversity where non-Claude models fall back to the session model. Evidence: `pstack/docs/harness/claude-code.md:34-38,48-67`; `pstack/skills/poteto-mode/SKILL.md:91-101`.

Other required pieces are outside pstack. `create-skill` and `/loop` are Cursor built-ins; `deslop`, `control-ui` and `control-cli` come from cursor-team-kit. Some workflows also need git worktrees, gh or optional Origin, Node/Bun, a live app harness, or connected evidence MCPs. Evidence: `pstack/skills/poteto-help/SKILL.md:114-118`; `pstack/skills/poteto-mode/playbooks/opening-a-pr.md:5-30`; `pstack/skills/poteto-mode/playbooks/orchestrate.md:15-23`.

`statechart` has a material install effect: the first run downloads TLC and Java through mise, about 305 MB, unless existing tools are supplied. `make-bot-ui` needs Cursor routines and secret requests plus a local server and Tailscale; it is not a generic page-builder skill. Evidence: `pstack/skills/statechart/SKILL.md:9-17`; `pstack/skills/make-bot-ui/SKILL.md:11-57,75-103`.

## Cross-bundle composition pitfalls

These are routing recommendations inferred from Poteto sources, not universal compatibility verdicts. The coordinating compiler should compare Matt evidence before marking a pair as conflicting.

1. Choose one top-level execution owner. Mode chooses a full playbook and coordinates its dependencies. Overlaying another independent complete planning or delivery workflow can duplicate or reorder phases. Evidence: `pstack/skills/poteto-mode/SKILL.md:121-149`; `pstack/skills/poteto-help/references/prompting.md:13-17`.
2. Preserve approval differences at the individual-skill and playbook level. Mode permits reversible external actions such as team chat and ticket updates without asking, while retaining an always-pause list. This text cannot override the actual host or human authorization. Evidence: `pstack/skills/poteto-mode/SKILL.md:81-89`.
3. Do not label all reviews read-only. `interrogate` is read-only, but `/no-comments` deletes comments and then fixes accepted code issues. It asks for approval to encode a constraint; the source nevertheless says to delete an unencoded comment and report the constraint open. That is a consequential policy to surface before composing with comment-preserving workflows. Evidence: `pstack/skills/no-comments/SKILL.md:19-24`; `pstack/agents/comment-sicko.md:14-30`.
4. `reflect` waits for approval before skill edits but automatically files backlog issues without waiting. `automate-me` ships a personal mode through a PR. These are different side-effect and approval profiles despite both being skill-improvement flows. Evidence: `pstack/skills/reflect/SKILL.md:45-60`; `pstack/skills/automate-me/SKILL.md:75-96`.
5. Babysit stops at merge-ready and never authorizes merging. Shipping needs independent per-PR live verdicts. Autopilot-full can merge within its granted queue, whereas Autopilot-stack reserves landing for the operator. These are different delivery permissions under the same mode entry point. Evidence: `pstack/skills/poteto-mode/playbooks/babysit.md:19-21`; `pstack/skills/poteto-mode/playbooks/shipping.md:5-10`; `pstack/skills/poteto-mode/playbooks/autopilot-full.md:7-23`; `pstack/skills/poteto-mode/playbooks/autopilot-stack.md:3-10`.
6. Cost is not only a model choice. Multi-phase planning requires ten live lanes, unit and perf evidence for each PR, and a human review gate for interaction changes. Mode's general style also prescribes grounding and architecture/delegation gates. Show these burdens rather than ranking workflows solely by descriptive similarity. Evidence: `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:13-15,63-76,96-124`; `pstack/skills/poteto-mode/SKILL.md:19-36`.
7. Preserve source-specific uncertainty under prose cleanup. Teach explicitly keeps why's confidence language even while rewriting for clarity. A shared catalog should not treat unslop as permission to remove evidential caveats. Evidence: `pstack/skills/teach/SKILL.md:11-19`; `pstack/skills/why/references/epistemics.md:5-37`.

## Remaining uncertainty

No upstream instructions or executables were run. Host model availability, MCP access, installation behavior and workflow correctness are untested. Findings describe this downloaded revision, not a live production guarantee. Reference and agent files were read where they materially explain scope or behavior; not every script implementation or source-specific MCP example was audited. Effects are conservative capability summaries and still depend on the selected task and playbook. Cross-bundle compatibility remains provisional until the coordinator compares the Matt records and the actual host constraints.
