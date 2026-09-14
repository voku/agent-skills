---
id: sec-data-exposure
title: HTTPS Enforcement and Sensitive Data Protection
category: sec
priority: CRITICAL
triggers: [plaintext-http, leaked-password-hash, credit-card-in-log, api-key-in-response, missing-hsts]
tags: [security, https, hsts, sensitive-data, data-masking, pii]
---

# HTTPS Enforcement & Sensitive Data Protection

**Trigger Anchor:** Enforce HTTPS with HSTS; scrub password hashes, full payment cards, secret keys, and unmasked PII from all response bodies and logging pipelines.

---

### Bad
```typescript
// ❌ Exposing internal credentials in user response and logging raw payment card
app.get('/users/me', async (req, res) => {
  const user = await db.users.find(req.user.id);
  res.json(user); // Leaks password_hash, mfa_secret, and stripe_customer_secret!
});

app.post('/checkout', (req, res) => {
  logger.info('Processing payment', { body: req.body }); // Logs full PAN & CVV!
});
```

### Good
```typescript
// ✅ Explicit serialization DTOs, HSTS headers, and payment tokenization
app.use((req, res, next) => {
  res.setHeader('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
  next();
});

app.get('/users/me', async (req, res) => {
  const user = await db.users.find(req.user.id);
  res.json({
    id: user.id,
    email: user.email,
    name: user.name,
    created_at: user.created_at
  });
});
```
