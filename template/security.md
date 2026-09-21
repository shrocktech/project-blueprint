# Security Defaults

Apply alongside [AGENTS.md](AGENTS.md). Keep implementation details and reporting procedures in private `docs/internal/`, without secret values.

- **Secrets and logs:** Never commit credentials or expose them in logs, errors, screenshots, issue reports, URLs, or client bundles. Keep customer content and personal information out of diagnostic outputs. Examples use placeholders; review staged changes.
- **Test data:** Use synthetic data by default. Production data requires explicit authorization and documented safeguards. Separate development/test resources from production.
- **Access:** Use credentials proactively within approved scope and least privilege. Enforce authentication, ownership, tenant boundaries, and authorization server-side; test allowed and denied cases. Do not disable controls or request blanket administrator access to make a task pass.
- **Reporting:** Use the documented private vulnerability channel. If missing, ask privately; do not invent a contact or publish sensitive evidence. An exposed secret requires notification and authorized revocation/rotation; deleting its visible text is insufficient.

## Credential storage

- Hash login passwords with the supported framework's salted adaptive password APIs; prefer Argon2id for new custom authentication where supported. Preserve WordPress's native APIs and upgrade path. Never store plaintext/reversible login passwords or use a fast general-purpose hash. Offer reset/change, not retrieval.
- Protect recoverable provider secrets with existing secret storage or a maintained authenticated-encryption library. Follow its key generation/nonce requirements; do not invent cryptography. Tokens needed only for local verification may use an appropriate non-recoverable verifier. Masking and encoding are not encryption.
- Keep encryption keys separate from credential records and database backups, outside source control, web roots, and bundles. Limit decryption to authorized server operations; fail closed on missing keys or failed authentication. Document key versions, rotation, protected backup/recovery, and any existing gaps. Do not casually rotate unrelated framework keys/salts.
- Use HTTPS. Normal settings responses expose presence/status only, never saved secrets or ciphertext for browser decryption. Do not persist secrets in browser storage. Enforce the keep/replace/remove behavior defined in [design.md](design.md) on the server; presentation is not an access control.
- Stored-secret reveal needs an explicit product requirement, recoverable credentials, server-side user/tenant checks, recent authentication where warranted, no response caching, audit events without secret values, and prompt clearing. It must never happen while merely loading settings.
- Verify with synthetic credentials: password verification or encryption round-trip/tamper rejection, authorization, state changes, and absence of leaks in responses/logs/browser storage. Existing storage migrations are deliberate tested work, not a blueprint-adoption side effect.

Use current [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) and [cryptographic storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) guidance. Follow [packages.md](packages.md) and [updates.md](updates.md) for dependency security; production secrets stay out of update-test and merge jobs.

## Security review

Define security/data requirements during `specs` and implement them during `build`. Complete the review at `DEVELOPMENT: security`; security remains ongoing through `PRODUCTION`. Verify applicable protections before collecting real customer data, including waitlists. Use applicable requirements from the latest stable [OWASP ASVS](https://github.com/OWASP/ASVS) and stack/provider guidance.

- **Data and promises:** Trace collection, storage, APIs/vendors, logs, backups, retention, export, and deletion. Verify actual behavior against policies, documentation, and marketing under [legal.md](legal.md) and [offering.md](offering.md). Data-practice changes require policy-impact review; resolve mismatches before the corresponding collection or publication without silently weakening approved commitments.
- **Accounts and administration:** Test authentication, administrator MFA, sessions, recovery, least privilege, and denied role/tenant access, including admin APIs and background operations.
- **Application and infrastructure:** Review code, dependencies, credential handling, API/input/upload protections, hosting/storage configuration, repository/CI/deployment access, backups, and recovery. Combine automated checks with code/configuration review and allowed/denied behavior tests in authorized environments.
- **Abuse prevention:** Verify rate limits, login throttling, security alerts, and appropriate IP restrictions under [OWASP authentication guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html). Include account-based protections; shared/changing IPs make blanket bans insufficient and risk legitimate-user lockouts. Test recovery and proxy-derived IP handling where applicable.

Record the date, candidate/configuration, reference versions, scope, requirement coverage, evidence, severity, justified exclusions, unresolved risks, fixes, and retests in private `docs/internal/`. Missing required checks remain unverified; a clean scan alone is insufficient.

Unresolved critical/high findings or unverified required controls block beta or release. During `RELEASE: validation`, recheck controls affected by beta fixes and verify final offering/data claims. Repeat affected checks for later changes; phase completion never authorizes deployment.
