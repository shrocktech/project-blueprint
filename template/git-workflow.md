# Git and Issue Workflow

Apply during development and queue work, not merely because the user asks a question or requests a review. Follow [AGENTS.md](AGENTS.md).

## Status and labels

Verify repository, Issues, and Project access before development; create/link the Project if missing. During bootstrap, create/claim the setup issue, then establish needed label/status definitions before assigning them; preserve existing mappings. Use a board grouped by Status, with these five statuses in order and exactly one matching uppercase workflow label:

| Status / label | Color | Meaning |
| --- | --- | --- |
| `BACKLOG` | Gray | Future/unapproved work; do not implement. |
| `TO DO` | Blue | Approved work expected to be done. |
| `IN PROGRESS` | Yellow | Implementation underway, paused, or ready to resume. |
| `IN REVIEW` | Lavender | Final testing, agent review, or delivery verification underway. |
| `DONE` | Green | Closed as completed, verified and delivered. |

Match Project status colors to the nearest available palette color.

Project authorization is separate from repository authorization; inspect token scopes and account/organization permissions before attributing a failure to the plan. Synchronize through available tools during active work; background synchronization is optional. Report genuine missing access with exact setup steps, not a plan-upgrade request.

Only `IN REVIEW` has a stage label: `testing` or `deployment`. Deployment means final integration and delivery verification; ordinary work targets development, with staging only if authorized and active. Production requires release authorization. Follow [project.md](project.md) for environments. Documentation-only work needs verified remote integration, not runtime deployment.

Use `IN PROGRESS` without a stage while building. Move finished work to `IN REVIEW` + `testing`, then `deployment` for integration/delivery. Replace previous status/stage labels. Required fixes return to `IN PROGRESS` without a stage, then repeat verification. Review means agent verification and automated checks; it adds no mandatory PR or human approval.

Routine pending checks stay `IN REVIEW`; record the candidate, run links, and remaining checks in the issue. Recheck results during active work and queue refreshes; pending, skipped, or unavailable required checks are not passes. If progress requires a user answer, setup, or provider/dependency change, use the pause flow below, even when discovered during review.

Use `bug`, `feature`, and `enhancement` while useful. Optional backlog items use `BACKLOG` plus exactly one descriptive label:

| Label | Meaning |
| --- | --- |
| `idea` | Early thought worth exploring. |
| `suggestion` | Recommended improvement with a brief reason. |
| `proposal` | Developed recommendation with scope, benefits, effort, and a decision needed. |

Choose the best fit; replace rather than stack these labels as the item develops. None authorizes implementation. At completion remove every label except `DONE`. Never mark canceled or unfinished issues completed.

## Paused work

Keep the issue open in the `IN PROGRESS` column with exactly `IN PROGRESS` and one reason label; remove its stage/type labels:

| Label | Color | Who must act |
| --- | --- | --- |
| `paused: decision` | Bright pink | User must answer, choose, or supply missing information. |
| `paused: setup` | Red | User must complete an action unavailable to the agent, such as account verification. |
| `paused: external` | Silver | Provider, service, or dependency must change; no user action unless stated. |

Try available APIs/tools and authorized autonomous actions first. Before removing labels, record prior status, any review stage, and type labels in the issue comment; preserve the worktree. Continue independent work; otherwise leave a handoff and take other approved work. Avoid repeated unchanged retries or nudges. For multiple blockers, label the next dependency and briefly list the others; change the reason as work advances.

After an answer or completed setup resolves all blockers, keep the issue open with only `IN PROGRESS` and matching Project status: ready to resume. Preserve removed labels in comments. Verify external dependencies; retain the appropriate pause while blocked. At task boundaries, read new comments and resume eligible owned work before new `TO DO` unless reprioritized. On resumption restore useful types, with a stage only for `IN REVIEW` testing/delivery; honor later user changes and ownership. Recheck external waits at task boundaries or through configured monitoring; label changes do not wake idle agents.

Quote pause labels exactly in commands and searches: `gh issue list --label 'paused: decision'` or `label:"paused: decision"`.

## Brief notes and proposals

For a requested guided review, use `issue-interview` at its recorded location: one question at a time with a recommendation and defer/answer-in-issue choices. Immediately comment each answer, apply the paused/ready rules above, and verify labels/Project status before the next question. Never batch updates or start implementation queue work during the interview.

Keep notes to the problem, what was tried/submitted, and the smallest next action. Use verified direct setup/settings/request links; otherwise give the official entry page and exact navigation. Never put secrets or token-bearing URLs in notes.

For decisions or optional proposals, ask one brief question: **A — Recommended** with a short reason, then useful **B/C** alternatives and tradeoffs. Allow the user's own answer; during interviews always include the D/E choices in the interview skill. For setup, provide short numbered steps, exact controls, expected result, and what to report back. For submitted requests, give the reference/status and say when no user action is needed. Do not promise monitoring without an actual runner.

Proactively record worthwhile optional items as separate `BACKLOG` issues with the appropriate descriptive label above. Check for duplicates and link the originating issue and evidence; keep notes proportionate to the label and continue approved work. Do not disguise necessary safety/correctness blockers as optional items. On explicit approval or a user move to `TO DO`, synchronize status and remove all `idea`, `suggestion`, and `proposal` labels; discussion alone is not approval.

## Issue-first and live queue

