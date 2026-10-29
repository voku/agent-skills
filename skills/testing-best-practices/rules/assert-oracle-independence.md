---
id: assert-oracle-independence
title: Independent Test Oracles and Counterexamples
category: assert
priority: HIGH
triggers: [self-confirming-tests, mirror-implementation-test, circular-oracle, tautological-assertion, tdd-red-without-requirement]
tags: [testing, tdd, assertions, oracles, falsification]
---

# Independent Test Oracles and Counterexamples

**Trigger Anchor:** Before accepting RED or GREEN, derive expected behavior from an approved requirement, public contract, independently checked example, or invariant, not from the same implementation being tested.

## Test Design Challenge Before GREEN

For each material behavior test, identify the exact requirement it protects, the observable input and outcome, and the source of the expected result. Ask two questions:

1. Could a *different correct implementation* satisfy the requirement but fail this test?
2. Could a *plausibly incorrect implementation* pass this test?

A RED test that fails because of broken setup, an arbitrary string, or an accidental implementation choice is not strong evidence of the requested behavior. Re-ground the oracle before implementing a fix. When no meaningful test seam exists, record the limitation rather than manufacture RED.

## Bad: Circular Oracle

```php
<?php

declare(strict_types=1);

$expected = $formatter->format($value);
$actual = $formatter->format($value);
self::assertSame($expected, $actual);
```

The assertion compares one production result with the same production result. An incorrect formatter passes.

## Better: An Independent Contract

```php
<?php

declare(strict_types=1);

// Requirement: inactive accounts must never receive an access grant.
self::assertFalse($policy->mayGrantAccess(new Account(active: false)));
```

The expected denial comes from the security contract, not from consulting `mayGrantAccess()` to derive the expected value. Also cover an allowed case so an implementation that always denies cannot pass the entire suite.

## Review and Evidence

- Cross-check the test against the original task/Contract, not just the developer's implementation explanation.
- Prefer independently specified examples, public invariants, boundary partitions, and negative scenarios.
- Avoid snapshot-only proofs, tautologies, and reimplementing the production algorithm inside the test.
- Independent review context reduces correlated assumptions, but does not itself validate the oracle.
- Record concrete evidence for both probes, or state UNKNOWN; do not claim behavior was tested from prompt wording alone.
- Precise labels, error codes, or strings may be legitimate contractual outcomes. Keep those assertions when the requirement explicitly makes them stable.
