---
id: asset-pipeline-optimization
title: "Static Asset Pipeline: ESM Imports, SVGs, Fonts, and Public Directory"
category: asset
priority: HIGH
triggers: [vite-asset-handling, svg-as-component, web-font-loading, public-vs-assets-import, image-optimization]
tags: [vite, assets, svg, fonts, images, public-dir]
---

# Static Asset Pipeline: ESM Imports, SVGs, Fonts, and Public Directory

**Trigger Anchor:** Import static assets via ESM for hashing and build processing, use `@svgr/rollup` or SVG sprite symbols instead of raw inline SVGs, and preload self-hosted WOFF2 fonts while keeping unreferenced root files in `/public`.

---

### Bad
```tsx
// ❌ Unhashed public assets, render-blocking web fonts, and inlined SVG monstrosities
export function BadHeader() {
  return (
    <header>
      {/* Absolute path to /public bypasses Vite bundler: no cache-busting hash on deploy */}
      <img src="/images/hero-banner.png" alt="Hero" />

      {/* Massive inline SVG path bloats TSX bundle and re-parses on every re-render */}
      <svg viewBox="0 0 24 24" className="h-6 w-6">
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" fill="currentColor" />
      </svg>

      {/* External CSS @import blocks initial render */}
      <style>{`@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');`}</style>
    </header>
  );
}
```

### Good
```typescript
// ✅ vite.config.ts: SVGR configuration for icon components
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import svgr from 'vite-plugin-svgr';

export default defineConfig({
  plugins: [
    react(),
    svgr({
      svgrOptions: { icon: true }, // Scales SVG to 1em by default
    }),
  ],
});
```

```html
<!-- ✅ index.html: Preload critical self-hosted font to eliminate Flash of Unstyled Text (FOUT) -->
<head>
  <link rel="preload" href="/fonts/inter-latin-400.woff2" as="font" type="font/woff2" crossorigin />
</head>
```

```tsx
// ✅ src/components/Header.tsx: ESM asset imports with automated hashing & modern image formats
import heroAvif from '@/assets/images/hero-banner.avif';
import heroWebp from '@/assets/images/hero-banner.webp';
import heroPng from '@/assets/images/hero-banner.png';
import LogoIcon from '@/assets/icons/logo.svg?react'; // Transformed into lightweight SVG component

export function Header() {
  return (
    <header className="flex items-center justify-between p-4">
      <LogoIcon className="h-8 w-8 text-indigo-600" aria-label="Company Logo" />

      {/* Responsive modern image format fallback with lazy loading */}
      <picture>
        <source srcSet={heroAvif} type="image/avif" />
        <source srcSet={heroWebp} type="image/webp" />
        <img
          src={heroPng}
          alt="Hero"
          loading="lazy"
          decoding="async"
          width={800}
          height={400}
          className="rounded-lg object-cover"
        />
      </picture>
    </header>
  );
}
```
