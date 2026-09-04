# PHP Static Analysis — Full Compiled Reference

Implementation guidance for making PHP code provably typed under a strict static analyzer.

**Version:** 1.0.0 | **Rules:** 6 | **License:** MIT

---

## Operational Contract

When applying this skill, agents must:
- Treat this skill as repo-owned guidance and defer to repository or task-specific instructions when they conflict.
- Resolve an analyzer message by making its claim untrue, not by hiding the message.
- State for each finding whether the cause is a wrong contract or a missing proof, and fix it at the owning layer.
- Verify with the project's own analyzer command on the changed scope, and claim a pass only after observing its exit code.
- Never widen a public contract, add a directory-wide exclusion, or extend a baseline to keep a build green without saying so explicitly.

## Rules

See `rules/` for the six rule files and `rules/_sections.md` for ordering and severity.
