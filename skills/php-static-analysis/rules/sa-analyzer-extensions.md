
---
title: Analyzer Extensions
impact: MEDIUM
impactDescription: Casts sprinkled around dynamic helpers because the analyzer was never taught what they return
tags: php, static-analysis, php-static-analysis, sa-analyzer-extensions
---

## Rule

When a helper's return type depends on its arguments, teach the analyzer with a dynamic return type extension instead of casting at every call site. When a repository rule keeps being explained in review, encode it as a custom rule.

## What to Do

- Write a dynamic return type extension for global or container helpers whose result type is argument-dependent.
- Turn a repeatedly-explained convention into a custom analyzer rule, so it is enforced rather than remembered.
- Keep custom rules cheap: screen by method or class name first, cache declarations, and avoid walking the whole node tree per file.
- Run the whole repository once after adding a rule, and check that the fix it demands survives the project's own auto-fixer pipeline.

## Incorrect

```php
$value = (string) config('app.name');   // repeated wherever the helper is used
```

## Correct

```php
// A return type extension resolves config('app.name') to string once, for every call site.
$value = config('app.name');
```

## Notes

- An extension is worth writing when the cast count exceeds the extension's size; below that, a typed wrapper is simpler.
- A custom rule without a test that proves it fires is a suggestion, not a constraint.
