---
id: doc-openapi
title: OpenAPI Contracts, Examples, and Changelogs
category: doc
priority: MEDIUM
triggers: [missing-api-docs, schema-drift, missing-error-examples, undocumented-breaking-change]
tags: [documentation, openapi, swagger, examples, changelog]
---

# OpenAPI Contracts, Examples & Changelogs

**Trigger Anchor:** Publish contract-first OpenAPI 3.1 specs with realistic request/response examples for all status codes, paired with a machine-readable changelog.

---

### Bad
```yaml
# ❌ Vague OpenAPI schema without status codes, types, or realistic examples
paths:
  /orders:
    post:
      summary: Create order
      responses:
        '200':
          description: OK
```

### Good
```yaml
# ✅ Complete OpenAPI 3.1 specification with schema constraints and full examples
paths:
  /orders:
    post:
      summary: Create order
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
            examples:
              standardOrder:
                value:
                  items: [{ product_id: 'prod_123', quantity: 2 }]
      responses:
        '201':
          description: Order successfully created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '422':
          description: Validation error
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ProblemDetails'
```
