---
id: responsive-layout-systems
title: Mobile-First Responsive Breakpoints, Grids, and Container Queries
category: responsive
priority: CRITICAL
triggers: [desktop-first-anti-pattern, broken-mobile-layout, un-responsive-grid, container-query-needed]
tags: [tailwind, css, responsive, mobile-first, grid, flex, container-queries]
---

# Mobile-First Responsive Breakpoints, Grids, and Container Queries

**Trigger Anchor:** Build mobile-first layouts using unprefixed base classes for small screens, progressive breakpoint prefixes (`sm:`, `md:`, `lg:`, `xl:`), responsive CSS Grid (`grid-cols-1 md:grid-cols-3`), and container queries (`@container` / `@lg:grid-cols-2`) for modular widgets.

---

### Bad
```html
<!-- ❌ Desktop-first mindset with awkward overrides and fixed pixel dimensions -->
<div class="w-[1200px] flex flex-row sm:flex-col">
  <!-- Breaks on mobile screens under 1200px; backwards breakpoint thinking -->
  <div class="w-[400px]">Sidebar</div>
  <div class="w-[800px]">Main Content</div>
</div>
```

### Good
```html
<!-- ✅ Mobile-first: 1 column on mobile, scales to 3 columns on desktop -->
<div class="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid grid-cols-1 gap-6 md:grid-cols-12">
    <!-- Sidebar: full-width mobile, 4-cols desktop -->
    <aside class="md:col-span-4 lg:col-span-3">
      <nav class="sticky top-4 space-y-2">...</nav>
    </aside>

    <!-- Main: full-width mobile, 8-cols desktop -->
    <main class="md:col-span-8 lg:col-span-9">
      <!-- ✅ Container Query widget: responds to card width, not viewport width -->
      <section class="@container">
        <div class="grid grid-cols-1 @md:grid-cols-2 @xl:grid-cols-3 gap-4">
          <!-- Widget Cards -->
        </div>
      </section>
    </main>
  </div>
</div>
```

### Breakpoint Order
- Base: Unprefixed (0px - 639px, mobile phones)
- `sm:`: >= 640px (tablets / large phones)
- `md:`: >= 768px (tablets landscape)
- `lg:`: >= 1024px (laptops / desktops)
- `xl:`: >= 1280px (large screens)
