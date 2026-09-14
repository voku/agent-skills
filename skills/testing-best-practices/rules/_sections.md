# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Test Structure (struct)

**Impact:** CRITICAL  
**Description:** Fundamental patterns for organizing test code: AAA pattern, scenario-focused descriptive naming, single logical assertions, and scoped lifecycle hooks (`beforeAll`/`beforeEach`/`afterEach`/`afterAll`).

## 2. Test Isolation (iso)

**Impact:** CRITICAL  
**Description:** Tests must run independently and deterministically without shared mutable state, order dependencies, or resource leaks, using test doubles to freeze time and isolate boundaries.

## 3. Assertions (assert)

**Impact:** HIGH  
**Description:** Effective assertions expressing clear intent: specific matchers, standard `expect(actual).toBe(expected)` ordering, named domain constants, and reusable custom matchers.

## 4. Test Data (data)

**Impact:** HIGH  
**Description:** Maintainable test data generation: factory functions with sensible defaults, fluent builders, seeded faker generation, minimal sufficient inputs, and realistic fixtures.

## 5. Mocking (mock)

**Impact:** MEDIUM  
**Description:** Mock only at external system boundaries (HTTP, DB, message queues), verify essential side effects, and simulate realistic contracts (e.g. MSW).

## 6. Coverage (cov)

**Impact:** HIGH  
**Description:** Evidence-driven coverage: regression-first reproduction before fixes, adversarial input probing, decision branch and error path testing, and avoiding vanity line coverage.

## 7. Performance (perf)

**Impact:** LOW  
**Description:** Fast developer feedback loops: sub-50ms unit tests using memory doubles, parallel test execution, and tiered test organization.
