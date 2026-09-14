---
id: perf-network-batching
title: "Network I/O Reduction, Batching, and Payload Sizing"
category: network-io
priority: HIGH
triggers: [round-trip-fanout, synchronous-api-in-loop, payload-overfetching, chatty-remote-calls]
tags: [performance, network-io, batching, http-calls, round-trips]
---

# Network I/O Reduction, Batching, and Payload Sizing

**Trigger Anchor:** Batch remote API and directory service calls into single multi-get/bulk requests; avoid sequential round trips inside loops; select only required columns/fields rather than over-fetching.

---

### Bad
```php
// ❌ Sequential chatty network calls inside loop (50 network round trips!)
foreach ($accountIds as $accountId) {
    $ldapAccount = $ldapClient->findUserBySamAccountName($accountId);
    $results[] = $ldapAccount;
}

// ❌ Over-fetching: pulling all 45 columns of large text/blobs when only 2 are needed
$activeUsers = DB::select('SELECT * FROM users WHERE status = 1');
```

### Good
```php
// ✅ Single batched directory lookup query with OR filter
$samFilters = array_map(static fn(string $id): string => '(sAMAccountName=' . ldap_escape($id, '', LDAP_ESCAPE_FILTER) . ')', $accountIds);
$bulkLdapFilter = '(|' . implode('', $samFilters) . ')';
$results = $ldapClient->search($baseDn, $bulkLdapFilter, ['sAMAccountName', 'mail', 'displayName']);

// ✅ Targeted column selection reducing network and memory payload
$activeUsers = DB::select('SELECT id, name, email FROM users WHERE status = 1');
```
