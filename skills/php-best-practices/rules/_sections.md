# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Type System (type)

**Impact:** CRITICAL
**Description:** Strict type enforcement is the foundation of reliable PHP code. Type declarations prevent bugs, enable static analysis, and provide self-documenting contracts. Essential for modern PHP 8.x development.

## 2. Modern PHP Features (modern)

**Impact:** CRITICAL
**Description:** PHP 8.x features that reduce boilerplate and improve code clarity. Each rule is annotated with its minimum PHP version. Always check the project's PHP version before suggesting features. Covers: constructor promotion (8.0), enums (8.1), readonly (8.1/8.2), typed constants and #[\Override] (8.3), property hooks and asymmetric visibility (8.4), and pipe operator (8.5).

## 3. PSR Standards (psr)

**Impact:** HIGH
**Description:** PHP-FIG standards (PSR-4 autoloading, PSR-12 coding style, naming conventions) ensure code interoperability and maintainability. Following PSR standards is expected in professional PHP development.

## 4. SOLID Principles (solid)

**Impact:** HIGH
**Description:** SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) create maintainable, testable, and flexible code architectures.

## 5. Error Handling (error)

**Impact:** HIGH
**Description:** Proper exception handling, custom exceptions, exception hierarchies, and resource cleanup strategies prevent silent failures and enable graceful error management.

## 6. Performance (perf)

**Impact:** MEDIUM
**Description:** Performance optimizations including lazy loading, generators, native array/string functions, and avoiding globals improve application scalability and resource usage.

## 7. Security (sec)

**Impact:** CRITICAL
**Description:** Security practices including input validation, output escaping, password hashing, prepared statements, and file upload validation protect against OWASP Top 10 vulnerabilities.

## 8. PHPStan PHPDoc (phpstan)

**Impact:** CRITICAL
**Description:** PHPStan-compatible PHPDoc annotations (generics, array-shapes, class-strings, int-ranges, conditional return types) extend PHP's native type system and maximise static-analysis coverage.

## 9. Design Patterns (design)

**Impact:** HIGH
**Description:** Value objects over primitives eliminates primitive obsession and enforces domain invariants at construction time. Avoiding magic-heavy design ensures all behavior is visible to static analysis and IDEs.

## 10. Legacy Migration (legacy)

**Impact:** HIGH
**Description:** Structured, incremental strategy for modernising legacy PHP codebases: safety-net first, automated Rector transforms, incremental type coverage, Strangler Fig isolation of legacy code.

## 11. Tooling (tooling)

**Impact:** CRITICAL
**Description:** Mandatory PHPStan + php-cs-fixer validation loop run before every commit and enforced in CI. Provides objective quality metrics and automated style enforcement.
