# Testing Best Practices v2.0.0

Unit testing, integration testing, and TDD principles for reliable, maintainable test suites.

## Overview

- **Test structure:** AAA pattern, descriptive names, single logical assertion, scoped lifecycle hooks
- **Test isolation:** Independent, deterministic, zero shared mutable state, guaranteed cleanup, test doubles
- **Assertions:** Specific matchers, `expect(actual).toBe(expected)`, domain constants, custom matchers
- **Test data:** Factories with defaults, fluent builders, seeded faker, minimal inputs, realistic fixtures
- **Mocking:** Boundaries only, verify interactions, avoid over-mocking, MSW contract simulation
- **Coverage:** Regression-first reproduction, adversarial probing, edge cases, error scenarios, meaningful coverage
- **Performance:** Sub-50ms unit tests, parallel execution, tiered test organization
- **Total Rules:** 11 rules across 7 categories

## Categories

### 1. Test Structure (Critical)
AAA pattern, single logical assertions, descriptive scenario naming, and scoped setup/teardown hooks.

### 2. Test Isolation (Critical)
Self-contained tests, zero shared mutable state, deterministic execution, explicit resource cleanup, and test doubles.

### 3. Assertions (High)
Specific matchers, expected-actual ordering, domain constants over magic numbers, and custom matchers.

### 4. Test Data (High)
Factories, builders, seeded faker generation, minimal sufficient inputs, and realistic fixtures.

### 5. Mocking (Medium)
Mock at external system boundaries, preserve real internal logic, verify interactions, and use realistic MSW contracts.

### 6. Coverage (High)
Regression-first bug reproduction, adversarial probing, boundary values, error paths, and avoiding vanity metrics.

### 7. Performance (Low)
Sub-50ms unit tests, multi-threaded parallel execution, and organized speed tiers (unit/integration/e2e).

## Usage

```
Write tests for this service class
Review my test code for best practices
Set up testing strategy for this project
```

## References

- [Vitest Documentation](https://vitest.dev)
- [Jest Documentation](https://jestjs.io)
- [Testing Library](https://testing-library.com)
- [MSW (Mock Service Worker)](https://mswjs.io)
