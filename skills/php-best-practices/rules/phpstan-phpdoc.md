---
title: PHPStan-Style PHPDoc Annotations
impact: CRITICAL
impactDescription: Enables precise static analysis, generics, and type inference beyond native PHP types
tags: phpstan, phpdoc, generics, array-shapes, type-safety, static-analysis
---

# PHPStan-Style PHPDoc Annotations

Use PHPStan-compatible PHPDoc annotations to express types that PHP's native type system cannot represent: generic collections, array shapes, class-strings, int-ranges, and conditional return types. These annotations are consumed by PHPStan, Psalm, and IDE tooling to catch bugs at analysis time.

## Bad Example

```php
<?php

declare(strict_types=1);

class UserRepository
{
    // Return type says array but shape is unknown to static analysis
    public function findAll(): array
    {
        return $this->db->fetchAll('SELECT * FROM users');
    }

    // Caller receives mixed[] - no type safety downstream
    public function paginate(int $page): array
    {
        return [
            'data'  => $this->findAll(),
            'total' => 100,
            'page'  => $page,
        ];
    }

    // Class name stored as string - PHPStan cannot verify it exists
    public function resolveHandler(string $class): object
    {
        return new $class();
    }

    // Count could be negative - constraint not expressed
    public function getCount(): int
    {
        return $this->db->count('users');
    }
}
```

## Good Example

```php
<?php

declare(strict_types=1);

/**
 * @template T of object
 */
class Collection
{
    /** @var list<T> */
    private array $items = [];

    /**
     * @param T $item
     */
    public function add(object $item): void
    {
        $this->items[] = $item;
    }

    /**
     * @return list<T>
     */
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
        $clone = clone $this;
        $clone->items = array_values(array_filter($this->items, $predicate));
        return $clone;
    }
}

class UserRepository
{
    /**
     * @return list<array{id: int, name: string, email: string, created_at: string}>
     */
    public function findAll(): array
    {
        return $this->db->fetchAll('SELECT id, name, email, created_at FROM users');
    }

    /**
     * @return array{data: list<User>, total: int<0, max>, page: int<1, max>}
     */
    public function paginate(int $page): array
    {
        return [
            'data'  => $this->mapToEntities($this->findAll()),
            'total' => $this->db->count('users'),
            'page'  => $page,
        ];
    }

    /**
     * @param class-string<HandlerInterface> $class
     */
    public function resolveHandler(string $class): HandlerInterface
    {
        return new $class();
    }

    /** @return int<0, max> */
    public function getCount(): int
    {
        return $this->db->count('users');
    }
}
```

## Array Shapes

Use `array{...}` for fixed-key associative arrays whose structure is known:

```php
<?php

declare(strict_types=1);

/**
 * @param array{name: string, email: string, age?: int} $data
 * @return array{id: int, name: string, email: string}
 */
function createUser(array $data): array
{
    // PHPStan knows exactly which keys exist and their types
    return [
        'id'    => generateId(),
        'name'  => $data['name'],
        'email' => $data['email'],
    ];
}

/**
 * @param array{
 *     driver: non-empty-string,
 *     host: non-empty-string,
 *     port: int<1, 65535>,
 *     database: non-empty-string,
 *     username: string,
 *     password: string,
 * } $config
 */
function createConnection(array $config): \PDO
{
    return new \PDO(
        "mysql:host={$config['host']};dbname={$config['database']}",
        $config['username'],
        $config['password'],
    );
}
```

## Generics

Use `@template` to express type-safe generic classes and functions:

```php
<?php

declare(strict_types=1);

/**
 * @template TKey of array-key
 * @template TValue
 */
class TypedMap
{
    /** @var array<TKey, TValue> */
    private array $storage = [];

    /**
     * @param TKey   $key
     * @param TValue $value
     */
    public function set(mixed $key, mixed $value): void
    {
        $this->storage[$key] = $value;
    }

    /**
     * @param TKey $key
     * @return TValue|null
     */
    public function get(mixed $key): mixed
    {
        return $this->storage[$key] ?? null;
    }
}

/**
 * @template T
 * @param list<T>        $items
 * @param callable(T): bool $predicate
 * @return list<T>
 */
function filterList(array $items, callable $predicate): array
{
    return array_values(array_filter($items, $predicate));
}
```

## Class-String Types

Use `class-string` to constrain strings that must be valid, instantiable class names:

```php
<?php

declare(strict_types=1);

/**
 * @param class-string $className
 */
function instantiate(string $className): object
{
    return new $className();
}

/**
 * @template T of Model
 * @param class-string<T> $modelClass
 * @return T
 */
function findFirst(string $modelClass): mixed
{
    return $modelClass::query()->first();
}

// PHPStan verifies that UserRepository::class is a valid class-string<RepositoryInterface>
$repo = findFirst(UserRepository::class);
```

## Int-Range Types

Use `int<min, max>` to constrain integer ranges and communicate valid bounds:

```php
<?php

declare(strict_types=1);

/** @return int<0, max> */
function countItems(): int
{
    return count($this->items); // never negative
}

/** @param int<1, 100> $perPage */
function paginate(int $perPage = 15): Paginator
{
    // $perPage is guaranteed 1-100
}

/** @return int<0, 255> */
function parseColorChannel(string $hex): int
{
    return hexdec($hex) & 0xFF;
}

/** @return positive-int */
function nextId(): int
{
    return $this->sequence->next();
}
```

## Conditional Return Types

Use `@return ($param is SomeType ? ReturnTypeA : ReturnTypeB)` for functions whose return type depends on their argument type:

```php
<?php

declare(strict_types=1);

/**
 * @param string|null $value
 * @return ($value is string ? int : null)
 */
function maybeLength(?string $value): ?int
{
    return $value !== null ? strlen($value) : null;
}

/**
 * @template T
 * @param T|null $value
 * @param T      $default
 * @return ($value is null ? T : T)
 */
function coalesce(mixed $value, mixed $default): mixed
{
    return $value ?? $default;
}
```

## Non-Empty and Special String Types

```php
<?php

declare(strict_types=1);

/** @param non-empty-string $slug */
function findBySlug(string $slug): ?Post { /* ... */ }

/** @return non-empty-list<User> */
function requireAtLeastOneAdmin(): array
{
    $admins = $this->findAdmins();
    if ($admins === []) {
        throw new \RuntimeException('No admins found');
    }
    return $admins;
}

/** @param numeric-string $amount */
function parseMoneyString(string $amount): Money { /* ... */ }
```

## Why

- **Static Analysis Coverage**: PHPStan/Psalm can verify generic collections, array shapes, and conditional types at analysis time — catching bugs before runtime
- **IDE Autocomplete**: Editors use these annotations for accurate autocompletion inside `foreach` loops, method chains, and array access
- **Generics Without Runtime Cost**: PHP has no runtime generics; `@template` gives the same safety guarantees at zero performance cost
- **Array Shape Safety**: `array{key: type}` eliminates the need for defensive `isset()` checks on known-structure arrays
- **Communicates Invariants**: `int<0, max>` and `non-empty-string` document assumptions that would otherwise require prose comments or runtime assertions

Reference: [PHPStan Generics](https://phpstan.org/blog/generics-in-php-using-phpdocs) | [PHPStan Array Shapes](https://phpstan.org/writing-php-code/phpdoc-types#array-shapes) | [PHPStan Int Masks](https://phpstan.org/writing-php-code/phpdoc-types)
