---
id: op-repo-owned-hierarchy
title: "Repo-Owned Instruction Hierarchy and Guidance Provenance"
category: hierarchy
priority: CRITICAL
triggers: [volatile-chat-prompt-rules, missing-repo-guidance, unlayered-instructions, prompt-injection-drift]
tags: [operational-prompting, agents-md, instruction-hierarchy, provenance, repo-owned]
---

# Repo-Owned Instruction Hierarchy and Guidance Provenance

**Trigger Anchor:** Store durable coding agent instructions in version-controlled repository files (`AGENTS.md`, path-scoped rules, skills) rather than conversational memory; resolve precedence explicitly from global host -> repository root -> path-scoped rule -> ephemeral task.

---

### Bad
```markdown
<!-- ❌ Relying on long, volatile system prompts pasted into chat each session -->
User: "Remember: always use strict types, never touch vendor files, use Docker make test,
and remember that table X has a weird column naming scheme..."
<!-- Lost on session clear or across different developers/agents! -->
```

### Good
```markdown
<!-- ✅ Root AGENTS.md establishes durable, version-controlled repository instructions -->
# AGENTS.md

## Repository Workflow
- Minimum validation gate: `composer ci` (or `make test_unit`)
- Environment: PHP 8.3 in Docker container

## Precedence Hierarchy
1. Task-specific prompt / user instruction
2. Path-scoped instructions (`modules/billing/AGENTS.md`)
3. Root `AGENTS.md`
4. Host-level default rules

## Architectural Invariants
- Authenticated user identity: `GlobalContainer::loggedInUserOrThrow()`
- Never execute external network side effects inside database transactions
```
