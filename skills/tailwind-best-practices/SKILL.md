---
name: tailwind-best-practices
description: Tailwind CSS patterns and conventions for v3 and v4. 5 rules across 5 categories covering responsive layouts, dark mode, component class merging with cn(), v3 config, and v4 CSS-first architecture. Use when writing responsive designs, implementing dark mode, creating reusable component styles, configuring Tailwind, or migrating from v3 to v4. Triggers on tasks involving Tailwind classes, responsive design, dark mode, CSS styling, or "migrate to Tailwind v4".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
  tailwindVersion: "3.4+ / 4.0+"
---

# Tailwind CSS Best Practices

Modern styling patterns for Tailwind CSS v3.4+ and v4.x. Contains **5 consolidated rules across 5 categories** covering responsive mobile-first layouts, balanced dark mode theming, component class composition with `cn()`, v3 theme extensions, and v4 CSS-first architecture.

## Metadata

- **Version:** 2.0.0
- **Framework:** Tailwind CSS v3.4+ / v4.0+
- **Rule Count:** 5 rules across 5 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Designing mobile-first responsive grids and container queries
- Implementing dark mode theming with dual-palette tokens
- Building reusable UI components using `cn()` and CVA
- Configuring or extending themes in `tailwind.config.js` (v3)
- Setting up or migrating to Tailwind CSS v4 with `@theme`

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Version | Rules |
|----------|----------|--------|--------|---------|-------|
| 1 | Responsive Design | CRITICAL | `responsive-` | v3 / v4 | 1 |
| 2 | Dark Mode | CRITICAL | `dark-` | v3 / v4 | 1 |
| 3 | Component Patterns | HIGH | `component-` | v3 / v4 | 1 |
| 4 | Theme Configuration (v3) | HIGH | `config-` | v3 | 1 |
| 5 | V4 & Migration | HIGH | `v4-` | v4 only | 1 |

## Quick Reference

### 1. Responsive Design (CRITICAL) — 1 rule
- [responsive-layout-systems.md](rules/responsive-layout-systems.md) - Build mobile-first layouts using unprefixed base classes for small screens, progressive breakpoint prefixes (`sm:`, `md:`, `lg:`, `xl:`), responsive CSS Grid (`grid-cols-1 md:grid-cols-3`), and container queries (`@container` / `@lg:grid-cols-2`) for modular widgets.

### 2. Dark Mode (CRITICAL) — 1 rule
- [dark-mode-theming.md](rules/dark-mode-theming.md) - Pair light and dark variants on every surface (`bg-white dark:bg-zinc-900 text-zinc-900 dark:text-zinc-100`), avoid harsh pure `#000` blacks, use soft zinc/slate backgrounds, and apply smooth color transitions (`transition-colors duration-200`).

### 3. Component Patterns (HIGH) — 1 rule
- [component-patterns-cn.md](rules/component-patterns-cn.md) - Combine conditional classes using `cn()` (`clsx` + `tailwind-merge`) to resolve utility precedence conflicts, and manage component variants with Class Variance Authority (CVA).

### 4. Theme Configuration (v3) (HIGH) — 1 rule
- [config-theme-extension.md](rules/config-theme-extension.md) - Extend Tailwind v3 themes within `theme.extend` rather than overriding root objects, define semantic color scales via CSS variables, and provide system fallbacks for custom font families.

### 5. V4 & Migration (HIGH) — 1 rule
- [v4-css-first-architecture.md](rules/v4-css-first-architecture.md) - Configure Tailwind v4 natively in CSS using `@theme`, `@utility`, and `@variant` directives, install via `@tailwindcss/vite` or `@tailwindcss/postcss`, and discard JS configuration files (`tailwind.config.js`).

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete Tailwind idioms.
