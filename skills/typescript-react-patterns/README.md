# TypeScript React Patterns

Portable type-safety guidance for modern React applications written in TypeScript.

## Canonical Source

`SKILL.md` defines activation and the high-level contract. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, compatibility table, or compiled example set.

## When to Use

Use this skill when typing component props, hooks, DOM events, refs, generic components, React Context, or discriminated UI state.

## Routing

1. Inspect the target repository's React/TypeScript versions and compiler/linter conventions.
2. Read `SKILL.md` first.
3. Load only the canonical rule files relevant to the current typing problem.
4. Preserve useful inference and reuse existing repository types where possible.
5. Verify with the repository's configured TypeScript/lint/test tooling.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, framework versions, or long examples into this file.
