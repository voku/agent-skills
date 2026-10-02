---
name: linux-strace
description: Diagnose Linux runtime bottlenecks with strace, especially PHP CLI, PHP-FPM, and Apache/PHP workloads. Use for slow requests, hanging processes, repeated database/socket I/O, blocking waits, filesystem chatter, DNS/network stalls, lock contention symptoms, and "where is this process spending time?" investigations. Prefer bounded evidence collection before code changes.
license: MIT
metadata:
  author: voku
  version: "1.0.0"
---

# Linux strace runtime profiling

Use `strace` when the question is about **runtime behavior at the syscall boundary**: what a process opens, reads, writes, connects to, waits on, retries, or blocks in.

This skill is particularly useful for PHP processes because a slow request can otherwise collapse into the extremely informative diagnosis "PHP is slow".

## Core rule

Observe first. Change code only after the trace supports a concrete bottleneck hypothesis.

`strace` can establish evidence such as:

- one PHP worker repeatedly writes to the same database socket;
- one request performs hundreds of small filesystem lookups;
- a process spends long intervals in `poll`, `recvfrom`, `connect`, `futex`, or file I/O;
- repeated failed syscalls create retry churn;
- child processes or external commands dominate request latency.

It **cannot automatically prove application semantics**. Repeated writes to a MySQL/MariaDB socket are strong evidence of database chatter, but not by themselves proof of a specific SQL N+1. SQL text may be unavailable or fragmented because of prepared statements, binary protocols, TLS, buffering, or string truncation.

## Part 1: ground the target

Before tracing, identify:

1. runtime: PHP CLI, PHP-FPM, Apache module, worker, queue consumer, cron;
2. exact process or command;
3. reproducible slow action;
4. whether the system is development, staging, or production;
5. current `strace` version and supported options.

Start with:

```bash
strace --version
strace --help
ps -eo pid,ppid,user,comm,args | grep -E 'php|php-fpm|apache2|httpd'
```

For PHP-FPM, prefer one worker that will handle a reproducible request instead of attaching to the entire pool immediately.

## Part 2: permission and safety boundary

Attaching uses `ptrace` and may be restricted by UID, capabilities, container boundaries, SELinux/AppArmor, or Yama:

```bash
cat /proc/sys/kernel/yama/ptrace_scope 2>/dev/null || true
```

Do not weaken host security settings automatically.

If elevated privileges are required, request explicit approval before using `sudo`.

Tracing can expose:

- SQL fragments and parameters;
- HTTP payloads;
- file paths;
- tokens or credentials;
- user data.

Treat trace output as sensitive. Prefer short captures, local reproduction, narrow syscall filters, and a unique private output file. For detailed traces, create the destination first:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
```

Reuse that variable only for the current capture and remove the file after the evidence has been extracted. Do not use predictable shared paths for sensitive traces.

`strace` is intrusive: ptrace stops/resumes tracees around syscalls and can perturb syscall-heavy workloads. Treat call shapes, endpoints, repetition, and obvious blocking as diagnostic evidence; validate any performance improvement again without `strace`.

Never use `--inject`, `--fault`, or syscall return-value manipulation during performance diagnosis unless fault injection is the explicit task.

## Part 3: choose the smallest useful flow

| Flow | Use when | Goal |
|---|---|---|
| A: summary | You only know "this is slow" | Find syscall families consuming time/calls |
| B: timed trace | You need the blocking operation | Find long individual syscalls and gaps |
| C: DB/socket chatter | You suspect repeated SQL or remote calls | Quantify repeated I/O to one socket |
| D: filesystem chatter | You suspect autoload/config/template/path overhead | Find repeated opens/stats/reads |
| E: hanging worker | A process appears stuck | Identify what it is waiting on now |

### Flow A: syscall summary first

Run the workload under `strace` when possible:

```bash
strace -f -c -- php path/to/script.php
```

Or attach to one existing process:

```bash
strace -f -c -p <PID>
```

Use the summary to rank calls by time, call count, and errors. For latency investigations, prefer wall-clock syscall time when supported:

```bash
strace -f -c -w -p <PID>
```

Without `-w`, the summary defaults to system CPU time spent in syscalls, which is not the same thing as elapsed request latency.

Useful follow-up signals:

- many `openat` / `newfstatat` calls -> filesystem/autoload/config chatter;
- many `connect` calls -> missing connection reuse or repeated remote setup;
- many `read` / `recvfrom` calls on one socket -> chatty dependency;
- high `poll` / `ppoll` / `epoll_wait` time -> waiting on external I/O;
- long or frequent `futex` -> lock/wait contention symptom;
- many failed syscalls -> retry/path-probing churn.

Do not optimize the largest call count blindly. A frequent cheap syscall may be irrelevant.

### Flow B: timed trace for latency

Capture timestamps, syscall duration, child processes, and decoded file descriptors:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -ttt -T -yy -s 256 -o "$trace_file" -p <PID>
```

