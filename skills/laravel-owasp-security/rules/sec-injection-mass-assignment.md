---
id: sec-injection-mass-assignment
title: "SQL, Command, and Mass-Assignment Injection Prevention"
category: injection
priority: CRITICAL
triggers: [sql-injection-raw-query, mass-assignment-request-all, unvalidated-order-by-column, shell-command-injection]
tags: [security, laravel, sql-injection, mass-assignment, command-injection, validation, owasp]
---

# SQL, Command, and Mass-Assignment Injection Prevention

**Trigger Anchor:** Always use parameterized PDO bindings (`?` or `:param`) in raw queries (`whereRaw`, `selectRaw`); validate and whitelist fillable model attributes; never pass `$request->all()` into model mutators; avoid raw shell executions.

---

### Bad
```php
// ❌ SQL injection via string concatenation in raw clauses
$status = $request->input('status');
$orders = DB::table('orders')
    ->whereRaw("status = '" . $status . "'") // SQLi vulnerability!
    ->get();

// ❌ Mass-assignment vulnerability allowing users to set admin role
$user = User::create($request->all()); // User can inject ['is_admin' => true]!

// ❌ Command injection via shell_exec with unescaped argument
$filename = $request->input('file');
shell_exec("pdftotext " . $filename . " output.txt");
```

### Good
```php
// ✅ Parameterized bindings in raw clauses
$status = $request->input('status');
$orders = DB::table('orders')
    ->whereRaw('status = ?', [$status])
    ->get();

// ✅ Safe mass-assignment using Form Request validated data and explicit $fillable
$validated = $request->validate([
    'name'  => ['required', 'string', 'max:255'],
    'email' => ['required', 'email', 'unique:users,email'],
]);
$user = User::create($validated);

// In User model:
// protected $fillable = ['name', 'email'];

// ✅ Safe command execution via Symfony Process with argument array
use Symfony\Component\Process\Process;

$process = new Process(['pdftotext', basename((string)$request->input('file')), 'output.txt']);
$process->mustRun();
```
