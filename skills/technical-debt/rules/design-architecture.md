---
id: design-architecture
title: "Design Debt: Coupling, Circularity, and Leaky Boundaries"
category: design
priority: HIGH
triggers: [circular-dependency, leaky-abstraction, shotgun-surgery, tight-coupling]
tags: [architecture, ddd, coupling, layering, boundaries]
---

# Design Debt: Coupling, Circularity, and Leaky Boundaries

**Trigger Anchor:** Break circular module dependencies, enforce unidirectional layering (UI -> Domain -> Infrastructure), encapsulate implementation details behind cohesive domain interfaces, and eliminate shotgun surgery by locating related changes together.

---

### Bad
```typescript
// ❌ Circular dependency: User imports Order, Order imports User
// User.ts
import { Order } from './Order';

export class User {
  id!: string;
  orders: Order[] = [];

  addOrder(order: Order): void {
    this.orders.push(order);
  }
}

// Order.ts
import { User } from './User';

export class Order {
  id!: string;
  user!: User; // ❌ Direct circular coupling leads to cycle import errors and impossible serialization
}
```

```php
<?php

declare(strict_types=1);

// ❌ Leaky abstraction: Domain entity coupled directly to HTTP framework Request & Session
namespace App\Domain\Model;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Session;

class Invoice
{
    // Leaks transport layer directly into core domain entity
    public function applyDiscountsFromRequest(Request $request): void
    {
        $sessionCode = Session::get('promo_code');
        // Domain logic now cannot run in CLI, queue worker, or unit test without mocked HTTP Session
    }
}
```

### Good
```typescript
// ✅ Decoupled domain models using foreign IDs or unidirectional aggregates
export interface OrderReference {
  readonly orderId: string;
  readonly totalCents: number;
}

export class User {
  constructor(
    public readonly id: string,
    private readonly recentOrders: OrderReference[] = [],
  ) {}
}
```

```php
<?php

declare(strict_types=1);

// ✅ Pure domain model decoupled from HTTP/Framework transport
namespace App\Domain\Model;

final class Invoice
{
    public function applyDiscount(PromoCode $code): void
    {
        // Pure domain logic; caller (controller or CLI command) passes typed domain value
    }
}
```
