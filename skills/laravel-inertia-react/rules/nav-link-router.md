---
id: nav-link-router
title: "Navigation: The Link Component and Programmatic Router"
category: nav
priority: HIGH
triggers: [full-page-reload-link, missing-preserve-state, external-link-inertia-trapped, noisy-history-stack]
tags: [inertia, react, navigation, link, router, preserve-state, replace]
---

# Navigation: The Link Component and Programmatic Router

**Trigger Anchor:** Use `<Link>` for internal SPA transitions, reserve standard `<a href="...">` for external URLs or file downloads, use `router.visit()` for programmatic navigation, and pass `preserveState: true` on query/filter updates.

---

### Bad
```tsx
// ❌ Using standard <a> tags for internal links causes full browser reloads
// ❌ Using <Link> for external URLs traps requests inside Inertia client router
export function Header() {
  return (
    <nav>
      {/* ❌ Causes full browser refresh, losing React state */}
      <a href="/dashboard">Dashboard</a>

      {/* ❌ Traps external navigation inside Inertia XHR request */}
      <Link href="https://stripe.com">Billing Portal</Link>
    </nav>
  );
}
```

### Good
```tsx
import { Link, router } from '@inertiajs/react';

export function NavigationBar() {
  const handleSearchChange = (query: string) => {
    // ✅ Programmatic navigation with state preservation and history replacement
    router.get(
      '/search',
      { q: query },
      {
        preserveState: true,
        preserveScroll: true,
        replace: true, // Prevents cluttering browser back button on every keystroke
      },
    );
  };

  return (
    <header className="flex items-center justify-between p-4">
      {/* ✅ Internal SPA navigation */}
      <Link
        href="/dashboard"
        className="nav-link"
        prefetch // Inertia v2+ prefetching on hover
      >
        Dashboard
      </Link>

      {/* ✅ Standard anchor for external URLs or direct downloads */}
      <a href="/invoices/export" download className="nav-link">
        Download CSV
      </a>

      {/* ✅ Method-override button link for logout */}
      <Link
        href="/logout"
        method="post"
        as="button"
        className="btn btn--danger"
      >
        Log Out
      </Link>
    </header>
  );
}
```
