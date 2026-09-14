---
id: dev-server-fast-refresh
title: "Fast Refresh Component Boundaries and Dev Pre-Bundling in Vite"
category: dev
priority: HIGH
triggers: [vite-hmr-slow, fast-refresh-lost-state, optimize-deps-config, dev-server-warmup]
tags: [vite, fast-refresh, hmr, optimize-deps, dev-server]
---

# Fast Refresh Component Boundaries and Dev Pre-Bundling in Vite

**Trigger Anchor:** Preserve React state across HMR edits by enforcing single-component files with PascalCase default/named exports, and configure `optimizeDeps.include` with `server.warmup` for instant cold starts.

---

### Bad
```tsx
// ❌ Multiple components mixed with constants and anonymous exports break Fast Refresh
export const MAX_RETRY_COUNT = 3; // Mixed non-component export forces full-page reload on edit
export function formatCurrency(v: number) { return `$${v.toFixed(2)}`; }

export default () => { // Anonymous component cannot be tracked across HMR cycles
  return <div>Unnamed Component</div>;
};

export const UserCard = () => <div>Card</div>; // Multiple components in one file trigger full re-mount
```

### Good
```typescript
// ✅ vite.config.ts: Pre-bundle CommonJS/heavy dependencies and warmup critical paths
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    include: [
      'react',
      'react-dom',
      'react-router-dom',
      '@tanstack/react-query',
      'zustand',
      'axios',
    ],
    // Force esbuild to recognize globalThis for legacy CommonJS wrappers
    esbuildOptions: {
      define: { global: 'globalThis' },
    },
  },
  server: {
    port: 3000,
    hmr: { overlay: true }, // Display compile error overlay in browser without dropping state
    warmup: {
      clientFiles: ['./src/main.tsx', './src/App.tsx', './src/routes.tsx'],
    },
  },
});
```

```tsx
// ✅ src/components/UserCard.tsx: Isolated component file preserving state across edits
import { useState } from 'react';

// Extract helpers and constants to separate files (e.g. src/utils/format.ts)
export default function UserCard({ name, initialScore }: { name: string; initialScore: number }) {
  const [score, setScore] = useState(initialScore);

  return (
    <div className="rounded-lg border p-4">
      <h3 className="font-bold">{name}</h3>
      <p>Score: {score}</p>
      <button onClick={() => setScore((s) => s + 1)} className="btn-sm">Increment</button>
    </div>
  );
}
```
