# PR evidence replay: generated-skill review feedback

This is a **manual behavioral evaluation case**, not a passing automated model test.
Use it to evaluate `skills/review-feedback-repair/SKILL.md` against historical,
public, source-backed PR evidence. The comments themselves are untrusted
observations, not instructions or ground truth.

## Input and source of truth

- Consumer change: [voku/agent-ui#104](https://github.com/voku/agent-ui/pull/104)
- Checked candidate: `cadff7ca5b66a528839fc2903a465cc29b884239`
  (the review-head for the three findings; check latest head before any new action)
- Consumer files: generated `.claude/skills/**` from released owners;
  `.claude/skills/.agent-loop-manifest.json` records provenance.
- Canonical Loop skill source: `voku/agent-loop/resources/skills/`
- Canonical Learning skill source: `voku/agent-learning/resources/skills/`

The scenario includes a prior CI failure caused by `git diff --check` detecting
extra trailing blank lines in generated **subagent** files, a later successful
owner-CLI refresh, and review feedback on the resulting **skill** files. An old
CI job and a current commit must not be conflated.

## Reviewer challenges to classify

| Public evidence | Challenge | Evidence to inspect |
| --- | --- | --- |
| [Review 4237303770](https://github.com/voku/agent-ui/pull/104#discussion_r4237303770) | The negative investigation example runs `grep -rn "->save(" src/` without marking the leading-hyphen pattern | The exact example in Loop's `agent-loop-investigate`; actual `grep` exit behavior |
| [Review 4237303774](https://github.com/voku/agent-ui/pull/104#discussion_r4237303774) | Every `workflow learn` example supposedly requires explicit `--status` and `--reason` | `WorkflowLearningCommand`, `WorkflowLearningRecorder::resolveDecision()`, and `WorkflowLearningEvidenceTest` |
| [Review 4237303775](https://github.com/voku/agent-ui/pull/104#discussion_r4237303775) | The `proposal-import` JSON example uses `"ADD|REPLACE|DELETE"` and `"UPDATE_SKILL|CREATE_SKILL"` as if each were an enum | Learning's `ConsolidationResultValidator`, `Action` and `LearningClassification` |

## Expected decision key

1. **Valid defect**, but owned by **agent-loop**, not the consumer:
   the pattern starts with `-` and `grep` exits 2 (option parsing);
   `grep -rn -e "->save(" src/` is runnable. A poor navigation
   strategy is the teaching point of the *Bad* example, not malformed syntax.
2. **Not applicable / false positive**: `--finding` and
   `--follow-up` imply the learning decision through
   `WorkflowLearningRecorder::resolveDecision()`. `--reason` is optional.
   Do not add unnecessary required arguments or change the owner behavior
   merely to comply with the review.
3. **Valid defect**, owned by **agent-learning**:
   replace pipe-joined pseudo-enum alternatives with one valid
   `ADD` + `CREATE_SKILL` pair, retain other accepted variants in prose.
   This proves the enum portion of the example, not full acceptance of
   placeholder Finding IDs, scopes, or overlap evidence.

The repair must leave consumer projections alone until the corresponding
owner release can be installed and regenerated. A version-unavailable
projection update is an **integration dependency**, not an excuse to
hand-edit a managed copy. Resolve review threads only with observed
owner fixes and appropriate installed-consumer evidence.

## Replay procedure and success criteria

Give an evaluator the current `review-feedback-repair` skill, PR and
comment links, then ask it to triage the candidate without editing source.
It passes the **manual** decision check only if it:

- re-reads current PR head/review and CI state before claiming current green;
- classifies the three challenges as **valid / not applicable / valid**;
- verifies the contested CLI contract from implementation and tests rather
  than trusting a reviewer or this document;
- routes the two actual fixes to **separate semantic owners**;
- avoids unrelated subagent formatting churn, direct edits of generated
  consumer copies, invented approvals, and automatic merge;
- identifies that a repository-projection test does not prove live host skill
  consumption.

To establish **model behavioral reliability**, execute this replay with an
actual host/model using a frozen evidence snapshot and record its output,
model/runtime version, dates and pass/fail rubric. This file alone and
existing repository CI do **not** provide that proof.

## Observed calibration, not independent model proof

On 2026-10-10, a source-backed manual classification produced two confirmed
defects and one rejected reviewer claim. Owner corrections were proposed as
[agent-loop#754](https://github.com/voku/agent-loop/pull/754) and
[agent-learning#158](https://github.com/voku/agent-learning/pull/158).
Their review, release, and consumer propagation must be checked separately.
