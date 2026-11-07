---
name: changelog
description: Assess customer impact at application issue completion, draft notable changelog entries, and audit an exact public release candidate against the previous public release.
---

# Application changelog

Work from the application root. Its `documentation.md` governs the lifecycle, migration and publication of `project/CHANGELOG.md`. Follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/): keep the working `Unreleased` section first, released versions newest first, and use only populated categories (Added, Changed, Deprecated, Removed, Fixed, Security).

## Completing an issue

Inspect the issue's verified outcome and final diff. Would a customer notice different behavior or need to take action? After go-live, add or refine one concise entry per distinct outcome under `Unreleased` before integration. Combine related commits and reconcile concurrent entries. Skip internal cleanup and formatting. For breaking changes, name the affected behavior and migration step. Describe security fixes in disclosure-safe terms.

During initial development and private beta, keep evidence in the issue until the changelog is due. Preserve any existing changelog and its drafts under the project's migration rules.

## Auditing a public release

1. Identify the previous public release commit and exact candidate. Inspect their full diff and intervening history, including reverts. Cross-check completed issues and tests against what customers can actually use. For the first public launch, summarize verified capabilities. If an existing product's baseline is uncertain, report the coverage gap.
2. Reconcile the candidate with the draft in both directions: add missing outcomes, combine duplicates, correct unsupported claims and keep future work separate. Preserve published entries and dates. Record the compared commits and any unresolved discrepancies in the release issue.
3. For an authorized release, group only included entries under the release version and date (`YYYY-MM-DD`). Verify migration instructions, links and rendered customer output. Derive release notes from the same entries and exclude private evidence and unreleased drafts. Follow the application's `launch.md` and release authority for tagging and publication.
