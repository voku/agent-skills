---
id: ux-motion-layout-stability
title: "Reduced Motion Preferences, Layout Stability (CLS), and Image Loading"
category: motion
priority: CRITICAL
triggers: [prefers-reduced-motion, cumulative-layout-shift, image-dimension-layout-shift, responsive-images-lazy]
tags: [motion, animation, cls, core-web-vitals, images, performance]
---

# Reduced Motion Preferences, Layout Stability (CLS), and Image Loading

**Trigger Anchor:** Respect `prefers-reduced-motion` to suppress vestibular discomfort, prevent Cumulative Layout Shift (CLS) by supplying explicit image dimensions / aspect ratios, and optimize media with `loading="lazy"`.

---

### Bad
```html
<!-- ❌ Unconstrained animations and missing image dimensions triggering layout shift -->
<style>
  /* Infinite aggressive animation running indiscriminately */
  .spinner {
    animation: spin 1s infinite linear;
  }
  @keyframes spin { 100% { transform: rotate(360deg); } }
</style>

<!-- ❌ Missing width/height attributes: browser cannot compute aspect ratio before download, causing CLS -->
<img src="/photos/hero.jpg" alt="Hero banner" />
```

### Good
```css
/* ✅ Global CSS: Instantly disable transitions and animations when user requests reduced motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```tsx
// ✅ React image component with reserved layout space, lazy loading, and modern format fallbacks
export function StableHeroImage({
  src,
  alt,
  width = 800,
  height = 450,
}: {
  src: string;
  alt: string;
  width?: number;
  height?: number;
}) {
  return (
    <div
      className="relative overflow-hidden rounded-xl bg-zinc-100"
      style={{ aspectRatio: `${width} / ${height}` }} // Reserves exact bounding box before image loads
    >
      <img
        src={src}
        alt={alt}
        width={width}
        height={height}
        loading="lazy"
        decoding="async"
        className="h-full w-full object-cover transition-opacity duration-300"
      />
    </div>
  );
}
```
