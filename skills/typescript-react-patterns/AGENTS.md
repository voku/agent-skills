# TypeScript React Patterns — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second TypeScript/React rule inventory, count, compatibility table, or compiled example set here.

## Fast Path

1. Inspect the target repository's React and TypeScript versions, compiler options, component conventions, and configured lint/type-check/test commands.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Prefer existing repository conventions when multiple TypeScript representations are equally sound.
4. Use precise React/DOM types and preserve inference where it improves the call-site API.
5. Validate with the repository's configured TypeScript, lint, and test tooling rather than assuming a generic command.

## Ownership Boundary

- `SKILL.md` owns activation and the high-level TypeScript/React contract.
- `rules/` owns detailed component, hook, event, ref, generic, context, and utility-type guidance.
- the target repository owns installed React/TypeScript versions, JSX/runtime mode, compiler/linter policy, component architecture, and validation commands.
- React and TypeScript upstream own version-sensitive type and API behavior.
- this projection owns no independent typing semantics.

## Evidence Boundary

- Do not promote stylistic preferences such as `interface` versus `type` into universal correctness rules when both model the required contract.
- Do not copy legacy React/TypeScript patterns merely because they appeared in an older compiled guide.
- Prefer compiler evidence and the actual target API over casts or manually duplicated types.
- Treat polymorphic components, refs, and context helpers as design choices that must fit the repository rather than mandatory abstractions.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, framework versions, or long examples back into this file.
