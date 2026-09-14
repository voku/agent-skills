---
id: mock-boundaries
title: Mock at System Boundaries
category: mock
priority: MEDIUM
triggers: [mocking-internal-utils, over-mocking-logic, unverified-mock-calls, incomplete-mock-payloads, mock-returns-true]
tags: [mocking, boundaries, minimal-mocking, msw, verification]
---

# Mock at System Boundaries

**Trigger Anchor:** Mock only at external boundaries (HTTP, DB, message queues); preserve real internal logic, simulate realistic contracts (e.g. MSW), and verify critical side effects.

---

## Boundary Mocking vs Internal Utility Mocking

### Bad
```typescript
// ❌ Mocking internal helpers couples test to file structure and skips real business logic
vi.mock('./tax-calculator', () => ({ calculateTax: vi.fn().mockReturnValue(10) }));
vi.mock('./format-currency', () => ({ formatCurrency: vi.fn().mockReturnValue('$110') }));

test('processes order', () => {
  const result = processOrder({ price: 100 });
  expect(result.formatted).toBe('$110'); // Tests fake wiring, not real calculation!
});
```

### Good
```typescript
// ✅ Internal logic executes for real; only boundary clients (HTTP/DB) are mocked
test('processes order and charges boundary gateway', async () => {
  const mockGateway = { charge: vi.fn().mockResolvedValue({ id: 'txn_1', status: 'paid' }) };
  const processor = new OrderProcessor(mockGateway); // Real tax and pricing logic run

  const result = await processor.processOrder({ price: 100, taxRate: 0.1 });

  expect(result.total).toBe(110);
  expect(mockGateway.charge).toHaveBeenCalledWith(110);
  expect(mockGateway.charge).toHaveBeenCalledTimes(1);
});
```

---

## Realistic Contract Simulation with MSW

### Bad
```typescript
// ❌ Primitive mock response ignores real API schema and missing field errors
const mockFetch = vi.fn().mockResolvedValue({ ok: true, json: () => Promise.resolve({ success: true }) });
```

### Good
```typescript
// ✅ MSW intercepts HTTP requests with realistic payloads and error codes
import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  http.get('/api/users/:id', ({ params }) => {
    if (params.id === 'unknown') return HttpResponse.json({ error: 'User not found' }, { status: 404 });
    return HttpResponse.json({ id: params.id, name: 'Alice', email: 'alice@test.com', role: 'member' });
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('loads complete user profile via real HTTP client', async () => {
  const client = new UserApiClient();
  const user = await client.getUser('123');
  expect(user.role).toBe('member');
});
```
