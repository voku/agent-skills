---
id: schema-structured-data
title: "Structured Data: JSON-LD Schemas, @graph Composition, and Rich Results"
category: schema
priority: HIGH
triggers: [json-ld-structured-data, schema-org-article, schema-org-product, schema-graph-composition, rich-snippets-validation]
tags: [seo, schema, json-ld, structured-data, rich-snippets, breadcrumbs]
---

# Structured Data: JSON-LD Schemas, @graph Composition, and Rich Results

**Trigger Anchor:** Embed Schema.org structured data using valid `<script type="application/ld+json">`, link related entities (Organization, WebSite, Breadcrumbs, Article/Product) using `@graph`, and validate against Google Rich Results.

---

### Bad
```html
<!-- ❌ Broken microdata or unstructured scattered scripts missing mandatory properties -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Widget"
  /* ❌ Missing offers, price, priceCurrency, and availability causes Google Rich Results error */
}
</script>
```

### Good
```tsx
// ✅ Article page with combined Organization, Breadcrumbs, and Article schema via @graph
export function ArticleJsonLd({
  article,
  siteUrl = 'https://acmecloud.com',
}: {
  article: { title: string; slug: string; excerpt: string; publishedAt: string; modifiedAt: string; author: string; image: string };
  siteUrl?: string;
}) {
  const schema = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': `${siteUrl}/#organization`,
        name: 'Acme Cloud',
        url: siteUrl,
        logo: {
          '@type': 'ImageObject',
          url: `${siteUrl}/logo.png`,
        },
      },
      {
        '@type': 'BreadcrumbList',
        '@id': `${siteUrl}/blog/${article.slug}#breadcrumb`,
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: 'Home', item: siteUrl },
          { '@type': 'ListItem', position: 2, name: 'Blog', item: `${siteUrl}/blog` },
          { '@type': 'ListItem', position: 3, name: article.title },
        ],
      },
      {
        '@type': 'Article',
        '@id': `${siteUrl}/blog/${article.slug}#article`,
        isPartOf: { '@id': `${siteUrl}/#website` },
        headline: article.title,
        description: article.excerpt,
        datePublished: article.publishedAt,
        dateModified: article.modifiedAt,
        mainEntityOfPage: `${siteUrl}/blog/${article.slug}`,
        author: {
          '@type': 'Person',
          name: article.author,
        },
        publisher: { '@id': `${siteUrl}/#organization` },
        image: {
          '@type': 'ImageObject',
          url: article.image,
          width: 1200,
          height: 630,
        },
      },
    ],
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}
```
