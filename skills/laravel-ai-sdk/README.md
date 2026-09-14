# Laravel AI SDK

Portable guidance for building and reviewing AI-powered features with Laravel's AI SDK.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, provider catalog, or compiled API reference.

## When to Use

Use this skill when a Laravel project uses `laravel/ai` for agents, tool calling, structured output, embeddings/RAG, media generation, provider resilience, or deterministic AI testing.

## Routing

1. Ground the installed Laravel, PHP, and AI SDK versions from the target repository.
2. Read `SKILL.md` to select the canonical rule files matching the observed task.
3. Load only those rules instead of compiling the whole AI SDK catalog into context.
4. Follow project-local provider configuration, schemas, storage, queueing, and test conventions when they are stronger or more specific.
5. Validate through the repository's configured toolchain and report only observed results.

## Stable Boundaries

- Treat tool schemas and structured outputs as executable contracts.
- Verify provider/model capabilities and SDK APIs against the installed version before recommending them.
- Prefer explicit resilience and observable failure handling over silent fallback behavior.
- Keep embeddings/RAG concerns grounded in the application's actual storage and retrieval path.
- Use deterministic fakes/assertions for tests rather than depending on live providers.

## Projection Boundary

Do not copy current rule IDs, counts, category totals, provider/API inventories, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.

## References

- [Laravel AI SDK Documentation](https://laravel.com/docs/13.x/ai-sdk)
- [Laravel AI SDK Repository](https://github.com/laravel/ai)
