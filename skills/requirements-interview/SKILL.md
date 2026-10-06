---
name: requirements-interview
description: Clarify an under-specified feature or engineering task before implementation. Use when the request leaves product behavior, scope, constraints, edge cases, acceptance criteria, or compatibility decisions unresolved.
license: MIT
metadata:
  author: Agent Skills Team
  version: "1.0.0"
---

# Requirements Interview

Turn an ambiguous feature or engineering request into an implementation-ready contract without starting implementation.

## Ground First

Before asking the user questions:

1. Read the smallest relevant repository evidence: existing code, tests, docs, issue text, and nearby patterns.
2. Separate facts already answered by the repository from genuine unknowns.
3. Do not ask the user to restate information the repository already makes clear.

## Interview Discipline

- Ask one unresolved question at a time when interaction is available.
- Start with the problem and desired outcome, then converge toward implementation-relevant detail.
- Challenge conflicting assumptions instead of silently choosing one.
- Make scope explicit: what is included, what is intentionally deferred, and what must not change.
- Cover only concerns that are relevant to the task, such as failure states, permissions, compatibility, migration, persistence, APIs, UI states, or operational constraints.
- When a minor default is reasonable, state the proposed default and why. Do not hide it as an assumption.
- Distinguish a missing fact from a decision that requires human authority.
- Stop asking when remaining unknowns no longer affect behavior, scope, architecture, acceptance, or verification.

## Output Contract

Produce a concise implementation-ready summary with:

- **Problem / outcome**: what needs to change and why.
- **Scope**: included work and explicit non-goals.
- **Requirements**: observable behavior and important edge cases.
- **Constraints**: compatibility, security, performance, migration, operational, or policy limits that matter.
- **Acceptance criteria**: falsifiable outcomes that can prove the work complete.
- **Technical implications**: repository areas, contracts, or architecture likely affected, without pretending a final design is already approved.
- **Open decisions**: only decisions that still require explicit human authority.

## Boundary

This skill clarifies intent. It does not own implementation, branch creation, issue state, pull requests, approvals, workflow lifecycle, or mutation authority.

If the target repository already has a governed workflow, hand the clarified contract back to that workflow instead of inventing a parallel phase machine.

Do not implement until the user or the authoritative project workflow has authorized implementation.
