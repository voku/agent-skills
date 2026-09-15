# Clean Code Principles

Portable software-design guidance for SOLID, DRY, KISS, YAGNI, separation of concerns, composition, Law of Demeter, fail-fast behavior, encapsulation, and an appropriate repository boundary.

## Canonical Source

`SKILL.md` defines activation, rule routing, and high-level decision discipline. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, pattern catalog, or compiled example set.

## When to Use

Use this skill for architecture review, refactoring, code-quality discussions, coupling/change-pressure analysis, or evaluating whether an abstraction is justified.

## Routing

1. Ground the target repository's architecture and conventions.
2. Read `SKILL.md` first.
3. Load only the canonical rules relevant to the observed problem.
4. Prefer the smallest design improvement supported by evidence.
5. Validate with repository tests and configured analysis tooling.

## Decision Boundary

Clean-code principles are heuristics, not a demand to add interfaces, layers, patterns, or abstractions. Report the concrete problem first and the principle second.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, pattern inventories, or long examples into this file.
