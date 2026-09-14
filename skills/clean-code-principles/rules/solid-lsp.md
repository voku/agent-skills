---
id: solid-lsp
title: Liskov Substitution Principle (LSP)
category: solid-principles
priority: critical
triggers: [subclass-throws-unsupported, unexpected-null-return, strengthened-precondition, weakened-postcondition, instanceof-branching]
tags: [SOLID, LSP, liskov-substitution, contracts, invariants]
---

# Liskov Substitution Principle (LSP)

**Trigger Anchor:** Subtypes must be substitutable for base types without altering program correctness. Do not strengthen preconditions, weaken postconditions, or change invariants.

---

### Bad (Behavioral Invariant Violation)
```typescript
// ❌ Subtype changes setter contract, breaking caller invariants
class Rectangle {
  constructor(protected w: number, protected h: number) {}
  setWidth(w: number) { this.w = w; }
  setHeight(h: number) { this.h = h; }
  area() { return this.w * this.h; }
}

class Square extends Rectangle {
  // Secretly mutates both dimensions: breaks callers expecting independent width/height
  setWidth(w: number) { this.w = w; this.h = w; }
  setHeight(h: number) { this.w = h; this.h = h; }
}
```

### Bad (Strengthened Precondition / Unexpected Throw)
```typescript
// ❌ Subtype refuses valid inputs accepted by base contract
interface PaymentGateway {
  charge(amount: number): Promise<string>;
}

class StrictGateway implements PaymentGateway {
  async charge(amount: number): Promise<string> {
    if (amount < 50) throw new Error('Minimum $50 required'); // ❌ Surprise precondition!
    return 'txn_123';
  }
}
```

### Good
```typescript
// ✅ Model by capability interfaces rather than leaky subclassing
interface Shape {
  area(): number;
}

class Rectangle implements Shape {
  constructor(private w: number, private h: number) {}
  area() { return this.w * this.h; }
}

class Square implements Shape {
  constructor(private size: number) {}
  area() { return this.size * this.size; }
}
```
