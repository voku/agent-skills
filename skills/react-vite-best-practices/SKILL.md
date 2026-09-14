---
name: react-vite-best-practices
description: React and Vite performance optimization guidelines. Use when writing, reviewing, or optimizing React components built with Vite. Triggers on tasks involving Vite configuration, build optimization, code splitting, lazy loading, HMR, bundle size, or React performance.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# React + Vite Best Practices

Curated, high-density performance optimization guide for React applications built with Vite. Focuses on production build tuning, route/component code splitting, dev server Fast Refresh, static asset pipelines, type-safe environments, and bundle budgeting.

## Quick Reference

| Category | Impact | Rule File | Primary Focus |
|----------|--------|-----------|---------------|
| **Build Optimization** | CRITICAL | [`build-production-tuning`](rules/build-production-tuning.md) | Manual chunks, modern targets (`baseline-widely-available`), tree shaking, Brotli/Gzip compression |
| **Code Splitting** | CRITICAL | [`code-splitting-lazy`](rules/code-splitting-lazy.md) | `React.lazy()`, granular `<Suspense>` skeletons, dynamic `import()`, intent/idle prefetching |
| **Development** | HIGH | [`dev-server-fast-refresh`](rules/dev-server-fast-refresh.md) | `optimizeDeps.include`, server warmup, pure component files for reliable Fast Refresh |
| **Asset Handling** | HIGH | [`asset-pipeline-optimization`](rules/asset-pipeline-optimization.md) | ESM imports, SVGR icons, self-hosted font preloading, AVIF/WebP pictures, `/public` separation |
| **Environment Config** | HIGH | [`env-management-security`](rules/env-management-security.md) | Strongly-typed `vite-env.d.ts`, `VITE_` prefix enforcement, zero client-secret leakage |
| **Bundle Analysis** | MEDIUM | [`bundle-analysis-budget`](rules/bundle-analysis-budget.md) | `rollup-plugin-visualizer`, chunk size limits, eliminating legacy package bloat |

## Core Configuration Reference

### Production Vite Configuration (`vite.config.ts`)

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import compression from 'vite-plugin-compression';
import svgr from 'vite-plugin-svgr';
import path from 'path';

export default defineConfig({
  plugins: [
    react(),
    svgr({ svgrOptions: { icon: true } }),
    compression({ algorithm: 'brotliCompress', ext: '.br' }),
  ],
  resolve: {
    alias: { '@': path.resolve(__dirname, './src') },
  },
  build: {
    target: 'baseline-widely-available',
    sourcemap: 'hidden',
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react') || id.includes('react-dom')) return 'vendor-react';
            if (id.includes('@tanstack') || id.includes('zustand')) return 'vendor-core';
            return 'vendor-libs';
          }
        },
      },
    },
  },
  optimizeDeps: {
    include: ['react', 'react-dom', 'react-router-dom', '@tanstack/react-query', 'zustand'],
  },
});
```
