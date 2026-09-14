# Operational Prompting — Agent Projection

**Version:** 2.0.0  
**Rules:** 4 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent operational semantics here.

## Fast Path

1. Put durable guidance in reviewed repository files, not conversational memory.
2. Resolve instruction provenance and precedence explicitly.
3. Bound changes to the smallest verified scope and define observable stop conditions.
4. Validate through executable commands and observed evidence, not prose claims.
5. Keep portable heuristics here; move concrete CLI/API/schema/runtime instructions to the tool that owns them.

## Rule Index

| Priority | Rule | Trigger Anchor |
|----------|------|----------------|
| CRITICAL | [`op-repo-owned-hierarchy`](rules/op-repo-owned-hierarchy.md) | Durable instruction or provenance problem |
| CRITICAL | [`op-scope-stopping-contracts`](rules/op-scope-stopping-contracts.md) | Unbounded scope, drive-by refactor, missing stop condition |
| HIGH | [`op-validation-evidence-loops`](rules/op-validation-evidence-loops.md) | Unverified success claim or missing executable validation |
| MEDIUM | [`op-portable-skill-manifests`](rules/op-portable-skill-manifests.md) | Vendor lock-in, duplicated tool semantics, missing standard skill frontmatter |

## Canonical Ownership Boundary

`agent-skills` owns portable, tool-neutral engineering guidance. If correctness depends on a concrete tool command, option, schema, file layout, generated artifact, output contract, or runtime/lifecycle behavior, the tool repository owns the canonical instructions.

Examples:

- "Prefer exact validation commands" is portable guidance and belongs here.
- "Run `tool-x foo --bar` and parse field `baz`" belongs with `tool-x`.
- Standard Agent Skills frontmatter belongs here; a second private `.ai/skills/*.yaml` manifest contract does not.

## Evidence Contract

- Name the exact validation command.
- Observe and report its exit status.
- Preserve raw evidence closely enough that another reviewer can falsify the claim.
- Do not convert missing evidence into a success statement.

## Scope Contract

- Identify the smallest affected file/behavior surface.
- Avoid unrelated cleanup or refactoring.
- State the stopping condition before broadening the change.
- Escalate only when a real decision is required.

## Detailed Guidance

Read the four canonical rule files for trigger-specific Bad/Good examples and trade-offs. If this projection disagrees with `SKILL.md` or a rule file, the canonical skill surface wins and this projection must be corrected.
