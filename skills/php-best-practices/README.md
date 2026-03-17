# PHP Best Practices

Modern PHP 8.x patterns, PSR standards, SOLID principles, PHPStan-style PHPDoc, value objects, and a mandatory static-analysis tooling loop for clean, maintainable code.

## Overview

**Important:** Always detect the project's PHP version (`composer.json` or `php -v`) before giving advice. Only suggest features available in the detected version.

This skill provides guidance for:
- PHP 8.0 - 8.5 modern features (version-annotated)
- Type system best practices
- PSR standards compliance
- SOLID principles
- PHPStan-style PHPDoc (generics, array shapes, class-strings, int-ranges)
- Value objects and no-magic design
- Legacy code migration strategy
- Mandatory PHPStan + php-cs-fixer validation loop

## Workflow

Every PHP coding task follows three phases:

1. **DEFINE / SCOPE** — confirm PHP version, state the problem, run RCA for bugs
2. **DESIGN / PLANNING** — class boundaries, value objects, PHPDoc shapes, modifiers
3. **CODING / FEEDBACK** — implement, run `php-cs-fixer fix && phpstan analyse`, iterate

## Categories (61 rules)

### 1. Type System (Critical) — 9 rules
Strict types, return types, union/intersection types, nullable handling, void/never.

### 2. Modern PHP Features (Critical) — 16 rules
8.0: constructor promotion, match, named args. 8.1: enums, readonly. 8.2: readonly classes. 8.3: typed constants, #[\Override]. 8.4: property hooks, asymmetric visibility. 8.5: pipe operator.

### 3. PSR Standards (High) — 6 rules
PSR-4 autoloading, PSR-12 coding style, naming conventions, file structure, namespaces.

### 4. SOLID Principles (High) — 5 rules
Single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion.

### 5. Error Handling (High) — 5 rules
Custom exceptions, exception hierarchy, specific catches, finally cleanup, never suppress errors.

### 6. Performance (Medium) — 5 rules
Generators, lazy loading, native array/string functions, avoiding globals.

### 7. Security (Critical) — 5 rules
Input validation, output escaping, password hashing, prepared statements, file upload security.

### 8. PHPStan PHPDoc (Critical) — 1 rule
Generics (`@template`), array shapes (`array{key: type}`), `class-string<T>`, `int<min, max>`, conditional return types.

### 9. Design Patterns (High) — 2 rules
Value objects over primitives (self-validating, immutable domain types). Avoiding magic-heavy design (`__get`/`__call`) in favour of explicit typed methods.

### 10. Legacy Migration (High) — 1 rule
Incremental modernisation: PHPStan baseline → Rector transforms → type coverage → Strangler Fig isolation.

### 11. Tooling (Critical) — 1 rule
Mandatory PHPStan + php-cs-fixer loop; composer scripts; CI (GitHub Actions) integration; PHPStan level 0→9 guide.

## Usage

Ask Claude to:
- "Review my PHP code"
- "Check PHP types"
- "Audit PHP for SOLID"
- "Check PHP best practices"
- "Run PHPStan analysis on this code"
- "Migrate this legacy PHP class"

## Key Guidelines

### Always Use
- `declare(strict_types=1)` at file start
- Constructor property promotion
- Readonly properties for immutable data
- Enums instead of class constants
- Match expressions over switch
- Named arguments for clarity
- Type declarations everywhere
- PHPStan `@template` / array-shape annotations on public APIs
- Value objects for domain primitives (UserId, Email, Money)
- `final` by default; open only when extension is intentional

### Avoid
- Mixed type when specific type possible
- Hard-coded dependencies
- Fat interfaces
- Suppressing errors with @
- Global variables
- God classes
- Magic `__get` / `__set` / `__call` outside framework infrastructure
- Bare primitives where value objects express domain constraints

### Tooling Loop (mandatory)
```bash
vendor/bin/php-cs-fixer fix && vendor/bin/phpstan analyse
```

## References

- [PHP Manual](https://www.php.net/manual/)
- [PHP-FIG PSR Standards](https://www.php-fig.org/psr/)
- [PHP The Right Way](https://phptherightway.com/)
- [PHPStan](https://phpstan.org/)
- [php-cs-fixer](https://cs.symfony.com/)
- [Rector](https://getrector.com/)
