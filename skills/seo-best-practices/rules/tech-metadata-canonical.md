---
id: tech-metadata-canonical
title: "Technical SEO: Metadata, Canonical URLs, Robots.txt, and XML Sitemaps"
category: technical
priority: CRITICAL
triggers: [technical-seo-setup, canonical-url-missing, robots-txt-config, sitemap-xml-generation, duplicate-content-penalty]
tags: [seo, technical-seo, canonical, robots-txt, sitemaps, meta-tags]
---

# Technical SEO: Metadata, Canonical URLs, Robots.txt, and XML Sitemaps

**Trigger Anchor:** Include unique `<title>` and `<meta name="description">` tags on every page, declare authoritative self-referential `<link rel="canonical">` to prevent duplicate indexing, configure `robots.txt`, and generate dynamic XML sitemaps.

---

### Bad
```html
<!-- ❌ Missing canonical, generic duplicate title, query parameter URL soup -->
<head>
  <title>Home</title> <!-- Generic title causes low CTR and search ranking penalty -->
  <!-- ❌ No meta description -->
  <!-- ❌ No canonical tag: http, https, trailing slash, and tracking params index as separate duplicate pages -->
</head>
```

### Good
```html
<!-- ✅ HTML/Blade Layout: Complete technical SEO metadata -->
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <!-- Title: 50-60 chars with primary keyword and brand suffix -->
  <title>Enterprise Cloud Storage Solutions — Acme Cloud</title>

  <!-- Description: 150-160 chars compelling summary with clear call to action -->
  <meta name="description" content="Secure, high-availability S3-compatible cloud storage for distributed applications. Start with 50GB free tier and scale on demand." />

  <!-- Canonical URL: Strips tracking params, normalizes protocol, domain, and trailing slash -->
  <link rel="canonical" href="https://acmecloud.com/storage" />

  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
</head>
```

```txt
# ✅ public/robots.txt: Clear crawler directives and sitemap declaration
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /checkout/
Disallow: /*?*search=

Sitemap: https://acmecloud.com/sitemap.xml
```

```php
// ✅ routes/console.php: Automated XML sitemap generation with spatie/laravel-sitemap
use Spatie\Sitemap\Sitemap;
use Spatie\Sitemap\Tags\Url;
use App\Models\Article;

Schedule::command('sitemap:generate')->daily();

Artisan::command('sitemap:generate', function () {
    $sitemap = Sitemap::create()
        ->add(Url::create('/')->setPriority(1.0)->setChangeFrequency(Url::CHANGE_FREQUENCY_WEEKLY))
        ->add(Url::create('/storage')->setPriority(0.9)->setChangeFrequency(Url::CHANGE_FREQUENCY_MONTHLY));

    Article::published()->each(function (Article $article) use ($sitemap) {
        $sitemap->add(
            Url::create("/blog/{$article->slug}")
                ->setLastModificationDate($article->updated_at)
                ->setPriority(0.8)
                ->setChangeFrequency(Url::CHANGE_FREQUENCY_WEEKLY)
        );
    });

    $sitemap->writeToFile(public_path('sitemap.xml'));
});
```
