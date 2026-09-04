
---
title: Ignore & Baseline Scoping
impact: MEDIUM
impactDescription: Broad suppressions that also hide the next, unrelated defect in the same file or directory
tags: php, static-analysis, php-static-analysis, sa-ignore-scoping
---

## Rule

An ignore is an admission with a scope. Scope it to the exact reported line or the exact legacy file family, never to a directory because one cluster in it is noisy.

## What to Do

- Prefer an inline ignore on the reported line, with a short reason, over a configuration-wide exclusion.
- Remember that an inline ignore suppresses the line the analyzer reported, which for a multi-line statement is not necessarily its opening line.
- Add new violations to a baseline only when the rule was introduced for existing code; a violation written today is fixed today.
- When a rule is introduced with no baseline, keep it that way: the first new violation must fail, or the rule stops meaning anything.
- Re-check ignores when touching the surrounding code; an ignore that no longer fires is dead weight.

## Incorrect

```neon
# One noisy legacy cluster suppresses an entire tree.
parameters:
    excludePaths:
        - src/Legacy
```

## Correct

```php
/** @phpstan-ignore argument.type (legacy loader hands us a raw array; typed adapter tracked in TICKET-42) */
$loader->load($rawConfiguration);
```

## Notes

- A baseline is a snapshot of accepted debt, not a place to put today's shortcut.
- An ignore without a written reason will be copied by the next person who sees a similar message.
