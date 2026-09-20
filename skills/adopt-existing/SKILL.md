---
name: adopt-existing
description: Adopt or update the project blueprint in an existing application while preserving its stack, data, unfinished work, and deployments. Use for instruction/workflow migration, not routine feature implementation.
---

# Adopt an Existing Project

Confirm the target repository and blueprint revision. Plain filenames below refer to the target's instructions; before they are installed, consult the blueprint's `template/` equivalents. Never resolve them relative to this installed skill.

Adoption changes instructions and workflow, not application architecture, packages, data, or production behavior. Preserve existing functionality and project-specific requirements. Replacement of an established stack or architecture needs explicit permission.

After inspection, follow `git-workflow.md` for the setup issue and tracking bootstrap. Establish an owned isolated checkout before file edits or skill installation; preserve other agents' worktrees.

## Inspect and preserve

- Inventory instructions, branches, PRs, active worktrees, uncommitted work, architecture, dependencies, components, integrations, data, environments, deployment triggers, and available checks. Record what exists before changing it.
- Keep established CSS/component/icon frameworks and functioning custom code. Generic defaults fill gaps; they do not justify introducing a different framework or rebuilding features.
- Inventory and preserve schemas/migrations, configuration, secret storage, URLs, content, release history, published policies/terms, effective versions/dates, acceptance records, and live behavior. Do not discard another agent's work, reset shared history, migrate databases, replace live policies, or activate production workflows as an adoption side effect.
- Merge unique local requirements into target instructions/private docs. Consolidate obsolete workflow rules while preserving useful knowledge. Use an owned isolated issue checkout under `git-workflow.md`.

## Establish develop from current work

1. Fetch and compare actual branches and identify the current development state; the default branch may be stale. Record the source commit and where unfinished work will remain. For a live product, also identify the deployed version and production triggers; do not assume the branch tip equals the running version.
2. Follow the integration/release policy in `git-workflow.md`. If `develop` is missing, establish it from the verified appropriate state with its tracked files and history. If it exists, reconcile through reviewed/tested integration; never reset it to force alignment. Preserve unfinished work on owned branches and coordinate PR retargeting rather than merging every branch.
3. Direct new issues/PRs and maintenance integration to `develop`; update obsolete instructions and development automation references. Inspect repository and hosting triggers before pushing. Creating a branch does not switch a deployment.
4. Follow `project.md` for authorized development/test routing and optional staging. Verify the replacement preview and deployed commit before retiring an old preview. Preserve production routing and existing operational update settings. Branch transitions never relocate databases, uploads, hosted customer applications, or other runtime resources.
5. Record the final branches, routes/triggers, checks, and pending transition work in `docs/internal/`. Preserve `main`, its history, and any distinct deployed/unreleased states.

Before launch, development may already have happened on `main`; preserve that snapshot rather than emptying it. Continue testing on `develop` until the authorized first launch. An existing landing page or unpublished production domain can remain as-is.

For already-live products, preserve the current service and release baseline. If a transition cannot be isolated from production, pause that step with a brief recommendation while continuing independent work. Preserve tags, release notes, public docs, and changelog history. If a changelog is missing, draft from verified facts and future Unreleased entries; never invent history or treat adoption as a first launch. Subsequent release preparation follows `launch.md`.

## WordPress, when applicable

- Preserve core behavior, parent/child theme, plugins/custom plugins, hooks, shortcodes, blocks, page-builder content, and established Bootstrap/Tabler UI.
- Keep customizations in their supported locations; do not edit core/vendor/parent-theme files as a shortcut. Document existing modifications there and propose a separate migration.
- Enqueue scripts/styles through WordPress on relevant pages; avoid duplicate frameworks and CSS leaking between frontend, admin, and editor.
- Preserve the database, uploads/media, roles, settings, credentials, and paid-plugin licenses. Do not import development data into production or activate/deactivate plugins during adoption.
- Record PHP/WordPress checks and critical user journeys. Core/theme/plugin/dependency upgrades follow `updates.md` as separate maintenance work.

## Migrate instructions, tracking, and docs

1. Inventory labels and Project statuses across all issues, including closed ones. Record the old-to-new mapping in the adoption issue, preserving comments, ownership, dependencies, and meaningful priority/type information.
2. Apply canonical labels and four statuses under `git-workflow.md`. Remove obsolete definitions only when replacement is authorized, after remapping issues and updating filters/automation. Helpers only create/update label definitions; they do not migrate issues.
3. Keep truly completed issues closed with only `COMPLETED`; do not convert canceled work to completed. Started blockers stay `IN PROGRESS` with one pause reason, preserving type/stage history for resumption.
4. When adopting from `docs/wiki/` or an existing wiki, preserve useful pages, diagrams, assets, and history in private `docs/internal/` and repair links. Verify preservation before retiring wiki publishing jobs and completion requirements; never delete the only copy. Follow `documentation.md` for ongoing internal/public/admin docs and retain the application's release history.
5. Install applicable skills through the target agent's supported mechanism or retain a readable blueprint checkout. Verify discovery or explicit file access and record the locations in target `AGENTS.md`.
6. Complete compatible parts of `project.md`; document deferred maintenance or deployment changes honestly. Verify links, tracking, and unchanged application behavior in a safe development/test environment. Report changes and remaining user actions briefly with direct links.
