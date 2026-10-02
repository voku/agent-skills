# Changelog

Notable changes to the `voku/agent-skills` catalog are documented here.

This repository is a skill catalog rather than a Composer package, so entries are
dated and tied to Git commits instead of inventing a package version that no
runtime consumes.

## 2026-10-02 - High-signal catalog cleanup

### Removed

- Removed 21 broad or version-sensitive cookbook skills whose primary value was
  static reference knowledge rather than durable agent behavior:
  `api-design-patterns`, `clean-code-principles`, `e2e-playwright-testing`,
  all `laravel-*` skills, `php-best-practices`, `prd-writing`,
  `project-docs`, `react-vite-best-practices`, `seo-best-practices`,
  `state-management`, `tailwind-best-practices`, `technical-debt`,
  `typescript-react-patterns`, and `web-design-guidelines`.
- Removed static framework snapshots where current semantic owners are more
  reliable. Laravel, for example, now provides package-aware Boost documentation
  and guidelines for coding agents.
- Removed stale or misleading duplicated guidance rather than refreshing it in
  place. The retired catalog included an OWASP 2021 checklist after OWASP 2025
  was current, plus an API example that treated PATCH as inherently idempotent.

### Changed

- The catalog now favors behavior-changing skills: evidence discipline, focused
  review lenses, falsification, scoped execution, static-analysis rigor, runtime
  diagnosis, and workflow boundaries.
- Contribution guidance now requires a skill to earn its context cost instead of
  restating baseline model knowledge or live framework documentation.

## 2026-10-02 - Linux strace runtime profiling

### Added

- Added `linux-strace`, a bounded runtime-diagnostics skill for Linux processes,
  with explicit PHP CLI/PHP-FPM guidance for slow requests, hangs, repeated
  database/socket I/O, filesystem chatter, network waits, subprocess waits, and
  lock-contention symptoms.
- The skill separates syscall evidence from application-level conclusions:
  repeated database-socket traffic can establish chatty I/O, while exact SQL
  duplication or N+1 claims require decoded payloads or database/application
  instrumentation.
- Added permission, sensitive-output, bounded-capture, and profiler-handoff
  boundaries so `strace` does not become an excuse to trace an entire production
  host indefinitely.

## 2026-09-20 - First-party compact Git message guidance

### Changed

- Extended `git-workflow` commit guidance with a concise subject preference,
  rationale-only body rules, and an explicit no-mutation boundary for message
  formatting. This keeps the useful compact-message behavior in the canonical
  portable skill without requiring an external commit helper.

## 2026-09-11 - Fresh review and read-only role boundaries

### Changed

- `engineering-codelight` now prefers fresh-context semantic review built from
  the contract, artifact, and relevant evidence instead of implementation
  narration that can anchor an independent reviewer.
- Investigation and review roles should use host-enforced read-only capability
  boundaries when the host supports them, without turning those host mechanics
  into a second workflow or lifecycle.

## 2026-09-09 - Codelight engineering reasoning

### Added

- Added `engineering-codelight`, a compact, technology-neutral reasoning skill
  for non-trivial engineering work. It keeps evidence distinct from authority,
  preserves uncertainty and instruction provenance, respects owner boundaries,
  favors falsifiable small changes, re-grounds stale plans, makes recovery
  possible, and promotes transferable learning into structural constraints.
- Added CI checks for the skill's frontmatter/structure, nine-law core,
  workflow-neutral boundary, prohibited lifecycle/framework text, and 5 KiB
  preferred / 8 KiB review-size budgets.

## 2026-08-25 - Review rules, PHP static analysis, and dogfood closeout classification

### Added

- Added `php-static-analysis` skill providing implementation guidance for provably typed PHP code under strict analyzers (native types first, shape/generic precision, contract honesty, root-cause typing, scoped ignores, analyzer extensions).
- Added `dogfood-closeout-classification` skill enforcing classification of LLM inference points and private leak checks before session closeout and upstream commits.
- Added targeted review rules:
  - `code-review-error-handling`: `err-outcome-messaging` (outcome messaging discipline).
  - `code-review-simplicity`: `simp-premature-abstraction` (premature abstraction checks).
  - `code-review-type-safety`: `type-asymmetric-rigor` (consistent validation rigor across sibling branches).
  - `testing-best-practices`: `cov-adversarial-probe` (adversarial probing before happy-path tests) and `cov-regression-first` (regression test reproducing bug before fixing).

## 2026-08-14 - Falsification-safe adversarial review

### Changed

- `adversarial-review` now applies its numeric floor to distinct plausible
  failure-mode hypotheses or attack scenarios that must be investigated, not to
  confirmed defects that the reviewer is forced to produce.
- Disproving a hypothesis is explicitly useful falsification evidence and
  `CLEAN` remains a valid result after the requested probes find no
  evidence-backed defect.
- Documented the ownership boundary between the context-light
  `agent-recall-compiler review first-draft` lens and the project-grounded L2
  `adversarial-review` recipe.

### Fixed

- Removed the Goodhart-shaped incentive to manufacture findings merely to satisfy
  an adversarial-review count.

## 2026-08-13 - Scoped compatibility review

### Added

- Added the L2 `breaking-change-review` recipe. It turns current task scope and
  repo-owned project policy into a project-specific compatibility review rather
  than assuming either permanent backward compatibility or unrestricted breakage.
- The recipe prefers coordinated owner/consumer migration and deletion of
  the old path before compatibility layers when the applicable project policy
  allows breaking change, and blocks when policy is missing or contradictory.

## 2026-08-09 - Governed operational prompting and coding simplicity

### Added

- Added `coding-simplicity`, an implementation-time skill that searches for the
  smallest correct solution in this order: no change, existing repository owner,
  standard library, native platform capability, installed dependency, shared
  root-cause fix, then minimum new code. Safety and verification floors remain
  mandatory.
- Added a reusable `operational-prompting/operating-prompts.json` catalog with
  explicit L1/L2 recipe levels. Most engineering recipes are L2 so current
  project recall can turn reusable method into a project-specific L1 execution
  contract instead of shipping generic prompts with placeholders.
- Added L2 recipes for planning horizons, regression hunting, coverage plus
  mutation testing, deletion-first review, missingness audits, adversarial review,
  reproduce-before-fix, reject-and-restart, and multi-pass
  correctness/simplification work.
- Added context-independent L1 controls for continuation, evidence reporting, and
  bounded retry/stop behavior.

### Changed

- Operational contracts now use the five-part shape `Goal + Context + Constraints
  + Verification + Done When`. Verification defines the measurement procedure;
  Done When defines the observable stopping condition.
- Code-review skills are targeted independent lenses rather than an automatic
  review swarm. Start with the dominant lens and allow at most one evidence-backed
  handoff when another concern becomes primary.
- Reusable recipes carry no hidden task thresholds or project commands. Numeric
  floors, retry limits, mutation commands, horizons, and other policy are explicit
  caller arguments; repository facts come from the consuming project's recall.

### Fixed

- Repository badges, installation commands, clone examples, and per-skill `npx`
  examples now point at `voku/agent-skills` instead of the upstream fork owner.
