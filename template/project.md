# Project Setup and Environments

During setup, fill facts/commands in [AGENTS.md](AGENTS.md); routine tasks use those verified values. For an existing application, use the `adopt-existing` skill at its recorded location before merging instructions. Setup does not authorize application upgrades, data changes, or production deployment.

## Setup interview

Always conduct a short owner interview at initial installation/adoption, including small projects, before configuring choices. Inspect the project and any private standing preferences supplied by the owner. Pre-fill the interview summary with applicable defaults, including the Monid choice. Offer Monid on every initial interview and ask only about unresolved choices or conflicts. Project-specific decisions and protections take precedence. Keep the shared preference record private and free of credentials. Spending, host access and release authority require explicit scope for this project. Recommend simpler defaults for small projects and additional review/environment tools when complexity, collaboration or release risk warrants them. Preserve established protections, allow the owner's own answer, and record decisions. Routine refreshes reuse those answers and ask only about material changes; they do not repeat the initial interview.

| Question | Recommended default | Alternative to discuss |
| --- | --- | --- |
| What branding should this project use? | Preserve existing identity/tools; establish the [brand foundation and settings page](design.md#brand-foundation-and-settings), with owner-approved essentials before styled UI. | Create or extend an identity; offer optional Cofoundy Brand Skills only where needed and record the choice. |
| How would you like changes reviewed? | Agent verification and direct integration under [git-workflow.md](git-workflow.md). | Pull requests. Separately establish whether they require human approval or agent review and passing checks; preserve existing protections. |
| Do you want to evaluate concurrent agent sessions with one live preview? | Use the existing owned issue checkouts/worktrees. | Optional [experimental multi-agent mode](optional-tools.md#experimental-multi-agent-mode), selected by the owner for disposable evaluation only; record declined or deferred without repeated prompts. |
| Do you need a separate staging environment? | Development and production under [environment defaults](#environment-defaults). | Explicitly requested staging for release or integration checks; preserve existing staging. |
| Do agent tasks need persistent or remote browser sessions? | Use the existing browser tools and required Playwright tests. | Select optional [Steel Browser](optional-tools.md#steel-browser) when session management, remote browsing, or page extraction would help. |
| Would this project benefit from GSD's additional planning tools? | Blueprint's existing workflow. | Consider [GSD Core](https://github.com/open-gsd/gsd-core) for larger projects or complex work spanning multiple sessions. Install only when selected. |
| Should agents capture reusable workflow lessons? | Offer optional [Task Observer](optional-tools.md#task-observer); record enabled, declined, or deferred without repeated prompts. | Keep ordinary issue notes without installing an observer. |
| Use Monid for development and testing? | Always offer [Monid](optional-tools.md#monid-for-development); record the choice, budget and secure credential entry location. | Existing direct tools/APIs; decline or defer Monid. |
| Which protected key and authorized machines should `.env` encryption use? | Configure and verify [git-crypt at setup](security.md#encrypted-env-with-git-crypt); record the protected key path and access scope. | Preserve established secure storage during adoption; an explicit local-only exception keeps `.env` ignored and untracked. Plaintext `.env` is never pushed. |
| When should weekly maintenance run? | Verify a shared schedule for Blueprint updates and security checks under [updates.md](updates.md). | Record unavailable/declined automation and active-session fallback explicitly. |
| Does the VM permit Saturday updates and reboots? | [Late Saturday maintenance](updates.md#weekly-vm-maintenance) with recorded timezone, host scope, downtime and reboot authorization. | Preserve a suitable existing window or provider-managed maintenance; shared hosts use one job. |

Record the resulting setup decisions in project `AGENTS.md`, linking detailed configuration and verified automation status in private project docs. Proceed on those decisions without another confirmation or repeated routine interviews; explain genuine setup blockers. Required tooling in the setup checklist is not an optional interview choice; Context7 remains the preferred reference with official-docs fallback, and production releases still require explicit authorization.

If GSD is selected, follow its current official installation guidance. Project `AGENTS.md` and Blueprint rules remain authoritative; GitHub issues/Projects remain the work queue and completion record. GSD plans support approved issues, and its implementation phases do not advance the product lifecycle. Configure its review, delivery, and automation behavior to honor recorded choices; GSD does not independently authorize tags or releases.

## Project workspace

New and existing applications use lowercase `project/` for project knowledge and project-specific AI resources. Create directories as content is needed:

```text
project/
  CHANGELOG.md   # At go-live preparation, or migrated when already present
  assets/
    brand/
    notes/
    canvas/
    files/
  docs/
    internal/
      brand/
    public/
    admin/       # When needed
  skills/
  agents/
```

Keep `AGENTS.md`, `CLAUDE.md`, README, encrypted `.env` and the Blueprint guide entrypoints at the application root. Application source, served assets, tests, framework-required configuration and installed tool discovery directories retain their supported locations. Blueprint's own `template/` and reusable `skills/` are distribution resources. `project/skills/` and `project/agents/` hold project-specific authored resources; register or install them through each tool's supported mechanism, verify discovery and record canonical and installed locations in root `AGENTS.md`. Use one authoritative source for each resource and verify any generated or linked installation rather than editing duplicate copies.

Apply [workspace migration](documentation.md#workspace-migration) during initial adoption and Blueprint updates in existing projects. Record workspace paths, migration issue/status and any required external private storage in root `AGENTS.md`. Folder names confer no privacy: apply [documentation access rules](documentation.md) and [secret and recovery rules](security.md#local-development-secrets) to notes, canvases, attachments and AI resources too. Encrypt secret-bearing files and account for assets or native canvas formats needing external backups. Only explicitly approved public documentation/assets enter published output.

## Setup checklist

Record each required tool's installed version/revision, location, and verification status. Record reasoned `not applicable` only where its owning rule permits exclusion; otherwise record a blocker for the applicable phase under [checks by phase](security.md#checks-by-phase). Record deferred tools and non-blocking Graphify failures explicitly; do not call them verified. Setup completion requires the records and verification applicable to the current phase.

1. Record the phase/subphase under [phases.md](phases.md), launch state, actual development/deployed commits, branches, triggers, services, and checks. New projects start at `DEVELOPMENT: planning`; existing projects retain their verified position, asking only if unclear. Mark undeployed/unconfigured items explicitly. Establish integration under [git-workflow.md](git-workflow.md) without discarding unfinished work.
2. Complete [Playwright setup](#playwright), selected [Steel Browser setup](optional-tools.md#steel-browser), and [linting and formatting](packages.md#linting-and-formatting); [Open Code Review setup](#open-code-review) and the full device matrix follow [checks by phase](security.md#checks-by-phase) at `DEVELOPMENT: security`. Fill and verify the command table from scripts/CI; identify blocked or inapplicable commands. Keep the human-facing quick start in README.
3. Establish private `project/docs/internal/` and its index under [documentation.md](documentation.md). Add `project/docs/public/` and optional `project/docs/admin/` only when needed; record each source, destination, build command, audience, and access restrictions. Verify links and existing delivery without publishing an unauthorized release.
4. Complete [Betterleaks secret-scanning setup](security.md#secret-scanning); [Trivy](security.md#dependency-and-configuration-scanning) and applicable [ZAP testing](security.md#application-and-api-security-testing) are installed and verified at `DEVELOPMENT: security` under [checks by phase](security.md#checks-by-phase). Create and protect the project-root `.env` and placeholder-only `.env.example` under [local secret handling](security.md#local-development-secrets); configure and verify standard [git-crypt encryption](security.md#encrypted-env-with-git-crypt), including plaintext blocking and scan-scope tests, before tracking `.env`. Inventory all [recovery dependencies and protected backups](security.md#local-development-secrets), record recovery objectives and restore-test evidence/gaps, and verify applicable recovery readiness. Document test-data setup, secret configuration, and private vulnerability reporting under [security.md](security.md), without secret values. Record business/service regions and existing policies under [legal.md](legal.md); assess applicable notices before real personal-data collection, including pre-launch. Identify existing commercial decisions and customer-facing pages under [offering.md](offering.md). Adoption does not authorize replacing live policies or offers.
5. Configure maintenance under [updates.md](updates.md), including [weekly VM maintenance](updates.md#weekly-vm-maintenance) and [periodic Blueprint checks](updates.md#periodic-blueprint-maintenance); [NVD/OSV advisory monitoring and health verification](updates.md#advisory-monitoring-and-health) is configured at `DEVELOPMENT: security`; record schedules, coverage, checks, runner/run links, last successful checks, and gaps. Distinguish active-agent work from verified unattended automation; record package rationale.
6. Set up [Graphify](#graphify), complete [WordPress skills setup](#wordpress-skills) for WordPress projects, and verify access to current product references under [packages.md](packages.md#current-product-references). Record blueprint revision, local exceptions, and accessible skill locations in `AGENTS.md`. Verify installed discovery or explicit reading from a retained blueprint checkout. Application domains and provider details belong in project docs, not the reusable blueprint.

## WordPress skills

WordPress sites, themes, and plugins require the applicable skills from the official [WordPress agent-skills pack](https://github.com/WordPress/agent-skills). During setup/adoption, install `wordpress-router`, `wp-project-triage`, and relevant specialist skills project-scoped through the active agent's supported mechanism, following current upstream instructions. Include each skill's references and helper scripts; verify discovery and required helper dependencies, and record the upstream revision and installed locations in project `AGENTS.md`.

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
