# React + Vite Best Practices — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second React/Vite rule inventory, count, plugin matrix, or compiled `vite.config.ts` here.

## Fast Path

1. Inspect `package.json`, the Vite config, routes/components, existing plugins, browser target, deployment setup, and current build evidence.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Start from a concrete performance, loading, development, asset, environment, or bundle problem rather than applying a generic optimization template.
4. Prefer existing project conventions and dependencies before introducing new plugins or configuration.
5. Validate with the repository's configured build, tests, type checks, and relevant bundle/performance evidence.

## Ownership Boundary

- `SKILL.md` owns activation, grounding, and the high-level decision contract.
- `rules/` owns detailed build, code-splitting, dev-server, asset, environment, and bundle guidance.
- the target repository owns installed versions, dependencies, browser support, aliases, routing, hosting, compression, environment names, and validation commands.
- React/Vite upstream owns version-sensitive APIs and build behavior.
- this projection owns no independent React/Vite semantics.

## Evidence and Security Boundary

- Do not add `vite-plugin-compression`, SVGR, bundle visualizers, manual chunks, `optimizeDeps` entries, or other dependencies/configuration without repository evidence that they solve the current problem.
- Do not copy a fixed vendor-chunk map into projects with different dependency graphs.
- Treat client-exposed environment values as public; never place secrets behind a `VITE_` prefix.
- Prefer measured bundle/build/runtime evidence over generic percentage claims or copied thresholds.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, tool versions, or long examples back into this file.
