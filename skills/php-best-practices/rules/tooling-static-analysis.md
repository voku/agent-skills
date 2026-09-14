---
id: tooling-static-analysis
title: Static Analysis, Generics, and Quality Tooling
category: tooling
priority: HIGH
triggers: [untyped-array, missing-phpdoc-shape, phpstan-error, mixed-return, template-generics, cs-fixer]
tags: [static-analysis, phpstan, psalm, generics, phpdoc, array-shapes, cs-fixer]
---

# Static Analysis, Generics, and Quality Tooling

**Trigger Anchor:** Supplement native PHP types with precise PHPDoc array shapes (`array{id: int, name: string}`), `list<T>`, and `@template` generics; run PHPStan at level 8+ and enforce automated formatting with PHP-CS-Fixer.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Untyped array parameters and returns hide shape defects until runtime
class UserRepository
{
    /**
     * @param array $filters
     * @return array
     */
    public function findUsers(array $filters): array
    {
        // No shape guarantee: callers guess keys, PHPStan cannot verify property access
        return [
            ['id' => 1, 'name' => 'Alice'],
        ];
    }

    /**
     * Untyped factory returning object
     */
    public function make(string $class): object
    {
        return new $class();
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

/**
 * @phpstan-type UserPayload array{id: int, email: string, roles: list<string>}
 */
final readonly class UserRepository
{
    /**
     * ✅ Precise array shapes and list<T> guarantees structure and index order
     *
     * @param array{status?: string, minAge?: int} $filters
     * @return list<UserPayload>
     */
    public function findUsers(array $filters): array
    {
        return [
            ['id' => 1, 'email' => 'alice@example.com', 'roles' => ['admin', 'user']],
        ];
    }

    /**
     * ✅ Generic instantiation preserves return type at call-site without casting
     *
     * @template T of object
     * @param class-string<T> $class
     * @return T
     */
    public function make(string $class): object
    {
        return new $class();
    }
}
```
