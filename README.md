# Project Blueprint

Reusable instructions for new and existing projects. You decide what to build and when to release; agents handle the authorized technical work.

This blueprint evolves without a changelog; agents check at implementation-session start and queue updates under [AGENTS.md](template/AGENTS.md), keeping current guidance until approved adoption.

![Application workflow: planning, build, security, release, launch, and ongoing production. Gray BACKLOG, blue TO DO, yellow IN PROGRESS, lavender REVIEW with testing/delivery, and green COMPLETED after comment checks and posted results. Owned worktrees, pink decision/red setup/silver external pauses, and live queue refresh. Security checks and authorization precede beta and public launch.](assets/project-workflow-landscape.jpg)

Application workflow overview. [Open the full-size landscape JPEG](assets/project-workflow-landscape.jpg) (11 × 8.5 inches).

## How you operate

| Situation | Your action |
| --- | --- |
| Start or adopt a project | Give the agent the setup prompt below and repository access. |
| Request implementation | Tell the agent or move an issue to `TO DO`. It refreshes the live queue, including tasks added during work. |
| Save an idea or recommendation | Use `BACKLOG` plus one: `idea` (early thought), `suggestion` (recommended improvement), or `proposal` (developed recommendation needing a decision). Approval moves it to `TO DO` and removes the descriptor. |
| `paused: decision` | Answer the recommended A or another option, or give your own answer. |
| `paused: setup` | Complete the linked user-only steps and report the result. |
| `paused: external` | Read the provider/dependency status; usually no action is needed. |
| Clear several pending answers | Request an issue interview with the prompt below. |
| Prepare an offer | Request pricing research with the prompt below; choose a recommendation or give your own terms. |
| Change phase | Say “move to security” or name the next phase; the agent records your decision under [phases.md](template/phases.md). |
| Release | Instruct the agent which release to perform. Passing tests alone does not authorize production. |
| Update these standards | Request a blueprint change; existing projects follow the update guidance in their `AGENTS.md`. |

The board and matching issue labels follow `BACKLOG → TO DO → IN PROGRESS → REVIEW → COMPLETED`. `REVIEW` shows finished implementation undergoing tests, automated checks, or final delivery verification; it does not require your review of every issue. Fixes return to `IN PROGRESS`.

Paused issues stay `IN PROGRESS` with one pause reason. Comment when a blocker is resolved; the agent verifies it before resuming. During interviews, it immediately records each answer and leaves resolved issues labeled only `IN PROGRESS`, visibly ready to resume. When work resumes, testing/delivery returns to `REVIEW`. Unresolved blockers keep their pause reason.

