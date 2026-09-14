# Contributing to agent-skills

Thank you for your interest in contributing! We welcome new skills, improvements to existing skills, bug fixes, and documentation updates.

## Skill Specification

Every skill lives in its own subdirectory under `skills/<skill-name>/` and must include a `SKILL.md` file following the [Agent Skills](https://agentskills.io/) specification:

- Frontmatter in YAML format at the beginning of `SKILL.md`:
  ```yaml
  ---
  name: <skill-name>
  description: <clear, actionable description of what the skill does and when to use it>
  license: MIT
  metadata:
    author: <author or organization>
    version: "1.0.0"
  ---
  ```
- The directory name must match the `name` field in the frontmatter.
- The `description` should be precise so coding agents can trigger the skill accurately when relevant.
- Markdown content should provide concise, high-signal instructions, rules, and examples.

## Knowledge ownership and lifecycle

`agent-skills` owns portable, tool-neutral engineering guidance. Before adding or materially changing a skill or rule, establish that this repository is the right semantic owner.

Use these questions as a decision contract:

1. **Is the guidance portable and tool-neutral?** If correctness depends on one tool's CLI, API, schema, file layout, generated artifacts, or lifecycle behavior, keep the canonical instructions with that tool instead.
2. **Does the guidance still require engineering judgment?** Heuristics and context-dependent practices belong here. Objective invariants are candidates for structural enforcement.
3. **What evidence justifies the guidance?** Prefer a concrete failure, review finding, experiment, issue, regression, or other observable engineering cost over taste or convention alone.
4. **Does another skill or semantic owner already express the same principle?** Extend or reuse the existing owner instead of creating overlapping guidance under a new name.
5. **Could code own this instead?** Prefer an owner API, type, invariant, regression test, static-analysis rule, formatter rule, or automation when it can enforce the behavior reliably.
6. **What would make this guidance removable?** Retire or shrink prose when it becomes stale, duplicated, disproven, harmful, tool-owned, or already structurally enforced.

Do not add lifecycle metadata merely to classify prose. First prove a real consumer needs machine-readable lifecycle data. A smaller skill catalog with sharper ownership is preferable to preserving every historical rule forever.

## Adding or Updating a Skill

1. Fork the repository and clone your fork.
2. Create a feature branch: `git checkout -b feature/my-new-skill`
3. Create a new directory under `skills/<my-skill-name>/` and add `SKILL.md`.
4. Validate that `SKILL.md` contains valid YAML frontmatter and well-formed Markdown.
5. Update `CHANGELOG.md` with your additions or improvements.
6. Submit a pull request.

## Pull Requests

- Keep pull requests focused on a single skill or topic.
- Ensure the skill name is unique and directory name matches the `name` attribute.
- Verify frontmatter syntax and Markdown formatting.
- Follow the pull request template provided.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
