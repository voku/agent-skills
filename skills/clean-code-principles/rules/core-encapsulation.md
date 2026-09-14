---
id: core-encapsulation
title: Encapsulation
category: core-principles
priority: critical
triggers: [public-mutable-properties, external-array-mutation, bypassed-domain-invariants, anemic-data-bag]
tags: [encapsulation, information-hiding, domain-invariants]
related: [solid-srp, core-law-demeter, solid-isp]
---

# Encapsulation

**Trigger Anchor:** Hide internal state. Expose intention-revealing methods that guarantee domain invariants are never violated by external callers.

---

### Bad (Direct Property Mutation Bypassing Invariants)
```typescript
// ❌ Callers directly manipulate internal state without validation or invariant checks
class Order {
  public items: OrderItem[] = [];
  public total: number = 0;
}

// External caller can corrupt invariants:
order.items.push(newItem); // Total is now out of sync!
order.total = -50; // Invalid negative total!
```

### Good (Encapsulated State with Invariant Protection)
```typescript
// ✅ Internal state is private; methods protect domain consistency
class Order {
  private _items: OrderItem[] = [];

  addItem(item: OrderItem): void {
    if (item.price < 0) throw new InvalidPriceError();
    this._items.push(item);
  }

  get items(): readonly OrderItem[] {
    return [...this._items]; // Read-only copy prevents external tampering
  }

  get total(): number {
    return this._items.reduce((sum, i) => sum + i.price * i.quantity, 0);
  }
}
```
