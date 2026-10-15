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

Use this skill when task or repository evidence reveals **at least one** decision-relevant signal:

- An implementation is prescribed, but the needed outcome or responsibility is not established.
- A proposed persistence, duplication, hash, integration, or abstraction may duplicate an existing owner's capability.
- A local failure may be caused by a producer/consumer contract mismatch or a recurring cross-call-site mechanism.
- Repeated investigation of one layer is not reducing uncertainty, while an independent observation point exists.
- A proposed structural fix has not been distinguished from sufficient local containment.

Do **not** activate merely because work is complex. Skip it for an isolated, understood, low-risk fix, routine implementation or validation, or a review already owned by a specialist lens. Do not reopen a verified authorized product decision based only on aesthetic preference. Use \`requirements-interview\` for missing human product intent, \`coding-simplicity\` for choosing implementation surface, and \`code-review-*\` for targeted review findings.

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

1. Separate **observed behavior**, **hypothesis**, **falsifying evidence**, and **unresolved authority**. Do not promote a plausible story to a fact.
2. Inspect the smallest relevant owner contract, caller/consumer, state, test, log, or safe reproduction. Prefer two genuinely independent sources when a second direction would materially narrow the search.
3. Compare the plausible outcomes: **no change**, **local containment/correction**, or **structural prevention**. Select depth by recurrence evidence, blast radius, risk, reversibility, and cost, not by a preference for redesign.
4. Preserve verified requirements, temporal semantics, persistence needs, privacy/trust boundaries, authorization, and existing safety guarantees. Simpler is not equivalent unless those constraints still hold.
5. If further investigation would not alter the next safe choice, **stop**. If evidence is unavailable, report the specific unknown; if only a human can set intended behavior or accept risk, route that decision to the authorized owner.

A useful result can be: "This feature is unnecessary under verified conditions", "Apply the local fix", "Measure at this other boundary", or "Seek authority". Avoid generic recommendations to "investigate more".

## Decision examples

- **Proposed hash of surname and birth date:** First ask who detects changes and who owns historical state. If the producer already has the *required current and prior values*, can compare them with equivalent normalization and timing, and no privacy/persistence boundary requires the hash, propose **no hash implementation**. Otherwise retain the required mechanism or identify the precise missing fact. Do not assume comparing current values alone detects historical changes.
- **Dry basement with subtle damage signs:** Treat experience as a leak hypothesis, not proof. For one verified failed fitting with healthy surrounding pipe, repair locally. For measured deterioration across sections, investigate broader prevention. Do not prescribe full replacement from unease alone.
- **Incorrect UI data:** If browser-to-API tracing stalls, compare the API's observed payload with persistence-to-domain evidence; converge on the first mismatched contract. Do not automatically inspect every layer.
- **Unclosed file handle:** Close it safely for an isolated defect, using an existing scoped cleanup construct where appropriate. Consider structural prevention only if sibling paths or exception cases show a recurring mechanism.
- **Counterexample:** A verified one-line bounds bug with a failing regression test needs a bounded fix, not a new requirements interview, a second investigation direction, or recursive "why" questions.

## Stop and hand off

Once the next choice is supported, state concisely: **observed signal; selected perspective (if needed); decisive evidence or missing fact; next action and its boundary**. Valid actions include no change, local fix, targeted investigation, second-direction probe, justified structural prevention, human decision, or stop due to diminishing value.

This skill supplies reasoning, not branch, implementation, approval, merge, release, or agent-loop lifecycle authority. \`engineering-codelight\` remains the owner of general evidence/authority discipline and \`operational-prompting\` of portable task contracts. Do not create a separate orchestration process.
