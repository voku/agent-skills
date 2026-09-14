---
id: core-web-vitals-perf
title: "Core Web Vitals and Performance: LCP, INP, CLS, and Resource Hints"
category: performance
priority: CRITICAL
triggers: [core-web-vitals-audit, lcp-optimization, inp-long-tasks, cls-prevention, font-display-swap]
tags: [seo, performance, cwv, lcp, inp, cls, web-vitals, fonts, images]
---

# Core Web Vitals and Performance: LCP, INP, CLS, and Resource Hints

**Trigger Anchor:** Pass Google Core Web Vitals thresholds: LCP < 2.5s (preload hero + `fetchpriority="high"`), INP < 200ms (yield main thread via `scheduler.yield()`), and CLS < 0.1 (explicit media dimensions and font-display: swap).

---

### Bad
```html
<!-- ❌ Lazy-loading above-the-fold hero image and unreserved dynamic content -->
<head>
  <!-- ❌ Missing preconnect to font origin adds 300ms network handshake latency -->
</head>
<body>
  <!-- ❌ Lazy loading the LCP element causes severe LCP penalties (>4.0s) -->
  <img src="/hero.jpg" loading="lazy" />

  <!-- ❌ Ad container with zero initial height pushes main text down when loaded (CLS > 0.3) -->
  <div id="dynamic-ad-banner"></div>
</body>
```

### Good
```html
<!-- ✅ Fast resource discovery, prioritized hero image, and layout reservation -->
<head>
  <!-- 1. Resource hints for critical third-party origins -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- 2. Preload hero image for instantaneous LCP discovery -->
  <link rel="preload" as="image" href="/images/hero-1200.avif" type="image/avif" fetchpriority="high" />

  <style>
    /* 3. Swap fonts instantly to prevent invisible text (FOIT) */
    @font-face {
      font-family: 'Inter';
      src: url('/fonts/inter.woff2') format('woff2');
      font-display: swap;
    }
  </style>
</head>
<body>
  <header>
    <!-- Above-the-fold LCP image: NO lazy loading, explicit dimensions, high fetch priority -->
    <picture>
      <source srcset="/images/hero-1200.avif" type="image/avif" />
      <source srcset="/images/hero-1200.webp" type="image/webp" />
      <img
        src="/images/hero-1200.jpg"
        alt="Acme Cloud Platform Dashboard"
        width="1200"
        height="600"
        fetchpriority="high"
        decoding="sync"
        class="h-auto w-full object-cover"
      />
    </picture>
  </header>

  <!-- Reserved aspect ratio prevents Cumulative Layout Shift -->
  <div style="min-height: 250px; aspect-ratio: 970 / 250;" class="bg-zinc-100">
    <div id="dynamic-content-slot"></div>
  </div>
</body>
```

```typescript
// ✅ INP optimization: Break long-running CPU tasks by yielding to main thread
async function processLargeDataset(items: any[]) {
  for (let i = 0; i < items.length; i++) {
    processItem(items[i]);

    // Yield control back to browser every 50 items so user taps/clicks are responsive (<200ms)
    if (i % 50 === 0 && 'scheduler' in window && 'yield' in (window as any).scheduler) {
      await (window as any).scheduler.yield();
    }
  }
}
```
