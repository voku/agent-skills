---
id: type-composition
title: Advanced Type Composition (Unions, Intersections, DNF, Void, Never)
category: type
priority: CRITICAL
triggers: [missing-nullable, loose-return, complex-type-union, intersection-type, never-return]
tags: [types, unions, intersections, dnf, nullable, void, never]
---

# Advanced Type Composition

**Trigger Anchor:** Use native union (`A|B`), intersection (`A&B`), and DNF (`(A&B)|C`) types for precise contracts. Use `void` for non-returning methods and `never` for methods that always throw or exit.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Vague PHPDoc instead of native union/intersection; missing void/never
class Dispatcher
{
    /**
     * @param mixed $handler
     * @return mixed
     */
    public function dispatch($handler, $data)
    {
        if (!$handler) {
            exit(1); // missing never return
        }
        return null; // missing void
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Precise union, intersection, DNF, void, and never return types
final class Dispatcher
{
    /**
     * Accepts an object that is both Traversable and Countable, or an array
     */
    public function processCollection((Traversable&Countable)|array $items): void
    {
        foreach ($items as $item) {
            // ...
        }
    }

    public function findUser(string|int $identifier): ?User
    {
        return $identifier === 0 ? null : new User($identifier);
    }

    public function terminate(string $reason): never
    {
        throw new RuntimeException("Terminating: {$reason}");
    }
}
```
