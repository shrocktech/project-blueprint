# Agent Instructions

Follow the user's latest instructions. Fill project facts and commands during setup; read detailed guides only for the current task.

At implementation-session start, check [weekly Blueprint maintenance](updates.md#periodic-blueprint-maintenance) and, from `DEVELOPMENT: security`, [advisory monitor health](updates.md#advisory-monitoring-and-health). Run due checks and triage findings.

## Project facts

- Purpose, users, stack, runtime, package manager, directories: to be filled in.
- Lifecycle: stop TODO/10; phase TODO; subphase TODO (`none` for `PRODUCTION`); active plan TODO. Use [phases.md](phases.md) for current focus and transitions.
- Owner: the human authorized to bind the project/business; record their role and delegates. Policy approval requires explicit legal/business delegation; development or release access alone does not confer it.
- Business and customer/service jurisdictions: record verified scope in private project docs; no assumed country.
- Conventions: link existing formatter/linter configuration and patterns.
- Brand: canonical kit and implementation tokens TODO; approval/provisional scope TODO; protected Brand Guidelines settings route and editor roles TODO. Follow [design.md](design.md#brand-foundation-and-settings).
- Hosting constraint: GitHub Free for public/private repositories; no required upgrade, paid features, billed usage, or visibility change.
- Private documentation index, dependency rationale, automation status: record verified locations.
- Workspace: repository layout under [project.md](project.md#project-workspace); record canonical documentation/assets/skills/agents paths, supported installed discovery locations, external private storage and migration issue/status. Existing projects follow [workspace migration](documentation.md#workspace-migration) during adoption/updates.
- Recovery: private inventory/runbook, backup destinations and health, independent key/access recovery, restore objectives/cadence and last verified drill or blockers TODO under [security.md](security.md#local-development-secrets).
- Vulnerability intelligence: link the private inventory and [monitor health record](updates.md#advisory-monitoring-and-health), verified command/job, schedule, last successful check and coverage gaps; unconfigured until verified.
- Standing preferences: private location or `none`.
- Blueprint source: TODO; recorded default branch and adopted commit: TODO; local exceptions: TODO; last successful check/reviewed revision: TODO; maintenance issue/schedule and pending changes: TODO.
- Skill locations: record verified paths for applicable `adopt-existing`, `issue-interview`, `interface-design`, `pricing-research`, `legal-review`, and `changelog` skills during setup. A source folder alone does not install skills.
- Task Observer: TODO — enabled, declined, or deferred; if enabled, record pinned source/revision, skill location, private stable observation path, and activation verification under [Task Observer setup](optional-tools.md#task-observer).
- Encrypted `.env`: standard setup; protected key path, authorized hosts and verified encryption/unlock/plaintext-blocking checks TODO under [security.md](security.md#encrypted-env-with-git-crypt). Record any owner-approved local-only exception; plaintext `.env` must never be committed or pushed.

## Verified commands

| Operation | Directory | Command / status |
| --- | --- | --- |
| Install | TODO | TODO — unverified |
| Run locally | TODO | TODO — unverified |
| Build | TODO | TODO — unverified |
| Test | TODO | TODO — unverified |
| Lint / types | TODO | TODO — unverified |
| Format check | TODO | TODO — unverified |

Use actual scripts/CI. Run applicable commands before marking them verified; identify inapplicable or blocked checks. Never include secret values.

## Always apply

- Record skipped, blocked or unverified checks, their impact and the next action. Claim only coverage supported by evidence.
- Load enabled Task Observer for substantial tasks, resumptions and related feedback or reviews under its [activation rules](optional-tools.md#task-observer).
- Claim an issue and use an owned checkout. Follow [delivery and closure](git-workflow.md#isolation-branches-and-delivery), [live queue refresh](git-workflow.md#issue-first-and-live-queue) and [authorization](git-workflow.md#authorization).
- When offered credentials, prepare the [local secret entry](security.md#local-development-secrets). Use synthetic test data, run [secret scans](security.md#secret-scanning) and check [git-crypt at session start](security.md#encrypted-env-with-git-crypt).
- Apply the [review scope](git-workflow.md#delegated-code-review) to the integration or production candidate.
- Preserve existing frameworks, working features, data, and deployment behavior. Replacing an established stack needs explicit approval. Use the `adopt-existing` skill when adopting/updating this blueprint in an existing project.
- Follow [navigation and route changes](design.md#navigation-and-route-changes): update development routes and references directly; do not add speculative legacy redirects or aliases.
- Maintain [Graphify infrastructure](project.md#graphify) and, for web-facing UI, [Playwright browser testing](project.md#playwright) at the level set by [checks by phase](security.md#checks-by-phase); use [current product references](packages.md#current-product-references) for external technologies.

## Autonomy

At or above 90% confidence, proceed within approved scope; this is judgment, not a measured probability. Otherwise investigate, asking only about material unresolved architecture, security, customer-data, billing, licensing, legal, destructive-operation, or product decisions. Continue independent work.

Use available APIs/tools without repeating authorization requests. Submit routine task-required access/support requests or appeals when authorized; report truthful references and next steps without inventing attestations or commitments. Routine tested dependency integration is pre-approved.

## Read when relevant

| Task | Guidance |
| --- | --- |
| Phase planning or transitions | [phases.md](phases.md) |
| Setup or environments | [project.md](project.md) |
| Existing-project adoption | `adopt-existing` skill at its recorded location, before changes |
| WordPress implementation or review | Required [WordPress skills](project.md#wordpress-skills) at their recorded locations |
| Issues, implementation, queue, commits | [git-workflow.md](git-workflow.md) |
| User-requested issue interview | `issue-interview` skill at its recorded location |
| UI | [design.md](design.md), including desktop/tablet/mobile coverage; `interface-design` and installed `playwright-cli` skills for implementation and verification |
| Selected tools or disposable shared-preview evaluation | [Optional tool setup](optional-tools.md) |
| Marketing, pricing, packaging, or refunds | [offering.md](offering.md); `pricing-research` skill for initial or material commercial decisions |
| Documentation | [documentation.md](documentation.md) |
| Issue completion or public release audit | Use the recorded `changelog` skill to assess the issue's customer impact or audit the exact candidate under the [changelog rules](documentation.md#changelog). |
| Security or customer-data changes | [security.md](security.md) |
| `.env` locked, key missing, new machine or repository, key rotation | [Encrypted `.env` with git-crypt](security.md#encrypted-env-with-git-crypt) |
| Dependency, build, or infrastructure changes | [Trivy scans](security.md#dependency-and-configuration-scanning) |
| Code quality | [Linting and formatting](packages.md#linting-and-formatting) |
| Personal-data practices, customer terms, or policies | [legal.md](legal.md); `legal-review` skill for policy preparation or material review |
| Product references / package choice / updates | [packages.md](packages.md) / [updates.md](updates.md) |
| Launch / release | [launch.md](launch.md) |

Read current code, issue comments, and applicable skills. Resolve material instruction conflicts explicitly. Obtain missing Blueprint skills from `skills/<name>/SKILL.md` at the adopted source/revision; obtain external skills from the upstream source linked in their setup guidance. Establish missing source facts from the supplied checkout or ask; never guess a repository or record an unapplied revision as adopted. `agent.md` redirects here; `CLAUDE.md` imports it.
