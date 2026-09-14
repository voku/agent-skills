# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Technical crawling foundation & Core Web Vitals | Always |
| HIGH | Schema structured data, on-page, and SPA SEO | Most web projects |
| MEDIUM | Social previews and cross-platform sharing | Public pages |

## Section Overview

### 1. Technical SEO & Crawling (`tech`)
- **Impact:** CRITICAL
- **Rules:** `tech-metadata-canonical`
- **Description:** Complete indexing foundations: `<title>`, meta description, `<link rel="canonical">`, clean URL routing, `robots.txt`, and XML sitemap generation.

### 2. Structured Data (`schema`)
- **Impact:** HIGH
- **Rules:** `schema-structured-data`
- **Description:** JSON-LD structured data implementation (Article, Product, BreadcrumbList, Organization) using `@graph` composition and Google Rich Results validation.

### 3. Social Sharing Cards (`social`)
- **Impact:** HIGH
- **Rules:** `social-meta-tags`
- **Description:** Open Graph (`og:*`) and Twitter Card (`twitter:*`) tags with standardized 1200x630 preview images and secure absolute HTTPS URLs.

### 4. Core Web Vitals & Performance (`perf`)
- **Impact:** CRITICAL
- **Rules:** `core-web-vitals-perf`
- **Description:** Meeting Google CWV thresholds: LCP (<2.5s) via hero preloading and `fetchpriority="high"`, INP (<200ms) with `scheduler.yield()`, and CLS (<0.1) with aspect ratios.

### 5. On-Page Content & Mobile-First (`onpage`)
- **Impact:** HIGH
- **Rules:** `onpage-content-mobile`
- **Description:** On-page semantic structure: single primary `h1`, descriptive anchor text for internal link equity, alt descriptions, and 100% mobile-desktop content parity.

### 6. React SPA & Inertia.js SEO (`spa`)
- **Impact:** HIGH
- **Rules:** `spa-ssr-inertia-seo`
- **Description:** Server-Side Rendering (SSR) configuration for SPAs, `@inertiaHead` layout integration, and Inertia `<Head>` component with `head-key` deduplication.
