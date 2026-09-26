# Security Defaults

Apply alongside [AGENTS.md](AGENTS.md). Keep implementation details and reporting procedures in private `docs/internal/`, without secret values.

- **Secrets and logs:** Never commit credentials or expose them in logs, errors, screenshots, issue reports, URLs, or client bundles. Keep customer content and personal information out of diagnostic outputs. Examples use placeholders; review staged changes.
- **Test data:** Use synthetic data by default. Production data requires explicit authorization and documented safeguards. Separate development/test resources from production.
- **Access:** Use credentials proactively within approved scope and least privilege. Enforce authentication, ownership, tenant boundaries, and authorization server-side; test allowed and denied cases. Do not disable controls or request blanket administrator access to make a task pass.
- **Reporting:** Use the documented private vulnerability channel. If missing, ask privately; do not invent a contact or publish sensitive evidence. An exposed secret requires notification and authorized revocation/rotation; deleting its visible text is insufficient.

## Secret scanning

Secret scanning is required infrastructure. Use [Betterleaks](https://github.com/betterleaks/betterleaks) for new setups; preserve verified existing Gitleaks coverage during adoption rather than disabling it. Follow current upstream installation and [scanning guidance](https://github.com/betterleaks/betterleaks/blob/main/docs/scanning.md).

- Install a verified official release and record its version, configuration, and commands in project setup docs, with commands linked from `AGENTS.md`. Scan working files and repository history during setup; fetch the history needed for the recorded scope rather than treating a shallow checkout as complete coverage.
- Install and verify a staged-change pre-commit check without replacing Graphify or other hooks. Before integration, independently scan the exact candidate's files and incoming commit history; hooks alone do not establish a pass. Findings or scan errors block delivery until resolved or narrowly adjudicated below. Missing/skipped checks are not passes.
- Verify detection and a failing check with a harmless synthetic secret fixture in an isolated temporary test repository, then verify clean input passes. Never use real credentials or commit the fixture to the application repository.
- Enable redacted output and keep findings/reports private; never paste secret values into issues, logs, or shared artifacts. Investigate every finding. Allow only narrow, documented false-positive or confirmed revoked-secret exceptions; never blanket-baseline unresolved credentials. Handle exposed secrets under the reporting rule above. History rewriting requires separate authorization.
- Keep live credential validation disabled by default; provider requests require authorization for that scope. Maintain the scanner and review rule changes under [updates.md](updates.md), retesting detection after changes. Use its CLI locally and in authorized CI within existing resource limits; neither paid services nor uploaded security reports are prerequisites. Record automation gaps and retain local checks when CI is unavailable.

## Credential storage

- Hash login passwords with the supported framework's salted adaptive password APIs; prefer Argon2id for new custom authentication where supported. Preserve WordPress's native APIs and upgrade path. Never store plaintext/reversible login passwords or use a fast general-purpose hash. Offer reset/change, not retrieval.
- Protect recoverable provider secrets with existing secret storage or a maintained authenticated-encryption library. Follow its key generation/nonce requirements; do not invent cryptography. Tokens needed only for local verification may use an appropriate non-recoverable verifier. Masking and encoding are not encryption.
- Keep encryption keys separate from credential records and database backups, outside source control, web roots, and bundles. Limit decryption to authorized server operations; fail closed on missing keys or failed authentication. Document key versions, rotation, protected backup/recovery, and any existing gaps. Do not casually rotate unrelated framework keys/salts.
- Use HTTPS. Normal settings responses expose only presence/status and permitted API-key previews to authorized credential managers; never return full saved secrets or ciphertext for browser decryption. Do not persist secrets in browser storage. Enforce [design.md](design.md)'s keep/replace/remove behavior server-side; presentation is not access control.
- Generate display-only API-key preview metadata server-side during saving; bind it to the confirmed credential and replace/clear it with that credential. Never decrypt existing secrets merely to populate settings. Allow fragments only for documented key formats with sufficient unpredictable content remaining hidden and provider rules permitting disclosure; short, unknown, or unsuitable keys return no preview. Never expose overlapping fragments, full keys, or original lengths. Passwords never have partial previews.
- Full stored-secret reveal needs an explicit product requirement, recoverable credentials, server-side user/tenant checks, recent authentication where warranted, no response caching, audit events without secret values, and prompt clearing. It must never happen while merely loading settings.
- Verify with synthetic credentials: password verification or encryption round-trip/tamper rejection, authorization, state changes, preview fallback/synchronization and denied cross-user/tenant access, and absence of unintended leaks in responses/logs/browser storage. Existing storage migrations are deliberate tested work, not a blueprint-adoption side effect.

Use current [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) and [cryptographic storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) guidance. Follow [packages.md](packages.md) and [updates.md](updates.md) for dependency security; production secrets stay out of update-test and merge jobs.

## Security review

Define security/data requirements in `planning`, implement during `build`, and review at `DEVELOPMENT: security`; continue through `PRODUCTION`. Verify protections before real customer-data collection, including waitlists. Use applicable requirements from latest stable [OWASP ASVS](https://github.com/OWASP/ASVS) and current stack/provider guidance.

- **Data and promises:** Trace collection, storage, APIs/vendors, logs, backups, retention, export, and deletion against policies, docs, and marketing under [legal.md](legal.md) and [offering.md](offering.md). Review policy impacts of data-practice changes; resolve mismatches before collection/publication without silently weakening approved commitments.
- **Accounts and administration:** Test authentication, administrator MFA, sessions, recovery, least privilege, and denied role/tenant access, including admin APIs and background operations.
- **Application and infrastructure:** Review code, dependencies, credentials, API/input/upload protections, hosting/storage configuration, repository/CI/deployment access, backups, and recovery. Combine automated checks, code/configuration review, and allowed/denied tests in authorized environments.
- **Abuse prevention:** Verify rate limits, login throttling, alerts, and appropriate IP restrictions using [OWASP authentication guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html). Include account-based protections; shared/changing IPs undermine blanket bans and risk legitimate-user lockouts. Test applicable recovery and proxy-derived IP handling.

Record date, candidate/configuration, reference versions, scope, coverage, evidence, justified exclusions, risks, fixes, and retests in private `docs/internal/`. A clean scan alone is insufficient. Rate findings with [OWASP risk rating](https://community.owasp.org/OWASP_Risk_Rating_Methodology), recording likelihood, impact, assumptions, and rationale. Reclassification requires evidence; never lower severity merely to pass.

Unverified required controls or unresolved critical/high findings block beta/release. Only the owner may accept a specific finding in writing: privately record its severity, release/environment scope, rationale, compensating controls, remediation tracking, review/expiry date, and approval reference. Acceptance waives only that finding while valid; preserve its severity and unresolved status. Reassess at the recorded date or when scope/conditions change. Agents cannot accept risks. Acceptance cannot turn missing checks into passes, weaken customer commitments, or authorize deployment.

During `RELEASE: validation`, recheck beta fixes and final offering/data claims. Repeat affected checks for later changes.
