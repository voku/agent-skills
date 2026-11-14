---
id: sec-injection-defense
title: "Injection Defense: Parameterized Queries, Command Isolation, and Path Traversal"
category: injection
priority: CRITICAL
triggers: [sql-injection, raw-string-concatenation, command-injection, shell-exec-untrusted, path-traversal-basename]
tags: [security, sql-injection, command-injection, path-traversal, parameterized-queries]
---

# Injection Defense: Parameterized Queries, Command Isolation, and Path Traversal

**Trigger Anchor:** Always parameterize SQL queries, isolate process execution using argument arrays (never raw shell string interpolation), and sanitize filesystem paths with basename/whitelisting against directory traversal.

---

### Bad
```php
// ❌ SQL Injection via string interpolation in query
$userId = $_GET['user_id'];
$result = $pdo->query("SELECT * FROM users WHERE id = '" . $userId . "'");

// ❌ Command Injection via shell_exec with unescaped shell argument
$filename = $_POST['filename'];
$output = shell_exec("gzip /tmp/uploads/" . $filename);

// ❌ Path Traversal allows reading arbitrary system files
$file = $_GET['file'];
$content = file_get_contents('/var/www/uploads/' . $file); // e.g. file=../../etc/passwd
```

### Good
```php
// ✅ Parameterized query using prepared statements and typed parameters
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = :id');
$stmt->execute(['id' => (int)$_GET['user_id']]);
$result = $stmt->fetch();

// ✅ Safe process execution using argument lists (no shell invocation)
use Symfony\Component\Process\Process;

$filename = basename((string)$_POST['filename']);
$process = new Process(['gzip', '/tmp/uploads/' . $filename]);
$process->mustRun();

// ✅ Path traversal prevention via basename and realpath boundary check
$safeFilename = basename((string)$_GET['file']);
$uploadDir = realpath('/var/www/uploads');
$targetPath = realpath($uploadDir . '/' . $safeFilename);

if ($targetPath === false || !str_starts_with($targetPath, $uploadDir . DIRECTORY_SEPARATOR)) {
    throw new AccessDeniedException('Invalid file path.');
}
$content = file_get_contents($targetPath);
```
