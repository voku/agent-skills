---
name: laravel-best-practices
description: Laravel conventions and best practices for architecture, Eloquent, controllers, APIs, validation, and security. 8 rules across 5 categories. Use when creating controllers, models, migrations, validation, services, or structuring Laravel applications. Triggers on tasks involving Laravel architecture, Eloquent, database, API development, or PHP patterns.
license: MIT
metadata:
  author: Laravel Community
  version: "3.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel Best Practices

Modern Laravel patterns, RESTful conventions, Eloquent ORM optimization, single-purpose actions, and security standards. Contains **8 consolidated rules across 5 categories** for building scalable, maintainable Laravel applications.

## Metadata

- **Version:** 3.0.0
- **Laravel Version:** 11.x - 13.x
- **PHP Version:** 8.2+
- **Rule Count:** 8 rules across 5 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Creating controllers, models, and service/action layers
- Writing database queries, relationships, and migrations
- Implementing input validation and form requests
- Building and versioning RESTful JSON APIs
- Hardening model mass-assignment and authorization

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Architecture & Structure | CRITICAL | `arch-` | 2 |
| 2 | Eloquent & Database | CRITICAL | `eloquent-` | 2 |
| 3 | Controllers & API Design | HIGH | `controller-` | 2 |
| 4 | Validation & Requests | HIGH | `validation-` | 1 |
| 5 | Security | HIGH | `sec-` | 1 |

## Quick Reference

### 1. Architecture & Structure (CRITICAL) — 2 rules
- [arch-layers-actions.md](rules/arch-layers-actions.md) - Extract business logic from controllers into invokable single-purpose Action classes or Services, transport structured request data via typed readonly DTOs, and encapsulate domain rules inside immutable Value Objects.
- [arch-events-queues.md](rules/arch-events-queues.md) - Decouple domain side effects using domain events and queued listeners, configure explicit queue routing, and ensure all queue jobs are idempotent.

### 2. Eloquent & Database (CRITICAL) — 2 rules
- [eloquent-querying.md](rules/eloquent-querying.md) - Prevent N+1 queries with eager loading (`with()`), process large record sets via cursor/chunking (`lazy()`, `chunkById()`), and encapsulate reusable query constraints in dedicated local query scopes.
- [eloquent-modeling.md](rules/eloquent-modeling.md) - Define model attribute casts via the modern `casts()` method returning typed cast arrays/enums, use `Attribute::make()` closures for accessors/mutators, and automate record lifecycles using the `Prunable` trait.

### 3. Controllers & API Design (HIGH) — 2 rules
- [controller-conventions.md](rules/controller-conventions.md) - Keep controllers thin and declarative by adhering to standard RESTful resource methods or single-action invokables (`__invoke`), leveraging route model binding, and delegating all business logic to dedicated actions.
- [controller-api-resources.md](rules/controller-api-resources.md) - Always transform HTTP API responses using `JsonResource` or `ResourceCollection` classes; never serialize Eloquent models directly to JSON.

### 4. Validation & Requests (HIGH) — 1 rule
- [validation-rules.md](rules/validation-rules.md) - Encapsulate validation in dedicated FormRequest classes, validate complex nested arrays using wildcard notation (`items.*.id`), leverage `Rule::when()` for conditional constraints, and create invokable `ValidationRule` classes.

### 5. Security (HIGH) — 1 rule
- [sec-mass-assignment.md](rules/sec-mass-assignment.md) - Protect models from mass-assignment privilege escalation by explicitly declaring `$fillable` attributes or using `Model::shouldBeStrict()`, and never pass raw `$request->all()` to model creation or updates.

## Key Patterns (Quick Reference)

```php
<?php

declare(strict_types=1);

namespace App\Http\Controllers\Orders;

use App\Domain\Orders\Actions\CreateOrderAction;
use App\Domain\Orders\Data\CreateOrderData;
use App\Http\Requests\Orders\StoreOrderRequest;
use App\Http\Resources\OrderResource;
use Illuminate\Http\JsonResponse;

final class StoreOrderController
{
    public function __invoke(
        StoreOrderRequest $request,
        CreateOrderAction $createOrder,
    ): JsonResponse {
        $order = $createOrder(CreateOrderData::fromRequest($request));

        return (new OrderResource($order))
            ->response()
            ->setStatusCode(201);
    }
}
```

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete Laravel patterns.
