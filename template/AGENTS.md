# Agent Instructions

Follow the user's latest instructions. Fill project facts and commands during setup; read detailed guides only for the current task.

## Project facts

- Purpose, users, stack, runtime, package manager, directories: to be filled in.
- Lifecycle: phase TODO; subphase TODO (`none` for `PRODUCTION`); active plan TODO. Use [phases.md](phases.md) for current focus and transitions.
- Owner: the human authorized to bind the project/business; record their role and delegates. Policy approval requires explicit legal/business delegation; development or release access alone does not confer it.
- Business and customer/service jurisdictions: record verified scope in private project docs; no assumed country.
- Conventions: link existing formatter/linter configuration and patterns.
- Hosting constraint: GitHub Free for public/private repositories; no required upgrade, paid features, billed usage, or visibility change.
- Private documentation index, dependency rationale, automation status: record verified locations.
- Blueprint source (repository or URL): TODO; adopted revision: TODO; local exceptions: TODO.
- Skill locations: record verified paths for applicable `adopt-existing`, `issue-interview`, `interface-design`, `pricing-research`, and `legal-review` skills during setup. A source folder alone does not install skills.

## Verified commands

| Operation | Directory | Command / status |
| --- | --- | --- |
| Install | TODO | TODO — unverified |
| Run locally | TODO | TODO — unverified |
| Build | TODO | TODO — unverified |
| Test | TODO | TODO — unverified |
| Lint / types | TODO | TODO — unverified |

Use actual scripts/CI. Run applicable commands before marking them verified; identify inapplicable or blocked checks. Never include secret values.

## Always apply

- Development needs an issue and an isolated issue branch/worktree; an existing dedicated checkout suffices. Follow [git-workflow.md](git-workflow.md) for verified direct integration and release authorization.
- Never update `main` or deploy production without an explicit release instruction; passing tests and a completed issue are not that instruction.
- Done means verified behavior, current affected docs, successful integration/delivery, and a closed issue labeled only `COMPLETED`.
- During implementation, refresh live work after each completed/paused issue and before stopping; continue newly added actionable approved work. Questions, reviews, and interviews do not start the implementation queue.
- Never expose or commit secrets; use synthetic test data. Credentials authorize approved work only.
- Preserve existing frameworks, working features, data, and deployment behavior. Replacing an established stack needs explicit approval. Use the `adopt-existing` skill when adopting/updating this blueprint in an existing project.

## Autonomy

At or above 90% confidence, proceed within approved scope; this is judgment, not a measured probability. Otherwise investigate, asking only about material unresolved architecture, security, customer-data, billing, licensing, legal, destructive-operation, or product decisions. Continue independent work.

Use available APIs/tools without repeating authorization requests. Submit routine task-required access/support requests or appeals when authorized; report truthful references and next steps without inventing attestations or commitments. Routine tested dependency integration is pre-approved.

## Read when relevant

| Task | Guidance |
| --- | --- |
| Phase planning or transitions | [phases.md](phases.md) |
| Setup or environments | [project.md](project.md) |
| Existing-project adoption | `adopt-existing` skill at its recorded location, before changes |
| Issues, implementation, queue, commits | [git-workflow.md](git-workflow.md) |
| User-requested issue interview | `issue-interview` skill at its recorded location |
| UI | [design.md](design.md); `interface-design` skill for page/form layout and interaction work |
| Marketing, pricing, packaging, or refunds | [offering.md](offering.md); `pricing-research` skill for initial or material commercial decisions |
| Documentation | [documentation.md](documentation.md) |
| Security or customer-data changes | [security.md](security.md) |
| Personal-data practices, customer terms, or policies | [legal.md](legal.md); `legal-review` skill for policy preparation or material review |
| Package choice / updates | [packages.md](packages.md) / [updates.md](updates.md) |
| Launch / release | [launch.md](launch.md) |

Read current code, issue comments, and applicable skills. Resolve material instruction conflicts explicitly. For missing skills, use `skills/<name>/SKILL.md` from the recorded source/revision. Establish missing source facts from the supplied checkout or ask; never guess a repository. If no revision is recorded, resolve the source's default branch and record the retrieved commit without inventing adoption history. `agent.md` redirects here; `CLAUDE.md` imports it.
