---
name: interface-design
description: Plan, implement, or review compact application pages and forms using the project's established UI stack. Use for layout, icons, alignment, responsive form structure, or action-feedback work.
---

# Interface Design

Read the target project's `AGENTS.md` and `design.md`; filenames refer to that project, not this skill directory. Use the recorded blueprint source/revision if guidance is missing. Apply `design.md` to the requested pages. For review-only tasks, report findings without edits or submissions.

## Establish the pattern

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

Before implementation, map the action states in `design.md` to the application's data source, form/state utilities, validation boundaries, and expected result. Select an authorized test environment and synthetic data.

## Verify the rendered result

Inspect the rendered page at desktop and narrow mobile widths, with zoom, wrapping labels, helper text, and errors. Compare spacing, alignment, overflow, and reading/tab order against `design.md`. Correct defects within implementation scope.

For affected menus, features, or checkout, check icons in supported themes and collapsed navigation. Verify provider asset terms and payment/security cues against the real integration.

Exercise the form against the state table in `design.md`: try edits/reverts, incomplete inputs, paste/autofill, repeated click/Enter, delayed/failed responses, and edits during pending requests. Observe status messages, request counts, retained drafts, and persisted results, including recovery after an uncertain outcome. For credential fields, exercise saved/replace/cancel/remove states with synthetic secrets.

Check keyboard navigation, label activation, error associations, focus, and status announcements. Confirm persistence by reloading or reading back through the application. Report unavailable checks explicitly; source inspection or a passing build does not constitute visual verification.

For implementation, record affected patterns and exceptions in the project's internal docs. Report verification and remaining limitations briefly.

## References when needed

Use applicable guidance for the established stack; upstream examples do not override project requirements or authorize framework replacement.

- [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines): interaction and visual-review guidance; select relevant principles, not brand-specific preferences.
- [Lucide accessibility guidance](https://lucide.dev/how-to/accessibility): icon labels, controls, and decorative handling.
- [shadcn Field](https://ui.shadcn.com/docs/components/field): field composition in compatible projects.
- [Bootstrap form layouts](https://getbootstrap.com/docs/5.3/forms/layout/) and [Tabler forms](https://docs.tabler.io/ui/forms): existing Bootstrap/Tabler interfaces.
- [WAI form validation](https://www.w3.org/WAI/tutorials/forms/validation/) and [status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html): accessible errors and action feedback.
