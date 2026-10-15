---
name: engineering-reframing
description: Reframe an engineering problem when evidence suggests the proposed solution, requirement, ownership, or failure explanation might be wrong. Use before implementing a suspect plan or when diagnosis stalls, to select one useful investigation perspective and decide when to stop. Do not use for clear bounded fixes, routine reviews, or speculative redesign.
license: MIT
metadata:
  author: Agent Skills Team
  version: "1.0.0"
---

# Engineering Reframing

Question the problem only when doing so could change the next engineering decision. A suspicious pattern is a hypothesis to test, not evidence of a defect. This is an optional reasoning lens, not a workflow or a required sequence of questions.

## Activation gate

Activate only when **concrete evidence** suggests a decision-relevant doubt:

- A proposed mechanism lacks a verified outcome, consumer, or owner.
- A new hash, persisted state, or abstraction may duplicate an existing capability.
- A local failure may reflect a shared cause or producer/consumer mismatch.
- A single trace has stalled while independent evidence exists.
- A broad fix is proposed for a possibly isolated defect.

Skip clear bounded fixes, routine validation, and specialist reviews. Do not reopen authorized requirements based on taste. Use `requirements-interview` for unresolved product intent, `coding-simplicity` for implementation choices, and `code-review-*` for review findings.

## Select one perspective

Choose the perspective with the highest chance of changing the decision at the lowest justified investigation cost. Switch only if new evidence warrants it; never run all perspectives by default.

| Signal | Perspective | Cheapest useful probe |
| --- | --- | --- |
| Proposed mechanism precedes a verified need | **Zoom out** | Name the desired observable outcome, consumer, and actual state owner; check whether the mechanism is necessary |
| Behavior breaks at a concrete boundary | **Zoom in** | Find the violated invariant, state transition, and one observation that could falsify the leading cause |
| A single trace stalls and independent endpoints exist | **Converge** | Trace producer and consumer, or UI-to-API and persistence-to-domain, toward one shared contract |
| A requirement or causal claim rests on another assumption | **Ask why** | Question that link once, using source, data, tests, or a domain owner to check the answer |
| A local fix might leave recurrent failures | **Prevention depth** | Compare isolated trigger, causal mechanism, contributing conditions, and recurring vulnerability |

Ask another "why" only if the previous answer exposes a new *decision-relevant* assumption. Neither five questions nor one "root cause" is mandatory. Causation may have multiple contributing mechanisms.

## Evidence before depth

1. Label **observation**, **hypothesis**, **falsifier**, and **unknown/authority decision**; never invent a causal link.
2. Check the smallest relevant contract, state, caller, consumer, test, log, or safe reproduction. A second direction must provide independent evidence.
3. Compare **no change**, **local correction**, and **structural prevention** by recurrence, impact, reversibility, and cost.
4. Preserve verified behavior, timing/history, persistence, security, privacy, and authorization boundaries.
5. Stop when another probe cannot change the decision, evidence costs more than its value, or human authority is needed. Name the unknown.

## Decision examples

- **Proposed hash:** Ask who detects changes and owns prior state. If the producer already has comparable old/new values and timing, normalization, persistence, and privacy permit it, choose **no hash**. Otherwise retain the mechanism or identify missing evidence; current-only comparison cannot detect history.
- **Plumber / recurrence:** Subtle damage signs suggest a hypothesis, not proof. One failed fitting warrants local repair; verified deterioration across sections can justify prevention.
- **Wrong UI data:** When one trace stalls, inspect independent API and persistence/domain evidence and converge on the first divergent contract, not every layer.
- **Leaked file handle:** Fix an isolated exception path using existing scoped cleanup. Investigate prevention if sibling paths show a shared mechanism.
- **Stop asking why:** Ask again only when an answer exposes a decision-relevant assumption; stop once the answer cannot change the action.
- **Counterexample:** A known off-by-one bug with a failing regression needs a bounded fix, not a second investigation or redesign.

## Stop and hand off

State: **observed signal; chosen perspective; decisive evidence or missing fact; smallest justified next action**. Options: no change, local fix, targeted/second-direction probe, structural prevention, human decision, or stop.

This skill owns perspective choice, **not** implementation, approval, or lifecycle. `engineering-codelight` owns evidence/authority discipline; `operational-prompting` owns task contracts. Respect the project's workflow.