For a command:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -ttt -T -yy -s 256 -o "$trace_file" -- php path/to/script.php
```

Interpret:

- the value in angle brackets from `-T` is syscall duration;
- `-ttt` gives comparable absolute timestamps;
- `-yy` associates descriptors with paths/sockets when available;
- `-f` follows forks/clones and is important for shell-outs and workers.

Start broad only long enough to identify the hot resource. Then narrow the capture.

### Flow C: repeated SQL / database socket activity

First locate the database connection in a short `-yy` trace. Look for Unix sockets such as MySQL/MariaDB socket paths or TCP connections to the configured DB host/port.

Then narrow to the descriptor when supported:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -ttt -T -yy --trace-fds=<FD> \
  -o "$trace_file" \
  -e trace=read,write,readv,writev,recvfrom,recvmsg,sendto,sendmsg \
  -p <PID>
```

To inspect payload bytes for a known descriptor:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -ttt -T -yy -s 4096 \
  -o "$trace_file" \
  -e trace=read,write,recvfrom,sendto \
  -e read=<FD> -e write=<FD> \
  -p <PID>
```

Use payload inspection only when necessary because it increases sensitive-data exposure.

Classify findings conservatively:

- **confirmed:** repeated writes/reads to the same DB socket within one request;
- **likely:** repeated similar payloads or request/response packet shapes;
- **not proven:** exact SQL duplication or N+1 without decoded application-level evidence.

When SQL text is not visible, correlate with application query logs, DB general/slow query logs, profiler instrumentation, or framework/database tracing. Do not invent query text from packet timing.

### Flow D: filesystem and autoload chatter

Trace file-related activity:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -ttt -T -yy \
  -o "$trace_file" \
  -e trace=%file,read,readlink,getdents64 \
  -p <PID>
```

Look for:

- the same path probed repeatedly;
- repeated missing-file lookups;
- excessive autoloader path searches;
- repeated config/template reads;
- unexpected network filesystems or slow mounts.

A high count alone is not enough. Correlate repeated paths with measured duration and the slow request window.

### Flow E: hanging or long-running process

For a worker that appears stuck:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
strace -f -tt -T -yy -o "$trace_file" -p <PID>
```

Common interpretations:

| Syscall | Typical meaning |
|---|---|
| `poll`, `ppoll`, `select`, `epoll_wait` | waiting for I/O/event |
| `recvfrom`, `recvmsg`, `read` on socket | waiting for peer response |
| `connect` | connection establishment / network problem |
| `futex` | lock or synchronization wait |
| `wait4`, `waitid` | waiting for child process |
| `openat`, `newfstatat`, `readlink` | filesystem/path resolution |
| repeated `ENOENT` / `EACCES` | failed path/permission probing |

If the process is CPU-bound and making few syscalls, `strace` is the wrong primary tool. Hand off to CPU profiling such as `perf`, sampling profilers, or language-level profiling.

## Part 4: keep captures bounded

Prefer a reproducible request plus an external timeout:

```bash
umask 077
trace_file="$(mktemp "${TMPDIR:-/tmp}/strace.XXXXXX")"
timeout --signal=INT 15s strace -f -ttt -T -yy -s 256 -o "$trace_file" -p <PID>
```

On newer `strace` versions, `--syscall-limit=<N>` is another useful guard.

Do not attach to every PHP-FPM worker for minutes unless the narrower experiment failed and the broader capture is justified.

## Part 5: analysis workflow

Reduce the trace before proposing fixes.

Useful questions:

1. Which descriptors/resources account for the slow window?
2. Which syscalls have the longest individual durations?
3. Which paths or socket endpoints repeat?
4. Are repetitions expected protocol behavior or avoidable application work?
5. Does one request trigger many DB round trips, filesystem probes, DNS lookups, or subprocess waits?
6. Is time spent in kernel syscalls, external waiting, or userspace CPU between syscalls?

For large captures, use ordinary text tooling to group evidence:

```bash
grep -E 'connect|recvfrom|sendto|read\(|write\(|openat|newfstatat|futex|poll|wait4' "$trace_file"
```

Do not claim userspace CPU hotspots from the absence of slow syscalls. The correct conclusion is only that syscall evidence does not explain the time.

## Reporting contract

Return evidence in this order:

```text
TARGET: <process/command and reproduction>
CAPTURE: <bounded strace command>
OBSERVED:
- <timestamp/resource/syscall evidence>
BOTTLENECK:
- <confirmed bottleneck or "not established">
CONFIDENCE:
- confirmed | likely | unknown
NEXT:
- <smallest next measurement or code change>
```

Separate:

- observed syscall facts;
- interpretation;
- application-level assumptions;
- recommended code changes.

A code change should name the measured waste it removes.

## Cross-tool handoff

Use another profiler when the evidence boundary moves:

- CPU-bound userspace code -> `perf` or a sampling profiler;
- exact SQL duplication/query plan -> DB logs, query profiler, `EXPLAIN`;
- PHP function-level attribution -> Xdebug profiler, Tideways, Blackfire, or equivalent;
- memory growth -> heap/memory profiler;
- kernel scheduling/CPU contention -> `perf sched`, eBPF, or system-level tooling.

Do not keep expanding `strace` after it has answered the syscall-level question.

## References

- strace manual: https://man7.org/linux/man-pages/man1/strace.1.html
- strace project: https://strace.io/
- Inspired by the flow-oriented structure of Intel's `linux-perf` skill:
  https://github.com/intel/intel-performance-skills/blob/main/skills/linux-perf/SKILL.md
