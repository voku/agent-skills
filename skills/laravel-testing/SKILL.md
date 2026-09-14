---
name: laravel-testing
description: Laravel testing with Pest PHP or PHPUnit. 6 rules across 6 categories covering HTTP feature tests, model factories, database assertions, faking facades, authentication testing, and Pest organization. Triggers on tasks involving HTTP tests, model factories, database assertions, mocking facades, authentication testing, or test organisation patterns.
license: MIT
metadata:
  author: Laravel Community
  version: "2.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel Testing — Pest PHP & PHPUnit

High-density testing guide for Laravel applications using Pest PHP or PHPUnit. Contains **6 consolidated rules across 6 categories** covering HTTP feature testing, model factories, database state assertions, facade fakes, authentication, and test organization.

## Metadata

- **Version:** 2.0.0
- **Laravel Version:** 11.x - 13.x
- **PHP Version:** 8.2+
- **Rule Count:** 6 rules across 6 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Writing feature or unit tests for Laravel endpoints and services
- Testing HTTP endpoints and verifying JSON schemas
- Defining model factories, states, and relationships
- Asserting database state and soft deletes
- Faking Mail, Queue, Notification, Event, or Storage facades
- Testing authenticated routes and Sanctum token abilities
- Organising test suites with Pest `describe` blocks and datasets

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | HTTP & Feature Tests | CRITICAL | `http-` | 1 |
| 2 | Model Factories | CRITICAL | `factory-` | 1 |
| 3 | Database Assertions | HIGH | `db-` | 1 |
| 4 | Faking Facades | HIGH | `fake-` | 1 |
| 5 | Authentication Testing | HIGH | `auth-` | 1 |
| 6 | Test Organisation | MEDIUM | `pest-` | 1 |

## Quick Reference

### 1. HTTP & Feature Tests (CRITICAL) — 1 rule
- [http-feature-testing.md](rules/http-feature-testing.md) - Structure HTTP endpoint tests around Arrange-Act-Assert, isolate tests with `RefreshDatabase`, and verify API payloads using fluent JSON assertions (`AssertableJson`).

### 2. Model Factories (CRITICAL) — 1 rule
- [factory-definitions.md](rules/factory-definitions.md) - Define minimal default factory states, encapsulate variations in explicit state methods (`admin()`, `canceled()`), chain relationships with `for()` and `has()`, and generate alternating values with sequences.

### 3. Database Assertions (HIGH) — 1 rule
- [db-assertions.md](rules/db-assertions.md) - Verify database persistence using built-in assertions (`assertDatabaseHas`, `assertDatabaseMissing`, `assertModelExists`, `assertSoftDeleted`) instead of manual query counts.

### 4. Faking Facades (HIGH) — 1 rule
- [fake-facades.md](rules/fake-facades.md) - Intercept and test side effects by faking Laravel facades (`Mail::fake()`, `Queue::fake()`, `Event::fake()`, `Storage::fake()`) with callback assertions verifying payload contents.

### 5. Authentication Testing (HIGH) — 1 rule
- [auth-testing.md](rules/auth-testing.md) - Authenticate test requests using `actingAs($user, $guard)` for session web guards, and `Sanctum::actingAs($user, $abilities)` for token-authenticated API endpoints.

### 6. Test Organisation (MEDIUM) — 1 rule
- [pest-organization.md](rules/pest-organization.md) - Group related tests inside `describe` blocks, isolate shared test setup in `beforeEach()`, and eliminate repetitive test cases with parameterised `->with([...])` datasets.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete Pest/PHPUnit examples.
