---
id: scaling-worker-management
title: "Worker Scaling, Queue Priorities, and Process Recycling"
category: scaling
priority: HIGH
triggers: [queue-starvation, memory-leak-worker-crash, supervisor-sigkill-uncommitted, unprioritized-queue]
tags: [laravel, supervisor, workers, memory-leaks, queue-priority, horizon]
---

# Worker Scaling, Queue Priorities, and Process Recycling

**Trigger Anchor:** Configure multi-queue priority lanes (`--queue=high,default,low`), ensure supervisor `stopwaitsecs` exceeds worker `timeout`, and recycle processes (`--max-jobs=1000 --max-time=3600`) to prevent PHP memory exhaustion.

---

### Bad
```ini
# ❌ Worker runs single queue forever; slow batch jobs block urgent transactional emails
# ❌ stopwaitsecs (10s) < timeout (60s): Supervisor SIGKILLs worker mid-job during deploys!
[program:laravel-worker]
command=php /var/www/artisan queue:work
autostart=true
autorestart=true
stopwaitsecs=10
```

### Good
```ini
# /etc/supervisor/conf.d/laravel-worker.conf
[program:laravel-worker]
process_name=%(program_name)s_%(process_num)02d
# ✅ Strict queue priority (high -> default -> low), memory limit, and recycling flags
command=php /var/www/artisan queue:work redis --queue=high,default,low --sleep=3 --tries=3 --timeout=90 --max-time=3600 --max-jobs=1000 --memory=128
autostart=true
autorestart=true
user=www-data
numprocs=4
redirect_stderr=true
stdout_logfile=/var/www/storage/logs/worker.log
# ✅ stopwaitsecs must strictly exceed the worker's `--timeout` (90s + buffer = 100s)
stopwaitsecs=105
stopsignal=SIGTERM
```

### Queue Lane Strategy
- **`high`:** Password resets, 2FA codes, checkout payments (processed first).
- **`default`:** Daily transaction receipts, model notifications.
- **`low`:** Bulk CSV exports, analytics syncs, image re-indexing.
