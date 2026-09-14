# SEO Best Practices — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent SEO rule inventory, audit encyclopedia, version table, or compiled copy of the rule examples here.

## Fast Path

1. Ground the target application's rendering stack, routes, templates/components, and deployment behavior before making SEO claims.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the page or audit concern.
3. Distinguish source-code evidence from measurements that require runtime tooling such as PageSpeed, Search Console, or Rich Results tests.
4. Lead with crawlability/indexability and materially observable user/search impact before cosmetic metadata preferences.
5. Report only observed results; unavailable runtime or external measurement evidence remains unknown rather than being converted into PASS.

## Ownership Boundary

- `SKILL.md` owns activation, audit workflow, and high-level routing.
- `rules/` owns detailed SEO guidance and examples.
- the target repository owns its rendering architecture, routes, content, deployment, and local validation commands.
- search-engine/vendor documentation owns external behavior and thresholds that may change over time.
- this projection owns no independent SEO semantics.

## Evidence Boundary

- Verify metadata, canonical URLs, robots/sitemap behavior, structured data, social tags, rendering/SSR behavior, and relevant image/font markup in real source before reporting them.
- Treat performance numbers as measurements, not properties inferred from code alone.
- Do not invent search rankings, traffic impact, indexing state, or Core Web Vitals measurements.
- For audits, preserve `PASS`, `FAIL`, `N/A`, and `UNKNOWN` distinctions when evidence differs.

## Projection Boundary

Do not copy current canonical rule IDs, counts, category totals, framework-version assumptions, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
