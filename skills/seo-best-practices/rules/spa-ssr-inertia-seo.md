---
id: spa-ssr-inertia-seo
title: "React SPA and Inertia.js SEO: SSR Architecture and Dynamic Head Management"
category: spa
priority: HIGH
triggers: [inertia-react-seo, react-spa-ssr, inertia-head-key, dynamic-meta-tags-spa]
tags: [seo, react, inertia, ssr, head, spa]
---

# React SPA and Inertia.js SEO: SSR Architecture and Dynamic Head Management

**Trigger Anchor:** Enable Server-Side Rendering (SSR) for indexable SPA pages, manage meta tags dynamically via Inertia's `<Head>` component, and use `head-key` to eliminate duplicate tags between layout and page.

---

### Bad
```tsx
// ❌ Client-only rendering with standard useEffect document.title manipulation
import { useEffect } from 'react';

export default function ProductPage({ product }: { product: any }) {
  useEffect(() => {
    // ❌ Client-only execution: Search engine bots see empty root div and default site title
    document.title = product.name;
  }, [product]);

  return <div>{product.name}</div>;
}
```

### Good
```php
// ✅ resources/views/app.blade.php: Server-rendered root layout with Inertia head directive
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    @viteReactRefresh
    @vite(['resources/js/app.jsx', "resources/js/Pages/{$page['component']}.jsx"])
    @inertiaHead
</head>
<body class="font-sans antialiased">
    @inertia
</body>
</html>
```

```tsx
// ✅ resources/js/Pages/Products/Show.tsx: Inertia <Head> with head-key deduplication
import { Head } from '@inertiajs/react';

interface Product {
  name: string;
  slug: string;
  description: string;
  image: string;
  price: number;
}

export default function ProductShow({ product }: { product: Product }) {
  return (
    <>
      <Head>
        <title>{`${product.name} — Acme Store`}</title>
        {/* head-key guarantees this tag replaces any generic description from parent layout */}
        <meta head-key="description" name="description" content={product.description} />
        <link rel="canonical" href={`https://acmestore.com/products/${product.slug}`} />

        <meta property="og:title" content={product.name} />
        <meta property="og:description" content={product.description} />
        <meta property="og:image" content={product.image} />
        <meta property="og:type" content="product" />
        <meta name="twitter:card" content="summary_large_image" />
      </Head>

      <main className="mx-auto max-w-5xl p-6">
        <h1 className="text-3xl font-bold">{product.name}</h1>
        <p className="mt-4 text-zinc-600">{product.description}</p>
        <p className="mt-2 text-2xl font-semibold">${product.price.toFixed(2)}</p>
      </main>
    </>
  );
}
```
