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
