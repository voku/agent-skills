# Laravel AI SDK — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent Laravel AI rule inventory, version table, provider catalog, or compiled copy of rule examples here.

## Fast Path

1. Ground the target project's installed Laravel, PHP, and `laravel/ai` versions before recommending SDK behavior.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the current task.
3. Keep agent architecture, tool integration, embeddings/RAG, media/resilience, and test-fake concerns in their owning rule boundaries.
4. Treat schemas, tool contracts, structured output, provider configuration, and fake/assertion APIs as executable interfaces that require version evidence.
5. Validate with the target repository's configured tests and toolchain; report only observed results.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed Laravel AI guidance and examples.
- the target repository owns installed package/framework versions, provider configuration, application contracts, and local validation commands.
- Laravel/package upstream documentation owns version-sensitive SDK behavior.
- this projection owns no independent AI SDK semantics.

## Evidence Boundary

- Verify agent classes, provider/model attributes, tool schemas, structured output contracts, embedding/vector-store usage, and fakes in real source before making compatibility claims.
- Do not infer provider capabilities or current SDK APIs from an old example.
- Keep external AI failures observable and bounded; provider fallback does not turn an unknown or failed result into success.
- For tests, prefer deterministic fakes and explicit prompt/output assertions over live-provider dependence.

## Projection Boundary

Do not copy the current canonical rule IDs, rule counts, category totals, provider/API tables, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
