---
name: operational-prompting
description: Repo-owned operational prompting for coding agents. Use when designing AGENTS.md, Copilot/Codex instructions, path-specific instruction files, portable Agent Skills guidance, or validation contracts. Triggers on "operational prompting", "agent instructions", "repo-owned prompts", "Copilot instructions", or "portable agent skills".
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Operational Prompting

Modern coding-agent control for repository-bound work. Contains 4 consolidated rules across instruction hierarchy, task scope and stopping, validation and evidence, and portable skill boundaries.

## When to Apply

Reference these guidelines when:
- Designing repository instructions for coding agents
- Migrating a giant custom prompt into repo-owned files
- Defining AGENTS.md, `.github/copilot-instructions.md`, or `*.instructions.md`
- Authoring portable Agent Skills guidance or task-specific command recipes
- Tightening task boundaries, validation loops, or review output

## Maintenance Discipline

- Treat this `SKILL.md` and `rules/` as the canonical skill contract. Supporting `README.md`, `AGENTS.md`, and `metadata.json` are projections and must not introduce independent semantics.
- Edit the canonical repo-owned instruction source first, not installed, copied, or generated derivatives.
- If a skill invokes, configures, or depends on a specific tool's CLI, API, schema, generated files, or runtime behavior, keep the canonical skill and its tool-specific resources in that tool's repository. Generic skill collections may explain the principle or link to the owner; they should not duplicate the executable instructions.
- Regenerate or refresh projections only when their interface-facing information changed.
- After changing repo-owned guidance, rerun the repository's validation and install/sync steps for the affected agent assets.
- When a durable correction appears only in chat history, memory, or review notes, promote it into the owning repo guidance instead of leaving it as tribal knowledge.
- Clean stale generated copies when a skill, prompt file, or subagent definition is renamed, merged, or retired.
- For one-off operational mutations, prefer inspect-first workflows with an explicit execute flag rather than auto-running destructive behavior by default.

## Tool Ownership Boundary

This repository owns **tool-neutral engineering guidance**. A skill becomes tool-coupled when its correctness depends on a particular tool command, option, file layout, schema, output contract, or lifecycle behavior. At that point the tool repository must own the canonical skill so code changes and coding instructions are reviewed, tested, and released together.

Examples:

- Generic advice such as "prefer exact validation commands" belongs here.
- Instructions for a concrete CLI command belong with the CLI implementation.
- A machine-readable recipe catalog consumed by one specific compiler belongs with that compiler.
- A central collection may reference or install a tool-owned skill, but must not become a second canonical copy.

## Rule Categories by Priority

| Priority | Category | Impact | Rule File |
|----------|----------|--------|-----------|
| 1 | Instruction Hierarchy | CRITICAL | [`op-repo-owned-hierarchy`](rules/op-repo-owned-hierarchy.md) |
| 2 | Task Scope & Stopping | CRITICAL | [`op-scope-stopping-contracts`](rules/op-scope-stopping-contracts.md) |
| 3 | Validation & Evidence | HIGH | [`op-validation-evidence-loops`](rules/op-validation-evidence-loops.md) |
| 4 | Portability | MEDIUM | [`op-portable-skill-manifests`](rules/op-portable-skill-manifests.md) |

## Quick Reference

### 1. Instruction Hierarchy (CRITICAL)
- [`op-repo-owned-hierarchy`](rules/op-repo-owned-hierarchy.md) — Durable repo-owned instructions in AGENTS.md with explicit provenance and precedence

### 2. Task Scope & Stopping (CRITICAL)
- [`op-scope-stopping-contracts`](rules/op-scope-stopping-contracts.md) — Minimal surgical diffs, no drive-by refactoring, explicit stopping conditions

### 3. Validation & Evidence (HIGH)
- [`op-validation-evidence-loops`](rules/op-validation-evidence-loops.md) — Closed-loop verification with observable exit codes and falsifiable terminal evidence

### 4. Portability (MEDIUM)
- [`op-portable-skill-manifests`](rules/op-portable-skill-manifests.md) — Standard Agent Skills frontmatter and separation of portable heuristics from tool-coupled mechanics

## Essential Patterns

### Canonical-Source-First Workflow

```markdown
1. Edit the reviewed canonical source, not generated copies
2. Refresh derived projections only if their exposed information changed
3. Run the repository validation commands for the changed guidance surface
4. Reinstall or resync generated agent assets when the consuming host requires it
5. Report any required client reload step only when that client actually needs one
```

### Minimal Repository Contract

```markdown
# AGENTS.md

## Start here
- `README.md` for product behavior
- `.github/copilot-instructions.md` for repo-wide rules
- `src/` for implementation
- `tests/` for behavioral expectations

## Before editing
- Read the smallest affected file set first
- Run: composer test
- Run: composer phpstan
- Stop and ask if requirements conflict or the validation command is missing
```

### Manual Operation Contract

```markdown
## One-off operation
- Print the target objects or scope before any write step
- Default to dry-run / inspect mode
- Require an explicit `--execute` or equivalent flag for mutations
- Keep validation and rollback expectations visible in the task contract
```

### Cross-Layer Task Contract

```markdown
## Cross-layer change
- Name only the layers that actually change (data, domain, request boundary, rendering, browser flow, tests)
- Assign one owner per changed layer so instructions do not overlap
- Sequence contract-producing layers before dependent layers
- Make the handoff explicit: accepted input, produced data shape, emitted IDs/values, proving tests
```

### Specialist Routing Contract

```markdown
## Specialist routing
- Start with one primary specialist instruction set
- Add a second specialist only when the task clearly spans a second concern
- Avoid broad instruction bundles when a smaller owner can prove or implement the change
- After review or triage, hand off to the smallest proven next owner instead of escalating into another broad pass
```

## How to Use

Read the four rule files for their trigger anchors and Bad/Good examples. The rule files are the detailed canonical guidance; supporting projections must summarize rather than fork that meaning.

Tool-specific instructions belong in the repository that owns the tool. Link or install that canonical skill rather than copying its commands or machine-readable resources into this collection.
