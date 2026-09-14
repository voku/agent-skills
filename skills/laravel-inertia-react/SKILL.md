---
name: laravel-inertia-react
description: Laravel + Inertia.js + React integration patterns. 5 rules across 5 categories covering page props, useForm lifecycle, Link & router navigation, shared middleware props, and persistent layouts. Triggers on tasks involving Inertia.js, page props, form handling, or Laravel React integration.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel + Inertia.js + React

Full-stack integration patterns for building reactive monoliths with Laravel, Inertia.js (v1/v2), and React. Contains **5 consolidated rules across 5 categories** covering page typing and partial reloads, form handling with `useForm`, client routing, global shared props, and persistent layouts.

## Metadata

- **Version:** 2.0.0
- **Framework:** Laravel 11.x - 13.x + Inertia.js React
- **Rule Count:** 5 rules across 5 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Creating and typing Inertia page components (`PageProps<T>`)
- Implementing forms, file uploads, and progress bars with `useForm`
- Managing client-side navigation with `<Link>` and `router.visit()`
- Sharing global state (auth user, flash messages) via middleware
- Implementing persistent layouts to preserve state during navigation

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Page Components | CRITICAL | `page-` | 1 |
| 2 | Forms & Validation | CRITICAL | `form-` | 1 |
| 3 | Navigation & Routing | HIGH | `nav-` | 1 |
| 4 | Shared Data | HIGH | `shared-` | 1 |
| 5 | Layouts | MEDIUM | `layout-` | 1 |

## Quick Reference

### 1. Page Components (CRITICAL) — 1 rule
- [page-props-reloads.md](rules/page-props-reloads.md) - Strongly type Inertia page props with `PageProps<T>`, manage title and SEO metadata with `<Head>`, and optimize filtering/pagination with partial reloads (`only: ['users']`) and scroll preservation (`preserveScroll: true`).

### 2. Forms & Validation (CRITICAL) — 1 rule
- [form-useform-lifecycle.md](rules/form-useform-lifecycle.md) - Manage forms via Inertia's `useForm<T>()` hook, bind Laravel validation errors per field (`errors.field`), disable submit buttons during `processing`, and track file upload progress (`progress.percentage`).

### 3. Navigation & Routing (HIGH) — 1 rule
- [nav-link-router.md](rules/nav-link-router.md) - Use `<Link>` for internal SPA transitions, reserve standard `<a href="...">` for external URLs or file downloads, use `router.visit()` for programmatic navigation, and pass `preserveState: true` on query/filter updates.

### 4. Shared Data (HIGH) — 1 rule
- [shared-props-middleware.md](rules/shared-props-middleware.md) - Centralize global application state (authenticated user, flash messages, Ziggy routes) in `HandleInertiaRequests::share()`, and access them type-safely via `usePage<PageProps>()`.

### 5. Layouts (MEDIUM) — 1 rule
- [layout-persistent.md](rules/layout-persistent.md) - Define persistent layouts using `Page.layout = (page) => <AppLayout>{page}</AppLayout>` so layout component trees survive page navigation without unmounting or resetting internal state.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete Inertia React examples.
