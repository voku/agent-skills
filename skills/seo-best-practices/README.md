# SEO Best Practices

Portable guidance for implementing and auditing technical SEO, structured data, social metadata, Core Web Vitals-related markup, on-page/mobile content, and SPA/SSR crawlability.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level audit workflow. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, version table, or compiled SEO checklist.

## When to Use

Use this skill when implementing or reviewing search metadata, canonical/robots/sitemap behavior, structured data, Open Graph/social cards, crawlable rendering, on-page semantics, or evidence-backed performance-related SEO work.

## Routing

1. Ground the application's rendering stack and relevant page/template/component paths.
2. Read `SKILL.md` to select the canonical rule files that match the observed concern.
3. Load only those rules rather than compiling the entire SEO catalog into context.
4. Separate source-code checks from external/runtime measurements.
5. Validate through the target repository and appropriate external tools where evidence is actually available.

## Stable Boundaries

- Do not infer indexing, rankings, traffic impact, or measured Core Web Vitals from source code alone.
- Prefer explicit canonical/indexing contracts and valid structured metadata over speculative SEO tweaks.
- Keep mobile and desktop content semantics aligned unless the product intentionally differs.
- For SPA/SSR applications, verify what crawlers actually receive rather than assuming client-side rendering is sufficient.
- Preserve `PASS`, `FAIL`, `N/A`, and `UNKNOWN` distinctions in audit output.

## Projection Boundary

Do not copy the current rule list, rule count, category totals, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.

## References

- [Google Search Central](https://developers.google.com/search)
- [web.dev Core Web Vitals](https://web.dev/articles/vitals)
- [Schema.org](https://schema.org/)
- [Open Graph Protocol](https://ogp.me/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
