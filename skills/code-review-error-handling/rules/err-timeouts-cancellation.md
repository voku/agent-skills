---
id: err-timeouts-cancellation
title: "Bounded Operations, Timeouts, and Cancellation Discipline"
category: resilience
priority: CRITICAL
triggers: [unbounded-network-call, missing-http-timeout, infinite-socket-wait, missing-cancellation-token, blocking-io-thread]
tags: [error-handling, timeouts, cancellation, network-io, resilience, bounded-execution]
---

# Bounded Operations, Timeouts, and Cancellation Discipline

**Trigger Anchor:** Bound all external I/O, network requests, and distributed locks with explicit connect and read timeouts; propagate cancellation signals or check execution deadlines to prevent worker thread starvation.

---

### Bad
```php
// ❌ Unbounded HTTP call blocks worker thread indefinitely on unresponsive upstream
$client = new \GuzzleHttp\Client();
$response = $client->get('https://partner-api.example.com/data'); // Default: infinite timeout!

// ❌ Bare file_get_contents with no stream context timeout
$content = file_get_contents('https://external-service.org/feed.xml');

// ❌ Infinite polling loop without deadline or max attempts
while (!$job->isFinished()) {
    sleep(1); // Hangs forever if job crashes silently
}
```

### Good
```php
// ✅ Explicit connect and transfer timeouts on all HTTP clients
$client = new \GuzzleHttp\Client([
    'connect_timeout' => 2.0,  // Fast fail on unreachable host
    'timeout'         => 10.0, // Bound maximum read duration
]);
$response = $client->get('https://partner-api.example.com/data');

// ✅ Explicit stream context with timeout
$context = stream_context_create([
    'http' => [
        'timeout' => 5.0,
        'ignore_errors' => true,
    ],
]);
$content = file_get_contents('https://external-service.org/feed.xml', false, $context);

// ✅ Bounded polling with explicit timeout deadline and max attempts
$deadline = microtime(true) + 30.0;
$attempts = 0;
$maxAttempts = 30;

while (!$job->isFinished()) {
    if (microtime(true) > $deadline || ++$attempts > $maxAttempts) {
        throw new TimeoutException('Job polling timed out after 30 seconds.');
    }
    usleep(500_000); // 500ms
}
```
