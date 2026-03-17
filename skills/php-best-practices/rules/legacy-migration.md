---
title: Legacy Code Migration Strategy
impact: HIGH
impactDescription: Safely modernizes legacy PHP codebases without introducing regressions
tags: legacy, migration, refactoring, rector, phpstan, modernization
---

# Legacy Code Migration Strategy

Migrating legacy PHP code requires a structured, incremental approach. Never rewrite everything at once. Apply the Strangler Fig pattern: add a safety net first, then refactor in small, verifiable steps guided by static analysis.

## Migration Phases

### Phase 1 — Safety Net (Do First)

Before touching any code, establish baselines so regressions surface immediately:

```bash
# 1. Capture current PHPStan baseline (do not fix violations yet)
vendor/bin/phpstan analyse --generate-baseline phpstan-baseline.neon

# 2. Capture current php-cs-fixer diff (do not apply yet)
vendor/bin/php-cs-fixer fix --dry-run --diff > /tmp/cs-baseline.diff

# 3. Ensure existing tests pass before any change
vendor/bin/pest --stop-on-failure
# or
vendor/bin/phpunit
```

```neon
# phpstan.neon — start permissive, tighten over time
includes:
    - phpstan-baseline.neon

parameters:
    level: 0          # raise to 1, 2, … 9 as violations are fixed
    paths:
        - src
```

### Phase 2 — Automated Syntax Modernization

Use Rector to apply safe, automated transformations:

```bash
# Install Rector
composer require --dev rector/rector

# Dry-run to preview changes
vendor/bin/rector process src --dry-run

# Apply when satisfied
vendor/bin/rector process src
```

```php
<?php

// rector.php — incremental upgrades
use Rector\Config\RectorConfig;
use Rector\Set\ValueObject\SetList;
use Rector\Set\ValueObject\LevelSetList;

return RectorConfig::configure()
    ->withPaths([__DIR__ . '/src'])
    ->withSets([
        LevelSetList::UP_TO_PHP_81,   // bump to target PHP version
        SetList::DEAD_CODE,
        SetList::CODE_QUALITY,
        SetList::TYPE_DECLARATION,
    ]);
```

### Phase 3 — Incremental Type Coverage

Add types file-by-file. Start with the most-called classes:

```php
<?php

// BEFORE — typical legacy file
class UserService
{
    function getUser($id)
    {
        return $this->db->query("SELECT * FROM users WHERE id = $id");
    }

    function createUser($data)
    {
        // Mixed $data, no return type, SQL injection risk
        $this->db->query("INSERT INTO users ...");
    }
}
```

```php
<?php

declare(strict_types=1);

// AFTER — incrementally typed
final class UserService
{
    public function __construct(
        private readonly UserRepository $repository,
    ) {}

    public function getUser(int $id): ?User
    {
        return $this->repository->find(new UserId($id));
    }

    /** @param array{name: string, email: string} $data */
    public function createUser(array $data): User
    {
        return $this->repository->create(
            name: new UserName($data['name']),
            email: new Email($data['email']),
        );
    }
}
```

### Phase 4 — Extract, Isolate, Replace

Apply the Strangler Fig pattern to isolate legacy logic:

```php
<?php

declare(strict_types=1);

// Step 1 — Wrap legacy code behind a typed interface
interface LegacyOrderGateway
{
    /** @return array{id: int, total: float, status: string} */
    public function fetchOrder(int $id): array;
}

// Step 2 — Adapter delegates to legacy code
final class LegacyOrderAdapter implements LegacyOrderGateway
{
    public function fetchOrder(int $id): array
    {
        // Calls the old global function / procedural code
        $raw = legacy_get_order($id);
        return [
            'id'     => (int) $raw['order_id'],
            'total'  => (float) $raw['order_total'],
            'status' => (string) $raw['order_status'],
        ];
    }
}

// Step 3 — New service depends on the interface, not the legacy code
final class OrderService
{
    public function __construct(
        private readonly LegacyOrderGateway $gateway,
    ) {}

    public function getOrder(int $id): Order
    {
        $data = $this->gateway->fetchOrder($id);
        return Order::fromArray($data);
    }
}

// Step 4 — When ready, replace LegacyOrderAdapter with a proper repository
// without touching OrderService
```

## What to Fix First (Priority Order)

| Priority | Fix | Why |
|----------|-----|-----|
| 1 | Add `declare(strict_types=1)` | Foundation for all other type work |
| 2 | Fix SQL injection (prepared statements) | Security — immediate risk |
| 3 | Add return types to public methods | Unblocks PHPStan analysis |
| 4 | Replace `array` params with typed arrays / value objects | Eliminates `mixed` propagation |
| 5 | Extract classes from God classes | Enables focused unit testing |
| 6 | Replace `@` suppression with proper error handling | Unmasks hidden failures |
| 7 | Raise PHPStan level | Validates all prior work |

## Never Do This

```php
<?php

// DON'T: big-bang rewrite of a working class
// Copy-paste the class, rewrite from scratch, hope tests cover it
// Result: weeks of work, high regression risk

// DON'T: mix legacy and modern code in the same function
function processOrder($id) // no types
{
    $order = legacy_get_order($id); // old code
    return new ModernOrderDTO(...); // new code — incompatible styles
}

// DON'T: remove tests to make the migration easier
```

## Tracking Migration Progress

Commit a migration checklist to the repository:

```markdown
## Migration Progress

- [x] PHPStan baseline captured (1,423 violations at level 0)
- [x] Rector applied — PHP 8.1 syntax transformations
- [x] `declare(strict_types=1)` added to all files
- [ ] PHPStan level raised to 3 (current: 1)
- [ ] SQL injection: 12 of 34 query sites migrated to PDO
- [ ] Value objects: UserId, Email, Money created; 8 of 25 services migrated
- [ ] God class `OrderManager` (1,200 lines) → extract 4 focused classes
```

## Why

- **No Regressions**: The safety net (tests + PHPStan baseline + CS baseline) catches unintended behavior changes at every step
- **Incremental Confidence**: Small steps produce visible, verifiable progress rather than a long-running rewrite branch
- **Tool-Assisted**: Rector automates ~80% of mechanical transformations, freeing human effort for architectural decisions
- **PHPStan Level as Metric**: Raising the level from 0 → 9 provides a measurable, objective indicator of type-safety improvement
- **Strangler Fig**: The legacy code continues to run while new code grows around it, reducing risk to production

Reference: [Rector Documentation](https://getrector.com/documentation) | [PHPStan Baseline](https://phpstan.org/user-guide/baseline) | [Strangler Fig Pattern — Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)
