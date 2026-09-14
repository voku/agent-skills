# Laravel + Inertia.js + React — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent rule inventory, version table, dependency matrix, or compiled copy of examples here.

## Fast Path

1. Ground the target repository's Laravel, Inertia, React, TypeScript, Ziggy, and PHP versions before recommending version-sensitive behavior.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the current task.
3. Keep page props/reloads, form lifecycle, navigation, shared props, and persistent layouts in their owning rule boundaries.
4. Prefer target-repository types, routes, middleware, and configured validation commands over generic examples.
5. Report only validation and runtime behavior that was actually observed.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed Laravel/Inertia/React guidance and examples.
- the target repository owns installed versions, page/component types, route names, middleware shape, application contracts, and validation commands.
- upstream Laravel/Inertia/React/Ziggy documentation owns version-sensitive framework behavior.
- this projection owns no independent integration semantics.

## Evidence Boundary

- Verify page props and shared props in source before asserting their shape.
- Verify installed package versions before using a specific Inertia or React API.
- Preserve server-side validation and authorization boundaries when changing client form behavior.
- Do not infer route names or Ziggy availability from examples.
- Persistent layouts and state-preservation options are behavioral choices; use them only where the target flow requires them.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs, counts, dependency tables, and framework-version matrices do not belong here.
