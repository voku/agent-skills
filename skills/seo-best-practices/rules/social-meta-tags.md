---
id: social-meta-tags
title: "Social Sharing Optimization: Open Graph and Twitter/X Cards"
category: social
priority: HIGH
triggers: [open-graph-tags, twitter-cards-meta, social-preview-image, og-image-resolution]
tags: [seo, social, open-graph, twitter-cards, og-image, meta-tags]
---

# Social Sharing Optimization: Open Graph and Twitter/X Cards

**Trigger Anchor:** Include standardized Open Graph (`og:*`) and Twitter Card (`twitter:*`) tags, provide a high-resolution 1200x630px social preview image, and maintain absolute HTTPS URLs for all image assets.

---

### Bad
```html
<!-- ❌ Relative URLs, missing dimensions, missing Twitter card declarations -->
<head>
  <!-- ❌ Relative path fails on external social platform scrapers (Facebook, LinkedIn, Slack, X) -->
  <meta property="og:image" content="/images/banner.jpg" />
  <!-- ❌ Missing twitter:card falls back to plain unformatted text on X -->
</head>
```

### Good
```html
<!-- ✅ Comprehensive Open Graph and Twitter Card tags -->
<head>
  <!-- Essential Open Graph -->
  <meta property="og:site_name" content="Acme Cloud" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://acmecloud.com/blog/modern-cloud-architecture" />
  <meta property="og:title" content="Modern Cloud Architecture Patterns in 2026" />
  <meta property="og:description" content="Discover key patterns for distributed scalability, zero-trust security, and cost optimization." />

  <!-- High-res preview image (1200x630 ratio: 1.91:1) with explicit dimensions and HTTPS absolute path -->
  <meta property="og:image" content="https://acmecloud.com/images/social/cloud-architecture-1200x630.jpg" />
  <meta property="og:image:secure_url" content="https://acmecloud.com/images/social/cloud-architecture-1200x630.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Diagram illustrating modern cloud architecture patterns" />

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@AcmeCloud" />
  <meta name="twitter:creator" content="@johndoe" />
  <meta name="twitter:title" content="Modern Cloud Architecture Patterns in 2026" />
  <meta name="twitter:description" content="Discover key patterns for distributed scalability, zero-trust security, and cost optimization." />
  <meta name="twitter:image" content="https://acmecloud.com/images/social/cloud-architecture-1200x630.jpg" />
</head>
```
