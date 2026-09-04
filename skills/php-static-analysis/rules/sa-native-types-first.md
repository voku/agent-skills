
---
title: Native Types First
impact: CRITICAL
impactDescription: PHPDoc used where a real PHP type would have made the contract enforceable at runtime
tags: php, static-analysis, php-static-analysis, sa-native-types-first
---

## Rule

Express a type with PHP itself before writing an annotation. PHPDoc is for what the language cannot say - shapes, generics, ranges, conditional returns - not for repeating what a parameter, property, or return type could declare.

## What to Do

- Add the native parameter, property, and return types first, including nullability.
- Reach for PHPDoc only when the remaining precision is inexpressible in PHP.
- When a property has no native type and comparisons on it are flagged, add the type it should have had; do not loosen the comparison to make the message disappear.
- Give a typed property on a readonly class an explicit default when the analyzer reports it as uninitialized.

## Incorrect

```php
/** @var int $count */
$count = (int) $row->count;
```

## Correct

```php
public int $count;   // declared on the source, so every reader inherits it

$count = $row->count;
```

## Notes

- A cast paired with an inline `@var` widens a precise type and then re-narrows it; the reader loses the information that the source was already typed.
- Keep an explicit conversion where the source really is untyped: request input, environment values, or a driver that genuinely returns strings.
