---
name: php-best-practices
description: PHP 8.x strict typing, modern language features, type safety, PHPStan + php-cs-fixer validation, value objects, no-magic design, and static analysis tooling. Use when reviewing PHP code, checking type safety, auditing code quality, or ensuring PHP best practices. Triggers on "review PHP", "check PHP code", "audit PHP", "PHP best practices", or "PHP static analysis".
license: MIT
metadata:
  author: php-community
  version: "4.0.0"
  phpVersion: "8.0 - 8.5"
---

# PHP Best Practices

Modern PHP 8.x patterns, PSR standards, strict type system, SOLID principles, security, performance, value objects, no-magic design, and PHPStan static analysis for writing clean, maintainable, analyzable PHP code.

> **Core philosophy:** Prefer explicit, analyzable, intention-revealing code with strict contracts and safe defaults. Reject magic, duplication, vague naming, and hidden failure modes.

## Step 1: Detect PHP Version

**Always check the project's PHP version before giving any advice.** Features vary significantly across 8.0 - 8.5. Never suggest syntax that doesn't exist in the project's version.
```json
{ "require": { "php": "^8.1" } }   // -> 8.1 rules and below
{ "require": { "php": "^8.3" } }   // -> 8.3 rules and below
{ "require": { "php": ">=8.4" } }  // -> 8.4 rules and below
```

Also check the runtime version:
```bash
php -v   # e.g. PHP 8.3.12
```

### Feature Availability by Version

| Feature | Version | Rule |
|---------|---------|------|
| Union types, match, nullsafe, named args, constructor promotion, attributes | 8.0+ | `type-`, `modern-` |
| Enums, readonly properties, intersection types, first-class callables, never | 8.1+ | `type-`, `modern-` |
| Readonly classes, DNF types, true/false/null standalone types | 8.2+ | `type-`, `modern-` |
| Typed class constants, `#[\Override]`, `json_validate()` | 8.3+ | `modern-` |
| Property hooks, asymmetric visibility `public private(set)` | 8.4+ | `modern-` |

**Only suggest features available in the detected version.**

## When to Apply

Reference these guidelines when:
- Writing or reviewing PHP code
- Implementing classes, value objects, and interfaces
- Leveraging PHP 8.x modern language features
- Ensuring strict type safety and static analyzability
- Following PSR standards and architectural principles
- Enforcing security (prepared statements, escaping, hashing)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Types | CRITICAL | `type-` |
| 2 | Modern PHP | CRITICAL | `modern-` |
| 3 | Error Handling | HIGH | `error-` |
| 4 | Security | CRITICAL | `sec-` |
| 5 | Performance | MEDIUM | `perf-` |
| 6 | Architecture & Design | HIGH | `design-`, `solid-` |
| 7 | PSR Standards | HIGH | `psr-` |
| 8 | Quality Tooling & Analysis | CRITICAL | `tooling-` |

## Quick Reference

### Types (CRITICAL)
- [type-strict-declarations.md](rules/type-strict-declarations.md) - Enforce `declare(strict_types=1)`, explicit parameter/return/property types, and avoid `mixed`
- [type-composition.md](rules/type-composition.md) - Composition types: unions (`|`), intersections (`&`), DNF types, `void`, `never`, and explicit nullability

### Modern PHP (CRITICAL)
- [modern-enums.md](rules/modern-enums.md) - Backed and pure enums with methods, interfaces, and exhaustive match handling
- [modern-readonly.md](rules/modern-readonly.md) - Immutable data structures via readonly classes, readonly properties, and typed constants
- [modern-property-hooks.md](rules/modern-property-hooks.md) - Property hooks (`get`/`set`) and asymmetric visibility (`public private(set)`)
- [modern-constructor-arguments.md](rules/modern-constructor-arguments.md) - Constructor property promotion and named arguments
- [modern-expressions.md](rules/modern-expressions.md) - Modern syntax: match expressions, nullsafe operator (`?->`), arrow functions, first-class callables
- [modern-attributes.md](rules/modern-attributes.md) - Native attributes for metadata and `#[\Override]` for compile-time inheritance verification

### Error Handling (HIGH)
- [error-handling.md](rules/error-handling.md) - Typed domain exceptions, narrow catch blocks, guaranteed resource cleanup in `finally`, and zero `@` suppression

### Security (CRITICAL)
- [sec-core-security.md](rules/sec-core-security.md) - Parameterized SQL statements, context-aware output escaping, password hashing, and safe file uploads

### Performance (MEDIUM)
- [perf-efficiency.md](rules/perf-efficiency.md) - Memory streaming via generators (`yield`), native string/array optimizations, and zero global state

### Architecture & Design (HIGH)
- [design-value-objects.md](rules/design-value-objects.md) - Self-validating immutable value objects over primitives, and elimination of magic methods (`__get`/`__set`)
- [solid-principles.md](rules/solid-principles.md) - Single responsibility, open/closed, Liskov substitution, interface segregation, and dependency injection

### PSR Standards (HIGH)
- [psr-standards.md](rules/psr-standards.md) - PSR-4 autoloading namespace mapping, PSR-12 code style, and naming conventions

### Quality Tooling & Analysis (CRITICAL)
- [tooling-static-analysis.md](rules/tooling-static-analysis.md) - PHPDoc precision layer: array shapes (`array{id: int}`), `list<T>`, `@template` generics, PHPStan level 8+, and PHP-CS-Fixer

## Key Patterns (Quick Reference)

```php
<?php

declare(strict_types=1);

namespace App\Domain;

// Modern PHP 8.2+ readonly class with promoted properties & enums
enum Role: string
{
    case Admin = 'admin';
    case User = 'user';
}

final readonly class User
{
    /**
     * @param list<string> $permissions
     */
    public function __construct(
        public int $id,
        public string $email,
        public Role $role = Role::User,
        public array $permissions = [],
    ) {}

    public function isAdmin(): bool
    {
        return $this->role === Role::Admin;
    }
}

// Modern PHP 8.4+ Property Hooks & Asymmetric Visibility
class Product
{
    public private(set) string $sku;

    public string $title {
        set => trim($value);
        get => ucfirst($this->title);
    }

    public function __construct(string $sku, string $title)
    {
        $this->sku = $sku;
        $this->title = $title;
    }
}
```

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete modern PHP idioms.
