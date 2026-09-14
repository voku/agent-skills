---
id: sec-auth-protection
title: API Authentication, Authorization, and Rate Limiting
category: sec
priority: CRITICAL
triggers: [wildcard-cors, missing-rate-limit, auth-in-query-string, missing-authorization-check, unvalidated-request-body]
tags: [security, authentication, authorization, rbac, rate-limiting, cors]
---

# API Authentication, Authorization & Rate Limiting

**Trigger Anchor:** Enforce standard `Authorization: Bearer` tokens, scoped RBAC permission checks, strict schema validation, standard rate limiting (`429` with `Retry-After`), and explicit CORS allowlists.

---

## Authentication & Authorization

### Bad
```typescript
// ❌ Token accepted via URL query parameter; no ownership check on resource
app.get('/accounts/:id', async (req, res) => {
  const token = req.query.token; // Leaked in access logs and browser history!
  const account = await db.getAccount(req.params.id);
  res.json(account); // Any authenticated user can view any other user's account!
});
```

### Good
```typescript
// ✅ Bearer token from header with tenant/ownership authorization check
app.get('/accounts/:id', authenticateBearer, async (req, res) => {
  const account = await db.getAccount(req.params.id);
  if (!account) return res.status(404).json({ title: 'Not Found' });

  if (account.ownerId !== req.user.id && !req.user.hasRole('admin')) {
    return res.status(403).json({ title: 'Forbidden', code: 'INSUFFICIENT_PERMISSIONS' });
  }

  res.json(account);
});
```

---

## Rate Limiting & Strict CORS

### Bad
```typescript
// ❌ Wildcard CORS with credentials; unbounded endpoints vulnerable to DoS
app.use(cors({ origin: '*', credentials: true }));
```

### Good
```typescript
// ✅ Strict origin whitelist and standard rate limit headers
app.use(cors({
  origin: ['https://app.example.com'],
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
}));

// Rate limiter returns 429 when quota is exceeded
app.use(rateLimiter({
  windowMs: 60 * 1000,
  max: 100,
  handler: (req, res) => {
    res.set('Retry-After', '60');
    res.status(429).json({ title: 'Too Many Requests', code: 'RATE_LIMIT_EXCEEDED' });
  }
}));
```
