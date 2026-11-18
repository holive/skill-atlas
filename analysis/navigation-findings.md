# V2 navigation findings

## Scope and ownership

This file records a bounded source investigation for the navigation dataset. It does not activate the upstream skills. The upstream instructions are evidence about recommendations, not instructions for this build. The English copy is an interpretation of the pinned source snapshots in `catalog/skills.json`. Runtime compatibility and installation are not asserted.

- Navigation rules belong to `catalog/navigation.json`; the shared resolver should interpret those data without embedding alternative routing rules.
- Regression paths belong to `catalog/navigation-cases.json`. They check consistency of the authored graph, not independent semantic recommendation quality.
- The catalog remains the source for stable qualified IDs, source URLs, classifications, and source requirements. Search should index every catalog entry; this menu is deliberately selective.
- This bounded change leaves the original binary graph and its analysis lock untouched.

## Source-derived decisions

1. **Module testing strategy is not a code explanation.** `matt/codebase-design` explicitly covers making modules testable, defines the interface as the test surface, and is a reference to consult. Its `DEEPENING.md` differentiates in-process dependencies, local substitutes, owned remote transports, and true external systems. Both strategy outcomes request a concrete testability map, rather than merely recommending `how` or `teach`. The graph asks whether isolated execution is allowed or the task is analysis only. Neither outcome claims isolated success proves production integration.
2. **TDD is a conditional next phase.** Matt’s current `tdd` requires the seams to be written down and confirmed before any tests, and explicitly calls codebase-design a reference rather than a session to run. The strategy outcomes suggest it only when tests are requested, seams agreed, and execution permitted. Poteto’s `tdd` is specifically a bug workflow with a cheap local path or explicit request. Feature development and bug regressions therefore have separate leaves.
3. **Real-app and formal verification are different tasks.** The create/maintain app skills actually start and drive the app; app strategy must not leak onto the no-full-system route. Formal verification records bounds, assumptions, synchronization, and a deliberate failing variant. Its checks do not prove the entire system.
4. **Settled discussion becomes a spec.** `matt/to-spec` synthesizes the existing conversation rather than reopening the whole interview, but still asks for testing-seam agreement and publishes to the configured tracker. This is distinct from implementation and from ticket slicing.
5. **Advice is narrower than architect.** Poteto architect compares designs and continues to implementation by default. The design-only route uses Matt’s reference; the implementation route states architect’s default and opt-in checkpoint.
6. **Review, communication, readiness, and landing have separate boundaries.** Matt code-review produces separate standards/spec reports; interrogate synthesizes adversarial findings without auto-fixing; Matt pr is a body-writing template. Babysit ends at merge-ready, while Shipping merges only an independently verified contiguous run. The two Poteto routes name their real playbooks, without invented slash commands.
7. **Context is immediately reachable.** The context goal goes directly to portable handoff or read-only catch-up. It applies to coding tasks too and does not hide behind a software/non-software fork.
8. **Workflow improvement is discoverable.** Triage, retrospective, repeated-mistake prevention, prompt sharpening, and parallel coordination are direct options. More specialized setup, verification maintenance variants, writing flows, principles, and experimental entries remain discoverable by full-catalog search.

## Exact source ownership anchors

Source paths below are relative to `/Users/hugooliveira/projects/skill-atlas/sources/<collection>/`. Catalog URLs are pinned to the compiled snapshot commit. The source files and relevant discriminator passages were reread during this investigation.

| Decision | Source passage |
| --- | --- |
| Testability vocabulary and test surface | `matt/skills/engineering/codebase-design/SKILL.md`, lines 1–8, 61–100; `DEEPENING.md`, dependency categories and seam discipline |
| TDD seam agreement and reference scope | `matt/skills/engineering/tdd/SKILL.md`, section “Seams: where tests go” |
| Bug-only practical regression path | `poteto/pstack/skills/tdd/SKILL.md`, description and “If a Failing Test Is Impractical” |
| Settled conversation synthesis | `matt/skills/engineering/to-spec/SKILL.md`, lines 1–24 |
| Default implementation after design | `poteto/pstack/skills/architect/SKILL.md`, “Phase C: Agree (opt-in)” and “Phase D” |
| Report rather than auto-fix | `poteto/pstack/skills/interrogate/SKILL.md`, lines 7–9 |
| PR readiness is not landing | `poteto/pstack/skills/poteto-mode/playbooks/babysit.md`, lines 3–7 and 21–23 |
| Independent verification before landing | `poteto/pstack/skills/poteto-mode/playbooks/shipping.md`, lines 3–10 |
| Live diagnosis is not a product fix | `poteto/pstack/skills/poteto-mode/playbooks/runtime-forensics.md`, full playbook |
| Safe app harness generation and proof | `poteto/pstack/skills/create-verification-skill/SKILL.md`, lines 9–40 |
| App maintenance scope | `poteto/pstack/skills/maintain-verification-skill/SKILL.md`, lines 9–25 and 29–37 |
| Bounded formal proof and real failing variant | `poteto/pstack/skills/create-formal-verification-skill/SKILL.md`, “What makes it good” and “Prove it before you hand off” |
| Portable handoff | `matt/skills/productivity/handoff/SKILL.md`, lines 8–16 |
| Read-only current-chat catch-up | `poteto/pstack/skills/ketchup/SKILL.md`, lines 9–17 |

