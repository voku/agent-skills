---
id: op-scope-stopping-contracts
title: "Minimal Scope, Surgical Diffs, and Falsifiable Stopping Conditions"
category: task-scope
priority: CRITICAL
triggers: [unbounded-agent-drift, drive-by-refactoring, infinite-looping-agent, missing-stopping-condition]
tags: [operational-prompting, task-scope, surgical-diffs, stopping-conditions, boundaries]
---

# Minimal Scope, Surgical Diffs, and Falsifiable Stopping Conditions

**Trigger Anchor:** Constrain agent tasks to minimal surgical diffs addressing the verified issue; prohibit unsolicited drive-by refactorings or cosmetic churn; specify explicit stopping conditions and decision-required escalation gates.

---

### Bad
```markdown
<!-- ❌ Vague prompt leading to unbounded scope creep and churn -->
Fix the bug in the user login page and tidy up the codebase while you're at it.
<!-- Agent proceeds to reformat 40 unrelated files, upgrade dependencies, and rewrite the router! -->
```

### Good
```markdown
<!-- ✅ Explicit scope boundary and falsifiable completion criteria -->
Task: Fix null-pointer exception in `UserSessionHandler::getTenantId()` when session expires.

## Scope Guardrails
- Mutate ONLY `app/Auth/UserSessionHandler.php` and its unit test `tests/Unit/UserSessionHandlerTest.php`.
- Do NOT reformat adjacent code or rename public methods.

## Stopping Condition
1. Reproduce with failing test: `vendor/bin/phpunit tests/Unit/UserSessionHandlerTest.php`
2. Implement surgical null check.
3. Test passes with exit code 0.
4. Stop and report diff summary. Do NOT commit or deploy without confirmation.
```
