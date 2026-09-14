# Project Documentation

Portable guidance for documentation structure, baseline files, content quality, cleanup, and lifecycle management.

## Canonical Source

`SKILL.md` defines when this skill applies and the bootstrap/audit operating modes. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, stack matrix, or compiled example set.

## When to Use

Use this skill when bootstrapping project documentation, auditing Markdown files, cleaning up stale or duplicate docs, deciding what to keep/archive/delete, or organizing ADRs and documentation structure.

## Routing

1. Inspect the target repository and identify whether the task is bootstrap, audit, or focused reference work.
2. Read `SKILL.md` first.
3. Load only the relevant rule files for structure/naming, essential baseline, Markdown quality, hygiene/cleanup, or lifecycle/freshness.
4. Base KEEP / UPDATE / ARCHIVE / DELETE decisions on repository evidence.
5. Surface deletion candidates for human approval rather than silently removing documentation.

## Projection Boundary

Do not copy current rule IDs, counts, tool-version tables, or long worked examples into this file. If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection.
