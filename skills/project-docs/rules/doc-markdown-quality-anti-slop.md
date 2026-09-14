---
id: doc-markdown-quality-anti-slop
title: "Markdown Quality: Anti-Slop Detection, Headings, and Code Block Fencing"
category: quality
priority: HIGH
triggers: [markdown-ai-slop, missing-code-fence-language, skipped-heading-level, broken-markdown-links]
tags: [markdown, quality, anti-slop, headings, code-blocks, links]
---

# Markdown Quality: Anti-Slop Detection, Headings, and Code Block Fencing

**Trigger Anchor:** Strip AI filler phrases, sign-offs, and excessive apologetic prose; enforce single `h1` with sequential heading levels; tag all fenced code blocks with explicit language identifiers; and use descriptive relative markdown links.

---

### Bad
```markdown
<!-- ❌ Conversational AI slop, untagged code blocks, non-descriptive links -->
Certainly! Here is the complete guide you requested. I hope this helps you on your coding journey!

### Fast Setup <!-- Skipped h1 and h2 directly to h3 -->

To run the application, execute this in your terminal:

```
php artisan serve
```

For more details on installation, please click [here](https://example.com/docs).

Let me know if you need anything else! Happy coding! 🚀
```

### Good
```markdown
<!-- ✅ High-density, professional technical documentation -->
# Local Environment Setup

Step-by-step procedure for initializing the local development stack.

## Service Dependencies

Start required infrastructure containers:

```bash
docker compose up -d postgres redis
```

## Application Bootstrap

Run migrations and initialize the search vector indices:

```bash
php artisan migrate --seed
php artisan ai:sync-embeddings
```

For environment variable reference, consult the [configuration guide](docs/guides/local-development.md#environment-variables).
```
