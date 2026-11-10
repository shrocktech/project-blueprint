---
name: interface-design
description: Plan new interfaces or scoped redesigns, implement or review pages and forms using the project's UI stack. Use for design interviews, responsive layouts, navigation, icons, shared controls and action feedback.
---

# Interface Design

Read the target project's `AGENTS.md` and `design/README.md`; filenames refer to that project, not this skill directory. Use the recorded blueprint source/revision if guidance is missing. Apply `design/README.md` to the requested pages. For review-only tasks, report findings without edits or submissions.

## Establish the pattern

For a new visual direction or requested redesign, follow the target project's `design/README.md` Design interview before implementation; use selected tools through `standards/optional-tools.md`. Routine screen work reuses approved choices without repeating the interview. Identify the existing shared controls and their source paths before building; implement missing controls within the approved UI foundation.

Inspect nearby screens, shared components, icon mappings, spacing tokens, validation, and notifications. Sketch the requested content using those conventions, for example:

```text
Page title                              Optional page actions
Short context, only when useful

Section title
[Related short field] [Related field] [Related field]
[Long or complex field spanning the available width]
[ ] Option with an associated label

Result/status                           Cancel | Save
```

Adapt the example to the task's content and actions; it is an application-form pattern, not a universal screen structure.

Before implementation, map the action states in `design/README.md` to the application's data source, form/state utilities, validation boundaries, and expected result. Select an authorized test environment and synthetic data.

## Verify the rendered result

Use the project's required Playwright setup, official `playwright-cli` skill at its verified location, and recorded commands under `standards/project.md` to exercise affected user journeys with synthetic data. Follow the target agent's supported browser-tool access rules. Run relevant existing tests and add repeatable regression coverage for important changed behavior. Inspect the rendered browser or captured screenshots as well as assertions; automated passes alone do not establish visual correctness.

Use the device coverage required by `standards/security.md` checks by phase and the desktop/tablet/mobile matrix in `design/README.md`, including intermediate widths and both sides of affected breakpoints. Configure device/touch behavior as well as viewport dimensions; inspect portrait/landscape changes, zoom, wrapping labels, helper text, and errors. Compare spacing, alignment, overflow, and reading/tab order against the design rules. Exercise menus, dialogs, and essential actions at each device class; a screenshot of the initial page alone does not verify interaction states. Correct defects within implementation scope and rerun affected checks.

For affected menus, features, or checkout, check icons in supported themes and collapsed navigation. Verify provider asset terms and payment/security cues against the real integration.

Exercise the form against the state table in `design/README.md`: try edits/reverts, incomplete inputs, paste/autofill, repeated click/Enter, delayed/failed responses, and edits during pending requests. Observe status messages, request counts, retained drafts, and persisted results, including recovery after an uncertain outcome. For credential fields, exercise the credential states in `design/README.md` with synthetic secrets: saved masking and exact key length, eye reveal/hide, direct overwrite, unchanged/empty preservation, successful/failed saves, and navigation without saving. Verify masks never become submitted secrets and stored-secret reveal is authorized.

Check keyboard navigation, label activation, error associations, focus, and status announcements. Confirm persistence by reloading or reading back through the application. Report unavailable checks explicitly; source inspection or a passing build does not constitute visual verification.

For implementation, record affected patterns and exceptions in the project's internal docs with the tested routes/states, browser/device settings, candidate, and visual/assertion evidence. Distinguish emulation from physical-device checks and report verification gaps; do not claim untested device classes pass.

## References when needed

Use applicable guidance for the established stack; upstream examples do not override project requirements or authorize framework replacement.

- [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines): interaction and visual-review guidance; select relevant principles, not brand-specific preferences.
- [Lucide accessibility guidance](https://lucide.dev/how-to/accessibility): icon labels, controls, and decorative handling.
- [shadcn Field](https://ui.shadcn.com/docs/components/field): field composition in compatible projects.
- [Bootstrap form layouts](https://getbootstrap.com/docs/5.3/forms/layout/) and [Tabler forms](https://docs.tabler.io/ui/forms): existing Bootstrap/Tabler interfaces.
- [WAI form validation](https://www.w3.org/WAI/tutorials/forms/validation/) and [status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html): accessible errors and action feedback.
