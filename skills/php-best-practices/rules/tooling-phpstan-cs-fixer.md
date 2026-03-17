---
title: PHPStan + php-cs-fixer Validation Loop
impact: CRITICAL
impactDescription: Catches type errors and style violations automatically before every commit
tags: tooling, phpstan, php-cs-fixer, static-analysis, ci, quality
---

# PHPStan + php-cs-fixer Validation Loop

Run PHPStan and php-cs-fixer as a mandatory feedback loop: fix style first, then verify types. Never skip either step. Integrate both into CI so unreviewed code cannot be merged.

## Setup

### Install

```bash
composer require --dev phpstan/phpstan
composer require --dev friendsofphp/php-cs-fixer

# Optional but recommended:
composer require --dev phpstan/extension-installer   # auto-loads PHPStan extensions
composer require --dev phpstan/phpstan-strict-rules  # extra strictness rules
composer require --dev phpstan/phpstan-deprecation-rules
```

### PHPStan Configuration (`phpstan.neon`)

```neon
parameters:
    level: 8          # raise to 9 for maximum strictness; start at 0 for legacy projects
    paths:
        - src
        - tests
    checkMissingIterableValueType: true
    checkGenericClassInNonGenericObjectType: true
    reportUnmatchedIgnoredErrors: true
    strictRules:
        allRules: true

    # Uncomment when migrating a legacy codebase:
    # includes:
    #     - phpstan-baseline.neon
```

### php-cs-fixer Configuration (`.php-cs-fixer.php`)

```php
<?php

$finder = PhpCsFixer\Finder::create()
    ->in([__DIR__ . '/src', __DIR__ . '/tests'])
    ->name('*.php')
    ->notPath('bootstrap/cache')
    ->ignoreDotFiles(true)
    ->ignoreVCS(true);

return (new PhpCsFixer\Config())
    ->setRiskyAllowed(true)
    ->setRules([
        '@PSR12'                           => true,
        '@PHP81Migration'                  => true,
        '@PHP82Migration'                  => true,
        'strict_param'                     => true,
        'declare_strict_types'             => true,      // auto-adds declare(strict_types=1)
        'array_syntax'                     => ['syntax' => 'short'],
        'ordered_imports'                  => ['sort_algorithm' => 'alpha'],
        'no_unused_imports'                => true,
        'not_operator_with_successor_space' => true,
        'trailing_comma_in_multiline'      => true,
        'phpdoc_order'                     => true,
        'phpdoc_separation'                => true,
        'phpdoc_scalar'                    => true,
        'unary_operator_spaces'            => true,
        'binary_operator_spaces'           => true,
        'blank_line_before_statement'      => ['statements' => ['return', 'throw', 'if', 'foreach', 'while']],
        'class_attributes_separation'      => ['elements' => ['method' => 'one', 'property' => 'one']],
        'single_quote'                     => true,
        'no_extra_blank_lines'             => true,
    ])
    ->setFinder($finder);
```

## The Validation Loop

Run these two commands in this order on every change:

```bash
# Step 1: Fix style automatically
vendor/bin/php-cs-fixer fix

# Step 2: Verify types (read-only, no auto-fix)
vendor/bin/phpstan analyse

# One-liner for convenience:
vendor/bin/php-cs-fixer fix && vendor/bin/phpstan analyse
```

**Why this order?** php-cs-fixer reformats code (adding `declare(strict_types=1)`, adjusting whitespace, sorting imports). Running PHPStan after ensures it analyses the final, formatted code and reports accurate line numbers.

## Composer Scripts

Add shortcuts to `composer.json` so every developer uses the same commands:

```json
{
    "scripts": {
        "cs":       "php-cs-fixer fix",
        "cs:check": "php-cs-fixer fix --dry-run --diff",
        "stan":     "phpstan analyse",
        "analyse":  ["@cs", "@stan"],
        "test":     "pest",
        "check":    ["@analyse", "@test"]
    }
}
```

Usage:

```bash
composer analyse   # fix style then run static analysis
composer check     # full quality gate: style + types + tests
```

## CI Integration (GitHub Actions)

```yaml
# .github/workflows/quality.yml
name: Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
          tools: composer, cs2pr

      - run: composer install --no-interaction --prefer-dist

      - name: php-cs-fixer (check only in CI)
        run: vendor/bin/php-cs-fixer fix --dry-run --diff --format=checkstyle | cs2pr

      - name: PHPStan
        run: vendor/bin/phpstan analyse --error-format=github
```

## Interpreting PHPStan Output

```
 ------ ----------------------------------------------------------
  Line   src/Services/UserService.php
 ------ ----------------------------------------------------------
  42     Parameter $id of method UserService::find() expects int,
         string given.
  67     Method UserService::create() should return App\Models\User
         but returns App\Models\User|null.
 ------ ----------------------------------------------------------
```

Fix these by correcting the type mismatch, not by adding `// @phpstan-ignore-next-line`. Suppressions are acceptable only for false positives (e.g., third-party library issues); document them:

```php
// @phpstan-ignore-next-line -- PHPStan cannot infer return type of legacy_fn()
$result = legacy_fn($id);
```

## PHPStan Level Guide

| Level | What Is Checked |
|-------|----------------|
| 0 | Basic checks — unknown classes, methods, properties |
| 1 | Possibly undefined variables, unknown magic methods |
| 2 | Unknown methods on all expressions |
| 3 | Return type checking |
| 4 | Dead code — always-false conditions |
| 5 | Methods/functions argument type checking |
| 6 | Type-check variables passed to native PHP functions |
| 7 | Report missing `@param`/`@return` type tags |
| 8 | Report nullable type mismatches |
| 9 | `mixed` type is not allowed without explicit annotation |

**Recommended progression for new projects:** start at 8, target 9.  
**Recommended progression for legacy projects:** start with `--generate-baseline`, fix violations, raise level by 1 at a time.

## Why

- **Automated Consistency**: php-cs-fixer eliminates style debates and enforces `declare(strict_types=1)` on every file automatically
- **Shift-Left Bug Detection**: PHPStan level 8+ catches `null` dereferences, type mismatches, and dead code before tests run
- **Living Documentation**: PHPDoc annotations required by PHPStan double as inline documentation consumed by IDEs
- **Objective Quality Metric**: PHPStan level is a measurable indicator of type-safety maturity; raise it incrementally
- **CI Enforcement**: The loop in CI ensures no unreviewed, non-conforming code reaches the main branch

Reference: [PHPStan](https://phpstan.org/) | [php-cs-fixer](https://cs.symfony.com/) | [Rector](https://getrector.com/)
