---
id: rest-endpoints
title: REST Resource Endpoints and HTTP Semantics
category: rest
priority: CRITICAL
triggers: [verbs-in-url, singular-resource-name, wrong-http-method, incorrect-status-code, deeply-nested-urls, get-mutation]
tags: [rest, resource-design, http-methods, status-codes, endpoints]
---

# REST Resource Endpoints & HTTP Semantics

**Trigger Anchor:** Model URLs as plural nouns representing resources; map operations to standard HTTP methods and status codes, keeping nesting shallow (maximum 2 levels).

---

## Resource Naming & Nesting

### Bad
```text
# ❌ Verbs in URLs, singular naming, and deep hierarchical nesting
GET  /getUser?id=123
POST /api/createOrder
POST /users/123/orders/456/items/789/deleteItem
POST /orders/123/cancelOrder
```

### Good
```text
# ✅ Plural nouns, standard HTTP verbs, shallow nesting, action sub-resources
GET    /users/123
POST   /orders
DELETE /orders/456/items/789
POST   /orders/123/cancellations     # Or POST /orders/123/cancel
```

---

## Method and Status Code Semantics

### Bad
```typescript
// ❌ Always returning 200 OK with error payload, or mutating on GET
app.get('/users/delete', (req, res) => {
  db.deleteUser(req.query.id);
  res.status(200).json({ status: 'error', message: 'User deleted' });
});
```

### Good
```typescript
// ✅ Correct HTTP method and canonical status codes
app.post('/users', async (req, res) => {
  const user = await db.createUser(req.body);
  res.status(201).location(`/users/${user.id}`).json(user);
});

app.delete('/users/:id', async (req, res) => {
  await db.deleteUser(req.params.id);
  res.status(204).send();
});
```
