# Composition and differences

Curator interpretations of pinned source evidence; not upstream compatibility guarantees.

## one-owner

**Compare:** matt/implement, matt/implement-spec, poteto/poteto-mode

Choose one execution coordinator for a task; treat the other complete workflow as an alternative. Borrow a focused reference only when its constraints fit the chosen workflow.

- [matt/skills/engineering/implement/SKILL.md:7–17](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/implement/SKILL.md#L7-L17): Owns implementation through tests, review, QA and commit.
- [poteto/pstack/skills/poteto-mode/SKILL.md:121–125](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L121-L125): Owns playbook selection and its required steps.

## tdd-name-collision

**Compare:** matt/tdd, poteto/tdd

Matt covers feature and bug TDD at confirmed public seams; Poteto is a practical bug regression route with explicit alternatives when test setup is disproportionate. Qualify every reference and preserve the confirmation difference.

- [matt/skills/engineering/tdd/SKILL.md:18–26](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L18-L26): User-confirmed public testing seams.
- [matt/skills/engineering/tdd/SKILL.md:34–38](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L34-L38): Red-green loop; refactoring occurs at review.
- [poteto/pstack/skills/tdd/SKILL.md:9–26](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/tdd/SKILL.md#L9-L26): Bug regression scope and impractical-test fallback.

## teach-name-collision

**Compare:** matt/teach, poteto/teach

Matt creates a persistent learning workspace with lessons and history. Poteto explains a body of work through how/why investigations. Select by desired result rather than name similarity.

- [matt/skills/productivity/teach/SKILL.md:8–20](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/teach/SKILL.md#L8-L20): Stateful learning workspace.
- [poteto/pstack/skills/teach/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/teach/SKILL.md#L9-L15): Conversational explanation using how and why.

## approval-policy

**Compare:** matt/grilling, matt/tdd, poteto/poteto-mode

Surface source approval checkpoints as part of the comparison. Upstream autonomy prose cannot grant authority beyond the human request, actual tools or host policy.

- [matt/skills/productivity/grilling/SKILL.md:28–30](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md#L28-L30): Human decisions and final shared-understanding gate.
- [matt/skills/engineering/tdd/SKILL.md:22–24](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/tdd/SKILL.md#L22-L24): Testing-seam confirmation.
- [poteto/pstack/skills/poteto-mode/SKILL.md:81–87](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L81-L87): Reversible actions and always-pause source policy.

## host-readiness

**Compare:** poteto/poteto-mode, poteto/poteto-help, poteto/setup-pstack

Pstack has Cursor assumptions and an explicit Claude Code adapter. Inclusion in this catalog does not establish Codex execution support or model availability.

- [poteto/pstack/docs/harness/claude-code.md:3–38](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/docs/harness/claude-code.md#L3-L38): Existing Claude Code mappings and model fallback.
- [poteto/pstack/skills/poteto-mode/SKILL.md:91–101](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md#L91-L101): Task, agent type and model-role requirements.

## architecture-effects

**Compare:** matt/codebase-design, poteto/architect

Matt codebase-design is a vocabulary reference. Poteto architect explores candidates and implements by default. A design-only request needs an explicit checkpoint.

- [matt/skills/engineering/codebase-design/SKILL.md:8–18](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md#L8-L18): Reference vocabulary and module interface definitions.
- [poteto/pstack/skills/architect/SKILL.md:41–53](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/architect/SKILL.md#L41-L53): Default implementation and optional requested checkpoint.

## review-preparation-effects

**Compare:** matt/code-review, poteto/no-comments, poteto/interrogate

Distinguish reporting a review from modifying code in preparation for review. No-comments can delete comments; it must not be treated as a read-only quality checklist.

- [poteto/pstack/skills/no-comments/SKILL.md:19–24](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/no-comments/SKILL.md#L19-L24): Delegated comment deletion and approval rules.
- [poteto/pstack/skills/interrogate/SKILL.md:9–23](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/interrogate/SKILL.md#L9-L23): Review scope without automatically applying findings.

## migration-unit-scope

**Compare:** poteto/principle-outcome-oriented-execution, poteto/principle-sequence-verifiable-units

Choose explicit phase and verification-unit boundaries. Planned reversible intermediate breakage and green completed units are conditional constraints, not an unconditional pair of defaults.

- [poteto/pstack/skills/principle-outcome-oriented-execution/SKILL.md:13–21](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L13-L21): Allows planned scoped intermediate breakage with final verification.
- [poteto/pstack/skills/principle-sequence-verifiable-units/SKILL.md:9–15](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L9-L15): Each completed unit is checked before the next.
