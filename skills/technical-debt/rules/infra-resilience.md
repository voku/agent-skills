---
id: infra-resilience
title: "Infrastructure Debt: EOL Runtimes, Secrets, and Observability"
category: infra
priority: MEDIUM
triggers: [eol-runtime, deprecated-framework-api, build-warning, unmanaged-secret, observability-gap]
tags: [infrastructure, runtime, node, php, docker, secrets, logging, telemetry]
---

# Infrastructure Debt: EOL Runtimes, Secrets, and Observability

**Trigger Anchor:** Maintain supported LTS runtime engines (PHP/Node), treat build warnings as errors, migrate deprecated framework APIs, inject secrets via dedicated secret managers, and configure structured JSON logging with p95 telemetry.

---

### Bad
```dockerfile
# ❌ End-of-life runtime without security patches and baked-in secrets
FROM php:7.4-fpm-alpine

# ❌ Hardcoded secret baked directly into Docker image layer
ENV DB_PASSWORD="production_secret_123"

# ❌ Unstructured stdout spam without correlation IDs or severity levels
RUN echo "log_errors = On" >> /usr/local/etc/php/php.ini
```

### Good
```dockerfile
# ✅ Supported LTS runtime with non-root security context and runtime secret injection
FROM php:8.3-fpm-alpine

USER www-data

# Secrets injected at runtime via orchestration (K8s secret / AWS SSM / Doppler)
```

```php
<?php

declare(strict_types=1);

// ✅ Structured JSON logging with trace correlation IDs
Log::info('Order checkout completed', [
    'order_id' => $order->id,
    'duration_ms' => $stopwatch->durationMs(),
    'trace_id' => request()->header('X-Trace-Id'),
]);
```