## Primary recommendations and pinned source links

- [matt/code-review](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md) — `skills/engineering/code-review/SKILL.md`.
- [matt/codebase-design](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md) — `skills/engineering/codebase-design/SKILL.md`.
- [matt/diagnosing-bugs](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs/SKILL.md) — `skills/engineering/diagnosing-bugs/SKILL.md`.
- [matt/grill-with-docs](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) — `skills/engineering/grill-with-docs/SKILL.md`.
- [matt/handoff](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff/SKILL.md) — `skills/productivity/handoff/SKILL.md`.
- [matt/implement](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md) — `skills/engineering/implement/SKILL.md`.
- [matt/implement-spec](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement-spec/SKILL.md) — `skills/engineering/implement-spec/SKILL.md`.
- [matt/pr](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/pr/SKILL.md) — `skills/engineering/pr/SKILL.md`.
- [matt/prototype](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/prototype/SKILL.md) — `skills/engineering/prototype/SKILL.md`.
- [matt/research](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/research/SKILL.md) — `skills/engineering/research/SKILL.md`.
- [matt/retro](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/retro/SKILL.md) — `skills/engineering/retro/SKILL.md`.
- [matt/tdd](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md) — `skills/engineering/tdd/SKILL.md`.
- [matt/teach](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md) — `skills/productivity/teach/SKILL.md`.
- [matt/to-spec](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-spec/SKILL.md) — `skills/engineering/to-spec/SKILL.md`.
- [matt/to-tickets](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md) — `skills/engineering/to-tickets/SKILL.md`.
- [matt/triage](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/triage/SKILL.md) — `skills/engineering/triage/SKILL.md`.
- [poteto/architect](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md) — `pstack/skills/architect/SKILL.md`.
- [poteto/correct](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/correct/SKILL.md) — `pstack/skills/correct/SKILL.md`.
- [poteto/create-formal-verification-skill](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-formal-verification-skill/SKILL.md) — `pstack/skills/create-formal-verification-skill/SKILL.md`.
- [poteto/create-verification-skill](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/SKILL.md) — `pstack/skills/create-verification-skill/SKILL.md`.
- [poteto/how](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/SKILL.md) — `pstack/skills/how/SKILL.md`.
- [poteto/interrogate](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/SKILL.md) — `pstack/skills/interrogate/SKILL.md`.
- [poteto/ketchup](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup/SKILL.md) — `pstack/skills/ketchup/SKILL.md`.
- [poteto/maintain-verification-skill](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-verification-skill/SKILL.md) — `pstack/skills/maintain-verification-skill/SKILL.md`.
- [poteto/poteto-mode](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md) — `pstack/skills/poteto-mode/SKILL.md`.
- [poteto/sharpen](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/sharpen/SKILL.md) — `pstack/skills/sharpen/SKILL.md`.
- [poteto/swarm](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/swarm/SKILL.md) — `pstack/skills/swarm/SKILL.md`.
- [poteto/tdd](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/tdd/SKILL.md) — `pstack/skills/tdd/SKILL.md`.
- [poteto/teach](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/teach/SKILL.md) — `pstack/skills/teach/SKILL.md`.
- [poteto/technical-writing](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/technical-writing/SKILL.md) — `pstack/skills/technical-writing/SKILL.md`.
- [poteto/why](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md) — `pstack/skills/why/SKILL.md`.

## Validation and limits

- 10 goals, 12 question nodes, 35 outcomes, 35 explicit regression fixtures, and at most 2 follow-up questions on every route.
- Independently walked all goal starts, choice edges, and fixtures. No cycles, missing targets, duplicate question/outcome IDs, duplicate choice IDs, unreachable nodes, or uncovered outcomes. Every primary is a stable catalog entry; all primary, alternative, and support IDs exist.
- Every outcome has one primary, a concrete next step, a material boundary, prerequisites, and a conditional alternative. Reference primaries are explicitly labeled in their copy.
- Outcomes are recommendations from source semantics, not a guarantee that one author is universally better. Alternatives retain meaningful differences in output and action scope.
- Fixture coverage proves the authored graph resolves as intended. It does not measure recommendation precision on unseen user tasks. Parent should separately test the real user scenario, ambiguity, backtracking, and local-search recovery.
- The menu intentionally does not expose all 96 source entries. Full-catalog search is required to avoid making unrouted specialized or experimental entries invisible.
- Poteto’s source names Cursor-specific agents, model roles, control skills, cloud tools, and project-local directories. Recommendations preserve these requirements; the page does not install or invoke them.
- No refresh or upstream interpretation change is performed here. This graph is grounded in the current pinned full compilation; biweekly source refresh still needs the separate catalog workflow.


## 2026-11-18 maintenance reconciliation

The current guide adds a review-execution question before Interrogate, offers architecture sketches without the removed automatic implementation phase, refreshes source readiness and approval boundaries, and exposes the experimental software-factory reference only through opt-in search. All 36 guided scenarios and current browser paths passed. See `docs/maintenance/2026-11-18.md` and the navigation lock for current evidence; earlier notes above describe the original release.
