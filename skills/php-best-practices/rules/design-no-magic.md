---
title: Avoid Magic-Heavy Design
impact: HIGH
impactDescription: Preserves static-analysis visibility, improves IDE support, and makes code intent explicit
tags: design, magic-methods, static-analysis, readability, phpstan
---

# Avoid Magic-Heavy Design

PHP's `__get`, `__set`, `__call`, `__callStatic`, and `__invoke` are powerful escape hatches, but overusing them hides behavior from IDEs, PHPStan, and future maintainers. Prefer explicit, typed methods and properties. Reserve magic methods for framework infrastructure, proxies, and data-transfer layers where the trade-off is justified.

## Bad Example

```php
<?php

declare(strict_types=1);

// Magic __get/__set hides all property access from static analysis
class User
{
    private array $attributes = [];

    public function __get(string $name): mixed
    {
        return $this->attributes[$name] ?? null;
    }

    public function __set(string $name, mixed $value): void
    {
        $this->attributes[$name] = $value;
    }

    public function __call(string $name, array $args): mixed
    {
        // Dynamic method dispatch — impossible to statically verify
        if (str_starts_with($name, 'get')) {
            $key = lcfirst(substr($name, 3));
            return $this->attributes[$key] ?? null;
        }
        if (str_starts_with($name, 'set')) {
            $key = lcfirst(substr($name, 3));
            $this->attributes[$key] = $args[0];
            return null;
        }
        throw new \BadMethodCallException("Method {$name} not found");
    }
}

// Caller code:
$user = new User();
$user->email = 'alice@example.com'; // __set — no type check
$user->name  = 42;                  // Accepted silently — wrong type
$user->getNmae();                   // Typo — no compile-time error
echo $user->email;                  // __get — PHPStan returns mixed
```

## Good Example

```php
<?php

declare(strict_types=1);

// Explicit, typed, readonly-by-default properties
final class User
{
    public function __construct(
        public readonly UserId $id,
        private Email $email,
        private UserName $name,
        private UserStatus $status = UserStatus::Active,
    ) {}

    public function getEmail(): Email
    {
        return $this->email;
    }

    public function getName(): UserName
    {
        return $this->name;
    }

    public function isActive(): bool
    {
        return $this->status === UserStatus::Active;
    }

    public function deactivate(): void
    {
        $this->status = UserStatus::Inactive;
    }

    // No __get, no __set, no __call
    // PHPStan sees every property and method — full static analysis
}
```

## When Magic Methods Are Acceptable

Some frameworks and patterns legitimately require magic. Contain and document them:

```php
<?php

declare(strict_types=1);

/**
 * Eloquent-style dynamic query builder — magic is intentional here.
 * PHPStan plugin (larastan/larastan) provides type stubs for ->where() etc.
 *
 * @method static static where(string $column, mixed $value)
 * @method static list<static> get()
 * @property-read int $id
 * @property string $email
 */
abstract class Model
{
    /** @param list<mixed> $args */
    public function __call(string $name, array $args): mixed
    {
        // Framework-level magic: justified, documented via @method stubs
        return $this->newQuery()->$name(...$args);
    }

    /** @param list<mixed> $args */
    public static function __callStatic(string $name, array $args): mixed
    {
        return (new static())->$name(...$args);
    }
}

// Explicit subclass restores full type safety for domain code:
final class UserModel extends Model
{
    // Explicit scope methods replace magic:
    public static function active(): static
    {
        return static::where('status', 'active');
    }
}
```

## Fluent Builder Without Magic

Use explicit chaining instead of `__call` for internal builders:

```php
<?php

declare(strict_types=1);

// Bad — magic chaining
class QueryBuilder
{
    public function __call(string $method, array $args): static
    {
        $this->parts[$method] = $args;
        return $this;
    }
}

// Good — explicit, typed, analysis-friendly
final class QueryBuilder
{
    private ?string $table = null;
    /** @var list<string> */
    private array $columns = ['*'];
    /** @var list<array{column: string, value: mixed}> */
    private array $wheres = [];
    private ?int $limitValue = null;

    public function from(string $table): static
    {
        $clone        = clone $this;
        $clone->table = $table;
        return $clone;
    }

    public function select(string ...$columns): static
    {
        $clone          = clone $this;
        $clone->columns = $columns;
        return $clone;
    }

    public function where(string $column, mixed $value): static
    {
        $clone           = clone $this;
        $clone->wheres[] = ['column' => $column, 'value' => $value];
        return $clone;
    }

    /** @param int<1, max> $n */
    public function limit(int $n): static
    {
        $clone             = clone $this;
        $clone->limitValue = $n;
        return $clone;
    }

    public function toSql(): string
    {
        // Build SQL from explicit fields
        $cols = implode(', ', $this->columns);
        $sql  = "SELECT {$cols} FROM {$this->table}";
        // ... where clauses, limit
        return $sql;
    }
}
```

## Why

- **Static Analysis Visibility**: `__get`/`__call` return `mixed` unless annotated with PHPDoc stubs; explicit methods return precise types that PHPStan and Psalm can verify
- **IDE Support**: Explicit methods and properties provide autocompletion and "go to definition"; magic methods do not without stubs
- **Refactoring Safety**: Renaming an explicit property shows all usages; renaming a magic key does not
- **Readability**: A method signature communicates its contract; a `__call` dispatcher requires reading the implementation to understand what is available
- **Test Clarity**: Explicit methods are straightforward to mock; magic dispatchers require complex setup

Reference: [PHP Magic Methods](https://www.php.net/manual/en/language.oop5.magic.php) | [PHPStan — Magic Methods](https://phpstan.org/writing-php-code/phpdocs-basics#magic-methods)
