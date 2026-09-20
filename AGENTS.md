# Blueprint Repository Instructions

This repository maintains reusable project instructions. Read [README.md](README.md) for its layout and owner workflow. This root file governs blueprint maintenance; `template/AGENTS.md` is application payload. Edit its placeholders and guides as content rather than executing application setup here, except for rules explicitly adopted below.

Start sessions at the repository root and verify active instruction sources. Correct the session scope if a tool loads payload as maintenance guidance. This convention does not override nested-file discovery or precedence.

## Commands and verification

- No application installation, build, or runtime tests apply here.
- Review the diff and run `git diff --check` (or `git diff --cached --check`).
- Verify all relative Markdown links in both this repository and a copied `template/` directory.
- For skill edits, validate frontmatter and relevant references; verify that target-project filenames are not incorrectly resolved relative to the installed skill.
- For label-helper edits, preview with `pwsh -File scripts/setup-labels.ps1 -Repo OWNER/REPO -WhatIf` or `bash scripts/setup-labels.sh OWNER/REPO --dry-run` (requires jq). Resolve the target repository from the checkout, validate the helper, and verify authorized GitHub changes.

## Working rules

Use [template/git-workflow.md](template/git-workflow.md) for issues, tracking, live queues, and completion. This documentation repository uses only `main`: work in an owned isolated checkout or detached worktree based on `origin/main`, synchronize and verify, then push commits to `main` without force. Never create `develop` or publish additional branches here. Application branch and deployment rules belong to adopting projects. Questions and reviews do not start queue work.

Use the 90% judgment guideline and autonomous-work boundaries in [template/AGENTS.md](template/AGENTS.md); it is not a measured probability. Follow [template/security.md](template/security.md) for credentials and data. Read other templates only when changing their subject matter.

Keep all distributed files generic: no personal, company, account, repository, or application identities. Use placeholders; adopting projects record their own configuration, authority, and jurisdictions. Keep blueprint-maintenance notes outside `template/`. Maintain consistent README instructions, labels, and authorized autonomy. Verify integration into `main`, then close the issue with only `COMPLETED`.

All blueprint requirements must support GitHub Free for public and private repositories. Never require a plan upgrade, billed usage, or public visibility; document verified free alternatives.

Write templates and skills as current instructions for a first-time reader. Exclude revision narratives, prior decisions, and compatibility notes about earlier blueprint drafts.

Prefer tightening existing text and removing duplication over adding sections. Keep each rule in one place with task-specific pointers. Add a guide only for a distinct purpose an existing guide cannot serve clearly; record that reason in the issue. Preserve required behavior when trimming.
