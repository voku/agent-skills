---
name: laravel-best-practices
description: Laravel conventions and best practices for architecture, Eloquent, controllers, APIs, validation, and security. Use when creating controllers, models, migrations, validation, services, or structuring Laravel applications. Triggers on tasks involving Laravel architecture, Eloquent, database, API development, or PHP patterns.
license: MIT
metadata:
  author: Laravel Community
  version: "3.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel Best Practices

Modern Laravel patterns for application boundaries, Eloquent, controllers/API resources, validation, events/queues, and mass-assignment safety.

## When to Apply

Reference these guidelines when:
- Creating controllers, models, and service/action layers
- Writing database queries, relationships, and migrations
- Implementing input validation and form requests
- Building RESTful JSON APIs
- Hardening model mass-assignment and authorization boundaries

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Architecture & Structure | CRITICAL | `arch-` |
| 2 | Eloquent & Database | CRITICAL | `eloquent-` |
| 3 | Controllers & API Design | HIGH | `controller-` |
| 4 | Validation & Requests | HIGH | `validation-` |
| 5 | Security | HIGH | `sec-` |

## Quick Reference

### Architecture & Structure (CRITICAL)
- [arch-layers-actions.md](rules/arch-layers-actions.md) - Extract business logic from controllers into focused application/domain boundaries, transport structured request data through typed DTOs, and keep domain invariants explicit.
- [arch-events-queues.md](rules/arch-events-queues.md) - Decouple side effects with events/queued listeners where appropriate, route queues explicitly, and make jobs idempotent.

### Eloquent & Database (CRITICAL)
- [eloquent-querying.md](rules/eloquent-querying.md) - Prevent N+1 queries, process large record sets safely, and encapsulate reusable query constraints.
- [eloquent-modeling.md](rules/eloquent-modeling.md) - Use explicit casts, accessors/mutators, relationships, and lifecycle behavior with analyzable model contracts.

### Controllers & API Design (HIGH)
- [controller-conventions.md](rules/controller-conventions.md) - Keep controllers thin and declarative, use route model binding, and delegate business behavior to focused owners.
- [controller-api-resources.md](rules/controller-api-resources.md) - Transform HTTP API responses through explicit Resource/Collection contracts instead of exposing models directly.

### Validation & Requests (HIGH)
- [validation-rules.md](rules/validation-rules.md) - Encapsulate request validation and authorization, including nested/conditional constraints and reusable rules.

### Security (HIGH)
- [sec-mass-assignment.md](rules/sec-mass-assignment.md) - Keep model write boundaries explicit and never feed untrusted request payloads directly into persistence.

## Key Pattern

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

Read only the rule files relevant to the current task. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
