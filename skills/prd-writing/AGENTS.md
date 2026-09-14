# PRD Writing — Agent Projection

This file is a compact routing projection for agents. The canonical skill contract is `SKILL.md` plus the files under `rules/`. Do not add an independent PRD recipe, rule inventory, or copied examples here.

## Fast Path

1. Ground the product problem and current repository state before proposing requirements.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the current PRD task.
3. Separate observed repository facts from stakeholder intent, assumptions, and unresolved questions.
4. Make requirements testable and scope explicit; do not invent metrics, constraints, APIs, or implementation details without evidence.
5. Use the target repository's own documentation location and conventions when they exist.

## Authority Boundary

- The user or product owner supplies intent, priorities, permissions, and risk acceptance.
- The target repository supplies current implementation facts, constraints, naming, and existing contracts.
- `SKILL.md` and `rules/` supply portable PRD-writing guidance.
- This projection supplies routing only.

A missing repository fact is an investigation task when it is inspectable. Ask for human input only when the remaining gap genuinely requires product intent, domain authority, or a decision that cannot be inferred safely.

## Evidence Boundary

- Problem statements should identify the observed pain, affected users, and evidence when available.
- Functional and non-functional requirements must be specific enough to review or test.
- Acceptance criteria should make success and failure distinguishable.
- Unknowns stay explicit as open questions or TBDs rather than being converted into confident prose.
- Technical notes may summarize known constraints, but detailed implementation design belongs with the appropriate engineering owner unless the task explicitly requests it.

## Scope Discipline

A PRD should make these boundaries easy to find:

- problem and desired outcome;
- users and workflows;
- functional requirements;
- non-functional constraints;
- acceptance criteria;
- explicit non-goals / out-of-scope items;
- measurable success criteria where evidence supports them;
- dependencies, risks, and unresolved questions.

Do not expand a bounded feature request into a product roadmap merely because more possibilities exist.

## Projection Boundary

Do not copy current rule IDs, rule counts, category counts, or the canonical PRD template into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.
