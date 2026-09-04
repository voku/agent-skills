
---
title: Contract Honesty
impact: HIGH
impactDescription: A stricter, correct type relaxed to satisfy the analyzer, spreading the imprecision to every caller
tags: php, static-analysis, php-static-analysis, sa-contract-honesty
---

## Rule

Separate a wrong contract from a proof gap. If the strict type states the real intent, keep it and supply the missing proof; only change the declared type when the declaration itself was wrong.

## What to Do

- Ask which of the two the message means: "this value can really be something else" (wrong contract) or "I cannot see that it cannot" (proof gap).
- For a proof gap: narrow the input earlier, validate at the boundary, add a typed adapter, or assert once at the producer.
- Do not downgrade `literal-string`, `class-string<T>`, `non-empty-string`, or a union to a looser type to clear an error.
- Keep public contracts analyzable across call sites; a signature that only works because each caller knows an unwritten rule is not a contract.

## Incorrect

```php
// The analyzer cannot prove the value is non-empty, so the contract is widened.
- public function table(): non-empty-string
+ public function table(): string
```

## Correct

```php
// The contract stays; the proof moves to where the value enters.
public function __construct(private string $table)
{
    if ($table === '') {
        throw new InvalidArgumentException('table name must not be empty');
    }
}
```

## Notes

- A widened return type is a silent API change for every consumer, including future ones.
- When neither proof nor a correct narrower type is available yet, a scoped ignore with a written reason is more honest than a weakened signature.
