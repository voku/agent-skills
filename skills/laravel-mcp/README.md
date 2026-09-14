# Laravel MCP

Portable guidance for building and reviewing Laravel MCP servers, tools, prompts, resources, authentication boundaries, and tests.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, version table, or compiled set of examples.

## When to Use

Use this skill when a Laravel project integrates `laravel/mcp` or when the task is primarily about MCP server registration, callable tools, prompt/resource exposure, auth boundaries, or MCP-focused tests.

## Routing

1. Ground the installed Laravel, PHP, and MCP package versions from the target repository.
2. Read `SKILL.md` to identify the relevant canonical rule files.
3. Load only the rule guidance needed for the current change or review.
4. Follow project-local auth, validation, routing, and testing conventions where they are stronger or more specific.
5. Validate with the target repository's configured test/toolchain and report only observed results.

## Stable Boundaries

- Treat tool schemas and responses as public executable contracts.
- Keep auth fail-closed and reuse established middleware/authentication patterns where possible.
- Keep prompts/resources explicit and testable instead of hiding behavior in ambient application state.
- Prefer focused tests around MCP inputs, outputs, errors, and authorization boundaries.
- Verify framework/package behavior against the installed version before recommending an API.

## Projection Boundary

Do not copy current rule IDs, counts, category totals, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.

## References

- [Laravel MCP Documentation](https://laravel.com/docs/13.x/mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Laravel MCP Repository](https://github.com/laravel/mcp)
