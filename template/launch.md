# Launch Checklist

Use this checklist when the application is ready to go live. Routine development and internal prereleases do not require a customer changelog or public documentation site. Follow [git-workflow.md](git-workflow.md), [documentation.md](documentation.md), and [security.md](security.md).

For an already-live product, use this checklist for subsequent releases under [git-workflow.md](git-workflow.md). Preserve release history; adoption uses the `adopt-existing` skill and does not repeat first-launch setup.

## Prepare the first public launch

- **Release scope:** Record the launch issue, intended version, included features, known limitations, and verification results. Confirm launch authorization before promoting to production.
- **Release testing:** Test the recorded candidate on `develop.<domain>` or an isolated candidate preview under [project.md](project.md), keeping it stable during final checks. Staging is optional; use `staging.<domain>` only if explicitly requested and active. Do not provision staging as a launch prerequisite. Verify that the authorized production deployment uses the tested candidate.
- **Customer documentation:** Prepare the initial `docs/public/` set from reviewed technical docs: getting started, core tasks, and where to get help. Include installation or configuration instructions when relevant. Check that it describes the version being launched and contains no internal-only content.
- **Marketing and commercial consistency:** Under [marketing.md](marketing.md) and [pricing.md](pricing.md), verify landing pages, pricing pages, checkout, billing configuration, customer docs, and approved policies agree with the release. Confirm commercial decisions and test the advertised journey before activation. Repeat for each release affecting the offer.
- **Customer terms and privacy:** Follow [legal.md](legal.md). Verify applicable policies in `docs/public/legal/` match the release, have authorized terms and effective dates, and are linked where needed. Test applicable notices, consent/acceptance, and privacy controls; exclude unfinished drafts. Required disclosures must be ready before the corresponding collection or transactions, including any pre-launch waitlist/beta.
- **Administrator documentation, when needed:** Prepare `docs/admin/` for the released administration tasks. Build its documentation separately from that folder, verify its links and intended access, and keep restricted pages/assets out of public output. Skip this set when the product needs no separate administrator guide.
- **Customer changelog:** Create `CHANGELOG.md` during final go-live preparation and publish it at launch. Begin with the initial version, release date, and a short customer-readable summary. Do not reconstruct the development history or publish internal issue notes.
- **Release record:** Prepare the initial versioned release and its notes. Once the approved, tested changes reach `main`, tag the exact release commit and publish the release record. Keep its version and summary consistent with the changelog.
- **Customer links:** Provide stable links to documentation, the changelog, and the release details from the website or app where appropriate. A single changelog page may also serve as the release-notes page. If GitHub releases are private, publish the customer-safe notes on the website or docs instead of sending customers to an inaccessible link.
- **Operational readiness:** Verify production configuration, the critical user journeys, and the deployment/rollback procedure. Confirm backups and recovery for persistent data where applicable. Record project-specific checks in private `docs/internal/`.

## Go live and verify

Deploy the authorized release from `main` and publish the matching customer docs and applicable policies from `docs/public/`, administrator docs from `docs/admin/` when applicable, and changelog. Verify the live application and documentation links using the intended access levels, including denial of unauthorized access to restricted admin docs. Keep internal documentation private. Record the deployed version, documentation destinations, verification results, and any blockers in the launch issue before closing it.

## After launch

Maintain the changelog and applicable customer/administrator documentation as specified in [documentation.md](documentation.md). Publish only released entries; keep `Unreleased` drafts out of customer-facing output. Each later release should have a version, date, relevant customer notes, and working links. Keep this checklist short and add project-specific steps only when needed.