Every development change needs an issue with outcome and acceptance criteria. Read its current body, all comments including edits, dependencies, and ownership when claiming/resuming, changing stages, and before integration. Keep one primary active task per agent; record ownership and set `IN PROGRESS` before editing. Put corrections on the current issue; capture separate user requests as `TO DO` and finish the current task unless reprioritized. Unapproved discoveries belong in `BACKLOG`.

During authorized implementation/queue work:

1. Fetch current Issues and Project statuses at session start/resumption, after each completed or paused issue, and before selecting work. Read all result pages; a remembered starting list is not the queue.
2. Follow user priority, then eligible owned work (including `IN REVIEW` checks and ready resumptions), then available `TO DO`. Recheck ownership/status before claiming. Reconcile clear status/label drift from the latest user action; do not guess approval from ambiguous mismatches.
3. Complete or properly pause the task, then fetch again. Include new tasks added during the session; do not ask to continue already approved work.
4. Before stopping for lack of work, fetch again and confirm no actionable `TO DO` or eligible owned work remains. Pending `IN REVIEW` work needs a run/status handoff and an active session or verified runner for follow-up; never abandon it as done. Distinguish pending/paused/other-agent work from an empty queue. Failed reads do not prove emptiness.

Honor an explicit stop, review-only scope, or execution limit. Preserve a handoff if unable to continue. Later work requires an active session or separately configured wakeup; these instructions do not install automation.

## Isolation, branches, and delivery

Use `issue branch → develop → main` in every lifecycle phase. `develop` integrates finished work; `main` holds the preserved baseline, then authorized private-beta and public production releases. Do not update `main` or production without explicit release authorization; passing tests or changing phase is insufficient. Keep branches short-lived and never implement directly on shared branches. Beta releases and public opening follow [launch.md](launch.md).

Default to verified direct integration from the owned issue worktree, without a pull request (PR) or separate reviewer. Use a PR only when the owner requests one or existing repository rules require it. Do not introduce mandatory PRs or human review gates during setup; preserve existing protections. Dependabot update PRs follow [updates.md](updates.md).

Inspect status and worktrees, fetch, and create an issue branch/worktree from `origin/develop`:

```sh
git fetch origin
git worktree add ../worktrees/issue-<number> -b issue-<number> origin/develop
```

An existing isolated checkout/sandbox dedicated to this issue on its own branch satisfies the requirement; do not create redundant worktrees. Record the branch and location, verify ownership, and do all edits/tests/commits there. Never overwrite, stash, reset, or delete another agent's work. Dependabot's isolated PR branches are covered by [updates.md](updates.md); agent repairs still require owned isolation.

Before parallel work, record task boundaries, dependencies, and ownership in the issues. Coordinate overlapping changes; give shared schemas/migrations, interfaces, dependency manifests, and lockfiles one owner at a time. Other agents continue independent work; record handoffs before another agent edits the shared area.

Record and verify each active worktree's ports and test-resource identifiers. Isolate conflicting databases, storage, and services. With Docker, use a unique Compose project name and verify that explicit names, external volumes, bind mounts, and external services do not reconnect agents to shared mutable resources. If isolation is unavailable, serialize conflicting operations. Keep any setup scripts specific to the owning project.

Make small, coherent commits throughout the issue at working checkpoints: one focused behavior, fix, or preparatory refactor, with its relevant tests and docs. Run checks appropriate to each step and reference the issue in each commit. Avoid unrelated cleanup or accumulating an entire large feature into one commit; keep inseparable changes together, without arbitrary line-count or time quotas. Checkpoint commits stay in the owned issue checkout until the completed candidate passes delivery checks; committing does not authorize integration or deployment.

Before completing:

1. Refresh the body and every comment, including edits. Reconcile each request, correction, and question with the latest user decisions. Implement/verify required work and answer questions; deferring required work needs explicit user instruction and a linked follow-up. Never silently omit or split required work merely to close the issue.
2. Verify acceptance criteria and changed behavior with relevant tests, build/lint/type checks; report skipped or failed checks honestly. Update affected docs under [documentation.md](documentation.md), or explain why none are needed.
3. Review staged scope/secrets, commit any remaining changes with the issue reference, fetch current `develop`, and combine it with the issue branch in the owned checkout. Resolve conflicts and verify required checks pass on that exact candidate.
4. Push the tested candidate directly to `develop` with a normal fast-forward push, or use the requested/required PR path. If `develop` advances or the push is rejected, refresh and revalidate before retrying. Never force-push shared history, bypass protections, or integrate an untested replacement. Confirm remote integration, required delivery checks, and current documentation.
5. Post a brief result comment **on the issue**, covering changes, request/question outcomes, verification, docs, delivery, and commit links (PR links when used). Group related outcomes and link relevant comments; chat updates alone do not count. Read back the saved comment; a failed or unverified write blocks closure.
6. Refresh the body and all comments after posting the result. Resolve unaddressed new/edited input, repeat affected checks, update the result, and refresh again. Then set Project status and the only label to `DONE`, and close as completed. Immediately verify state/labels/Project and reread body/comments; missed unresolved input requires reopening with the appropriate status, review stage, or pause and continuing work. Automatic closing keywords/actions must not bypass these checks.

After verified closure, remove only your own clean merged worktree/branch and prune; preserve pending/paused work. Completion does not authorize a production release.
