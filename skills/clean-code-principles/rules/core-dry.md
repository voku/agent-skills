---
id: core-dry
title: Don't Repeat Yourself (DRY)
category: core-principles
priority: critical
triggers: [copy-pasted-validation, duplicate-status-strings, coincidental-duplication-trap, rule-of-three]
tags: [DRY, duplication, single-source-of-truth, extraction]
---

# Don't Repeat Yourself (DRY)

**Trigger Anchor:** Every piece of business knowledge or configuration must have a single authoritative representation. DRY applies to domain knowledge, not coincidental syntax similarity.

---

### Bad (Scattered Constants & Duplicated Logic)
```typescript
// ❌ Magic strings repeated across modules
// fileA.ts: if (order.status === 'pending') { ... }
// fileB.ts: return repo.findByStatus('pending');

// ❌ Validation logic copied across multiple endpoints
class UserController {
  create(data) {
    if (!data.email.includes('@') || data.password.length < 8) throw new Error('Invalid');
  }
  update(data) {
    if (!data.email.includes('@') || data.password.length < 8) throw new Error('Invalid');
  }
}
```

### Good (Single Source of Truth)
```typescript
// ✅ Centralized status definition
export const OrderStatus = {
  PENDING: 'pending',
  COMPLETED: 'completed',
} as const;

// ✅ Centralized validator
export class UserValidator {
  static validate(data: UserInput): void {
    if (!data.email.includes('@')) throw new ValidationError('Invalid email');
    if (data.password.length < 8) throw new ValidationError('Password too short');
  }
}
```

### Guardrail: When NOT to DRY (Coincidental Similarity)
```typescript
// ⚠️ Do NOT extract if reasons for change are independent:
function checkAdultAge(age: number) { return age >= 18; } // Legal statutory rule
function checkMinBulkOrder(qty: number) { return qty >= 18; } // Warehouse packaging rule
// Extract only after seeing true duplication 3 times (Rule of Three).
```
