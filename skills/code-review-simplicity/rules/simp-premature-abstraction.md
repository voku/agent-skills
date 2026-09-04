
---
title: Premature Abstraction
impact: HIGH
impactDescription: Abstractions introduced for a second caller that never arrived, and extractions that only add a navigation hop
tags: review, code-review, code-review-simplicity, simp-premature-abstraction
---

## Rule

Duplication is not automatically a finding. Review whether an introduced abstraction has a demonstrated second use, and whether an extraction expresses a real concept or merely moves code one indirection away.

## What to Review

- Flag an interface, factory, generic manager, configuration switch, or base class with exactly one real implementation or caller.
- Flag an extracted helper that has one call site, no independently testable behavior, and no domain meaning - the reader now has to jump to read a fragment.
- Do not flag two similar blocks in different modules as duplication when merging them would require runtime branching on which caller is active; two straight-line versions can be cheaper to read and safer to change than one parameterized version.
- Distinguish a genuine shared seam - an existing framework boundary, a real domain operation, a reused contract - from a helper created only to avoid repeating four lines.
- When flagging duplication, name the concrete existing seam that already owns the behavior; "this repeats" without a target is not an actionable finding.

## Incorrect

```text
The review demands that two similar handlers in unrelated modules be merged into a shared
base class, which then needs a flag to tell the two callers apart.
```

## Correct

```text
The review flags a new interface with one implementation and one caller, and proposes using the
concrete class directly until a second implementation exists.
```

## Notes

- The question is "what does this abstraction let us change more cheaply?" - if the answer is hypothetical, it is premature.
- Mark `tradeoff_required=true` when removing the abstraction changes a published API or an extension point others rely on.
