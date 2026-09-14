---
id: config-theme-extension
title: Tailwind v3 Theme Configuration and Extension
category: config
priority: HIGH
triggers: [accidental-palette-override, hardcoded-hex-in-classes, missing-theme-extend]
tags: [tailwind, config, tailwind-config-js, theme-extend, colors, typography]
---

# Tailwind v3 Theme Configuration and Extension

**Trigger Anchor:** Extend Tailwind v3 themes within `theme.extend` rather than overriding root objects, define semantic color scales via CSS variables, and provide system fallbacks for custom font families.

---

### Bad
```js
// ❌ Accidental wipeout: defining colors directly under `theme` deletes all default Tailwind colors!
module.exports = {
  theme: {
    colors: {
      brand: '#3b82f6', // Wipes out white, black, red, gray, etc.!
    },
  },
};
```

### Good
```js
// tailwind.config.js (v3.4+)
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./resources/**/*.{blade.php,js,jsx,ts,tsx}', './index.html'],
  darkMode: 'class',
  theme: {
    extend: {
      // ✅ Safely adds custom semantic tokens while preserving default palette
      colors: {
        brand: {
          50: '#eef2ff',
          500: '#6366f1',
          600: '#4f46e5',
          900: '#312e81',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      borderRadius: {
        '4xl': '2rem',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/container-queries'),
  ],
};
```
