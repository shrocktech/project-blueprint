# Git and Issue Workflow

Apply during development and queue work, not merely because the user asks a question or requests a review. Follow [AGENTS.md](AGENTS.md).

## Status and labels

Verify repository, Issues, and Project access before development; create/link the Project if missing. During bootstrap, create/claim the setup issue, then establish needed label/status definitions before assigning them; preserve existing mappings. Keep the four Project statuses synchronized with exactly one uppercase workflow label:

| Status / label | Meaning |
| --- | --- |
| `BACKLOG` | Future/unapproved work; do not implement. |
| `TO DO` | Approved work expected to be done. |
| `IN PROGRESS` | Started, including paused work. |
| `COMPLETED` | Closed as completed, verified and delivered. Purple (`A371F7`); purple Project status. |

Project authorization is separate from repository authorization; inspect token scopes and account/organization permissions before attributing a failure to the plan. Synchronize through available tools during active work; background synchronization is optional. Report genuine missing access with exact setup steps, not a plan-upgrade request.

Active work has one lowercase stage: `implementation`, `testing`, or `deployment`. Deployment means final integration and delivery verification in the intended environment; ordinary work targets development, with staging only if already authorized and active. Production requires release authorization. Follow the environment defaults in [project.md](project.md). Documentation-only work needs verified remote integration, not a runtime deployment.

Apply `implementation` when claiming new work, replace it with `testing` when verification begins, then with `deployment` before integration/delivery. Replace the previous stage rather than accumulating stages. If verification finds a fix, return to `implementation` and then `testing`; paused work uses the removal/restoration rules below.

Use `bug`, `feature`, and `enhancement` while useful; optional proposals use `BACKLOG` plus `suggestion`. At completion remove every label except `COMPLETED`. Never mark canceled or unfinished issues completed.

## Paused work

Keep the issue open in the `IN PROGRESS` column with exactly `IN PROGRESS` and one reason label; remove its stage/type labels:

| Label | Who must act |
| --- | --- |
| `paused: decision` | User must answer, choose, or supply missing information. |
| `paused: setup` | User must perform an action the agent cannot complete, such as verification or account setup. |
| `paused: external` | Provider, external service, or dependency must change; no user action unless stated. |

Try available APIs/tools and the authorized autonomous actions first. Before removing labels, record the paused stage and existing type labels (`bug`, `feature`, `enhancement`) in the issue comment; preserve the worktree. Continue independent work; if none remains, leave a handoff and take other approved work. Avoid repeated unchanged retries or nudges. When multiple blockers exist, label the immediate next dependency and list the others briefly; change the reason as work advances.

After an answer or completed setup resolves all blockers, keep the issue open with only `IN PROGRESS` and matching Project status: this means ready to resume. Preserve removed stage/type history in comments. An answer alone does not resolve an external dependency; verify it and retain the appropriate pause reason while blocked. At task boundaries, read new comments and resume eligible owned work before new `TO DO` unless reprioritized. Restore stage/type labels only when implementation resumes, honoring later user changes and ownership. Recheck external waits at task boundaries or through configured monitoring; label changes do not wake idle agents.

Quote pause labels exactly in commands and searches: `gh issue list --label 'paused: decision'` or `label:"paused: decision"`.

## Brief notes and proposals

For a requested guided review, use `issue-interview` at its recorded location: one question at a time with a recommendation and defer/answer-in-issue choices. Immediately comment each answer, apply the paused/ready rules above, and verify labels/Project status before the next question. Never batch updates or start implementation queue work during the interview.

Keep notes to the problem, what was tried/submitted, and the smallest next action. Use verified direct setup/settings/request links; otherwise give the official entry page and exact navigation. Never put secrets or token-bearing URLs in notes.

For decisions or optional proposals, ask one brief question: **A — Recommended** with a short reason, then useful **B/C** alternatives and tradeoffs. Allow the user's own answer; during interviews always include the D/E choices in the interview skill. For setup, provide short numbered steps, exact controls, expected result, and what to report back. For submitted requests, give the reference/status and say when no user action is needed. Do not promise monitoring without an actual runner.

