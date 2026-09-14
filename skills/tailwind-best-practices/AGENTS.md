# Tailwind CSS Best Practices — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second Tailwind rule inventory, count, version matrix, or compiled example set here.

## Fast Path

1. Inspect the target repository's Tailwind version, config/CSS entrypoints, build integration, and existing component conventions.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Keep v3 configuration guidance separate from v4 CSS-first guidance; do not mix the two models casually.
4. Prefer the repository's existing component/class-composition convention before introducing `cn()`, CVA, or new helper dependencies.
5. Validate through the target repository's configured build, lint, type-check, and visual/test tooling where available.

## Ownership Boundary

- `SKILL.md` owns activation, supported Tailwind scope, and high-level routing.
- `rules/` owns detailed responsive, dark-mode, component-composition, v3 theme-extension, and v4 CSS-first guidance.
- the target repository owns its installed Tailwind version, plugins, bundler integration, design tokens, component system, and validation commands.
- Tailwind upstream owns version-sensitive directives, configuration semantics, and migration behavior.
- this projection owns no independent styling semantics.

## Evidence Boundary

- Do not apply v3 `tailwind.config.js` guidance to a v4 CSS-first project without repository evidence.
- Do not delete configuration files or migrate directives merely because v4 exists; migration must be part of the task and supported by the target setup.
- Do not invent design tokens or component variants when the project already has an established system.
- Prefer observable layout/theme behavior and repository tooling over copied framework recipes.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs and counts belong to the canonical surfaces, not here.
