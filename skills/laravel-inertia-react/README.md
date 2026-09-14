# Laravel + Inertia.js + React

Portable guidance for Laravel applications that use Inertia.js with React.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, dependency/version matrix, or compiled set of examples.

## When to Use

Use this skill for work involving:
- typed Inertia page props and partial reload/state preservation;
- `useForm` lifecycle, validation errors, uploads, and processing state;
- `<Link>` / router navigation;
- middleware-provided shared props;
- persistent React layouts across Inertia navigation.

## Routing

1. Ground the target repository's Laravel, Inertia, React, TypeScript, Ziggy, and PHP versions.
2. Read `SKILL.md` to select the canonical rules matching the observed problem.
3. Load only those rule files instead of compiling the whole integration guide into context.
4. Preserve target-project route names, types, middleware contracts, and validation/authorization boundaries.
5. Validate through the target repository's configured toolchain and report only observed results.

## Stable Boundaries

- Server-side validation and authorization remain authoritative for writes.
- Shared props belong at the Inertia middleware/application boundary, not in duplicated client globals.
- Internal SPA navigation and external/download navigation are different contracts.
- State/scroll preservation and persistent layouts should be explicit behavioral choices.

## Projection Boundary

Do not copy current rule IDs, counts, dependency versions, or framework-version tables into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair the projection.

## References

- Inertia.js documentation: https://inertiajs.com/
- Laravel documentation: https://laravel.com/docs
- React documentation: https://react.dev/
