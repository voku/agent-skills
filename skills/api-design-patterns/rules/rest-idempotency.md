---
id: rest-idempotency
title: HTTP Idempotency and Safe Retries
category: rest
priority: CRITICAL
triggers: [non-idempotent-put, duplicate-charge, retry-side-effects, missing-idempotency-key]
tags: [rest, idempotency, put-vs-patch, safe-methods, retry]
---

# HTTP Idempotency & Safe Retries

**Trigger Anchor:** Ensure GET, PUT, and DELETE are strictly idempotent; require `Idempotency-Key` headers on mutating POST requests to protect against network retry duplicates.

---

## PUT vs PATCH Semantics

### Bad
```typescript
// ❌ Using PUT for partial mutation, causing accidental data erasure
// PUT /users/123 with body: { email: "new@example.com" }
app.put('/users/:id', async (req, res) => {
  // Overwriting entire record with partial payload deletes name, bio, and settings!
  const updated = await db.users.replace(req.params.id, req.body);
  res.json(updated);
});
```

### Good
```typescript
// ✅ PUT replaces whole resource; PATCH applies partial diff idempotently
app.put('/users/:id', async (req, res) => {
  // Requires full resource representation
  const user = await db.users.replace(req.params.id, req.body);
  res.json(user);
});

app.patch('/users/:id', async (req, res) => {
  // Applies delta without overwriting unspecified fields
  const user = await db.users.patch(req.params.id, req.body);
  res.json(user);
});
```

---

## Idempotency-Key on Mutating Operations

### Bad
```typescript
// ❌ Retrying a timed-out POST creates duplicate charges/orders
app.post('/payments', async (req, res) => {
  const charge = await stripe.charges.create(req.body);
  res.status(201).json(charge);
});
```

### Good
```typescript
// ✅ Cache response by Idempotency-Key to return identical response on retry
app.post('/payments', async (req, res) => {
  const key = req.headers['idempotency-key'];
  if (!key) return res.status(400).json({ error: 'Idempotency-Key required' });

  const cached = await redis.get(`idempotency:${key}`);
  if (cached) return res.status(200).json(JSON.parse(cached));

  const charge = await paymentGateway.charge(req.body);
  await redis.set(`idempotency:${key}`, JSON.stringify(charge), 'EX', 86400);

  res.status(201).json(charge);
});
```
