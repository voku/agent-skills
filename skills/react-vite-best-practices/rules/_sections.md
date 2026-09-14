# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Essential for production performance & caching | Always |
| HIGH | Key patterns for development speed and assets | Most projects |
| MEDIUM | Governance, bundle budgeting, and security | When scaling |

## Section Overview

### 1. Build Optimization (`build`)
- **Impact:** CRITICAL
- **Rules:** `build-production-tuning`
- **Description:** Vite build configuration for production: manual vendor chunking, modern target selection (`baseline-widely-available`), tree shaking, compression (Gzip/Brotli), and secure sourcemap handling.

### 2. Code Splitting (`split`)
- **Impact:** CRITICAL
- **Rules:** `code-splitting-lazy`
- **Description:** Route and component level code splitting with `React.lazy()` and granular `<Suspense>` boundaries, dynamic `import()` for heavy client libraries, and link/idle chunk prefetching.

### 3. Development Server (`dev`)
- **Impact:** HIGH
- **Rules:** `dev-server-fast-refresh`
- **Description:** Vite development server tuning, dependency pre-bundling with `optimizeDeps`, server warmup, and component structure constraints for reliable Fast Refresh.

### 4. Asset Handling (`asset`)
- **Impact:** HIGH
- **Rules:** `asset-pipeline-optimization`
- **Description:** Static asset pipeline: ESM asset imports with automated hashing, SVGR icon components, preloaded self-hosted fonts, modern image formats (`<picture>` with AVIF/WebP), and `/public` directory separation.

### 5. Environment Config (`env`)
- **Impact:** HIGH
- **Rules:** `env-management-security`
- **Description:** Strongly-typed environment variables via `src/vite-env.d.ts`, `VITE_` prefix enforcement, mode file cascading, and zero client-side secret exposure.

### 6. Bundle Analysis (`bundle`)
- **Impact:** MEDIUM
- **Rules:** `bundle-analysis-budget`
- **Description:** Bundle inspection and auditing with `rollup-plugin-visualizer`, chunk size budgets (`chunkSizeWarningLimit`), and eliminating legacy bloated dependencies.
