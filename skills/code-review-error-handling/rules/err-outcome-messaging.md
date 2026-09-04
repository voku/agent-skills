
---
title: Outcome Messaging Discipline
impact: HIGH
impactDescription: Reachable paths that report no outcome, report it twice, or claim success for a partially failed batch
tags: review, code-review, code-review-error-handling, err-outcome-messaging
---

## Rule

Every reachable path of a user-facing operation must surface exactly one outcome: not zero, not two. Review who reports the outcome - the caller or the callee - and whether that holds for every branch, including the ones where the callee never runs.

## What to Review

- Identify which side owns the message. When a callee already renders a specific message on every branch it executes and the caller has no further decision to drive, the caller ignoring the return value is correct - re-reporting only duplicates it.
- Check the branches where a guarded callee is skipped. `if ($target) { selfReportingCallee(); }` leaves the `else` silent, because the component that would have reported never ran. That branch needs its own message.
- Check aggregate messages after a loop. A success message may only be emitted when an accumulated all-succeeded flag confirms every item worked; otherwise report the failure or the mixed result.
- Check that a wrapper which owes its own caller a status does not swallow one. "The callee already told the user" is not a reason to drop a status the caller still needs for a decision.
- Check sibling call sites of the same shared function. If several places already consume its return value one way, a new site that treats it differently is a finding, not a local style choice.

## Incorrect

```text
The handler guards the call, so the failure branch returns early without rendering anything.
The user sees an unchanged screen and cannot tell whether the action ran.
```

```text
A loop deletes ten items, two fail, and the handler still shows the success summary
because no accumulated flag was checked before reporting.
```

## Correct

```text
The success branch relies on the callee's own message; the guarded else branch renders its own
error, and the loop reports success only when the accumulated all-succeeded flag is still true.
```

## Notes

- The deciding question is "does this caller still owe someone a decision or a message?", not "does the callee return a boolean?".
- An inverted legacy status (`true` means error) is normalized at the call site with an explicit comparison and a short comment, not by guessing at each site.
- Mark `cross_lens_candidate=true` when the silent path is really a state-consistency problem rather than a messaging one.
