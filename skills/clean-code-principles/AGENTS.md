# Clean Code Principles — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second rule inventory, count, pattern catalog, or compiled example set here.

## Fast Path

1. Inspect the target repository's architecture, language conventions, existing abstractions, tests, and static-analysis evidence.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Tie every recommendation to an observed design problem or change pressure.
4. Prefer the smallest useful correction over introducing abstractions merely to satisfy a named principle.
5. Validate with the repository's configured tooling and tests.

## Ownership Boundary

- `SKILL.md` owns activation, rule routing, and high-level decision discipline.
- `rules/` owns detailed SOLID, core-principle, and pattern guidance.
- the target repository owns its architecture, conventions, abstraction boundaries, and validation commands.
- this projection owns no independent clean-code semantics.

## Evidence Boundary

- Principles are heuristics, not automatic refactoring mandates.
- Similar code is not automatically duplicated knowledge.
- Interfaces, layers, repositories, and other abstractions require concrete pressure or boundary value.
- Prefer evidence about coupling, change cost, failure behavior, or comprehension over labels such as “not SOLID”.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, pattern inventories, or long examples back into this file.
