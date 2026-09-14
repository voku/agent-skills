---
id: core-separation-concerns
title: Separation of Concerns (SoC)
category: core-principles
priority: critical
triggers: [mixed-layers, sql-in-controllers, html-in-database-layer, business-logic-in-ui, tangled-responsibilities]
tags: [separation-of-concerns, layering, modularity, architecture]
related: [solid-srp, core-law-demeter]
---

# Separation of Concerns (SoC)

**Trigger Anchor:** Divide software into distinct sections, each addressing a separate technical or domain concern (e.g. presentation, domain logic, data access).

---

### Bad (Tangled Presentation, Business Logic, and SQL in One Place)
```typescript
// ❌ Controller mixes HTTP parsing, business rules, raw SQL, and HTML rendering
class OrderController {
  async handleRequest(req: Request, res: Response) {
    // 1. Raw SQL query
    const items = await db.query('SELECT * FROM cart WHERE user_id = ?', [req.userId]);

    // 2. Business calculation
    let total = items.reduce((sum, i) => sum + i.price, 0);
    if (total > 100) total *= 0.9;

    // 3. Presentation rendering
    res.send(`<div>Total: $${total}</div>`);
  }
}
```

### Good (Clean Layer Boundaries)
```typescript
// ✅ Presentation / HTTP Layer
class OrderController {
  constructor(private orderService: OrderApplicationService) {}

  async handleRequest(req: Request, res: Response) {
    const orderDto = await this.orderService.checkout(req.userId);
    res.json(orderDto);
  }
}

// ✅ Domain / Application Layer
class OrderApplicationService {
  constructor(private cartRepo: CartRepository) {}

  async checkout(userId: string): Promise<OrderDto> {
    const cart = await this.cartRepo.findByUser(userId);
    return cart.calculateCheckout();
  }
}
```
