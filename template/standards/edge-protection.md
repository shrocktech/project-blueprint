# Edge and App Protection

Apply alongside [security.md](security.md) to self-hosted web applications reached through Cloudflare and a reverse proxy. This guide covers how an application is exposed to the internet and protected in front of its own code: Cloudflare Tunnel, Cloudflare Access, a web application firewall (WAF) in the reverse proxy, Cloudflare edge rules, automatic bans, and the admin view that ties them together. Form-level protections stay in [Forms and untrusted input](security.md#forms-and-untrusted-input). Keep account IDs, list IDs, rule IDs, tokens and deployment hostnames in private `docs/internal/`.

Reference stack: Cloudflare (the Free plan is enough), `cloudflared`, Caddy with the Coraza WAF module and the OWASP Core Rule Set (CRS), a small root-run report and ban job, and an admin page in an existing authenticated application. Equivalent tools are fine when they satisfy every rule below. Projects on managed hosting, static hosting or a provider's platform record `Edge protection: not applicable` and the reason in `AGENTS.md`.

## Scope and phases

Tunnels, the proxy firewall, edge rules, the ban job and the admin view are host-level: set them up once per host or provider account, and have each project reference that setup rather than building its own. A project runs the [per-app checklist](#per-app-checklist) and records the shared protection it relies on. Changing shared host or account configuration needs authority for that host, not only for the project.

| When | What applies |
| --- | --- |
| Any hostname reachable from the internet, including development | Tunnel route to the proxy only, HTTPS, the application's own login, Access on staff and development sites, secret handling |
| From `DEVELOPMENT: security` | WAF imported in log-only mode, scanner-path edge rule, exceptions tuned |
| Before public launch | WAF blocking after the rollout below, bypass test, monitoring check |
| Once per host or account | Ban job, admin view, geolocation data |

## Principles

- **No open inbound ports.** Applications are reached only through an outbound-only Cloudflare Tunnel. The origin firewall allows no inbound HTTP or HTTPS from the internet; management ports and admin interfaces are never internet-facing.
- **One front door.** Every tunnel hostname routes to the reverse proxy, never straight to an application container. A route that bypasses the proxy bypasses the WAF; prove it under [Verification](#verification).
- **Defense in depth, in order:** edge rules and bans, then Access for staff applications, then the WAF in the proxy, then the application's own authentication, authorization and input validation. No layer replaces the application's own checks.
- **Never break real users.** New blocking starts in log-only mode, exceptions are narrow, and rollback is one line. When unsure, log rather than block.
- **Counts, not content.** WAF logs can contain what a person typed, such as a mistyped password. Logs stay root-only; dashboards, emails, issues and chat show counts, categories and paths without query strings, never matched values.

## Exposure and tunnels

- Run each tunnel with at least two connectors on different hosts, as services rather than foreground processes, so one connector dropping does not take the application offline. Watch HTTP 530 counts after any connector change.
- Keep tunnel tokens in the secret manager and in root-only service environment files (mode `600`), never on command lines visible in process listings. Rotate an exposed token on every connector.
- Hostnames that serve only the local network still go through the proxy and redirect HTTP to HTTPS. Local clients that resolve straight to the proxy bypass Cloudflare entirely, so every application enforces its own authentication; Access is never the only gate.
- Record the routing table (hostname, proxy, application) in private docs and back it up before each change. Tunnel configuration updates cut open streams; schedule them like proxy reloads.

## Identity in front of staff apps

- Put staff-only applications behind Cloudflare Access using only the organization's identity provider. Remove the email one-time-PIN method: it admits anyone with a mailbox at an allowed domain, including shared and former-staff mailboxes.
- Policies for admin tools name groups or explicit people, not whole email domains. Review membership when people leave.
- Exclude machine routes from Access and give them their own authentication: signed webhooks, OAuth and MCP endpoints, unsubscribe links, public forms and health checks. Agents and integrations cannot complete an interactive login.
- Before placing an identity or gate service behind Access, switch every application that calls it server-to-server to reach it over the local network, then verify each one. Otherwise moving the gate locks those applications out.
- A form that must stay public belongs in a public application with [form protections](security.md#forms-and-untrusted-input), not in an exception to a staff application's Access policy; redirect existing links.

## WAF in the reverse proxy

- **Install:** build Coraza or an equivalent with the OWASP CRS into the proxy image, on the latest versions. Automatic image updaters cannot see a locally built image, so rebuild on a recorded schedule and after upstream security releases, and record the installed versions.
- **Per-site switch:** every site imports one shared snippet with two arguments: the mode (`DetectionOnly` or `On`) and that site's own exceptions. Never switch a rule off for all sites to quiet one application.
- **Safe defaults,** replacing the stock recommended configuration where it differs:
  - Inspect the first 32 KB or so of form, JSON and XML bodies and let the rest stream through; never reject a request for size. A payload placed beyond that limit is not inspected, so the application's own validation remains required.
  - Do not parse binary bodies such as video, PDF and images as form fields.
  - Do not buffer response bodies, so streaming, downloads and WebSockets keep working.
  - Turn the WAF's full audit log off, because it stores submitted fields including passwords. Keep only the matched-rule log, root-only and rotated under [data retention](updates.md#update-policy).
  - Allow the HTTP methods the applications use, such as `PUT`, `PATCH` and `DELETE` for JSON APIs.
  - Trust client IP headers only from Cloudflare through your own tunnel.
- Bearer-token API routes may stay outside the WAF when the application authenticates every request; document each such route.
- Reloads close WebSockets. Schedule planned reloads and proxy redeployments outside business hours. Returning a site to log-only because users are blocked happens immediately, at any hour.

### Rollout per app

1. Start every new site in `DetectionOnly`.
2. Review the matches regularly. Separate scanners (unknown internet addresses probing paths such as `/.env`, `/.git` and `wp-*`) from legitimate traffic (local sources, signed-in routes, saves, uploads and webhooks).
3. For each real false positive, add the narrowest exception in that site's block: one rule plus one route, or one rule plus one field or cookie. Give custom rules their own ID range and record each with the reason and before/after evidence.
4. Before any site blocks, exempt its signed session and token cookies from the file-name and path rules, one rule and one cookie at a time. Random signed values occasionally contain strings those rules match and would lock that user out on every request.
5. Switch a site to `On` after at least seven days with no unexplained hits from local sources, saves or uploads. Start with simple read-only sites, and switch at most three sites in one session, outside business hours.
6. After switching, confirm the [bypass test](#verification) and review that site's blocked requests the next day. If a real user or integration is blocked, return the site to `DetectionOnly`, record it, then fix the exception.

## Edge rules

- Block known scanner paths at the edge so they never reach the origin: `/.env`, `/.git`, `/.svn`, `/.aws/`, `/.ssh/`, `/.vscode/`, `.php`, `/wp-admin`, `/wp-login`, `/wp-content`, `/wp-includes`, `/xmlrpc`, `/phpmyadmin`, `/cgi-bin/`, `/.htaccess` and `/.htpasswd`. Match on the lower-cased path.
- Scope the rule to application hostnames. Before enabling it, review at least a week of edge traffic for those paths with successful responses, per hostname. Exclude hostnames that legitimately use them, such as a WordPress site, and never block `/.well-known/`.
- Applications that answer 200 to every unknown path make scanner hits look like successes in analytics; confirm with a known-nonexistent path before treating a 200 as a leak.
- Scanners finish a sweep in under a minute, so blocking by path does more than blocking by address.

## Automatic bans

- **Mechanism:** a Cloudflare account IP list plus one zone rule that blocks addresses on it, applied to all hostnames. A job adds offenders to the list and the edge refuses them.
- **Evidence counted:** requests refused by the scanner-path edge rule, plus WAF matches whose target is the request path itself. Never count cookie, header or form-field matches; a real user's random cookie must not get them banned.
- **Threshold and duration:** ten or more probes from one internet address within an hour bans it for 90 days, then the ban lifts automatically. Avoid permanent bans: scanner addresses are rented servers that get reassigned, and list sizes are capped.
- **Never ban** private addresses, the organization's own public addresses (resolve dynamic ones each run), shared egress such as Cloudflare WARP and Apple iCloud Private Relay (exempt by network owner), or any address an admin unbanned.
- **Guard rails:** cap new bans per run, provide a file-based kill switch that stops new bans and a dry-run mode, and dry-run any backfill over past logs before applying it.
- **Credentials:** use a dedicated API token scoped to the ban list and read-only zone analytics, stored under [secret handling](security.md#local-development-secrets). Never use an account-wide key in a job.
- On the Free plan, aggregated firewall-event queries are unavailable; poll raw firewall events with a look-back window and de-duplicate by ray ID.

## Admin view and unban

- Put a firewall overview inside an existing admin-only application rather than a new public hostname. Check the role server-side on every route; the data endpoint returns 401 without a session.
- A root-run job writes a counts-only summary to a read-only mount. The page never reads the WAF log.
- Every section follows one period filter, including the banned list. Show suspicious requests, distinct sources, blocked and banned counts, hits from local sources (expected to stay at zero), activity over time, most-hit sites, what attackers seek in plain categories, country of origin, and the busiest sources with network owner.
- Keep geolocation local: use a downloaded IP-to-country and IP-to-network database with its required attribution shown, not a per-request lookup service. Label it as the server's location, not the person's.
- Unban is immediate: the control removes the address from the edge list and waits for the provider to confirm, records who and when on a never-ban list the ban job honors, and offers to allow banning again. State-changing endpoints follow [form protections](security.md#forms-and-untrusted-input) and validate the address server-side.
- A periodic check proves each blocking site still refuses the test attack at the proxy and through the edge, and alerts the admin when a request from a local source, a save or an upload was blocked.

## Per-app checklist

Run for every new or adopted application before it gets a public hostname, completing each item at the phase set in [Scope and phases](#scope-and-phases). Record results privately.

| Item | Done when |
| --- | --- |
| Tunnel route to proxy | The hostname resolves through the tunnel to the proxy; no direct application route exists |
| HTTPS and local path | HTTP redirects to HTTPS; local access still requires the application's login |
| Access decision | Staff-only sites use Access with the identity provider only; public and machine routes are listed and excluded with their own authentication |
| WAF import | The site block imports the WAF snippet in `DetectionOnly` with an empty exception list |
| Session cookie exception | Signed session and token cookie names are identified and exempted from path and file rules before `On` |
| Edge path rule | The hostname is covered by the scanner-path rule, or listed as an exemption with the reason |
| Application authentication | Server-side authentication and authorization apply on every route, including admin APIs |
| Public forms | [Form protections](security.md#forms-and-untrusted-input) are verified |
| Service credentials | Keys are per-application and least-privilege; read-only accounts are verified unable to write |
| Secrets | Stored in the secret manager and synced to the deployment; none in Git, logs or pages |
| Monitoring | The site appears in the firewall overview; the 403 check runs once it blocks |
| Change record | WAF, edge and Access changes are recorded with date, site, reason and before/after evidence |

## Verification

- **Before and after every proxy change:** request every hostname from inside and outside the network and compare status codes; the two runs must match. Validate the configuration in a copy before reloading.
- **Bypass test:** for each blocking site, a harmless test attack such as `?id=1' OR '1'='1`, with a marker the reports exclude, returns 403 both at the proxy and through the Cloudflare edge. A success response through the edge means a route skips the proxy.
- **Edge rule test:** scanner paths return 403 on application hostnames; exempt sites, sign-in pages and `/.well-known/` still answer normally.
- **Ban test:** add a documentation-range address such as `198.51.100.1` to the list, unban it from the admin view, and confirm the provider list no longer contains it.
- Keep evidence as counts, timestamps and status-code tables in private docs, never matched values.
