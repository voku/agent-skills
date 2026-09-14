---
id: layout-persistent
title: Persistent Layouts and Page Transitions
category: layout
priority: MEDIUM
triggers: [layout-remount-flicker, lost-sidebar-scroll-state, audio-player-interruption-navigation]
tags: [inertia, react, layouts, persistent-layout, page-transitions]
---

# Persistent Layouts and Page Transitions

**Trigger Anchor:** Define persistent layouts using `Page.layout = (page) => <AppLayout>{page}</AppLayout>` so layout component trees survive page navigation without unmounting or resetting internal state.

---

### Bad
```tsx
// ❌ Wrapping layout inside page component unmounts and remounts layout on every route change!
export default function DashboardPage() {
  return (
    <AppLayout> {/* ❌ Destroys sidebar scroll position and active video/audio players on navigation */}
      <h1>Dashboard Content</h1>
    </AppLayout>
  );
}
```

### Good
```tsx
import type { ReactNode } from 'react';
import { AppLayout } from '@/Layouts/AppLayout';

export default function DashboardPage() {
  return (
    <div className="dashboard-view">
      <h1 className="text-xl font-bold">Dashboard</h1>
      <p>Content updates smoothly without unmounting navigation or sidebars.</p>
    </div>
  );
}

// ✅ Persistent layout pattern: React reconciles layout outside page component subtree
DashboardPage.layout = (page: ReactNode) => <AppLayout title="Dashboard">{page}</AppLayout>;
```

```tsx
// resources/js/app.tsx
// ✅ Or configure automatic default persistent layout in resolve()
createInertiaApp({
  resolve: async (name) => {
    const pages = import.meta.glob('./Pages/**/*.tsx');
    const page = await pages[`./Pages/${name}.tsx`]();
    page.default.layout ??= (page: ReactNode) => <AppLayout>{page}</AppLayout>;
    return page;
  },
  setup({ el, App, props }) {
    createRoot(el).render(<App {...props} />);
  },
});
```
