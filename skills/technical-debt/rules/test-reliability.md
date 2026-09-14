---
id: test-reliability
title: "Test Debt: Coverage Gaps, Flakiness, and Slow Suites"
category: test
priority: HIGH
triggers: [untested-critical-path, flaky-test, disabled-test, slow-test-suite]
tags: [testing, flakiness, ci-speed, integration-tests]
---

# Test Debt: Coverage Gaps, Flakiness, and Slow Suites

**Trigger Anchor:** Ensure critical revenue/security paths have integration test coverage, quarantine or fix flaky tests immediately instead of re-running CI, track down disabled/skipped tests, and enforce test duration budgets (<10 minutes).

---

### Bad
```typescript
// ❌ Flaky test relying on real timers, arbitrary sleeps, and disabled assertions
describe('Notification Poller', () => {
  // ❌ Skipped test left forgotten without issue tracker reference
  it.skip('handles webhook retries on disconnect', () => {
    // Left disabled for 9 months
  });

  // ❌ Flaky: fails intermittently in CI depending on runner CPU load
  it('polls new notifications', async () => {
    startPolling();
    await new Promise((resolve) => setTimeout(resolve, 500)); // ❌ Race condition sleep
    expect(getReceivedCount()).toBeGreaterThanOrEqual(1);
  });
});
```

### Good
```typescript
// ✅ Deterministic test using mock timers and explicit condition awaiting
describe('Notification Poller', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('polls new notifications deterministically without race conditions', async () => {
    const poller = new NotificationPoller();
    poller.start();

    await vi.advanceTimersByTimeAsync(5000);

    expect(poller.receivedCount).toBe(1);
  });
});
```
