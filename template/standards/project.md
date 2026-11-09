# Project Setup and Environments

During setup, fill facts/commands in [AGENTS.md](../AGENTS.md); routine tasks use those verified values. For an existing application, use the `adopt-existing` skill at its recorded location before merging instructions. Setup does not authorize application upgrades, data changes, or production deployment.

## Setup interview

Interview the owner at every initial installation or adoption. Inspect the project and the private standing preferences recorded in `AGENTS.md`. Pre-fill known answers, preserve local protections and ask about unresolved choices. Recommend options proportionate to project size and risk. Always offer Monid. Record optional choices as selected, declined or deferred and revisit only on request or material change. Keep shared defaults private and credential-free. Spending and host access need project-specific scope.

| Question | Recommended default | Alternative to discuss |
| --- | --- | --- |
| What branding should this project use? | Preserve existing identity/tools; establish the [brand foundation and settings page](design.md#brand-foundation-and-settings), with owner-approved essentials before styled UI. | Create or extend an identity; offer optional Cofoundy Brand Skills only where needed and record the choice. |
| How would you like changes reviewed? | Agent verification and direct integration under [git-workflow.md](git-workflow.md). | Pull requests. Separately establish whether they require human approval or agent review and passing checks; preserve existing protections. |
| Do you want to evaluate concurrent agent sessions with one live preview? | Use the existing owned issue checkouts/worktrees. | Optional [experimental multi-agent mode](optional-tools.md#experimental-multi-agent-mode), selected by the owner for disposable evaluation only. |
| Do you need a separate staging environment? | Development and production under [environment defaults](#environment-defaults). | Explicitly requested staging for release or integration checks; preserve existing staging. |
| Do agent tasks need persistent or remote browser sessions? | Use the existing browser tools and required Playwright tests. | Select optional [Steel Browser](optional-tools.md#steel-browser) when session management, remote browsing, or page extraction would help. |
| Would this project benefit from GSD's additional planning tools? | Blueprint's existing workflow. | Consider [GSD Core](https://github.com/open-gsd/gsd-core) for larger projects or complex work spanning multiple sessions. Install only when selected. |
| Should agents capture reusable workflow lessons? | Offer optional [Task Observer](optional-tools.md#task-observer). | Keep ordinary issue notes without installing an observer. |
| Use Monid for development and testing? | Always offer [Monid](optional-tools.md#monid-for-development); record the choice, budget and secure credential entry location. | Existing direct tools/APIs; decline or defer Monid. |
| Which protected key and authorized machines should `.env` encryption use? | Configure and verify [git-crypt at setup](security.md#encrypted-env-with-git-crypt); record the protected key path and access scope. | Preserve established secure storage during adoption; an explicit local-only exception keeps `.env` ignored and untracked. Plaintext `.env` is never pushed. |
| When should weekly maintenance run? | Verify a shared schedule for Blueprint updates and security checks under [updates.md](updates.md). | Record unavailable/declined automation and active-session fallback explicitly. |
| Does the VM permit Saturday updates and reboots? | [Late Saturday maintenance](updates.md#weekly-vm-maintenance) with recorded timezone, host scope, downtime and reboot authorization. | Preserve a suitable existing window or provider-managed maintenance; shared hosts use one job. |

Record decisions in `AGENTS.md` and link private configuration and verification evidence. Proceed on settled choices.

If GSD is selected, follow its current official installation guidance. Project `AGENTS.md` and Blueprint rules remain authoritative; GitHub issues/Projects remain the work queue and completion record. GSD plans support approved issues, and its implementation phases do not advance the product lifecycle. Configure its review, delivery, and automation behavior to honor recorded choices; GSD does not independently authorize tags or releases.

## Project workspace

Use the repository root as the project workspace. Create directories when needed. Keep reference documents in `materials/documents/`, research and notes in `materials/notebooks/`, and editable diagrams and canvases in `materials/drawings/`. UI mockups, wireframes and editable brand artwork belong in `design/`. Keep shipped images, icons and fonts in the framework’s asset location. Follow [brand guidance](design.md#brand-foundation-and-settings) and maintain audience-specific [documentation](documentation.md) under root `docs/`.

Keep `README.md`, `AGENTS.md`, `CLAUDE.md`, the [license](legal.md#repository-license), the [changelog](documentation.md#changelog) when due, and encrypted `.env` at the application root. Keep the operating guides together in `standards/` and link them from root `AGENTS.md`. Preserve framework source, test, build and deployment paths. Add workflow or container files only when the project uses them.

Root `agents/` and `skills/` hold project-authored profiles and skills. Register them through each tool’s supported discovery mechanism, verify discovery and record the canonical and installed paths in `AGENTS.md`. Keep one editable source per resource. Blueprint’s reusable skills come from its distribution checkout.

Apply [workspace migration](documentation.md#workspace-migration) during initial adoption and Blueprint updates in existing projects. Record workspace paths, migration issue/status and any required external private storage in root `AGENTS.md`. Folder names confer no privacy: apply [documentation access rules](documentation.md) and [secret and recovery rules](security.md#local-development-secrets) to notes, canvases, attachments and AI resources too. Encrypt secret-bearing files and account for assets or native canvas formats needing external backups. Only explicitly approved public documentation/assets enter published output.

## Setup checklist

Record tool versions, locations and verification results for the current [checks by phase](security.md#checks-by-phase). Use `not applicable` only for exclusions the owning rule permits.

1. Record [phase](phases.md), launch state, actual development/deployed commits, branches, triggers and services. Mark unconfigured items. Start new projects at planning and preserve the verified position of existing projects. Establish [integration](git-workflow.md) without disturbing unfinished work.
2. Verify scripts/CI commands in `AGENTS.md` and the human quick start in README. Configure [Playwright](#playwright), selected [Steel](optional-tools.md#steel-browser), [lint/format](packages.md#linting-and-formatting) and phase-appropriate [delegated review](#open-code-review).
3. Establish the private index and applicable public/admin sources, destinations, builds and access under [documentation.md](documentation.md). Verify links and delivery.
4. Follow [security setup](security.md) for project-root secrets, encryption, scanning, recovery inventory, restore evidence, synthetic data and private reporting. Record jurisdictions and assess [notices](legal.md) before collecting personal data. Inventory existing [offers](offering.md), policies and customer-facing pages.
5. Configure and verify [maintenance](updates.md) for Blueprint, dependencies, advisories and hosts at the applicable phase. Record package rationale, schedules, actual run evidence and coverage.
6. Verify [Graphify](#graphify), applicable [WordPress skills](#wordpress-skills) and [product references](packages.md#current-product-references). Record Blueprint revision, exceptions and verified skill discovery or readable checkout in `AGENTS.md`.

## WordPress skills

WordPress sites, themes, and plugins require the applicable skills from the official [WordPress agent-skills pack](https://github.com/WordPress/agent-skills). During setup/adoption, install `wordpress-router`, `wp-project-triage`, and relevant specialist skills project-scoped through the active agent's supported mechanism, following current upstream instructions. Include each skill's references and helper scripts; verify discovery and required helper dependencies, and record the upstream revision and installed locations in project `AGENTS.md`.

For themes, preserve root `style.css` and the template entry points for the theme type (for example, `templates/index.html` in a standalone block theme or `index.php` in a standalone classic theme). For plugins, keep the main PHP file with its plugin header at the plugin root. These paths are relative to the installable component, including in repositories containing a whole site. See the [Theme Handbook](https://developer.wordpress.org/themes/core-concepts/theme-structure/) and [Plugin Handbook](https://developer.wordpress.org/plugins/plugin-basics/header-requirements/).

Use routing and triage to identify the project and select skills for WordPress work. Read and follow the selected skills before implementation or review: `wp-plugin-development` for plugin work, `wp-plugin-directory-guidelines` for applicable directory-compliance reviews, `wp-performance` for performance work, and `wp-phpstan` for PHPStan analysis. Select theme, block, REST API, or operations skills as the task requires; add missing relevant skills rather than loading the entire pack for every task. Directory submission rules do not automatically apply to private plugins.

Keep installed skills current under [updates.md](updates.md), verifying compatibility with the project's actual WordPress/PHP versions and tooling. Record unsupported checks as blockers; skill installation or updates do not authorize application upgrades. Project `AGENTS.md` remains authoritative for project conventions and scope. Resolve version-specific technical questions through [current product references](packages.md#current-product-references), using official WordPress documentation when needed rather than copying vendor manuals into project skills.

## Open Code Review

Open Code Review is required from the phase specified in [checks by phase](security.md#checks-by-phase), not an optional interview choice. Install the official [Alibaba CLI](https://github.com/alibaba/open-code-review) (`@alibaba-group/open-code-review`, command `ocr`) and its `open-code-review-delegate` skill through the active agent's supported mechanism, following [current delegation instructions](https://github.com/alibaba/open-code-review/blob/main/pages/src/content/docs/en/integrations/delegate.md). Verify CLI operation and skill discovery; record installed versions/revisions, skill location, and review commands in project `AGENTS.md`. Keep tooling current under [updates.md](updates.md).

Delegation uses the host agent's existing model allowance without a separate OCR model endpoint or API key; it is not unlimited free inference. Project instructions remain authoritative. Verify setup through the complete [delegated review workflow](git-workflow.md#delegated-code-review) on an actual change; record a blocker if none is available yet. A preview command alone cannot verify review completion.

## Playwright

Playwright is required for projects with a web-facing UI. Install and verify it during setup/adoption using [official guidance](https://playwright.dev/docs/intro), preserving the stack, tests, and package-manager conventions; desktop checks apply during `build` and the full device matrix from `DEVELOPMENT: security` under [checks by phase](security.md#checks-by-phase). Projects without a web-facing UI record `Playwright: not applicable` and the reason in `AGENTS.md`, and skip its test package, browsers, CLI/skill, and device-matrix verification. Reassess when a web UI is added; a planned UI that is not runnable yet is a setup blocker, not an exclusion.

- **Project-local browser:** keep the browser runtime within the project's existing LXC container or VM, with Playwright as the automation and verification layer. Include browser setup and lifecycle commands with the project; no separate browser VM or hosted browser service is required. Verify sandboxing, permissions, resource limits and project-specific profile isolation in the actual environment. Do not automatically disable browser protections or make the container privileged to solve launch failures; investigate compatible configuration and report genuine host limitations through existing setup rules.
- Install project development tooling (normally `@playwright/test`), required browser binaries, and system dependencies. Configure the application's test URL or local server, isolated test data, and browser coverage appropriate to supported users. Preserve useful unit and integration tests.
- Install Microsoft's official [Playwright CLI and agent skill](https://github.com/microsoft/playwright-cli) (`@playwright/cli`, skill `playwright-cli`) using current upstream instructions and the active agent's supported mechanism. Install the skill project-scoped with its references (upstream provides `playwright-cli install --skills`), verify CLI/browser operation and skill discovery, and record versions and the installed skill path in `AGENTS.md`. Project instructions remain authoritative. Use the skill for browser inspection and retain repeatable checks in the project's test suite; CLI installation alone does not replace `@playwright/test` coverage.
- Configure [desktop, tablet, and mobile coverage](design.md#desktop-tablet-and-mobile) using current [Playwright device emulation](https://playwright.dev/docs/emulation) and viewport settings. Install/verify the Blueprint `interface-design` skill through the target agent's supported mechanism, or record a verified readable source location when installation is unavailable. Verify rendering and critical interactions at the scope required by [checks by phase](security.md#checks-by-phase); record any application-readiness blocker rather than marking coverage complete.
- Run a repeatable smoke test against the actual application, asserting meaningful page content or behavior. Record the installed version, browser coverage, test command in `AGENTS.md`, and setup/results in private project docs. Package installation, an upstream example test, or a passing build alone does not verify setup. If the application cannot run yet, record the blocker and complete verification when it can; do not mark setup verified prematurely.
- During development, run affected browser tests and retain useful regression tests for critical journeys. Verify rendered UI through the `interface-design` skill. Investigate failures and report blocked/skipped checks explicitly before completion.
- For UI work with selected Impeccable, follow [browser iteration](design.md#browser-iteration), including helper cleanup and Playwright verification of the accepted source. Record Live Mode support and launch/cleanup commands alongside existing tooling; keep one application development server and preserve the project workflow.
- Maintain Playwright, its CLI/skill, and matching browsers under [updates.md](updates.md), following current upstream instructions and rechecking skill discovery after updates. Unattended runs use the recorded automation choice and authorized resources; local testing remains required when CI is unavailable.

## Graphify

Graphify is required infrastructure for adopting projects. Its agent tooling is installed at setup; an installation failure is recorded rather than blocking during `planning` and `build`, and it must be working from `DEVELOPMENT: security` under [checks by phase](security.md#checks-by-phase). Application upgrades remain separate work. Follow the [current official Graphify specifications](https://github.com/Graphify-Labs/graphify#readme) for installation and maintenance rather than copying its manual here.

- During setup/adoption, verify/install Graphify's Python CLI from [PyPI](https://pypi.org/project/graphifyy/) using `uv tool install graphifyy` or `pipx install graphifyy` per upstream guidance, and keep it current. Confirm the package's repository metadata points to `Graphify-Labs/graphify`; do not install the unrelated npm package of the same name. Install its project-scoped skill for the active agent, verify discovery, initialize/build the project graph, and install/verify supported Git hooks without discarding existing hooks.
- Keep the graph current throughout development. Use scoped graph queries before broad codebase exploration and verify findings against source files. After pulls/merges, run `graphify update .`; refresh changed docs, configuration, and other semantic sources through the current documented semantic-update procedure. Code hooks alone do not refresh semantic content.
- Periodically verify installation/version, skill discovery, hooks, and graph freshness with the project's maintenance checks. After Graphify or Python environment upgrades, refresh the skill and reinstall/verify hooks as upstream requires. Record the installed version, verified setup, checks, and any gaps in private project docs; update the version record after upgrades.
- Project `AGENTS.md` remains authoritative. Review generated guidance and merge only compatible additions; it must not overwrite, weaken, or replace project rules.

## Environment defaults

For hosted web applications, apply these during new or explicitly authorized environment setup:

| Environment | Address | Source |
| --- | --- | --- |
| Development and release testing | `develop.<domain>` | `develop`, after required checks |
| Production | Main production domain | `main`, through an authorized release |
| Optional staging | `staging.<domain>` | Recorded release candidate and defined trigger |

- Development and production are sufficient by default. Use `develop`, matching the branch, for new development subdomains. Staging is not a setup/release prerequisite.
- Create or activate staging DNS, hosting, resources, jobs, or a branch only on explicit owner or authorized human developer request. An agent recommendation alone is insufficient. Preserve existing environments during adoption; never silently rename/deactivate them. Staging does not require a permanent staging branch.
- Configure authorized automatic development deployment after checks; record actual destinations, triggers, and deployed commits. Production follows the workflow's release rule. Verify a replacement preview before retiring the previous one.
- A private beta may use production before public launch under [launch.md](launch.md). Lifecycle phase does not select an environment or activate staging.
- Isolate development/test databases, storage, credentials, sessions, and integrations. Use synthetic data and provider sandboxes or controlled substitutes; testing must not charge/message customers, purchase real resources, or modify customer applications. Restrict access; admin environment identification follows [design.md](design.md). Apply the same isolation to requested staging.
- During final testing, pin the candidate in a preview or hold deployments that would replace it. Record its commit; changes require affected checks again before promotion under [launch.md](launch.md).
