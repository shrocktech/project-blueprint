---
name: issue-interview
description: Walk the user through pending issue decisions or setup one question at a time, immediately recording answers and synchronizing pause labels. Use when the user requests an interview or guided review of blocked work.
---

# Issue Interview

Confirm the target repository and use its `git-workflow.md` for statuses and brief notes; this filename is relative to the project, not the installed skill. Use only for a requested walkthrough of pending answers. The interview updates issue records without starting implementation or authorizing releases.

## Prepare and ask

1. Fetch the live Issues, Project statuses, and relevant comments across all pages. Identify started issues that actually need user input, including blockers discovered in `IN REVIEW`; honor any requested scope or priority. Start with decisions that unblock other work, then actionable setup. Do not ask the user to solve a provider-only wait, an ordinary pending check, or a choice already answered. Review optional backlog proposals only when requested.
2. Give a brief count of items needing input, then ask **one short question at a time**. Include the issue number/title as a direct link, one sentence of context, and the smallest decision needed. If one issue has several decisions, handle them separately. Wait for the user's answer before asking the next question.
3. Offer **A — Recommended**, with a short reason, and useful **B/C** alternatives with brief tradeoffs. Do not invent alternatives merely to fill slots. Always include **D — Answer later; next question** and **E — I'll answer in the issue; next question**, with the exact issue link. Accept a custom answer, a request for explanation, or a stop at any time. A recommendation is never a default approval.
4. For setup, recommend the smallest action with verified direct links and exact steps. Do authorized API/tool work yourself first. Choosing to perform setup is not proof it was completed; verify the result before treating the blocker as resolved.

## Save each answer before the next question

Do this immediately after every answer, before asking the next question. Never collect a batch of answers for a final issue-update pass. The interview authorizes these answer comments and matching status/label updates; do not ask the user to repeat the answer in GitHub or remove the label manually.

1. Re-read the issue's latest comments, labels, and Project status so concurrent work is preserved. Post a brief comment recording the answer's meaning, scope, and resulting next step, not just the option letter. Exclude secrets or private information from public issues. If the answer was already posted directly in the issue, use that comment instead of duplicating it.
2. For started work whose blockers are verified resolved, immediately replace all issue labels with exactly `IN PROGRESS`. Keep it open with Project status `IN PROGRESS`; preserve ownership and record any removed stage/type history in the comment. This includes removing `paused: external` when the external blocker is resolved. Restore stage/type and matching status only when work resumes under `git-workflow.md`, including `IN REVIEW` for testing/delivery. Answering a question does not complete the issue.
3. If another decision, unfinished setup, or external dependency still blocks work, retain or switch to the appropriate pause reason and state the remaining blocker. For D/E, record the deferral, leave the pause intact, and skip it for the rest of this interview. An intention to answer in the issue or perform setup is not completion. Unapproved proposals remain `BACKLOG`.
4. Read back the saved comment, labels, and Project status. Then give a short linked confirmation such as "Recorded on #123; pause removed, ready to resume" or "Recorded on #123; still waiting for provider setup." Only then ask the next question. Do not imply that implementation has already restarted. If a write or verification fails, recover and retry without duplicating comments; report an unresolved failure and retain the pending answer rather than claiming synchronization or silently postponing it to the end.

## Continue and finish

- Respect other agents' active work. A product preference does not approve unrelated implementation, spending, or a release. Apply explicit backlog approval through the normal `TO DO` workflow; discussion alone leaves it in `BACKLOG`.
- Refresh relevant issues between answers and before finishing, including new user answers or blockers. Skip already resolved questions and track deferred items so they do not loop back. End with a short linked list of ready-to-resume, deferred, and still-blocked items. Do not promise that an idle agent will wake automatically.
