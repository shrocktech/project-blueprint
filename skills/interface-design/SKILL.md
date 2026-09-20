---
name: interface-design
description: Plan, implement, or review compact application pages and forms using the project's established UI stack. Use for layout, icons, alignment, responsive form structure, or action-feedback work.
---

# Interface Design

Read the target project's `AGENTS.md` and `design.md`; filenames here refer to that project, not this skill directory. Use the recorded blueprint source/revision if guidance is missing. `design.md` defines the layout, icon, form-action, and credential rules. Keep work within the requested pages and preserve existing frameworks, components, and native behavior.

## Establish the pattern

Inspect nearby working screens, shared components, icon mappings, spacing tokens, validation, and notification conventions. Reuse those patterns. For a new page, choose the smallest reusable structure that serves the task, for example:

```text
Page title                              Optional page actions
Short context, only when useful

Section title
[Related short field] [Related field] [Related field]
[Long or complex field spanning the available width]
[ ] Option with an associated label

Result/status                           Cancel | Save
```

Adapt field widths, grouping, and action placement to the content; use one clear primary action area without redundant controls. The example is an application-form pattern, not a required structure for every screen. Choose mobile reading order first, then expand related groups as space allows. Reuse shared layout components instead of patching individual screens with arbitrary margins.

Before implementation, identify the action states in `design.md`, the confirmed-data source, client/server validation boundaries, and the expected success result. Use existing form/state utilities where available. Compare meaningful values rather than whether a field was merely touched. Pending responses must not overwrite edits made after submission; retries must respect the action's duplication risk. Use synthetic data and the project's authorized test environment.

## Verify the rendered result

Inspect the actual page at representative desktop and narrow mobile widths, with zoom, wrapping labels, helper text, and errors. Check the header-to-content gap, field and button alignment, overflow, and usable controls. Correct visual defects; a passing build does not verify appearance.

For affected menus, feature groups, or checkout, check icon/text alignment, consistent meaning, muted contrast in supported themes, and collapsed-navigation labels. Verify provider assets and payment/security cues against the real integration; use the icon rules in `design.md`.

Exercise the affected form through unchanged, edited, reverted, incomplete, ready, pending, confirmed-success, and failure states. Check paste/autofill and keyboard submission. Simulate a delayed or failed request where practical to verify visible progress, duplicate prevention, retained input, and recovery. For credential fields, also check saved/replace/cancel/remove behavior without exposing secrets.

Check keyboard navigation, label activation, error associations, focus behavior, and accessible status announcements with available tools. Confirm the saved result by reloading or reading it back through the normal application flow. For a review-only task, report findings without submitting mutations. If rendering or a check is unavailable, state that limit; never claim visual verification from source inspection alone.

Record affected reusable patterns and justified exceptions in the project's internal docs. Report a brief verification result and remaining limitations.

## References when needed

Use applicable guidance for the established stack; upstream examples do not override project requirements or authorize framework replacement.

- [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines): interaction and visual-review guidance; select relevant principles, not brand-specific preferences.
- [Lucide accessibility guidance](https://lucide.dev/how-to/accessibility): icon labels, controls, and decorative handling.
- [shadcn Field](https://ui.shadcn.com/docs/components/aria/field): field composition in compatible projects.
- [Bootstrap form layouts](https://getbootstrap.com/docs/5.3/forms/layout/) and [Tabler forms](https://docs.tabler.io/ui/forms): existing Bootstrap/Tabler interfaces.
- [WAI form validation](https://www.w3.org/WAI/tutorials/forms/validation/) and [status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html): accessible errors and action feedback.
