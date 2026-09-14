# Testing Best Practices - Agent Documentation

**Version:** 2.0.0  
**Focus:** Unit Testing, Integration Testing, Test-Driven Development (TDD), Isolation, Mocking  
**Rules:** 11 rules across 7 categories  
**License:** MIT  

---

This skill provides testing best practices, isolation strategies, mock boundaries, and regression-first principles for building reliable, fast, and maintainable test suites.

## Operational Contract

When applying this skill, agents must:
- Treat this skill as repo-owned guidance and defer to repository or task-specific instructions when they conflict.
- Follow the regression-first discipline: isolate bugs in the narrowest failing test before modifying production code.
- Limit work to the smallest relevant test file and rule set for the current request.
- Stop and ask when the test framework, validation command, or requirement is missing or contradictory.
- Prefer machine-readable evidence first (e.g. failing assertion outputs, coverage diffs), then summarize tests added or updated.

## Validation & Evidence

- Run the repository's existing test command (e.g., `npm test`, `vitest run`, `composer test`, `pytest`) in documented order.
- If the repository does not define a test runner, say so instead of inventing one.

## When to Use This Skill

Activate this skill when:
- Writing unit, integration, or end-to-end tests
- Reviewing test code quality and test isolation
- Fixing bugs (verifying reproduction before code edits)
- Refactoring tests or resolving flaky test suites
- Designing mock strategies and test data generators
- Establishing test suites and CI testing tiers

## Trigger Phrases

- "write tests"
- "unit tests"
- "integration tests"
- "TDD"
- "testing best practices"
- "fix flaky test"
- "mock API"
- "test coverage"
- "regression test"

## Skill Structure

```
testing-best-practices/
├── SKILL.md              # Main skill definition & quick reference
├── AGENTS.md             # This file - agent guidance
├── README.md             # User-facing overview
├── metadata.json         # Structured metadata
└── rules/
    ├── _sections.md      # Category definitions
    ├── _template.md      # Rule template
    ├── struct-*.md       # Test Structure (2 rules: aaa-pattern, lifecycle)
    ├── iso-*.md          # Test Isolation (2 rules: independence, cleanup)
    ├── assert-*.md       # Assertions (1 rule: specific)
    ├── data-*.md         # Test Data (2 rules: factories, minimal)
    ├── mock-*.md         # Mocking (1 rule: boundaries)
    ├── cov-*.md          # Coverage (2 rules: regression-first, edge-cases)
    └── perf-*.md         # Performance (1 rule: fast-unit)
```

## Rule Categories

### 1. Test Structure (`struct-`, CRITICAL)
- `struct-aaa-pattern`: Arrange-Act-Assert narrative flow, single logical assertions per test, scenario-focused descriptive naming, and BDD (Given-When-Then) blocks.
- `struct-lifecycle`: Scoped lifecycle hooks (`beforeAll`/`afterAll` for heavy shared connections, `beforeEach`/`afterEach` for fresh per-test state).

### 2. Test Isolation (`iso-`, CRITICAL)
- `iso-independence`: Self-contained, deterministic tests with zero shared mutable state, order-independence, and controlled doubles for time and randomness.
- `iso-cleanup`: Explicit teardown of disk files, database tables, environment variables, servers, and event listeners.

### 3. Assertions (`assert-`, HIGH)
- `assert-specific`: Exact matchers (`toBe`, `toMatchObject`, `rejects.toThrow`), standard `expect(actual).toBe(expected)` ordering, named domain constants over magic numbers, and custom matchers.

### 4. Test Data (`data-`, HIGH)
- `data-factories`: Factory functions with sensible defaults, fluent builders for complex configurations, and seeded faker utilities for reproducible variety.
- `data-minimal`: Minimal sufficient test payloads vs realistic edge-case fixtures (unicode, format validation, centralized fixtures).

### 5. Mocking (`mock-`, MEDIUM)
- `mock-boundaries`: Mock only at external system boundaries (HTTP, databases, queues); keep internal business logic unmocked; simulate realistic contracts (MSW); verify essential side effects.

### 6. Coverage (`cov-`, HIGH)
- `cov-regression-first`: Narrowest failing reproduction test before code fixes; adversarial probing of boundaries, tenant scopes, and invalid transitions before writing happy paths.
- `cov-edge-cases`: Focus testing effort on decision branches, boundary values (null, empty, extremes), and error handling rather than vanity line-coverage numbers.

### 7. Performance (`perf-`, LOW)
- `perf-fast-unit`: Sub-50ms unit tests using in-memory doubles; parallel multi-core execution; tiered separation of fast unit tests from slower integration/e2e tests.

## Practical Application Examples

### Example 1: Bug Fix with Regression-First Discipline

**User:** "Fix a bug where users with expired subscriptions can still download invoices."

**Agent Approach:**
1. Reference `cov-regression-first` and `struct-aaa-pattern`.
2. Write a minimal failing test with an expired subscription payload attempting to download an invoice.
3. Run the test runner to prove failure (red).
4. Update production subscription guard logic.
5. Rerun the test to prove it passes (green).

### Example 2: Eliminating Flaky Tests

**User:** "Our test suite fails intermittently in CI but passes locally."

**Agent Approach:**
1. Reference `iso-independence` and `iso-cleanup`.
2. Inspect for shared mutable state (module variables, global caches, database rows persisting across tests).
3. Check for unmocked system clocks, timeouts, or race conditions.
4. Ensure `afterEach` hooks clean up modified `process.env` or scratch files.

### Example 3: Over-Mocking Refactoring

**User:** "Our tests break whenever we extract helper functions, even though the feature works."

**Agent Approach:**
1. Reference `mock-boundaries`.
2. Remove mocks on internal utility modules (e.g. currency formatters, validation functions).
3. Keep mocks strictly at boundary clients (HTTP requests, database drivers).
4. Verify tests pass against real business logic.
