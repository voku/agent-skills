---
id: solid-lsp
title: SOLID - Liskov Substitution Principle (LSP)
category: solid-principles
priority: critical
tags: [SOLID, LSP, liskov-substitution, contracts, preconditions, postconditions]
related: [solid-ocp, solid-isp, core-composition]
---

# Liskov Substitution Principle (LSP)

Subtypes must be substitutable for their base types without altering the correctness of the program. A caller holding a reference to a base class or interface must be able to use any implementer without knowing its concrete class and without encountering unexpected errors or side effects.

---

## 1. Contract & Invariant Violations (The Rectangle / Square Trap)

Subclasses must preserve the behavioral invariants of the base class.

### Bad Example

```typescript
// ❌ Subclass changes the behavior of setters, breaking parent assumptions
class Rectangle {
  constructor(protected width: number, protected height: number) {}

  setWidth(w: number) { this.width = w; }
  setHeight(h: number) { this.height = h; }
  getArea(): number { return this.width * this.height; }
}

class Square extends Rectangle {
  // Violates LSP: setting width secretly mutates height!
  setWidth(w: number) { this.width = w; this.height = w; }
  setHeight(h: number) { this.width = h; this.height = h; }
}

function resizeGeometry(rect: Rectangle) {
  rect.setWidth(5);
  rect.setHeight(4);
  // Caller expects 20, but with a Square it returns 16!
  assert(rect.getArea() === 20);
}
```

### Good Example

```typescript
// ✅ Model shapes by shared capabilities, not flawed inheritance
interface Shape {
  getArea(): number;
}

class Rectangle implements Shape {
  constructor(public readonly width: number, public readonly height: number) {}
  getArea(): number { return this.width * this.height; }
}

class Square implements Shape {
  constructor(public readonly size: number) {}
  getArea(): number { return this.size * this.size; }
}
```

---

## 2. Preconditions and Postconditions Rules

1. **Cannot strengthen preconditions**: A derived class cannot require more from the caller than the base type (e.g. arbitrarily refusing valid inputs or demanding new state).
2. **Cannot weaken postconditions**: A derived class cannot guarantee less than the base contract promises (e.g. returning `null` when a non-null result is promised).
3. **Cannot introduce unexpected exception types**: Subclasses must not throw checked or unhandled exceptions that callers of the base contract cannot anticipate.

### Bad Example

```typescript
interface PaymentGateway {
  // Base contract: accepts any positive amount, returns transaction ID string
  charge(amount: number): Promise<string>;
}

class StrictGateway implements PaymentGateway {
  async charge(amount: number): Promise<string> {
    // ❌ Strengthens preconditions: callers of PaymentGateway cannot anticipate this restriction
    if (amount < 50) {
      throw new Error('Minimum order is $50');
    }
    // ❌ Weakens postconditions: returns empty string instead of valid transaction ID
    return '';
  }
}
```

### Good Example

```typescript
// ✅ Derived implementations honor or widen the contract
class StandardGateway implements PaymentGateway {
  async charge(amount: number): Promise<string> {
    if (amount <= 0) throw new InvalidAmountError();
    return `TXN_${Date.now()}`;
  }
}
```

## Why it Matters

1. **Polymorphic Safety**: Any implementation can be substituted into existing workflows with zero special casing.
2. **Eliminates `instanceof` Checks**: Violating LSP forces callers to check concrete types (`if (obj instanceof X)`), destroying polymorphism.
3. **Predictable Composition**: Components rely on predictable contracts across tests, mocks, and production drivers.
