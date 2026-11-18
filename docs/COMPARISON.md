# Composition and differences

Curator interpretations of pinned source evidence; not upstream compatibility guarantees.

## one-owner

**Compare:** matt/implement, matt/implement-spec, poteto/poteto-mode

Choose one execution coordinator for a task; treat the other complete workflow as an alternative. Borrow a focused reference only when its constraints fit the chosen workflow.

- [matt/skills/engineering/implement/SKILL.md:7–17](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md#L7-L17): Owns implementation through tests, review, QA and commit.
- [poteto/pstack/skills/poteto-mode/SKILL.md:106–110](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L106-L110): Owns playbook selection and its required steps.

## tdd-name-collision

**Compare:** matt/tdd, poteto/tdd

Matt covers feature and bug TDD at confirmed public seams; Poteto is a practical bug regression route with explicit alternatives when test setup is disproportionate. Qualify every reference and preserve the confirmation difference.

- [matt/skills/engineering/tdd/SKILL.md:18–26](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L18-L26): User-confirmed public testing seams.
- [matt/skills/engineering/tdd/SKILL.md:34–38](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L34-L38): Red-green loop; refactoring occurs at review.
- [poteto/pstack/skills/tdd/SKILL.md:9–26](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/tdd/SKILL.md#L9-L26): Bug regression scope and impractical-test fallback.

## teach-name-collision

**Compare:** matt/teach, poteto/teach

Matt creates a persistent learning workspace with lessons and history. Poteto explains a body of work through how/why investigations. Select by desired result rather than name similarity.

- [matt/skills/productivity/teach/SKILL.md:8–20](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/teach/SKILL.md#L8-L20): Stateful learning workspace.
- [poteto/pstack/skills/teach/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/teach/SKILL.md#L9-L15): Conversational explanation using how and why.

## approval-policy

**Compare:** matt/grilling, matt/tdd, poteto/poteto-mode, poteto/principle-never-block-on-the-human

Surface each source approval checkpoint. The mode permits reversible team-chat and ticket actions, while Never Block requires confirmation for external messages and worker guidance stops for messages outside the run. These source boundaries differ; upstream autonomy cannot grant authority beyond the human request, actual tools or host policy.

- [matt/skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md#L28-L30): Human decisions and final shared-understanding gate.
- [matt/skills/engineering/tdd/SKILL.md:22–24](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md#L22-L24): Testing-seam confirmation.
- [poteto/pstack/skills/poteto-mode/SKILL.md:74–80](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L74-L80): Reversible actions and always-pause source policy.
- [poteto/pstack/skills/principle-never-block-on-the-human/SKILL.md:9–15](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-never-block-on-the-human/SKILL.md#L9-L15): The leaf keeps external-message confirmation distinct from reversible local work.
- [poteto/pstack/skills/poteto-mode/worker.md:3–7](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/worker.md#L3-L7): Worker restrictions include messages to someone outside the run.

## host-readiness

**Compare:** poteto/poteto-mode, poteto/poteto-help, poteto/setup-pstack

Pstack has Cursor assumptions and an explicit Claude Code adapter. Inclusion in this catalog does not establish Codex execution support or model availability.

- [poteto/pstack/docs/harness/claude-code.md:3–38](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/docs/harness/claude-code.md#L3-L38): Existing Claude Code mappings and model fallback.
- [poteto/pstack/skills/poteto-mode/SKILL.md:84–100](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/poteto-mode/SKILL.md#L84-L100): Task, agent type and model-role requirements.

## architecture-effects

**Compare:** matt/codebase-design, poteto/architect

Matt codebase-design supplies shared interface and seam vocabulary. The current Poteto architect leaf traces affected systems and compares concrete sketches before code, using arena only for large or contested designs. It no longer specifies its former automatic implementation phase or optional checkpoint. Request implementation separately when that is the next phase.

- [matt/skills/engineering/codebase-design/SKILL.md:8–18](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md#L8-L18): Reference vocabulary and module interface definitions.
- [poteto/pstack/skills/architect/SKILL.md:9–11](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/architect/SKILL.md#L9-L11): Current pre-code comparison of two shapes and conditional arena; former automatic implementation/checkpoint phases are absent.

## review-preparation-effects

**Compare:** matt/code-review, poteto/no-comments, poteto/interrogate

Distinguish standards/specification reporting, executable adversarial probes, and code cleanup. Interrogate creates isolated reproductions and keeps rerun-proven findings without applying product fixes. No-comments can delete comments and implement scoped root-cause fixes; it is not a read-only quality checklist.

- [matt/skills/engineering/code-review/SKILL.md:6–12](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md#L6-L12): Separate standards/specification reporting tracks.
- [poteto/pstack/skills/interrogate/SKILL.md:9–25](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/interrogate/SKILL.md#L9-L25): Executable adversarial reproductions and reruns, without product fixes.
- [poteto/pstack/skills/no-comments/SKILL.md:19–24](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/no-comments/SKILL.md#L19-L24): Comment deletions, scoped implementation and approval-gated encoding.

## migration-unit-scope

**Compare:** poteto/principle-outcome-oriented-execution, poteto/principle-sequence-verifiable-units

Choose explicit phase and verification-unit boundaries. Planned reversible intermediate breakage and green completed units are conditional constraints, not an unconditional pair of defaults.

- [poteto/pstack/skills/principle-outcome-oriented-execution/SKILL.md:13–21](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L13-L21): Allows planned scoped intermediate breakage with final verification.
- [poteto/pstack/skills/principle-sequence-verifiable-units/SKILL.md:9–13](https://github.com/cursor/plugins/blob/35a90942a7f02e1ebbc2443643179815f2147954/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L9-L13): Each completed unit is checked before the next.
