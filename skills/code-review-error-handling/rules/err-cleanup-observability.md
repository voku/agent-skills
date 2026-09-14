---
id: err-cleanup-observability
title: "Deterministic Resource Cleanup and Structured Observability"
category: observability
priority: HIGH
triggers: [leaked-file-handle, missing-finally-cleanup, unreleased-distributed-lock, unlogged-external-side-effect, logging-in-hot-loop]
tags: [error-handling, cleanup, finally, logging, audit-ordering, resource-management]
---

# Deterministic Resource Cleanup and Structured Observability

**Trigger Anchor:** Release resources (locks, file descriptors, transactions) deterministically in `finally` blocks; persist audit logs immediately after irreversible external mutations before local database writes; instantiate loggers outside loops.

---

### Bad
```php
// ❌ Lock is leaked if an exception is thrown inside the critical section
$lock = $lockFactory->createLock('resource-sync');
$lock->acquire(true);
$service->performCriticalSync(); // If this throws, lock is never released!
$lock->release();

// ❌ Inverted audit ordering: DB failure swallows audit record of external mutation
$ldapClient->modifyUserAttributes($userDn, $newAttributes);
$db->insertSyncHistory($userDn, $status); // If DB throws, external change was never logged!
$auditLogger->log('LDAP user attributes updated', ['dn' => $userDn]);

// ❌ Instantiating logger inside a tight loop allocates new syslog/file handles per iteration
foreach ($records as $record) {
    $logger = new SystemLogger('sync'); // Leaks OS handles / introduces severe overhead
    $logger->info('Record synced: ' . $record->id);
}
```

### Good
```php
// ✅ Deterministic lock release guaranteed by finally
$lock = $lockFactory->createLock('resource-sync');
$lock->acquire(true);
try {
    $service->performCriticalSync();
} finally {
    $lock->release();
}

// ✅ Audit log persisted immediately after irreversible external mutation, before DB bookkeeping
$ldapClient->modifyUserAttributes($userDn, $newAttributes);
$auditLogger->log('LDAP user attributes updated', [
    'dn' => $userDn,
    'changed_by' => $currentUser->getId(),
    'timestamp' => time(),
]);
// Local DB bookkeeping happens after external audit is guaranteed
$db->insertSyncHistory($userDn, $status);

// ✅ Reusable logger instantiated once outside the loop
$logger = new SystemLogger('sync');
foreach ($records as $record) {
    $logger->info('Record synced: ' . $record->id);
}
```
