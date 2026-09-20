# Project Blueprint

Reusable instructions for new and existing projects. You decide what to build and when to release; agents handle the authorized technical work.

## How you operate

| Situation | Your action |
| --- | --- |
| Start or adopt a project | Give the agent the setup prompt below and repository access. |
| Request implementation | Tell the agent or move an issue to `TO DO`. It refreshes the live queue, including tasks added during work. |
| Save an idea | Use `BACKLOG` + `suggestion`; approve it or move it to `TO DO` when ready. |
| `paused: decision` | Answer the recommended A or another option, or give your own answer. |
| `paused: setup` | Complete the linked user-only steps and report the result. |
| `paused: external` | Read the provider/dependency status; usually no action is needed. |
| Clear several pending answers | Request an issue interview with the prompt below. |
| Release | Instruct the agent which release to perform. Passing tests alone does not authorize production. |
| Update these standards | Request a blueprint change, then have existing projects adopt that revision. |

Paused issues stay `IN PROGRESS` with one pause reason. Comment when a blocker is resolved; the agent verifies it before resuming. During interviews, it immediately records each answer and leaves resolved issues labeled only `IN PROGRESS`, visibly ready to resume. Unresolved blockers keep their pause reason. Finished issues close with only purple `COMPLETED`.

Questions and reviews do not start unrelated implementation. The 90% confidence guideline is judgment, not a measured probability. Agents handle routine tested dependency updates without version-by-version decisions; unattended work requires a real runner.

## Setup prompt

> Set up this project using `<blueprint-source>`. Follow its README adoption steps. If an application already exists, use adopt-existing first and preserve its stack, data, working features, and live behavior. Merge instructions and configure only compatible, authorized automation.

Supply the blueprint URL or checkout in place of `<blueprint-source>`. `OWNER/REPO` below means the target repository. The adopting agent should:

1. Fetch this blueprint into a separate checkout and record its commit. Read [git-workflow.md](template/git-workflow.md) and, for an existing application, [adopt-existing](skills/adopt-existing/SKILL.md). Inspect before editing the target.
2. Create/claim a setup issue and follow the bootstrap order in [git-workflow.md](template/git-workflow.md).
3. Preview labels from the blueprint checkout: `pwsh -File scripts/setup-labels.ps1 -Repo OWNER/REPO -WhatIf` or `bash scripts/setup-labels.sh OWNER/REPO --dry-run` (requires `jq`); omit the preview flag to apply. Create/link the Project and configure its four statuses, preserving existing mappings under `adopt-existing`. Helpers only create/update label definitions; they do not migrate issue labels, configure Project fields, or delete old labels. Set the setup issue/Project to `IN PROGRESS` and add issue stage `implementation`.
4. Establish the integration baseline and an owned isolated setup branch/worktree before edits or skill installation. For an empty repository, create a minimal baseline within the setup issue, without application implementation or deployment. An existing dedicated isolated checkout suffices.
5. Merge [template/](template/) into the target root inside that checkout, preserving project rules and Git history. Procedures in `skills/` remain separate.
6. Make applicable [skills](skills/README.md) available through supported installation, or retain the blueprint checkout and record verified skill paths. Keep repository-local installations in the setup checkout. Fill facts/commands and complete `project.md`.
7. Verify links, applicable checks, documentation access, discovery, and automation/runner behavior. Record actual source/revision, skill locations, local exceptions, and remaining setup with direct links; copying instructions does not activate automation.

Existing applications retain their framework, custom code, and data; WordPress retains its themes/plugins and established Bootstrap/Tabler. The adoption skill covers label migration and transitioning current work to `develop` without losing history or unfinished work. Application upgrades and production-affecting changes are separate tasks.

## Interview prompt

> Interview me about paused or in-progress issues needing my input. Ask one brief question at a time with an issue link, A as your recommendation, useful B/C alternatives, D to answer later, and E to answer in the issue. Accept my own answer too. Immediately comment each answer on its issue. When resolved, leave only IN PROGRESS, verify the Project status, and confirm before the next question. Keep unresolved items paused. Finish with a brief linked recap; keep the session focused on the interview.

The [interview skill](skills/issue-interview/SKILL.md) defines the procedure, including verified setup, deferrals, and immediate updates.

## Customer terms and privacy

Use [legal.md](template/legal.md) and [legal-review](skills/legal-review/SKILL.md) for policies based on the project's actual jurisdictions and practices. Agents draft brief, accurate text without unsupported promises. The owner, defined in project `AGENTS.md`, or an explicitly authorized legal/business delegate approves initial policies and material changes. Approval may accompany a release that identifies the policy version. Non-substantive corrections need no repeat approval; qualified review follows `legal.md`.

> Review this project's customer terms and privacy needs using legal-review. Inspect the application and existing policies first, keep wording brief and factual, and ask only for missing material decisions. Prepare applicable drafts in docs/public/legal and report any unresolved questions.

Review before collecting real personal information, even for a waitlist or beta. The agent keeps policies aligned with later features; publishing follows your release authorization. A paid generator or outside skill is not required.

## Environments and costs

Use `develop.<domain>` from `develop` for development/release testing and the main domain from `main` for authorized production releases. Before launch, preserve `main` as a snapshot. Staging at `staging.<domain>` is optional and must be explicitly requested by you or an authorized human developer; preserve existing environments during adoption.

Use generic placeholders here. Record actual application domains, provider configuration, and deployment details only in the adopting project's appropriate documentation.

The blueprint supports GitHub Free for public and private repositories. Private technical docs are ordinary Markdown, with no wiki publishing. Agents use verified integration when native branch protection/auto-merge is unavailable; this is not server-enforced protection. Remain within included usage and existing authorized resources. Missing Project permissions require access setup, not necessarily a paid plan.

## File map

| Location | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Maintaining this blueprint repository |
| [template/AGENTS.md](template/AGENTS.md) | Project facts, commands, core rules, conditional reading map |
| [template/project.md](template/project.md) | Initial setup and environment defaults |
| [template/git-workflow.md](template/git-workflow.md) | Issues, labels, live queue, isolation, integration, release rules |
| [template/design.md](template/design.md) | Stack-compatible UI preferences |
| [template/security.md](template/security.md) | Credentials, data, access, and reporting |
| [template/legal.md](template/legal.md) | Project-specific jurisdictions, policy commitments, and review rules |
| [template/documentation.md](template/documentation.md) | Private internal, public, optional admin docs, and changelogs |
| [template/packages.md](template/packages.md) / [template/updates.md](template/updates.md) | Package choice and verified maintenance |
| [template/launch.md](template/launch.md) | Release preparation and verification |
| [skills/](skills/) | On-demand adoption, interview, and legal-review procedures |
| [PowerShell](scripts/setup-labels.ps1) / [Bash](scripts/setup-labels.sh) / [labels](scripts/labels.json) | Label setup and canonical colors |

`agent.md` points to `AGENTS.md`; `CLAUDE.md` imports it using `@AGENTS.md`. Verify the target tool's discovery during setup. Detailed guides and skills are read only when relevant.

## Maintaining this repository

Start from the repository root and follow its `AGENTS.md`. `template/AGENTS.md` belongs to the adopting application; treat it as payload while maintaining this blueprint. Verify active guidance because tools can also discover nested instruction files. Keep blueprint-maintenance notes outside `template/`.

This repository uses only `main`, with owned isolated checkouts or detached worktrees and issue tracking under root `AGENTS.md`. Verify links, skills, and affected helpers before committing and pushing. Application development/release branches are specified by the payload. This repository has no application runtime or dependency repair runner; configure and verify automation in each adopting project.
