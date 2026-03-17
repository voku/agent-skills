# PHPStan-Style PHPDoc Annotations

## Why it matters

PHP's native type system cannot express generic collections (`list<User>`), fixed-key array structures (`array{id: int, name: string}`), constrained integers (`int<1, 100>`), or conditional return types. Without PHPDoc precision annotations, PHPStan infers `mixed[]` for array parameters and `mixed` for many return types, turning static analysis into educated guesswork. Precision annotations are the difference between PHPStan catching a null dereference at analysis time and that null dereference crashing in production.

## Rule

Use PHPStan-compatible PHPDoc annotations only where native PHP cannot express enough — generic collections, array shapes, class-string constraints, int ranges, and conditional return types. Do not add PHPDoc for types that native declarations already cover. Inline `@var` is a last resort; restructure code to eliminate the ambiguity instead.

## Bad

```php
<?php

declare(strict_types=1);

// Untyped arrays — static analysis sees array<mixed>, caller sees nothing
class UserRepository
{
    public function findAll(): array
    {
        return $this->db->fetchAll('SELECT id, name, email FROM users');
    }

    public function paginate(int $page): array
    {
        return [
            'data'  => $this->findAll(),
            'total' => 100,
            'page'  => $page,
        ];
    }

    public function getCount(): int
    {
        return $this->db->count('users');  // could be 0 or more — no constraint expressed
    }
}
```

## Better

```php
<?php

declare(strict_types=1);

// Array shapes on fixed-key structures
class UserRepository
{
    /**
     * @return list<array{id: int, name: string, email: string}>
     */
    public function findAll(): array
    {
        return $this->db->fetchAll('SELECT id, name, email FROM users');
    }

    /**
     * @return array{data: list<array{id: int, name: string, email: string}>, total: int<0, max>, page: int<1, max>}
     */
    public function paginate(int $page): array
    {
        return [
            'data'  => $this->findAll(),
            'total' => $this->db->count('users'),
            'page'  => $page,
        ];
    }

    /** @return int<0, max> */
    public function getCount(): int
    {
        return $this->db->count('users');
    }
}
```

## Best

```php
<?php

declare(strict_types=1);

// Generics with @template for reusable typed collections
/**
 * @template T of object
 */
final class Collection
{
    /** @var list<T> */
    private array $items = [];

    /** @param T $item */
    public function add(object $item): void
    {
        $this->items[] = $item;
    }

    /** @return list<T> */
    public function all(): array
    {
        return $this->items;
    }

    /**
     * @param callable(T): bool $predicate
     * @return static
     */
    public function filter(callable $predicate): static
    {
        $clone        = clone $this;
        $clone->items = array_values(array_filter($this->items, $predicate));
        return $clone;
    }
}

// class-string constrains instantiation to verified class names
/**
 * @template T of HandlerInterface
 * @param class-string<T> $class
 * @return T
 */
function resolveHandler(string $class): HandlerInterface
{
    return new $class();
}

// Conditional return type: return type depends on argument nullability
/**
 * @param string|null $value
 * @return ($value is string ? int : null)
 */
function maybeLength(?string $value): ?int
{
    return $value !== null ? strlen($value) : null;
}

// non-empty-string and non-empty-list signal guaranteed non-emptiness
/**
 * @return non-empty-list<User>
 */
function requireAtLeastOneAdmin(): array
{
    $admins = findAdmins();
    if ($admins === []) {
        throw new \RuntimeException('No admins configured');
    }
    return $admins;
}
```

## Exceptions / trade-offs

- **Do not annotate what native types already express.** `public function getId(): int` needs no `@return int` PHPDoc — the native declaration is the contract.
- **Inline `@var` is a last resort.** If you need `/** @var User $user */` before a variable, the better fix is to restructure the code so PHPStan can infer the type from context.
- **`@param array $data`** with no shape annotation is worse than nothing — it silently widens the type to `mixed[]`. Either add a shape or use a typed DTO.
- PHPDoc on internal private helpers with obvious types adds noise without value.

## Static-analysis notes

- **`list<T>`** is a PHPStan/Psalm type for sequential arrays (keys 0, 1, 2…). Use it instead of `array<int, T>` for ordered collections.
- **`array{key: Type, ...}`** — PHPStan verifies key existence and types at every access site.
- **`class-string<T>`** — PHPStan verifies the string is a valid, instantiable class name that is a subtype of `T`.
- **`int<min, max>`** — PHPStan propagates the range constraint through arithmetic and comparisons.
- **`@template`** gives full generic safety at zero runtime cost. PHPStan infers the concrete type at each call site.
- **`non-empty-string`** and **`non-empty-list<T>`** eliminate the need for defensive `=== ''` or `=== []` guards after the annotation point.
- PHPStan level 7+ requires `@param`/`@return` annotations when native types are absent; level 9 flags all `mixed` usage.

## Related topics

- [type-mixed-avoid.md](type-mixed-avoid.md) — use precise annotations instead of leaving `mixed` in place
- [design-value-objects.md](design-value-objects.md) — value objects often eliminate the need for complex array shapes
- [tooling-phpstan-cs-fixer.md](tooling-phpstan-cs-fixer.md) — run PHPStan to validate annotations in CI
- [type-union-types.md](type-union-types.md) — prefer native union types over PHPDoc unions where PHP supports it
