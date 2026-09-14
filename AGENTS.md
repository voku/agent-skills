# Agent Skills Repository — Routing Guide

This file is a repository-level router. It must not become a compiled copy of every skill, rule inventory, activation matrix, or tool-specific contract.

## Repository ownership boundary

This repository owns **portable, tool-neutral engineering guidance**.

If guidance is only correct for one concrete tool's CLI, API, schema, generated artifacts, file layout, or lifecycle behavior, the canonical form belongs with that tool. Keep only the transferable engineering principle here and route consumers to the semantic owner for executable details.

For the `voku/agent-*` stack specifically:

- `voku/agent-recall-compiler` owns operating-prompt recipes, typed recipe arguments, rendering/template identity, and recipe applicability.
- `voku/agent-loop` owns governed Contract/Run lifecycle, approvals, canonical next actions, mutation authority, and workflow prompt envelopes.
- `voku/agent-skills` may teach portable reasoning, review, testing, language, and prompting heuristics, but must not keep a second canonical copy of those package contracts.

Before adding guidance, follow `CONTRIBUTING.md` and check whether a semantic owner already exists. Extend that owner rather than creating a differently named duplicate.

## Canonical skill contract

For each skill under `skills/<skill-name>/`:

1. `SKILL.md` is the canonical activation and high-level skill contract.
2. `rules/` contains canonical detailed guidance when the skill uses rule files.
3. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections only unless the skill explicitly establishes a narrower owner contract.

Supporting projections must summarize or route to canonical guidance. They must not introduce independent rule semantics, inventories, counts, or tool contracts.

Do not infer current rule inventory from this root file. This root file is **routing guidance only**. Do not add per-skill rule counts, copied rule inventories, hand-maintained skill activation tables, framework-version tables, or tool-specific execution recipes here.

## Routing workflow

1. **Ground the task first.** Inspect the target repository and task evidence needed to identify the actual language, framework, workflow, and dominant engineering concern. Do not infer a stack merely because this catalog contains a matching skill.
2. **Discover candidates from canonical frontmatter.** Inspect `skills/*/SKILL.md` and use each skill's `name` and `description` to decide whether it applies.
3. **Load the smallest useful set.** Prefer one primary skill. Add another only when the task genuinely spans a separate concern that the first skill does not own.
4. **Follow canonical detail.** When a selected skill points to files under `rules/`, load only the rules relevant to the current task rather than compiling the whole catalog into context.
5. **Respect stronger authority.** Current host/system/user/project instructions and the target repository's own workflow remain authoritative within their scope. A catalog skill is guidance, not a replacement lifecycle.
6. **Route tool-coupled facts to their owner.** If correctness depends on a concrete command, API, schema, output, path, or runtime behavior, verify it in the owning tool repository instead of reconstructing it here.

## Composition discipline

- Prefer a focused specialist over a broad bundle when one skill can answer the task.
- For `code-review-*` skills, start with the dominant review lens. Hand off to one narrower follow-up lens only when another concern becomes primary.
- `engineering-codelight` may provide a workflow-neutral reasoning lens for non-trivial work, but it does not replace the target repository's workflow or specialist implementation guidance.
- If two skills overlap, prefer the one that owns the more specific semantic boundary. Do not merge their prose into a new synthetic rule set.

## Evidence and validation

- Never claim a skill or rule is current because a projection file exists. Validate important operational claims against the canonical owner.
- When a canonical skill changes, update only projections whose exposed interface actually changed.
- If a projection repeatedly drifts, prefer thinning or deleting duplicated prose over adding another synchronization ritual.
- Mechanically decidable invariants should move toward tests, static analysis, CI, types, owner APIs, or automation when evidence justifies it. Retire redundant prose after the structural owner is reliable.

## Contribution boundary

Use `CONTRIBUTING.md` as the contribution contract. New or materially changed guidance must establish:

- that this repository is the right semantic owner;
- the evidence for the guidance;
- whether an existing skill already owns the principle;
- whether code or another deterministic mechanism can own it instead;
- what future condition would make the prose removable.

A smaller catalog with sharper ownership is preferable to a comprehensive catalog whose copies quietly disagree.
