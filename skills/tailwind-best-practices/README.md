# Tailwind CSS Best Practices

Portable guidance for responsive layouts, dark mode, component class composition, Tailwind v3 theme extension, and Tailwind v4 CSS-first architecture.

## Canonical Source

`SKILL.md` defines activation and high-level routing. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, framework-version matrix, or compiled example set.

## When to Use

Use this skill for Tailwind responsive design, dark-mode theming, reusable component classes, v3 theme configuration, or v3-to-v4 migration work.

## Routing

1. Inspect the target repository's installed Tailwind version and build/configuration model.
2. Read `SKILL.md` first.
3. Load only the relevant rule files for responsive layouts, dark mode, `cn()`/component composition, v3 theme extension, or v4 CSS-first architecture.
4. Preserve the project's existing design-token and component conventions unless the task explicitly changes them.
5. Keep v3 and v4 configuration models distinct and ground migrations in the target repository.

## Projection Boundary

Do not copy current rule IDs, counts, plugin inventories, or long worked examples into this file. If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection.
