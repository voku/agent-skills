---
id: build-production-tuning
title: "Production Build Tuning: Manual Chunks, Modern Targets, and Compression"
category: build
priority: CRITICAL
triggers: [vite-build-optimization, manual-chunks-config, bundle-too-large-warning, modern-browser-targets, gzip-brotli-compression]
tags: [vite, build, rollup, manualchunks, treeshaking, compression, sourcemaps]
---

# Production Build Tuning: Manual Chunks, Modern Targets, and Compression

**Trigger Anchor:** Configure manual vendor chunking, modern browser targets (`baseline-widely-available`), tree-shaking friendly ESM imports, and Gzip/Brotli compression in `vite.config.ts`.

---

### Bad
```typescript
// ❌ Monolithic bundle: vendor and app code merged; sourcemaps exposed in prod; legacy target bloat
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    target: 'es5', // Enforces heavy polyfills and legacy helpers
    sourcemap: true, // Leaks complete source code to public production environment
    // No rollup manualChunks: any app change invalidates entire vendor cache
  },
});
```

### Good
```typescript
// ✅ Optimized build: isolated vendor chunks for caching, modern syntax target, and compression
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import compression from 'vite-plugin-compression';
import path from 'path';

export default defineConfig({
  plugins: [
    react(),
    // Generate .gz and .br pre-compressed assets during build
    compression({ algorithm: 'brotliCompress', ext: '.br' }),
    compression({ algorithm: 'gzip', ext: '.gz' }),
  ],
  resolve: {
    alias: { '@': path.resolve(__dirname, './src') },
  },
  build: {
    target: 'baseline-widely-available', // Lean modern JS output
    sourcemap: 'hidden', // Generates sourcemaps for Sentry/error reporting without public sourceMappingURL
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        // Deterministic cache-busting filenames
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react') || id.includes('react-dom') || id.includes('scheduler')) {
              return 'vendor-react';
            }
            if (id.includes('@tanstack') || id.includes('zustand') || id.includes('axios')) {
              return 'vendor-core';
            }
            return 'vendor-libs';
          }
        },
      },
    },
  },
});
```
