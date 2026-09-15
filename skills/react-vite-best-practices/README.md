# React + Vite Best Practices

Portable performance guidance for React applications built with Vite.

## Canonical Source

`SKILL.md` defines activation, grounding, ownership, and decision discipline. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, plugin matrix, or compiled Vite configuration.

## When to Use

Use this skill for production-build tuning, code splitting, Vite development/Fast Refresh issues, asset delivery, environment exposure, or bundle analysis.

## Routing

1. Inspect the target repository's dependencies and Vite configuration.
2. Establish the concrete build/runtime/development problem with observable evidence.
3. Read `SKILL.md` and load only the relevant rule files.
4. Prefer the repository's existing plugins, browser support, deployment, and validation conventions.
5. Add configuration or dependencies only when they solve the demonstrated problem.

## Security Boundary

Client-exposed environment variables are public. Do not put secrets behind `VITE_` or assume a copied Vite example matches the target repository.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, framework/plugin versions, or long examples into this file.
