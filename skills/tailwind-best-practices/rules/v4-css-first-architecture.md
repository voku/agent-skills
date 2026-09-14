---
id: v4-css-first-architecture
title: "Tailwind v4 CSS-First Architecture, @theme, and Migration"
category: v4
priority: HIGH
triggers: [tailwind-v4-config-error, missing-at-theme-directive, v3-to-v4-migration-gap, custom-utility-at-utility]
tags: [tailwind-v4, css-first, at-theme, at-utility, vite-plugin, migration]
---

# Tailwind v4 CSS-First Architecture, @theme, and Migration

**Trigger Anchor:** Configure Tailwind v4 natively in CSS using `@theme`, `@utility`, and `@variant` directives, install via `@tailwindcss/vite` or `@tailwindcss/postcss`, and discard JS configuration files (`tailwind.config.js`).

---

### Bad
```js
// ❌ Using legacy tailwind.config.js and @tailwind directives in Tailwind v4
// main.css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Good
```css
/* resources/css/app.css (Tailwind v4) */
@import "tailwindcss";

/* ✅ CSS-first theme configuration replaces tailwind.config.js */
@theme {
  --color-brand-50: oklch(0.97 0.02 260);
  --color-brand-500: oklch(0.62 0.21 260);
  --color-brand-900: oklch(0.32 0.16 260);

  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  --breakpoint-3xl: 1920px;
}

/* ✅ Custom utility definition using @utility directive */
@utility content-auto {
  content-visibility: auto;
}

/* ✅ Custom variant definition */
@custom-variant pointer-fine (@media (pointer: fine));
```

### Setup with Vite
```ts
// vite.config.ts
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
});
```

### v3 → v4 Upgrade Steps
1. Run automated upgrade tool: `npx @tailwindcss/upgrade@next`
2. Remove `tailwind.config.js` and `postcss.config.js` (unless non-Tailwind PostCSS plugins exist).
3. Replace `@tailwind` directives in CSS with `@import "tailwindcss";`.
4. Migrate JS extensions into `@theme { ... }` CSS custom properties.
