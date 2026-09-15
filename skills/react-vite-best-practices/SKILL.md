---
name: react-vite-best-practices
description: React and Vite performance optimization guidelines. Use when writing, reviewing, or optimizing React components built with Vite. Triggers on tasks involving Vite configuration, build optimization, code splitting, lazy loading, HMR, bundle size, assets, or environment exposure.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# React + Vite Best Practices

Portable performance guidance for React applications built with Vite. The detailed owner rules cover production builds, code splitting, development-server behavior, assets, environment exposure, and bundle analysis.

## Grounding and Ownership

Before changing configuration or adding dependencies, inspect the target repository's `package.json`, Vite config, routes/components, existing plugins, browser/support target, deployment pipeline, and current build or bundle evidence.

- The target repository owns installed React/Vite versions, plugins, browser support, aliases, routing, hosting/CDN behavior, compression strategy, environment names, and validation commands.
- React and Vite upstream own version-sensitive framework and build-tool behavior.
- This skill owns portable review heuristics and decision boundaries, not a universal `vite.config.ts` template.
- Do not add compression, SVGR, bundle-visualizer, pre-bundling entries, manual chunks, or other dependencies/configuration merely because an example exists in a rule. Establish the repository need first.
- Never treat `VITE_` variables as a secret boundary; anything exposed to client code must be safe to ship to the browser.

## When to Apply

Use this skill when:
- build output or initial-load size needs investigation;
- route/component loading should be split or deferred;
- Vite development startup or Fast Refresh behavior is problematic;
- asset delivery needs optimization;
- environment variables or client-side configuration need review;
- bundle composition needs measurement and a budget.

## Canonical Rule Boundaries

### Production Build
- [build-production-tuning.md](rules/build-production-tuning.md) — production build tuning, targets, chunks, sourcemaps, tree shaking, and compression decisions.

### Code Splitting
- [code-splitting-lazy.md](rules/code-splitting-lazy.md) — route/component lazy loading, Suspense boundaries, dynamic imports, and prefetching.

### Development Server
- [dev-server-fast-refresh.md](rules/dev-server-fast-refresh.md) — Fast Refresh boundaries, dependency pre-bundling, and server warmup.

### Asset Pipeline
- [asset-pipeline-optimization.md](rules/asset-pipeline-optimization.md) — imported/public assets, images, SVGs, and fonts.

### Environment Security
- [env-management-security.md](rules/env-management-security.md) — typed environment variables, modes, `VITE_` exposure, and secret boundaries.

### Bundle Analysis
- [bundle-analysis-budget.md](rules/bundle-analysis-budget.md) — bundle inspection, dependency weight, chunk budgets, and regression evidence.

## Decision Discipline

1. Establish the observed problem and the repository's current configuration.
2. Load only the rule files relevant to that problem.
3. Prefer the smallest change supported by measurements or concrete repository evidence.
4. Avoid cargo-cult configuration and new plugin dependencies without a demonstrated need.
5. Validate with the repository's configured build, tests, type checking, and relevant bundle/performance evidence.

`README.md`, `AGENTS.md`, and `metadata.json` are supporting projections. If they disagree with this file or `rules/`, follow the canonical source and repair the projection.
