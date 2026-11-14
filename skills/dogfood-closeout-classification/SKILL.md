---
name: dogfood-closeout-classification
description: Enforce classification of LLM inference points and running private leak checks before closing sessions and upstreaming fixes. Triggers on "dogfood closeout", "closeout classification", "inference classification", "leak check public diffs", or "session closeout".
license: MIT
metadata:
  author: Agent Skills Team
  version: "1.0.0"
---

# Dogfood Closeout Classification

Durable closeout constraints for capturing, classifying, and hardening agent learnings while protecting private host project boundaries.

## When to Apply

Activate this skill when:
- Preparing to close a development session
- Documenting LLM inferences, gaps, or decisions from a dogfood run
- Upstreaming generic fixes from a private host project to public repositories
- Verifying the safety of public repository checkouts (`voku/agent-*`)

## Rules of Engagement

### 1. Collect and Classify LLM Inference Points
If a dogfood run contains any LLM inference points (gaps, implicit assumptions, or missing instructions), they must be classified before session closeout. Never close a session with generic "Follow-up: none" if unclassified inferences remain.

Classify each inference as exactly one of:
- `docs_fix` (clarifying repository or setup instructions)
- `skill_proposal` (identifying a repeatable workflow/recipe)
- `memory_proposal` (suggesting durable memory/guidance)
- `hard_constraint_candidate` (defining a checkable rule)
- `verifier_or_test_candidate` (recommending validator checks/test cases)
- `private_only_learning` (noting host-project-specific facts)
- `upstream_issue` (tracking external bugs or feature requests)
- `no_durable_learning` (requires an explicit, documented reason why no learning is retained)

### 2. Run Private Leak Checks Before Upstreaming
Before copying or committing any host-derived fixes into public `voku/agent-*` checkouts, execute a strict leak check on public diffs to prevent leakage of:
- Private project/customer names
- Internal directories/paths
- Internal URLs or server domains
- Database table or column symbols
- LDAP or Active Directory identifiers
- Email addresses
- Business-specific terminology
- Host-specific commands or environment details

### 3. Keep Environment Rules Private
Always document environment-specific commands or container setups inside private repository files. Generic public versions must be expressed abstractly:
- "Run validation commands in the runtime required by the host project's instructions."
Do not mention specific container names or host paths in public code or tests.
