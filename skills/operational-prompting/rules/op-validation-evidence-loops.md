---
id: op-validation-evidence-loops
title: "Machine-Readable Validation and Falsifiable Evidence"
category: validation
priority: HIGH
triggers: [unverified-prose-claim, fabricated-test-pass, missing-validation-command, hallucinated-green-ci]
tags: [operational-prompting, validation, evidence, commands, exit-codes, falsifiability]
---

# Machine-Readable Validation and Falsifiable Evidence

**Trigger Anchor:** Enforce closed-loop verification via executable commands with observable exit codes; never accept prose claims ("tests passed", "code looks good") without literal terminal output and exact file:line evidence.

---

### Bad
```markdown
<!-- ❌ Agent claims success without providing or executing validation commands -->
Agent: "I have updated the authentication handler. Everything looks correct and all tests pass."
<!-- No command was run; syntax errors or test regressions remain undetected! -->
```

### Good
```markdown
<!-- ✅ Closed-loop verification with executable commands and observed exit codes -->
## Validation Plan
Run the targeted verification suite:
```bash
php -l app/Auth/UserSessionHandler.php
vendor/bin/phpunit tests/Unit/UserSessionHandlerTest.php
vendor/bin/phpstan analyse app/Auth/UserSessionHandler.php
```

## Terminal Evidence Contract
- Report exact exit code (`0` for success).
- On failure, quote failing assertion and stack trace.
- Claim a pass ONLY after observing the clean execution output.
```
