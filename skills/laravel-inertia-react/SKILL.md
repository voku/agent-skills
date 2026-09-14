---
name: laravel-inertia-react
description: Laravel + Inertia.js + React integration patterns covering page props, useForm lifecycle, Link and router navigation, shared middleware props, and persistent layouts. Triggers on tasks involving Inertia.js, page props, form handling, or Laravel React integration.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel + Inertia.js + React

Full-stack integration patterns for building reactive monoliths with Laravel, Inertia.js, and React.

## When to Apply

Reference these guidelines when:
- Creating and typing Inertia page components (`PageProps<T>`)
- Implementing forms, file uploads, and progress feedback with `useForm`
- Managing client-side navigation with `<Link>` and `router.visit()`
- Sharing global state such as authenticated users or flash messages through middleware
- Implementing persistent layouts to preserve state during navigation

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Page Components | CRITICAL | `page-` |
| 2 | Forms & Validation | CRITICAL | `form-` |
| 3 | Navigation & Routing | HIGH | `nav-` |
| 4 | Shared Data | HIGH | `shared-` |
| 5 | Layouts | MEDIUM | `layout-` |

## Quick Reference

### Page Components
- [page-props-reloads.md](rules/page-props-reloads.md) - Strongly type Inertia page props, manage document metadata, and use partial reload/state preservation deliberately.

### Forms & Validation
- [form-useform-lifecycle.md](rules/form-useform-lifecycle.md) - Manage form state through `useForm`, surface Laravel validation errors, and make processing/upload state explicit.

### Navigation & Routing
- [nav-link-router.md](rules/nav-link-router.md) - Use Inertia navigation for internal transitions, standard links for external/download targets, and explicit router options for state preservation.

### Shared Data
- [shared-props-middleware.md](rules/shared-props-middleware.md) - Keep cross-page props in the Inertia middleware boundary and access them through typed page props.

### Layouts
- [layout-persistent.md](rules/layout-persistent.md) - Use persistent layouts when layout state should survive Inertia page navigation.

## How to Use

Read only the rule files relevant to the current task. Ground version-sensitive Inertia, React, Ziggy, and Laravel behavior in the target repository and upstream documentation. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
