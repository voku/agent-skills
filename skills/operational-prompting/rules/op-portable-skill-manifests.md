---
id: op-portable-skill-manifests
title: "Portable Skill Manifests and Tool-Neutral Boundaries"
category: portability
priority: MEDIUM
triggers: [vendor-locked-skill, tool-coupled-instructions, missing-skill-frontmatter, duplicated-cli-docs]
tags: [operational-prompting, skill-manifests, vendor-neutral, portability, frontmatter]
---

# Portable Skill Manifests and Tool-Neutral Boundaries

**Trigger Anchor:** Author skills with standardized YAML frontmatter (`name`, `description`, `metadata`) that operate across agent harnesses (Claude Code, Gemini CLI, Cursor, Copilot); keep tool-neutral heuristics separated from tool-coupled CLI implementations.

---

### Bad
```markdown
<!-- ❌ Vendor-locked skill hardcoded to a single proprietary agent extension -->
# My Custom Claude Tool
@anthropic-only: execute `claude-tool-internal-call --json`
// Fails when loaded by Cursor, Gemini CLI, or GitHub Copilot!
```

### Good
```markdown
<!-- ✅ Standard, vendor-neutral skill format with trigger metadata -->
---
name: database-optimization
description: Database query optimization, index analysis, and N+1 query prevention. Use when debugging slow queries, writing migrations, or adding indexes.
license: MIT
metadata:
  author: Agent Skills Contributors
  version: "1.0.0"
---

# Database Optimization

## Quick Reference
| Priority | Category | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| CRITICAL | N+1 Queries | [`perf-nplusone`](rules/perf-nplusone.md) | Eager loading and bulk lookups |
```
