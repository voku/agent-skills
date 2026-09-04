
---
title: Shape & Generic Precision
impact: CRITICAL
impactDescription: Loose array and mixed types that force every caller to re-validate a structure the producer already knows
tags: php, static-analysis, php-static-analysis, sa-shape-precision
---

## Rule

An array with a known key set is a shape, not an `array`. Declare `array{...}`, `list<T>`, `non-empty-list<T>`, `class-string<T>`, and template parameters wherever the code already knows more than `array` or `mixed`.

## What to Do

- Replace `array` with an explicit `array{key: type, optional?: type}` when the key set is fixed.
- Use `list<T>` for sequential arrays and `non-empty-string` / `non-empty-list<T>` when emptiness is already excluded.
- Use `class-string<T>` instead of `string` when the value is a class name that gets instantiated or compared.
- Build a known-key array with explicit conditional assignments so the flow reads top to bottom, instead of splicing keys in with `array_merge` and hiding which keys can exist.
- Introduce `@template` only when a reusable generic abstraction genuinely exists; a single implementation does not need one.

## Incorrect

```php
/** @return array<string, string> */
function options(): array
{
    return array_merge($extra, ['mode' => 'fast']);
}
```

## Correct

```php
/** @return array{mode: 'fast'|'safe', label?: non-empty-string} */
function options(): array
{
    $options = ['mode' => 'fast'];
    if ($label !== '') {
        $options['label'] = $label;
    }

    return $options;
}
```

## Notes

- Avoid over-annotating private implementation details the analyzer already infers.
- `mixed` at a boundary is acceptable only when it is validated once, immediately, into a precise type.
