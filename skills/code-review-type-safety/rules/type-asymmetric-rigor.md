
---
title: Asymmetric Rigor
impact: HIGH
impactDescription: The same value validated strictly in one branch and loosely in the sibling branch, so one path silently accepts what the other rejects
tags: review, code-review, code-review-type-safety, type-asymmetric-rigor
---

## Rule

Within one change, the same value, field, or return shape must be handled the same way in every sibling path. Trust it everywhere or validate it everywhere - a mix means one path is wrong, and the review has to say which.

## What to Review

- Compare sibling branches that read the same value: a strict comparison in one and a loose cast in the next is a finding, not a style difference.
- Compare validation depth: a field checked for type and emptiness in one place but only cast in another means the weaker place accepts input the stronger one rejects.
- Check half-applied abstractions: one value routed through a wrapper or accessor while adjacent values stay raw, without a stated reason.
- Check that a filter applied when producing a choice is re-applied when consuming the submitted value; a constrained input list is not a guarantee against a replayed or hand-built request.
- Accept a genuine difference when the reviewer can state the behavioral reason for it - a value that must stay unescaped for a downstream sink, for example - and expect that reason in a comment.

## Incorrect

```php
if ((int) $row['count'] > 0) { ... }     // one branch
if ($row['count'] === 1) { ... }         // the next branch, same field
```

## Correct

```text
The review names both sites, states which contract is the correct one, and asks for the other
to be brought in line - or for the difference to be justified where it stands.
```

## Notes

- Existing code is evidence, not authority: derive the pattern from the verified runtime contract, not from whichever sibling was written first.
- Mark `cross_lens_candidate=true` when the weaker path is also the one that crosses a trust boundary.
