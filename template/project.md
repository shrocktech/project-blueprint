# Project Setup and Environments

During setup, fill facts/commands in [AGENTS.md](AGENTS.md); routine tasks use those verified values. For an existing application, use the `adopt-existing` skill at its recorded location before merging instructions. Setup does not authorize application upgrades, data changes, or production deployment.

## Setup interview

Inspect the project and prior decisions first. Preserve established environments, protections, and preferences; ask only about unresolved choices or proposed changes before configuring them. Recommend a setup based on complexity, collaboration, and release risk, not size alone. Keep questions brief, allow the owner's own answer, and skip settled items.

| Question | Recommended default | Alternative to discuss |
| --- | --- | --- |
| How would you like changes reviewed? | Agent verification and direct integration under [git-workflow.md](git-workflow.md). | Pull requests. Separately establish whether they require human approval or agent review and passing checks; preserve existing protections. |
| Do you need a separate staging environment? | Development and production under [environment defaults](#environment-defaults). | Explicitly requested staging for release or integration checks; preserve existing staging. |
| Would this project benefit from GSD's additional planning tools? | Blueprint's existing workflow. | Consider [GSD Core](https://github.com/open-gsd/gsd-core) for larger projects or complex work spanning multiple sessions. Install only when selected. |
| Should approved maintenance continue when no agent session is active? | Use existing authorized automation; otherwise agents handle maintenance during active sessions. | Configure unattended maintenance under [updates.md](updates.md), explaining required access, resources, and costs before a decision. |

Summarize and record answers as setup decisions in project `AGENTS.md`, linking detailed configuration and verified automation status in private project docs. Proceed on those decisions without another confirmation or repeated routine interviews; explain genuine setup blockers. Graphify, Playwright, and [secret scanning](security.md#secret-scanning) remain required and Context7 remains the preferred reference with official-docs fallback; production releases still require explicit authorization.

If GSD is selected, follow its current official installation guidance. Project `AGENTS.md` and Blueprint rules remain authoritative; GitHub issues/Projects remain the work queue and completion record. GSD plans support approved issues, and its implementation phases do not advance the product lifecycle. Configure its review, delivery, and automation behavior to honor recorded choices; GSD does not independently authorize tags or releases.

## Setup checklist

1. Record the phase/subphase under [phases.md](phases.md), launch state, actual development/deployed commits, branches, triggers, services, and checks. New projects start at `DEVELOPMENT: planning`; existing projects retain their verified position, asking only if unclear. Mark undeployed/unconfigured items explicitly. Establish integration under [git-workflow.md](git-workflow.md) without discarding unfinished work.
2. Complete [Playwright setup](#playwright) and [Open Code Review setup](#open-code-review). Fill and verify the command table from scripts/CI; identify blocked or inapplicable commands. Keep the human-facing quick start in README.
3. Establish private `docs/internal/` and its index under [documentation.md](documentation.md). Add `docs/public/` and optional `docs/admin/` only when needed; record each source, destination, build command, audience, and access restrictions. Verify links and existing delivery without publishing an unauthorized release.
4. Complete [Betterleaks secret-scanning setup](security.md#secret-scanning). Document test-data setup, secret configuration, and private vulnerability reporting under [security.md](security.md), without secret values. Record business/service regions and existing policies under [legal.md](legal.md); assess applicable notices before real personal-data collection, including pre-launch. Identify existing commercial decisions and customer-facing pages under [offering.md](offering.md). Adoption does not authorize replacing live policies or offers.
5. Configure maintenance under [updates.md](updates.md), recording schedule, coverage, checks, runner/run links, and gaps. Distinguish active-agent work from verified unattended automation; record package rationale.
6. Set up [Graphify](#graphify) and verify access to current product references under [packages.md](packages.md#current-product-references). Record blueprint revision, local exceptions, and accessible skill locations in `AGENTS.md`. Verify installed discovery or explicit reading from a retained blueprint checkout. Application domains and provider details belong in project docs, not the reusable blueprint.

## Open Code Review

Open Code Review is required review tooling for adopting projects, not an optional interview choice. Install the official [Alibaba CLI](https://github.com/alibaba/open-code-review) (`@alibaba-group/open-code-review`, command `ocr`) and its `open-code-review-delegate` skill through the active agent's supported mechanism, following [current delegation instructions](https://github.com/alibaba/open-code-review/blob/main/pages/src/content/docs/en/integrations/delegate.md). Verify CLI operation and skill discovery; record installed versions/revisions, skill location, and review commands in project `AGENTS.md`. Keep tooling current under [updates.md](updates.md).

Delegation uses the host agent's existing model allowance without a separate OCR model endpoint or API key; it is not unlimited free inference. Project instructions remain authoritative. Verify setup through the complete [delegated review workflow](git-workflow.md#delegated-code-review) on an actual change; record a blocker if none is available yet. A preview command alone cannot verify review completion.

## Playwright

Playwright is required testing infrastructure for adopting projects. Install and verify it during setup/adoption; this is not an optional interview choice. Follow the [official setup guidance](https://playwright.dev/docs/intro), preserving the application's stack, existing tests, and package-manager conventions.

- Install project development tooling (normally `@playwright/test`), required browser binaries, and system dependencies. Configure the application's test URL or local server, isolated test data, and browser coverage appropriate to supported users. Preserve useful unit and integration tests.
- Run a repeatable smoke test against the actual application, asserting meaningful page content or behavior. Record the installed version, browser coverage, test command in `AGENTS.md`, and setup/results in private project docs. Package installation, an upstream example test, or a passing build alone does not verify setup. If the application cannot run yet, record the blocker and complete verification when it can; do not mark setup verified prematurely.
- During development, run affected browser tests and retain useful regression tests for critical journeys. Verify rendered UI through the `interface-design` skill. Investigate failures and report blocked/skipped checks explicitly before completion.
- Maintain Playwright and its matching browsers under [updates.md](updates.md), following current upstream instructions. Unattended runs use the recorded automation choice and authorized resources; local testing remains required when CI is unavailable.

## Graphify

Graphify is required infrastructure for adopting projects. Its agent tooling is part of setup; application upgrades remain separate work. Follow the [current official Graphify specifications](https://github.com/Graphify-Labs/graphify#readme) for installation and maintenance rather than copying its manual here.

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
