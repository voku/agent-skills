---
id: code-splitting-lazy
title: "Route and Dynamic Component Splitting with Suspense and Intent Prefetching"
category: split
priority: CRITICAL
triggers: [react-code-splitting, lazy-loading-routes, suspense-boundaries, dynamic-import-libraries, prefetch-on-hover]
tags: [react, vite, code-splitting, lazy, suspense, dynamic-import, prefetch]
---

# Route and Dynamic Component Splitting with Suspense and Intent Prefetching

**Trigger Anchor:** Split heavy routes and dynamic components with `React.lazy()` and granular `<Suspense>` boundaries, and trigger chunk prefetching on link hover/focus or browser idle time.

---

### Bad
```tsx
// ❌ Static top-level imports load heavyweight modules into the initial bundle
import React, { useState } from 'react';
import { Chart as ChartJS } from 'chart.js/auto'; // 200kB+ loaded upfront
import MonacoEditor from '@monaco-editor/react'; // 1.5MB+ loaded upfront
import DashboardPage from './pages/Dashboard';
import AnalyticsPage from './pages/Analytics';

export function App() {
  return (
    // Single monolithic Suspense: one slow route stalls entire interface
    <React.Suspense fallback={<div>Loading entire app...</div>}>
      <DashboardPage />
    </React.Suspense>
  );
}
```

### Good
```tsx
// ✅ Lazy route splitting, preloading wrapper, and granular Suspense skeletons
import React, { lazy, Suspense, useCallback, ComponentProps } from 'react';
import { Routes, Route, Link, LinkProps } from 'react-router-dom';

// Factory wrapper enabling programmatic chunk preloading
function lazyWithPreload<T extends React.ComponentType<any>>(
  factory: () => Promise<{ default: T }>
) {
  const Component = lazy(factory);
  (Component as any).preload = factory;
  return Component as typeof Component & { preload: typeof factory };
}

const Dashboard = lazyWithPreload(() => import('./pages/Dashboard'));
const Analytics = lazyWithPreload(() => import('./pages/Analytics'));
const Settings = lazyWithPreload(() => import('./pages/Settings'));

// Link component prefetching chunk on intent signals
export function PrefetchLink({ preload, onMouseEnter, onFocus, ...props }: LinkProps & { preload?: () => Promise<any> }) {
  const handlePreload = useCallback(() => {
    preload?.();
  }, [preload]);

  return (
    <Link
      {...props}
      onMouseEnter={(e) => { handlePreload(); onMouseEnter?.(e); }}
      onFocus={(e) => { handlePreload(); onFocus?.(e); }}
    />
  );
}

// On-demand heavy component loader (e.g. Export PDF dialog)
export function HeavyExportButton() {
  const handleExport = async () => {
    const { jsPDF } = await import('jspdf'); // Dynamic import executed only on click
    const doc = new jsPDF();
    doc.text('Report Export', 10, 10);
    doc.save('report.pdf');
  };

  return <button onClick={handleExport} className="btn-primary">Generate PDF</button>;
}

export function App() {
  return (
    <div className="layout">
      <nav>
        <PrefetchLink to="/dashboard" preload={Dashboard.preload}>Dashboard</PrefetchLink>
        <PrefetchLink to="/analytics" preload={Analytics.preload}>Analytics</PrefetchLink>
      </nav>
      <main>
        <Suspense fallback={<div className="h-64 animate-pulse rounded-lg bg-zinc-100" />}>
          <Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </Suspense>
      </main>
    </div>
  );
}
```
