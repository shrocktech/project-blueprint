# Design Standards

Apply these defaults to new UI when compatible with the established stack. Preserve existing frameworks, components, icons, and custom code; replacement needs explicit permission.

- For new projects, use the latest stable Tailwind CSS, verifying the version at installation.
- For compatible React projects, use shadcn/ui and shadcn-admin as the dashboard starting point; choose icons below. Other stacks use maintained native solutions under [packages.md](packages.md).
- WordPress keeps its theme/plugin UI and established Bootstrap/Tabler; blueprint adoption never introduces a replacement framework.
- Reuse components and keep interfaces simple, accessible, and consistent. Respect lockfiles; upgrades follow [updates.md](updates.md).

## Icons

- Use recognizable icons generously alongside labels in admin navigation, menus, actions, and feature groups. Include them on customer-facing pages where space allows and they improve scanning; keep text readable and avoid crowding.
- Keep the established icon set. For new choices, prefer [Lucide](https://lucide.dev/), [Heroicons](https://heroicons.com/), or [Bootstrap Icons](https://icons.getbootstrap.com/) as appropriate to the stack. Use one coherent set for general UI, consistent sizes, stroke/fill style, spacing, and meanings; load only needed assets.
- Default to muted monochrome using theme colors, with sufficient contrast in supported themes. Muted must not imply disabled. Reserve accent/status colors for meaningful states and provide non-color cues too.
- Use recognizable provider marks for service integrations where useful. Prefer permitted monochrome variants that fit the muted palette; respect asset licenses and brand-use rules. If no permitted muted variant exists, use a generic service icon with the provider name. Provider/payment marks may supplement the general UI set.
- Use card/payment icons at checkout and lock/shield icons for actual security features. Show only supported payment-brand marks; preserve payment-provider controls. Icons must not imply unverified certification, guarantees, or protection.
- Keep visible labels where practical; give icon-only buttons and collapsed navigation accessible names and discoverable text on focus/hover. Hide decorative icons from assistive technology, and keep icons inside the same button/link target as their label.

## Page and form layout

- Use a compact title/action row for application pages, with useful content directly below. Avoid oversized headers and decorative empty space in settings and administration screens.
- Reuse a page shell, header, content sections, field groups, checkbox rows, and action area in the established stack. Keep project-specific patterns in `docs/internal/`.
- Put two or three related short fields in a row when they fit comfortably; give long or complex controls more width. Stack on narrow screens and preserve logical reading/tab order. Do not force unrelated fields into columns.
- Use the existing spacing scale for page padding, field gaps, and sections. Align labels, control edges, and actions consistently; keep helper/error text associated with its field without displacing neighboring controls unnecessarily.
- Center checkboxes, radios, and icons beside single-line text; align controls to the first line of wrapping labels. Associate labels with controls and make the label clickable.
- Keep density comfortable: readable text, visible focus, usable hit targets, and layouts that reflow when zoomed. Compactness must not hide labels or clip content.

Use the `interface-design` skill at its recorded location for layout planning and rendered verification. Follow [AGENTS.md](AGENTS.md) for skill discovery.

## Save, submit, and feedback

Apply these defaults where compatible with the interaction; preserve established native flows that already provide clear feedback.

| State | Required behavior |
| --- | --- |
| Unchanged | Keep Save visible but inactive and visually subdued until values differ meaningfully from the last confirmed saved state. Reverting edits restores this state. |
| Incomplete or invalid | Keep Submit/Save inactive until applicable required fields are complete and supplied values pass client-checkable validation. Optional fields may stay empty. Explain what is missing or invalid near the fields; do not rely on clicking a disabled button to reveal errors. |
| Ready | Enable and emphasize the action. Creating/submitting a new record does not require edits when its defaults are valid. |
| Processing | Show immediate progress, such as a spinner with "Saving..." or a status message. Prevent duplicate activation by click or Enter, keep the action's layout stable, and expose busy/status changes to assistive technology. |
| Success | Show a clear confirmation or unmistakable result only after the server confirms success. Reset the saved baseline to confirmed values; preserve any newer unsaved edits. |
| Failure | Show a useful error and next step, preserve the draft safely, and allow correction or appropriate retry. A timeout or unknown outcome is not success; verify the result before retrying actions that could duplicate effects. |

- Reevaluate readiness after typing, clearing, selection, paste, and autofill. Show validation at helpful moments rather than interrupting every keystroke. Server-only checks run on submission; never make them an impossible prerequisite for enabling the button. Always validate and authorize server-side.
- Keep pending, success, and failure distinguishable through text, not just color or motion. Announce asynchronous status changes without stealing focus; associate field errors and keep them available until resolved.
- Native page navigation, including established WordPress flows, can provide progress feedback without an extra spinner. The destination must still communicate the outcome; a refresh alone is not proof of a successful save. Autosave needs equivalent saving/saved/error feedback. Record justified exceptions in project documentation.

## Credential fields, where applicable

- Mask secret inputs by default; provide an accessible, keyboard-operable eye toggle for the entered draft. Allow paste/password managers and appropriate autocomplete; the toggle must not submit the form.
- Represent a saved credential with fixed `********` and "Saved", based on server confirmation. Show "Not configured" otherwise. The display must contain neither the secret nor its length and must never be submitted as a replacement.
- Keep Replace/Remove explicit: unchanged means keep, cancellation discards the draft, and successful saving clears it. Failed saves never claim success. Do not fetch stored secrets just to populate the field; login passwords use change/reset.
- This file defines the credential UI states. Put application-specific request formats, components, and state diagrams in `docs/internal/`; verify accessibility and saved/replacement/cancel/error/removal behavior when implemented.

Credential storage and server-side enforcement follow [security.md](security.md).
