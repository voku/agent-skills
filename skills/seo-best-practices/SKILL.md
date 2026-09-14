---
name: seo-best-practices
description: SEO patterns, conventions, and audit for web applications. Use when implementing meta tags, structured data, Core Web Vitals, sitemaps, Open Graph, auditing SEO, or optimizing pages for search engines. Triggers on "audit SEO", "check SEO", "review SEO", or tasks involving search optimization, schema markup, or social sharing meta tags.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# SEO Best Practices & Audit Guide

Curated, high-density SEO patterns for web applications built with Laravel Blade and Laravel + Inertia.js + React. Covers technical metadata, JSON-LD structured data, social cards, Core Web Vitals, on-page content, and SPA SSR.

## Quick Reference

| Domain | Impact | Rule File | Primary Focus |
|--------|--------|-----------|---------------|
| **Technical SEO** | CRITICAL | [`tech-metadata-canonical`](rules/tech-metadata-canonical.md) | `<title>`, meta description, `<link rel="canonical">`, `robots.txt`, XML sitemaps |
| **Structured Data** | HIGH | [`schema-structured-data`](rules/schema-structured-data.md) | JSON-LD schemas (Article, Product, Breadcrumbs), `@graph` composition, Rich Results |
| **Social Sharing** | HIGH | [`social-meta-tags`](rules/social-meta-tags.md) | Open Graph (`og:*`), Twitter Cards (`summary_large_image`), 1200x630 image standards |
| **Core Web Vitals** | CRITICAL | [`core-web-vitals-perf`](rules/core-web-vitals-perf.md) | LCP (<2.5s) preload, INP (<200ms) yield, CLS (<0.1) aspect ratios, font swapping |
| **On-Page & Mobile** | HIGH | [`onpage-content-mobile`](rules/onpage-content-mobile.md) | Single primary `h1`, descriptive anchor text, alt tags, mobile-desktop content parity |
| **React SPA & SSR** | HIGH | [`spa-ssr-inertia-seo`](rules/spa-ssr-inertia-seo.md) | SSR crawlability, `@inertiaHead`, Inertia `<Head>` component, `head-key` deduplication |

---

## SEO Audit Mode

When the user asks to "audit SEO", "check SEO", or "review SEO" — run this audit against their codebase:

### Step 1: Detect Stack
- **Laravel Blade**: Check `resources/views/**/*.blade.php`. Meta tags go in Blade layout components. Sitemaps generated via `spatie/laravel-sitemap`.
- **Laravel + Inertia + React**: Check `package.json` for `@inertiajs/react`. Verify SSR setup (`resources/js/ssr.jsx`) and check `<Head head-key="...">` usage.

### Step 2: Run Verification Checklist
1. **Technical SEO**: Every page has a unique `<title>` (50-60 chars), `<meta name="description">` (150-160 chars), canonical link, valid `robots.txt`, and XML sitemap.
2. **Structured Data**: Check `<script type="application/ld+json">` on article, product, and breadcrumb pages using `@graph`.
3. **Core Web Vitals**: Verify hero images use `fetchpriority="high"` without `loading="lazy"`, images have explicit dimensions / aspect ratios (CLS), and fonts use `font-display: swap`.
4. **Social Sharing**: Check `og:title`, `og:description`, `og:image` (1200x630 absolute HTTPS), and `twitter:card`.
5. **Mobile-First**: Check `<meta name="viewport">` and verify content parity between mobile and desktop views.

### Step 3: Audit Summary Output
```markdown
## SEO Audit Summary
- **PASS**: X checks
- **FAIL**: X checks
- **Top Priority Fixes**: (list the 3 most impactful FAIL items with recommended code diffs)
```
