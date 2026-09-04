
---
title: Root-Cause Over Inline Assertion
impact: HIGH
impactDescription: The same value re-asserted at every call site because its source was never typed
tags: php, static-analysis, php-static-analysis, sa-root-cause-typing
---

## Rule

Fix the type where the value is produced, not where it is consumed. An inline `@var`, a cast, or an assertion repeated at several call sites is a sign that the producer's signature is the real defect.

## What to Do

- When the same annotation appears at more than one call site, move the type to the producing method, property, or factory.
- Prefer changing one owning signature over patching each caller, even when the patch is smaller per file.
- After removing a cast, expect the analyzer to reveal the next honest problem - a strict comparison on an untyped operand, for example - and fix that at its source too.
- Verify empirically how the source actually behaves at runtime before typing it; a driver or a legacy layer may already return the native type you were casting to.

## Incorrect

```php
$id = (int) $row->id;            // in five different call sites
$other = (int) $other->id;
```

## Correct

```php
final class Row
{
    public int $id;              // typed once, every caller inherits it
}
```

## Notes

- One root-cause change that fixes all callers beats five local patches, and it is the change a reviewer can verify.
- If the producing layer cannot be changed yet, wrap it once in a typed adapter instead of asserting at each consumer.
