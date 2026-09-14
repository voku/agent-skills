# Laravel MCP — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent MCP rule inventory, version table, or compiled copy of the rule examples here.

## Fast Path

1. Confirm the target project actually uses Laravel MCP and ground its installed package/framework versions from repository evidence.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Keep server registration/authentication, tool schemas, tool responses/error handling, and resources/prompts/testing in their owning rule boundaries.
4. Prefer the target repository's existing auth, validation, testing, and dependency-injection patterns over invented alternatives.
5. Report only observed validation results; missing runtime or package evidence remains unknown rather than assumed.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed Laravel MCP guidance and examples.
- the target repository owns its installed Laravel/PHP/package versions and local conventions.
- Laravel/MCP upstream documentation owns framework/package behavior that may change over time.
- this projection owns no independent MCP semantics.

## Evidence Boundary

- Verify routes, middleware/auth configuration, tool/resource/prompt classes, and tests in the target repository before claiming compatibility.
- Treat schemas and response contracts as executable interfaces, not descriptive prose.
- Do not recommend a Laravel/MCP API merely because it appears in a generic example; confirm it exists in the target version.
- Keep failures explicit and preserve causal context rather than converting exceptions into apparent success.

## Projection Boundary

Do not copy the current canonical rule list, rule count, category count, framework version table, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
