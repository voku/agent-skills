---
id: pattern-repository
title: Repository Pattern
category: design-patterns
priority: high
triggers: [raw-sql-in-business-logic, orm-leaking-to-domain, untestable-database-queries, query-duplication]
tags: [design-patterns, repository, data-access, persistence-decoupling]
related: [solid-dip, solid-srp, core-separation-concerns]
---

# Repository Pattern

**Trigger Anchor:** Mediate between the domain and data mapping layers using a collection-like interface for accessing domain entities. Keep raw queries out of business services.

---

### Bad (Raw SQL Leaking into Controllers & Business Logic)
```typescript
// ❌ Business service coupled to database schema and driver
class OrderService {
  async getActiveOrders(userId: string): Promise<Order[]> {
    const rows = await db.query(
      'SELECT o.*, i.sku, i.price FROM orders o JOIN order_items i ON o.id = i.order_id WHERE o.user_id = ? AND o.status = "active"',
      [userId]
    );
    // Complex mapping mixed into business service...
  }
}
```

### Good (Domain Entity Repository Contract)
```typescript
// ✅ Contract defines domain operations, hiding SQL / ORM specifics
interface OrderRepository {
  findById(id: string): Promise<Order | null>;
  findActiveByUser(userId: string): Promise<Order[]>;
  save(order: Order): Promise<void>;
}

class OrderService {
  constructor(private orders: OrderRepository) {}

  async completeOrder(id: string): Promise<void> {
    const order = await this.orders.findById(id);
    if (!order) throw new OrderNotFoundError(id);
    order.complete();
    await this.orders.save(order);
  }
}
```
