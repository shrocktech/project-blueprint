# Project Setup and Environments

During setup, fill facts/commands in [AGENTS.md](AGENTS.md); routine tasks use those verified values. For an existing application, use the `adopt-existing` skill at its recorded location before merging instructions. Setup does not authorize application upgrades, data changes, or production deployment.

## Setup checklist

1. Record the phase/subphase under [phases.md](phases.md), launch state, actual development/deployed commits, branches, triggers, services, and checks. New projects start at `DEVELOPMENT: specs`; existing projects retain their verified position, asking only if unclear. Mark undeployed/unconfigured items explicitly. Establish integration under [git-workflow.md](git-workflow.md) without discarding unfinished work.
2. Fill and verify the command table from scripts/CI; identify blocked or inapplicable commands. Keep the human-facing quick start in README.
3. Establish private `docs/internal/` and its index under [documentation.md](documentation.md). Add `docs/public/` and optional `docs/admin/` only when needed; record each source, destination, build command, audience, and access restrictions. Verify links and existing delivery without publishing an unauthorized release.
4. Document test-data setup, secret configuration, and private vulnerability reporting under [security.md](security.md), without secret values. Record business/service regions and existing policies under [legal.md](legal.md); assess applicable notices before real personal-data collection, including pre-launch. Identify existing commercial decisions under [pricing.md](pricing.md) and customer-facing pages under [marketing.md](marketing.md). Adoption does not authorize replacing live policies or offers.
5. Configure maintenance under [updates.md](updates.md), recording schedule, coverage, checks, runner/run links, and gaps. Distinguish active-agent work from verified unattended automation; record package rationale.
6. Record blueprint revision, local exceptions, and accessible skill locations in `AGENTS.md`. Verify installed discovery or explicit reading from a retained blueprint checkout. Application domains and provider details belong in project docs, not the reusable blueprint.

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
