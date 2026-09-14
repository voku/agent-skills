# Laravel Best Practices

Portable guidance for Laravel application architecture, Eloquent, controllers/resources, validation, events/queues, and security boundaries.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, framework-version table, or compiled set of examples.

## When to Use

Use this skill for general Laravel implementation or review work involving application structure, Eloquent/model behavior, controllers and API resources, validation, events/queues, or mass-assignment safety.

For database-performance work where query plans, indexes, locks, pagination, or zero-downtime migrations are the dominant concern, prefer the focused `laravel-database-optimization` skill.

## Routing

1. Ground the target project's Laravel/PHP versions and existing project conventions.
2. Read `SKILL.md` to select the canonical rules matching the observed problem.
3. Load only those rules instead of compiling the whole Laravel catalog into context.
4. Preserve project-local architecture and framework conventions unless evidence supports changing them.
5. Validate through the target repository's configured toolchain and report only observed results.

## Stable Boundaries

- Keep controllers thin and explicit; domain/application behavior belongs with focused owners.
- Make request validation, API transformation, and persistence boundaries visible and testable.
- Avoid N+1 and unsafe bulk persistence patterns, but route deep database optimization to its specialist skill.
- Keep queued side effects idempotent and failure behavior observable.
- Never pass untrusted request payloads directly into model mass assignment.

## Projection Boundary

Do not copy current rule IDs, counts, category totals, or framework-version tables into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.

## References

- [Laravel Documentation](https://laravel.com/docs)
- [Laravel Best Practices](https://github.com/alexeymezenin/laravel-best-practices)
