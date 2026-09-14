---
name: laravel-testing
description: Laravel testing with Pest PHP or PHPUnit covering HTTP feature tests, model factories, database assertions, faking facades, authentication testing, and test organization. Triggers on tasks involving HTTP tests, model factories, database assertions, mocking facades, authentication testing, or test organisation patterns.
license: MIT
metadata:
  author: Laravel Community
  version: "2.0.0"
  laravelVersion: "11.x - 13.x"
  phpVersion: "8.2+"
---

# Laravel Testing — Pest PHP & PHPUnit

High-density testing guide for Laravel applications using Pest PHP or PHPUnit.

## Framework Selection Boundary

Before writing or reviewing test syntax, determine the framework from the target repository rather than from this skill:

1. Inspect `composer.json` for `pestphp/pest` and `phpunit/phpunit`.
2. Treat `tests/Pest.php` as concrete evidence that Pest is configured.
3. When Pest is installed on top of PHPUnit, follow the repository's existing Pest conventions for new tests unless task-local evidence requires PHPUnit style.
4. If the repository does not establish a test framework or convention, do not invent one; keep the uncertainty explicit until the project contract resolves it.

Laravel assertions and application behavior remain the subject of the relevant rule files; wrapper syntax must follow the framework actually configured by the target project.

## When to Apply

Reference these guidelines when:
- Writing feature or unit tests for Laravel endpoints and services
- Testing HTTP endpoints and verifying JSON payloads
- Defining model factories, states, and relationships
- Asserting database state and soft deletes
- Faking Mail, Queue, Notification, Event, or Storage facades
- Testing authenticated routes and Sanctum token abilities
- Organising test suites with project-appropriate Pest or PHPUnit constructs

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | HTTP & Feature Tests | CRITICAL | `http-` |
| 2 | Model Factories | CRITICAL | `factory-` |
| 3 | Database Assertions | HIGH | `db-` |
| 4 | Faking Facades | HIGH | `fake-` |
| 5 | Authentication Testing | HIGH | `auth-` |
| 6 | Test Organisation | MEDIUM | `pest-` |

## Quick Reference

### HTTP & Feature Tests
- [http-feature-testing.md](rules/http-feature-testing.md) - Structure HTTP endpoint tests around observable behavior, isolate database state, and verify response payloads with Laravel's assertion APIs.

### Model Factories
- [factory-definitions.md](rules/factory-definitions.md) - Keep default factory state minimal and move scenario variation into explicit states, sequences, and relationships.

### Database Assertions
- [db-assertions.md](rules/db-assertions.md) - Verify persistence through Laravel's database/model assertions instead of ad-hoc query checks.

### Faking Facades
- [fake-facades.md](rules/fake-facades.md) - Isolate external side effects with Laravel fakes and assert the observable payload/dispatch behavior.

### Authentication Testing
- [auth-testing.md](rules/auth-testing.md) - Use the authentication mechanism configured by the route/application, including session guards or Sanctum abilities where applicable.

### Test Organisation
- [pest-organization.md](rules/pest-organization.md) - When the project uses Pest, group related behavior, share setup deliberately, and replace repetitive cases with datasets.

## How to Use

Read only the rule files relevant to the current task. Ground Laravel, Pest, PHPUnit, and package-version behavior in the target repository before choosing syntax or APIs. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
