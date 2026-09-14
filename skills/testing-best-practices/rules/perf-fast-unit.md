---
id: perf-fast-unit
title: Fast Execution, Parallelism, and Test Tiers
category: perf
priority: LOW
triggers: [slow-unit-tests, sequential-test-suite, flat-test-directory, sleep-in-tests]
tags: [performance, fast-unit, parallel, concurrency, tiers]
---

# Fast Execution, Parallelism & Test Tiers

**Trigger Anchor:** Keep unit tests sub-50ms using pure logic and memory doubles; run test suites concurrently across cores, and separate fast unit suites from slower integration/e2e tiers.

---

## In-Memory Speed vs Network/DB Delays

### Bad
```typescript
// ❌ Connecting to real databases and third-party APIs in unit tests (adds seconds)
test('creates user', async () => {
  const pool = new Pool({ connectionString: 'postgres://localhost/test' });
  const res = await pool.query('INSERT INTO users(name) VALUES ($1) RETURNING *', ['Alice']);
  expect(res.rows[0].name).toBe('Alice');
});
```

### Good
```typescript
// ✅ In-memory doubles and pure logic execute in <2ms
test('creates user with in-memory double', async () => {
  const memoryRepo = { users: new Map(), save: vi.fn(async (u) => memoryRepo.users.set(u.id, u)) };
  const service = new UserService(memoryRepo);

  const user = await service.create({ id: 'u-1', name: 'Alice' });

  expect(memoryRepo.save).toHaveBeenCalledWith(user);
});
```

---

## Parallel Execution & Tiered Test Organization

### Bad
```typescript
// ❌ Monolithic test directory running all unit, integration, and slow browser tests together
// vitest.config.ts
export default defineConfig({
  test: {
    include: ['tests/**/*.test.ts'], // Single 45-second run on every file save!
    pool: 'forks',
    poolOptions: { forks: { singleFork: true } } // Forced sequential execution
  }
});
```

### Good
```typescript
// ✅ Tiered execution: unit tests in watch mode (<1s feedback), integration/e2e in CI
// vitest.config.ts (unit default: multi-threaded, parallel)
export default defineConfig({
  test: {
    include: ['src/**/*.unit.test.ts'],
    pool: 'threads',
    poolOptions: { threads: { minThreads: 2, maxThreads: 8 } }
  }
});

// Separate config for integration tests needing isolated database schemas:
// vitest.config.integration.ts -> include: ['src/**/*.integration.test.ts']
```
