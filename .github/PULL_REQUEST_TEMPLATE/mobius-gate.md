<!-- mobius-gate: one PR per intent. Claude fills the artifacts; humans pass the gates. -->
Closes #ISSUE

## Artifacts
- Intent: `work/ISSUE/intent.md` · Spec: `work/ISSUE/spec.md` · Plan: `work/ISSUE/plan.md`
- Tests lock: `work/ISSUE/tests.lock` (written by the workflow when the plan is approved)

## Gates
- [ ] **Plan + tests** — review *Approve* by an approver (check `mg/tests-red` first: every new test must fail). Locks the tests.
- [ ] **Build** — `mg/ci` green, `mg/tests-locked` green.
- [ ] **E2E** — report read, environment `mg-e2e` approved (or label `mg:e2e-approved`).
- [ ] **Merge** — final code review and merge by a human.
- [ ] **Deploy** — environment `production` approved (or label `mg:deploy-approved`).

> A locked test looks wrong? Claude stops and explains in a PR comment. Only a human changes the test, then re-approves with `mg:relock` in the review.
