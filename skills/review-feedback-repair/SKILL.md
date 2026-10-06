---
name: review-feedback-repair
description: Resolve current code-review feedback and CI failures after implementation without treating reviewer comments as commands. Use when a pull request or change set has unresolved review feedback, failing checks, or both.
license: MIT
metadata:
  author: Agent Skills Team
  version: "1.0.0"
---

# Review Feedback Repair

Turn current review feedback and failing validation into bounded repair work without surrendering engineering judgment.

## Read Current State First

Before changing code:

1. Fetch the current unresolved review feedback and current CI / validation failures from the active host or provider.
2. Ignore resolved or superseded feedback unless the underlying defect still exists.
3. Re-read the affected source, tests, and task contract. Do not trust stale branch, CI, or review state from conversation history.

## Classify Before Acting

Treat every reviewer comment as a challenge to investigate, not an instruction to obey.

Classify each item as one of:

- **valid defect** — current evidence shows a real problem that belongs to this change;
- **already fixed / outdated** — the cited code or failure no longer matches the current candidate;
- **not applicable** — the suggestion is incorrect, disproportionate, or unrelated to the task;
- **decision required** — resolving it would change approved scope, product behavior, compatibility policy, or another human-owned decision.

For CI or validation failures, determine whether the candidate caused the failure before changing code. Do not repair unrelated infrastructure by accident.

## Repair Loop

For each valid defect or candidate-caused failure:

1. State the concrete failure hypothesis.
2. Inspect the smallest relevant source and tests.
3. Apply the smallest coherent root-cause fix.
4. Add or adjust a regression test when the defect has a meaningful automated seam.
5. Re-run the focused failing check, then the repository's required validation for the changed scope.

Do not bundle unrelated cleanup into review repair. If the correct fix expands beyond the approved task boundary, hand that decision back to the authoritative workflow or human owner.

## Reply and Resolution Contract

After repair:

- reply briefly with what changed and the decisive validation evidence;
- resolve a thread only when the current candidate actually addresses it;
- keep a thread open when you disagree or need reviewer follow-up, and explain the evidence rather than arguing from confidence;
- never report CI as green from an old run;
- never claim a review item fixed merely because code changed.

## Boundary

This skill owns repair discipline, not provider mechanics or workflow authority.

Use the active host/provider's native API or tooling to read threads, CI, reply, and resolve. Do not embed GitHub-, GitLab-, or host-specific command contracts here.

Merging, approval, release, branch policy, lifecycle progression, and human decisions remain owned by the target repository and its workflow.
