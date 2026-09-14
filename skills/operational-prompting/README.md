# Operational Prompting

Repo-owned operational prompting for coding agents. 4 consolidated rules across 4 categories.

**Version:** 2.0.0

## Overview

This skill provides guidance for:
- Keeping durable agent instructions in reviewed repository files
- Layering instruction provenance and precedence explicitly
- Bounding tasks to surgical changes with falsifiable stopping conditions
- Requiring executable validation and observable evidence
- Authoring portable Agent Skills guidance without duplicating tool-specific CLI/API/runtime semantics

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce independent operational semantics.

## Ownership boundary

This collection owns tool-neutral engineering guidance. If a skill invokes, configures, or depends on a specific tool's CLI, API, schema, output contract, file layout, or runtime behavior, its canonical instructions belong in that tool's repository so code and coding instructions are reviewed and released together. Link or install that tool-owned skill instead of keeping a second canonical copy here.

## Categories

### 1. Instruction Hierarchy (Critical)
Keep durable agent behavior in repository files and make instruction provenance and precedence explicit.

### 2. Task Scope & Stopping (Critical)
Limit edits to the smallest verified scope and define observable stop or escalation conditions.

### 3. Validation & Evidence (High)
Bind work to executable commands, observable exit codes, and falsifiable evidence.

### 4. Portability (Medium)
Use standard Agent Skills frontmatter and keep portable heuristics separate from tool-coupled mechanics.

## Rules

| Rule | Category | Impact |
|------|----------|--------|
| `op-repo-owned-hierarchy` | Instruction Hierarchy | CRITICAL |
| `op-scope-stopping-contracts` | Task Scope & Stopping | CRITICAL |
| `op-validation-evidence-loops` | Validation & Evidence | HIGH |
| `op-portable-skill-manifests` | Portability | MEDIUM |
