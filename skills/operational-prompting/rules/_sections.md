# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Instruction hierarchy, repo-owned guidance, and task scope | Repository setup, AGENTS.md authoring, and task definition |
| HIGH | Validation loops, terminal contracts, and falsifiable evidence | Test execution, linting, and CI pipelines |
| MEDIUM | Vendor-neutral skill manifests and portable tool boundaries | Skill creation and packaging |

## Section Overview

### 1. Instruction Hierarchy (`hierarchy`)
- **Impact:** CRITICAL
- **Rules:** `op-repo-owned-hierarchy`
- **Description:** Storing agent rules in version-controlled repository files; resolving precedence from host to task.

### 2. Task Scope & Stopping (`task-scope`)
- **Impact:** CRITICAL
- **Rules:** `op-scope-stopping-contracts`
- **Description:** Bounding task scopes, prohibiting drive-by refactorings, and defining unambiguous stopping conditions.

### 3. Validation & Evidence (`validation`)
- **Impact:** HIGH
- **Rules:** `op-validation-evidence-loops`
- **Description:** Closed-loop verification via observable CLI exit codes; demanding falsifiable terminal evidence.

### 4. Portability & Skill Manifests (`portability`)
- **Impact:** MEDIUM
- **Rules:** `op-portable-skill-manifests`
- **Description:** Standard YAML frontmatter, vendor-neutral skill authoring, and separating principles from CLI mechanics.
