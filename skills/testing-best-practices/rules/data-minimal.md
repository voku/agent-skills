---
id: data-minimal
title: Minimal and Realistic Test Data
category: data
priority: HIGH
triggers: [irrelevant-fixture-noise, ascii-only-strings, dummy-1234-placeholders, inline-repetitive-fixtures]
tags: [test-data, minimal, realistic, fixtures, edge-cases]
---

# Minimal & Realistic Test Data

**Trigger Anchor:** Include only the fields relevant to the behavior under test while ensuring values reflect real-world constraints (unicode, actual formats, reusable fixtures).

---

## Minimal Data vs Noise

### Bad
```typescript
// ❌ Cluttered test payload with dozens of fields irrelevant to email validation
test('validates email format', () => {
  const user = {
    id: 'u-1',
    name: 'John',
    email: 'john@example.com',
    billingPlan: 'enterprise',
    preferences: { darkTheme: true, notifications: ['email', 'sms'] },
    registeredIp: '192.168.1.1'
  };
  expect(validateEmail(user.email)).toBe(true);
});
```

### Good
```typescript
// ✅ Test passes only the exact input that matters
test('validates email format', () => {
  expect(validateEmail('john@example.com')).toBe(true);
  expect(validateEmail('invalid-format')).toBe(false);
});
```

---

## Realistic Edge Values & Shared Fixtures

### Bad
```typescript
// ❌ Unrealistic 'test' placeholders miss internationalization and gateway format rules
const dummyUser = { name: 'test', card: '1234', zip: '123' };
```

### Good
```typescript
// ✅ Realistic values (Unicode, gateway-provided test tokens, central fixtures)
export const billingFixtures = {
  visaSuccess: { paymentMethod: 'pm_card_visa' },
  cardDeclined: { paymentMethod: 'pm_card_chargeDeclined' }
};

test('handles international user names and standard gateway formats', async () => {
  const user = { name: 'José García-López', email: 'jose@example.com' };
  const payment = await processPayment(user, billingFixtures.visaSuccess, 99.50);

  expect(payment.status).toBe('succeeded');
});
```
