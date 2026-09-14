---
name: testing-best-practices
description: Unit testing, integration testing, and test-driven development principles. Use when writing tests, reviewing test code, improving test coverage, or setting up testing strategy. Triggers on "write tests", "review tests", "testing best practices", or "TDD".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Testing Best Practices

Unit testing, integration testing, and TDD principles for reliable, maintainable test suites. Contains 11 rules across 7 categories using TypeScript with Jest/Vitest.

## Metadata

- **Version:** 2.0.0
- **Rule Count:** 11 rules across 7 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Writing unit or integration tests
- Reviewing test code quality
- Improving test coverage strategy
- Setting up testing infrastructure
- Debugging flaky or slow tests

## Test Expansion Discipline

- For bug fixes, start with the narrowest failing regression test before changing production code.
- When asked for "more tests" or "more coverage", target a real branch, edge case, or defect-prone path instead of optimizing for headline line coverage.
- Set up only the dependencies the code under test actually touches.
- Follow the nearest existing repository test style before introducing a new test pattern.
- Prefer small local test doubles or inline collaborators when they keep the setup obvious and avoid unnecessary fixture sprawl.

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Test Structure | CRITICAL | `struct-` | 2 |
| 2 | Test Isolation | CRITICAL | `iso-` | 2 |
| 3 | Assertions | HIGH | `assert-` | 1 |
| 4 | Test Data | HIGH | `data-` | 2 |
| 5 | Mocking | MEDIUM | `mock-` | 1 |
| 6 | Coverage | HIGH | `cov-` | 2 |
| 7 | Performance | LOW | `perf-` | 1 |

## Quick Reference

### 1. Test Structure (`struct-`, CRITICAL)
- `struct-aaa-pattern` - Arrange-Act-Assert flow, single logical assertions, descriptive scenario naming, and BDD specifications
- `struct-lifecycle` - Scoped setup and teardown hooks (`beforeAll`, `beforeEach`, `afterEach`, `afterAll`)

### 2. Test Isolation (`iso-`, CRITICAL)
- `iso-independence` - Self-contained, deterministic tests with zero shared mutable state, order-independence, and controlled doubles
- `iso-cleanup` - Explicit cleanup of files, database tables, environment variables, network servers, and event listeners

### 3. Assertions (`assert-`, HIGH)
- `assert-specific` - Specific matchers, `expect(actual).toBe(expected)` convention, domain constants over magic numbers, and custom matchers

### 4. Test Data (`data-`, HIGH)
- `data-factories` - Factory functions with sensible defaults, fluent builders, and seeded faker generation
- `data-minimal` - Minimal sufficient test data vs realistic edge-case fixtures (unicode, format validation, shared fixtures)

### 5. Mocking (`mock-`, MEDIUM)
- `mock-boundaries` - Mock only at external system boundaries (HTTP, DB), preserve real business logic, verify interactions, and use MSW contracts

### 6. Coverage (`cov-`, HIGH)
- `cov-regression-first` - Narrowest failing reproduction test before code fixes, and adversarial probing before happy paths
- `cov-edge-cases` - Focus coverage on decision branches, boundary values (null, empty, extremes), and error paths over vanity metrics

### 7. Performance (`perf-`, LOW)
- `perf-fast-unit` - Sub-50ms unit tests using in-memory doubles, parallel test execution, and tiered test organization

## Essential Guidelines

### Regression-First Bug Fixes

```typescript
// Prefer this sequence:
// 1. isolate the bug in the smallest failing test
// 2. confirm it fails for the right reason (red)
// 3. change production code
// 4. rerun the same test until it passes (green)
// 5. widen validation only if the change touches shared behavior
```

### AAA Pattern (Arrange, Act, Assert)

```typescript
it('calculates total with discount', () => {
  // Arrange
  const cart = new ShoppingCart();
  cart.addItem({ name: 'Book', price: 20 });
  cart.applyDiscount(0.1);

  // Act
  const total = cart.getTotal();

  // Assert
  expect(total).toBe(18);
});
```

### Descriptive Test Names

```typescript
// ✅ Describes behavior and scenario
describe('UserService.register', () => {
  it('creates user with hashed password', () => {});
  it('throws ValidationError when email is invalid', () => {});
  it('sends welcome email after successful registration', () => {});
});
```

### Test Isolation

```typescript
// ✅ Each test sets up its own fresh instance
beforeEach(() => {
  mockRepository = { save: vi.fn(), find: vi.fn() };
  service = new OrderService(mockRepository);
});
```

## References

- [Vitest Documentation](https://vitest.dev)
- [Jest Documentation](https://jestjs.io)
- [Testing Library](https://testing-library.com)
- [MSW (Mock Service Worker)](https://mswjs.io)

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`
