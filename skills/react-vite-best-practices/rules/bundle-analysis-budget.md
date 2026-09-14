---
id: bundle-analysis-budget
title: "Bundle Inspection, Size Budgeting, and Bloat Prevention"
category: bundle
priority: MEDIUM
triggers: [bundle-analysis, rollup-plugin-visualizer, chunk-size-warning, lodash-moment-bloat]
tags: [vite, bundle-size, visualizer, rollup, performance, budget]
---

# Bundle Inspection, Size Budgeting, and Bloat Prevention

**Trigger Anchor:** Integrate `rollup-plugin-visualizer` into build tooling to audit vendor chunk sizes, set `chunkSizeWarningLimit`, and eliminate bloated legacy packages in favor of modern lightweight equivalents.

---

### Bad
```typescript
// ❌ Bloated legacy package imports pull entire multi-megabyte bundles into the client
import _ from 'lodash'; // ❌ Pulls entire lodash library instead of tree-shaken methods
import moment from 'moment'; // ❌ Massive locale files and mutable date structures

export function formatEvent(date: Date, tags: string[]) {
  const formattedDate = moment(date).format('MMMM Do YYYY');
  const uniqueTags = _.uniq(tags);
  return { formattedDate, uniqueTags };
}
```

### Good
```typescript
// ✅ vite.config.ts: Visualizer enabled conditionally for bundle auditing
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    process.env.ANALYZE === 'true' &&
      visualizer({
        open: true,
        filename: 'dist/stats.html',
        gzipSize: true,
        brotliSize: true,
      }),
  ],
  build: {
    chunkSizeWarningLimit: 500, // Warn during build if any single chunk exceeds 500kB
  },
});
```

```typescript
// ✅ Lean, tree-shakeable native / modern alternatives
import { format } from 'date-fns'; // Or native Intl.DateTimeFormat

export function formatEvent(date: Date, tags: string[]) {
  // Use native Date formatting and native Set for unique values
  const formattedDate = format(date, 'MMMM d, yyyy');
  const uniqueTags = Array.from(new Set(tags));
  return { formattedDate, uniqueTags };
}
```