Proactively record worthwhile optional improvements as separate `BACKLOG` + `suggestion` issues, checking for duplicates and linking the originating issue and evidence. Explain benefit, recommendation, and main cost briefly; keep working on approved scope. Do not disguise necessary safety/correctness blockers as optional suggestions. On explicit approval or a user move to `TO DO`, synchronize status and remove `suggestion`; discussion alone is not approval.

## Issue-first and live queue

Every development change, including small fixes, needs an issue with outcome and acceptance criteria. Read current comments, dependencies, and ownership before claiming it. Keep one primary active task per agent; record ownership and set `IN PROGRESS` + `implementation` before editing. Put corrections on the current issue; capture separate user requests as `TO DO` and finish the current task unless reprioritized. Unapproved discoveries belong in `BACKLOG`.

During authorized implementation/queue work:

1. Fetch current Issues and Project statuses at session start/resumption, after each completed or paused issue, and before selecting work. Read all result pages; a remembered starting list is not the queue.
2. Follow user priority, then eligible resumable owned work, then available `TO DO`. Recheck ownership/status before claiming. Reconcile clear status/label drift from the latest user action; do not guess approval from ambiguous mismatches.
3. Complete or properly pause the task, then fetch again. Include new tasks added during the session; do not ask to continue already approved work.
4. Before stopping for lack of work, fetch again and confirm no actionable `TO DO` or eligible resumable work remains. Distinguish paused/other-agent work from an empty queue. Failed reads do not prove emptiness.

Honor an explicit stop, review-only scope, or execution limit. Preserve a handoff if unable to continue. Later work requires an active session or separately configured wakeup; these instructions do not install automation.

## Isolation, branches, and delivery

Use `issue branch → develop → main` in every lifecycle phase. `develop` integrates finished work; `main` holds the preserved baseline, then authorized private-beta and public production releases. Do not update `main` or production without explicit release authorization; passing tests or changing phase is insufficient. Keep branches short-lived and never implement directly on shared branches. Beta releases and public opening follow [launch.md](launch.md).

Default to verified direct integration from the owned issue worktree, without a pull request (PR) or separate reviewer. Use a PR only when the owner requests one or existing repository rules require it. Do not introduce mandatory PRs or human review gates during setup; preserve existing protections. Dependabot update PRs follow [updates.md](updates.md).

Inspect status and worktrees, fetch, and create an issue branch/worktree from `origin/develop`:

```sh
git fetch origin
git worktree add ../worktrees/issue-<number> -b issue-<number> origin/develop
```

An existing isolated checkout/sandbox dedicated to this issue on its own branch satisfies the requirement; do not create redundant worktrees. Record the branch and location, verify ownership, and do all edits/tests/commits there. Never overwrite, stash, reset, or delete another agent's work. Isolate conflicting ports, databases, and services too. Dependabot's isolated PR branches are covered by [updates.md](updates.md); agent repairs still require owned isolation.

Before completing:

1. Verify acceptance criteria and changed behavior with relevant tests, build/lint/type checks; report skipped or failed checks honestly. Update affected docs under [documentation.md](documentation.md), or explain why none are needed.
2. Review staged scope/secrets, commit with the issue reference, fetch current `develop`, and combine it with the issue branch in the owned checkout. Resolve conflicts and verify required checks pass on that exact candidate.
3. Push the tested candidate directly to `develop` with a normal fast-forward push, or use the requested/required PR path. If `develop` advances or the push is rejected, refresh and revalidate before retrying. Never force-push shared history, bypass protections, or integrate an untested replacement.
4. Confirm remote integration, required delivery checks, and current internal documentation. Remove only your own clean completed worktree and merged branch, then prune; preserve paused work.
5. Add a brief result note with verification, docs, delivery, and commit links (PR links when used). Set Project status `COMPLETED`, replace all labels with only `COMPLETED`, and close with the completed reason. Verify all three agree. This does not imply a production release.
