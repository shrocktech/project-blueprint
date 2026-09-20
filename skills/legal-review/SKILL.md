---
name: legal-review
description: Assess and draft concise application terms and privacy policies for the project's actual jurisdictions and practices. Use for initial policies, material data-handling or customer-term changes, or applicability questions; not routine edits with no policy impact.
---

# Review Application Terms and Privacy

Confirm the target project. Plain filenames refer to its instructions, not files beside this installed skill; during adoption use the blueprint's template equivalents. Read `legal.md` and relevant `documentation.md` rules. Reviews do not start implementation queue work; authorized edits follow `git-workflow.md`.

## Establish facts first

Inspect existing policies, code, configuration, provider documentation, and recorded business decisions before interviewing the owner. Preserve approved commitments and effective versions. Use synthetic data, not customer records, to verify behavior.

Keep a compact private record in `docs/internal/` covering:

- Business identity and locations, customer/service regions, audience/ages, and verified contact channel.
- Data collected directly and automatically (including logs), purposes, processors/recipients, tracking/analytics, retention/backups, deletion, and implemented privacy controls.
- Accounts, payments, renewals/cancellation, refunds, customer content, and other product terms that actually apply.

Mark unknowns instead of inventing facts, contacts, residency, retention periods, or capabilities. Ask only material missing questions, one at a time, with a recommended answer and useful alternatives. Reuse existing owner decisions; do not ask for approval of routine accurate wording.

## Determine what applies

Use the jurisdictions recorded in project docs and examine actual operations, targeting, customer locations, processing, and transfers. Research relevant national, state/provincial, regional, and sector rules, including thresholds, age definitions, and exemptions. Never assume one country's rules apply everywhere or that a contract's governing-law clause removes other mandatory protections. Exemption from one law does not establish exemption from all disclosure duties.

Use current official statutes, regulators, and authoritative decisions. Record source links, effective/review dates, applicability rationale, and uncertainties privately; distinguish binding requirements from guidance and proposals. Do not add unsupported geographic restrictions or assume small scale removes every obligation.

Apply the review triggers and approval rules in `legal.md`. Assess the whole data flow and actual behavior, including recurring billing/cancellation, messaging consent and opt-outs, SMS STOP/HELP where applicable, and marketing-email unsubscribe handling. Check both applicable law and provider rules. Resolve material questions before dependent publication/activation while continuing independent work; do not certify compliance.

## Draft and verify

Prepare only relevant documents in `docs/public/legal/`, retaining existing routes where appropriate. Use short headings and plain language; no target word count overrides a required disclosure. Separate privacy explanations from contractual terms. Adapt reference material only when its license permits it; do not import another company's facts or commitments. Paid generators and outside skills are optional, not prerequisites.

Check promises against observed behavior and approved decisions. Explain actual disclosures, tracking, and deletion limits without absolutes. Do not invent warranties, refund rules, governing jurisdiction, dispute terms, or liability limits. Present missing material choices with a recommendation; record policy-version approval from the authority defined in `AGENTS.md` under `legal.md`.

Identify drafts as unpublished and exclude them from published builds until authorized. Verify working policy/contact links, required placement before collection or purchase, applicable notice/consent or acceptance mechanisms, and that implemented privacy choices work. A policy page alone does not implement those controls. Use the actual effective date/version; preserve a record of published versions and acceptance where applicable. Do not use revised wording as retroactive permission for new data uses.

Deliver a brief linked result: drafts or approved pages, verified facts/controls, and only outstanding decisions or legal questions. Update affected private/public docs with the issue. Publish through the existing release process; changing instructions or preparing a draft does not authorize production changes.