Before closing, the agent resolves every comment, posts results, and checks for missed input under the [completion checks](template/git-workflow.md#isolation-branches-and-delivery).

Routine work uses [verified direct integration](template/git-workflow.md#isolation-branches-and-delivery), respecting existing protections without adding mandatory pull requests or extra reviewers.

Questions and reviews do not start unrelated implementation. The 90% confidence guideline is judgment, not a measured probability.

## Project phases

| Parent | Subphases |
| --- | --- |
| **DEVELOPMENT** | planning → build → security |
| **RELEASE** | offering → beta → validation |
| **LAUNCH** | open → feedback → stabilize |
| **PRODUCTION** | None; final ongoing marketing, growth, maintenance, and feature releases |

[phases.md](template/phases.md) defines work and completion criteria. Direct transitions naturally, such as “move to security”; agents recommend advancement without repeated prompts. Changing phase does not authorize deployment or public opening. New features do not reset the product.

`planning` includes specifications, security requirements, and setup. Security applies throughout development, with a review before beta and rechecks during `validation`. [security.md](template/security.md#security-review) governs review scope, evidence, release requirements, and owner risk acceptance; findings stay private.

Owner/developer admin views separate **Environment** from **Project phase**: an invited production beta shows `PRODUCTION` and `RELEASE: beta`. Final `PRODUCTION` has no subphase. Customer-admin views need no lifecycle display; phases are not GitHub labels or Project fields.

## Project setup

Use the setup prompt in [Prompts](#prompts).

Supply the blueprint URL or checkout in place of `<blueprint-source>`. `OWNER/REPO` below means the target repository. The adopting agent should:

1. Fetch this blueprint into a separate checkout and record its commit. Read [git-workflow.md](template/git-workflow.md) and, for an existing application, [adopt-existing](skills/adopt-existing/SKILL.md). Inspect before editing the target.
2. Create/claim a setup issue and follow the bootstrap order in [git-workflow.md](template/git-workflow.md).
3. Preview labels from the blueprint checkout: `pwsh -File scripts/setup-labels.ps1 -Repo OWNER/REPO -WhatIf` or `bash scripts/setup-labels.sh OWNER/REPO --dry-run` (requires `jq`); omit the preview flag to apply. Create/link the Project and configure its five statuses and colors, preserving mappings under `adopt-existing`. Helpers only create/update label definitions; they do not migrate issue labels, configure Project fields, or delete old labels. Set the setup issue/Project to `IN PROGRESS` without a stage.
4. Establish the integration baseline and an owned isolated setup branch/worktree before edits or skill installation. For an empty repository, create a minimal baseline within the setup issue, without application implementation or deployment. An existing dedicated isolated checkout suffices.
5. Merge [template/](template/) into the target root inside that checkout, preserving project rules and Git history. Procedures in `skills/` remain separate.
6. Make applicable [skills](skills/README.md) available through supported installation, or retain the blueprint checkout and record verified skill paths. Keep repository-local installations in the setup checkout. Fill facts/commands and complete `project.md`.
7. Verify links, applicable checks, documentation access, discovery, and automation/runner behavior. Record actual source/revision, skill locations, local exceptions, and remaining setup with direct links; copying instructions does not activate automation.

Existing applications retain their framework, custom code, and data; WordPress retains its themes/plugins and established Bootstrap/Tabler. The adoption skill covers label migration and transitioning current work to `develop` without losing history or unfinished work. Application upgrades and production-affecting changes are separate tasks.

## Interface design

For UI work, agents follow [design.md](template/design.md) and the [interface-design skill](skills/interface-design/SKILL.md): compact headers, responsive field groups, consistent alignment, useful muted icons, and clear save/submit feedback. Favor icons alongside labels in admin menus, features, and checkout. Existing frameworks and native interactions remain in place. Agents verify the rendered result as well as form behavior.

Use the interface prompt in [Prompts](#prompts).

## Issue interviews

Use the interview prompt in [Prompts](#prompts).

The [interview skill](skills/issue-interview/SKILL.md) defines the procedure, including verified setup, deferrals, and immediate updates.

## Customer terms and privacy

Use [legal.md](template/legal.md) and [legal-review](skills/legal-review/SKILL.md) for policies based on the project's actual jurisdictions and practices. Agents draft brief, accurate text without unsupported promises. The owner, defined in project `AGENTS.md`, or an explicitly authorized legal/business delegate approves initial policies and material changes. Approval may accompany a release that identifies the policy version. Non-substantive corrections need no repeat approval; qualified review follows `legal.md`.

Use the legal prompt in [Prompts](#prompts).

Review before collecting real personal information, even for a waitlist or beta. The agent keeps policies aligned with later features; publishing follows your release authorization. A paid generator or outside skill is not required.

## Marketing and pricing

[offering.md](template/offering.md) keeps marketing and commercial decisions consistent before and after launch. The [pricing-research skill](skills/pricing-research/SKILL.md) compares products, costs, value, and refund terms, then recommends alternatives. You approve initial prices and material changes; agents keep pages, checkout, billing, and docs aligned. Policies follow the legal rules; publication follows release authorization.

Use the pricing prompt in [Prompts](#prompts). Research and business decisions stay in private project docs; approved customer policies belong in `docs/public/legal/`.

When marketing begins, the agent offers relevant Corey Haines skills linked in `offering.md`. Installation is optional, requires approval and review, and never happens during setup. The agent records your choice without repeated prompts; deferral does not block work.

## Environments and costs

Use `develop.<domain>` from `develop` for development/testing and the main domain from `main` for authorized production releases. During `RELEASE: beta`, an explicitly authorized private beta can run there with invitation-only access; public opening requires launch authorization under [launch.md](template/launch.md). Staging at `staging.<domain>` is optional and must be explicitly requested by you or an authorized human developer; preserve existing environments during adoption.

Use generic placeholders here. Record actual application domains, provider configuration, and deployment details only in the adopting project's appropriate documentation.

The blueprint supports GitHub Free for public and private repositories. Private technical docs are ordinary Markdown, with no wiki publishing. Agents use verified integration when native branch protection/auto-merge is unavailable; this is not server-enforced protection. Remain within included usage and existing authorized resources. Missing Project permissions require access setup, not necessarily a paid plan.

## File map

| Location | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Maintaining this blueprint repository |
| [template/AGENTS.md](template/AGENTS.md) | Project facts, commands, core rules, conditional reading map |
| [template/phases.md](template/phases.md) | Lifecycle focus, subphases, completion criteria, and user-directed transitions |
| [template/project.md](template/project.md) | Initial setup and environment defaults |
| [template/git-workflow.md](template/git-workflow.md) | Issues, labels, live queue, isolation, integration, release rules |
| [template/design.md](template/design.md) | Stack-compatible layouts, form actions, feedback, and credential fields |
| [template/offering.md](template/offering.md) | Accurate marketing, researched commercial decisions, and consistent customer information |
| [template/security.md](template/security.md) | Credentials, data, access, security review, release checks, and reporting |
| [template/legal.md](template/legal.md) | Project-specific jurisdictions, policy commitments, and review rules |
| [template/documentation.md](template/documentation.md) | Private internal, public, optional admin docs, and changelogs |
| [template/packages.md](template/packages.md) / [template/updates.md](template/updates.md) | Package choice and verified maintenance |
| [template/launch.md](template/launch.md) | Private beta, public opening, and release verification |
| [skills/](skills/) | Task-specific adoption, interview, interface-design, pricing-research, and legal-review procedures |
| [PowerShell](scripts/setup-labels.ps1) / [Bash](scripts/setup-labels.sh) / [labels](scripts/labels.json) | Label setup and canonical colors |

`agent.md` points to `AGENTS.md`; `CLAUDE.md` imports it using `@AGENTS.md`. Verify the target tool's discovery during setup. Detailed guides and skills are read only when relevant.

Start from the repository root and follow its `AGENTS.md`. `template/AGENTS.md` belongs to the adopting application; treat it as payload while maintaining this blueprint. Verify active guidance because tools can also discover nested instruction files. Keep blueprint-maintenance notes outside `template/`.

This repository uses only `main`, with owned isolated checkouts or detached worktrees and issue tracking under root `AGENTS.md`. Verify links, skills, and affected helpers before committing and pushing. Application development/release branches are specified by the payload. This repository has no application runtime or dependency repair runner; configure and verify automation in each adopting project.

## Prompts

**Setup**

> Set up this project using `<blueprint-source>`. Follow its README adoption steps. If an application already exists, use adopt-existing first and preserve its stack, data, working features, and live behavior. Merge instructions and configure only compatible, authorized automation.

**Interface design**

> Build or refine this screen using our design standards and interface-design skill. Reuse the established components, keep related fields compact, and verify button readiness, processing, success, and failure at desktop and mobile widths.

**Issue interview**

> Interview me about paused or in-progress issues needing my input. Ask one brief question at a time with an issue link, A as your recommendation, useful B/C alternatives, D to answer later, and E to answer in the issue. Accept my own answer too. Immediately comment each answer on its issue. When resolved, leave only IN PROGRESS, verify the Project status, and confirm before the next question. Keep unresolved items paused. Finish with a brief linked recap; keep the session focused on the interview.

**Legal review**

> Review this project's customer terms and privacy needs using legal-review. Inspect the application and existing policies first, keep wording brief and factual, and ask only for missing material decisions. Prepare applicable drafts in docs/public/legal and report any unresolved questions.

**Pricing research**

> Research comparable products' prices, packages, and refund terms using pricing-research. Give me a brief linked comparison, your recommended pricing and refund approach, and useful alternatives. Account for our costs and customer value. Reuse existing decisions, ask only what is missing, and identify inconsistencies in our landing page, checkout, billing, and docs.
