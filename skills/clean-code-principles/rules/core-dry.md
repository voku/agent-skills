---
id: core-dry
title: Don't Repeat Yourself (DRY)
category: core-principles
priority: critical
tags: [DRY, duplication, single-source-of-truth, extraction, maintainability]
related: [core-kiss, core-yagni, solid-srp]
---

# Don't Repeat Yourself (DRY)

Every piece of knowledge, business logic, or configuration must have a single, authoritative, unambiguous representation within a system.

DRY is about **knowledge duplication**, not syntax similarity. Code that looks identical but changes for different domain reasons should not be prematurely coupled.

---

## 1. Single Source of Truth for Values and Configuration

Avoid duplicating configuration, magic strings, and status values across multiple modules.

### Bad Example

```typescript
// ❌ Duplicate status strings and configuration scattered across files
// orderService.ts
if (order.status === 'pending') { /* ... */ }

// orderController.ts
return repo.findByStatus('pending');

// client.ts
const isPending = order.status === 'pending';
```

### Good Example

```typescript
// ✅ Single authoritative enum/constant
export const OrderStatus = {
  PENDING: 'pending',
  PROCESSING: 'processing',
  COMPLETED: 'completed',
  CANCELLED: 'cancelled'
} as const;

export type OrderStatus = typeof OrderStatus[keyof typeof OrderStatus];

// All layers reference the single source
if (order.status === OrderStatus.PENDING) { /* ... */ }
```

---

## 2. Extract Shared Domain Logic and Validation

When identical business rules or validations are repeated in multiple endpoints or workflows, extract them into reusable functions or domain services.

### Bad Example

```typescript
// ❌ Identical validation logic copy-pasted in multiple controllers
class UserController {
  createUser(data) {
    if (!data.email || !data.email.includes('@')) throw new Error('Invalid email');
    if (!data.password || data.password.length < 8) throw new Error('Password too short');
    // save...
  }

  updateUser(id, data) {
    if (!data.email || !data.email.includes('@')) throw new Error('Invalid email');
    if (!data.password || data.password.length < 8) throw new Error('Password too short');
    // update...
  }
}
```

### Good Example

```typescript
// ✅ Single validation module with centralized rules
export class UserValidator {
  static validate(data: UserInput): void {
    if (!data.email || !data.email.includes('@')) {
      throw new ValidationError('Invalid email address');
    }
    if (!data.password || data.password.length < 8) {
      throw new ValidationError('Password must be at least 8 characters');
    }
  }
}

class UserController {
  createUser(data) {
    UserValidator.validate(data);
    return this.service.create(data);
  }

  updateUser(id, data) {
    UserValidator.validate(data);
    return this.service.update(id, data);
  }
}
```

---

## 3. When NOT to DRY (Avoid Accidental Coupling)

Do not merge two pieces of code simply because they share identical lines if their **reasons for change** are independent.

```typescript
// ⚠️ Coincidental duplication - DO NOT extract into a shared helper:
function validateUserAge(age: number): boolean {
  return age >= 18; // Legal age requirement (statutory law)
}

function validateMinimumOrderQuantity(qty: number): boolean {
  return qty >= 18; // Warehouse packaging constraint (business policy)
}
// Merging these creates artificial coupling between legal compliance and warehouse operations.
```

### Rule of Three

Wait until you see duplication **three times** in the same context before extracting an abstraction. Extracting too early often results in the wrong abstraction, which is far more expensive to maintain than slight duplication.

## Why it Matters

1. **Defect Containment**: Fixing a bug or changing a business rule in one place fixes it everywhere.
2. **Consistency**: Eliminates subtle divergence where two copies drift apart over time.
3. **Auditability**: Makes it obvious where a given business rule is owned and enforced.
