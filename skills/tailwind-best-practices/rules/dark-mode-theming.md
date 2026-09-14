---
id: dark-mode-theming
title: "Dark Mode Theming: Dual-Palette Tokens and Transitions"
category: dark
priority: CRITICAL
triggers: [missing-dark-mode-contrast, un-styled-dark-mode, jarring-theme-switch, hardcoded-black-white]
tags: [tailwind, dark-mode, theming, color-palette, accessibility, transitions]
---

# Dark Mode Theming: Dual-Palette Tokens and Transitions

**Trigger Anchor:** Pair light and dark variants on every surface (`bg-white dark:bg-zinc-900 text-zinc-900 dark:text-zinc-100`), avoid harsh pure `#000` blacks, use soft zinc/slate backgrounds, and apply smooth color transitions (`transition-colors duration-200`).

---

### Bad
```html
<!-- ❌ Hardcoded pure black, blinding white contrast, missing dark borders -->
<div class="bg-white dark:bg-black text-black dark:text-white p-6 border border-gray-200">
  <!-- Missing dark:border-*, text contrast becomes harsh and unreadable -->
  <button class="bg-blue-600 text-white">Click Me</button>
</div>
```

### Good
```html
<!-- ✅ Balanced neutral tones (zinc-900/zinc-800), muted text, and styled borders -->
<div class="bg-white dark:bg-zinc-900 text-zinc-900 dark:text-zinc-100 border border-zinc-200 dark:border-zinc-800 rounded-xl p-6 shadow-sm transition-colors duration-200">
  <h2 class="text-lg font-semibold text-zinc-900 dark:text-zinc-50">Account Overview</h2>
  <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">Manage your team and billing profile.</p>

  <div class="mt-4 flex items-center gap-3">
    <button class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-sm font-medium transition-colors">
      Upgrade Plan
    </button>
    <button class="px-4 py-2 bg-zinc-100 hover:bg-zinc-200 dark:bg-zinc-800 dark:hover:bg-zinc-700 text-zinc-700 dark:text-zinc-200 rounded-lg text-sm font-medium transition-colors">
      Cancel
    </button>
  </div>
</div>
```

### Strategy Configuration
- **Tailwind v3 (`tailwind.config.js`):** `darkMode: 'class'` or `darkMode: 'selector'`
- **Tailwind v4 (CSS):** Class-based by default; toggled via `<html class="dark">`
