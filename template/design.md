# Design Standards

Apply these defaults to new UI when compatible with the established stack. Preserve existing frameworks, components, icons, and custom code; replacement needs explicit permission.

- For new projects, use the latest stable Tailwind CSS, verifying the version at installation.
- For compatible React projects, use shadcn/ui and shadcn-admin as the dashboard starting point; choose icons below. Other stacks use maintained native solutions under [packages.md](packages.md).
- WordPress keeps its theme/plugin UI and established Bootstrap/Tabler; blueprint adoption never introduces a replacement framework.
- Interfaces must be simple, accessible, and consistent. Respect lockfiles; upgrades follow [updates.md](updates.md).

## Icons

- Favor icons with labels in menus, features, and checkout where space allows. Keep one coherent general UI set: the established library or stack-appropriate [Lucide](https://lucide.dev/), [Heroicons](https://heroicons.com/), or [Bootstrap Icons](https://icons.getbootstrap.com/), with consistent sizing, style, and meaning.
- Default to muted monochrome with adequate contrast in supported themes; muted never means disabled. Accent/status colors need non-color cues.
- Provider/payment marks must follow asset licenses and brand-use terms. Prefer permitted muted variants, otherwise a generic icon with the provider name. Payment/security icons must reflect supported methods and actual features, never unverified security, guarantees, or certification.
- Keep visible labels where practical. Icon-only controls and collapsed navigation need accessible names and discoverable text on focus/hover. Hide decorative icons from assistive technology and include them within their label's button/link target.

## Page and form layout

- Use a compact title/action row for application pages, with useful content directly below. Avoid oversized headers and decorative empty space in settings and administration screens.
- Show a persistent badge for the current environment inside the admin header, normally upper right before utility icons: `DEVELOPMENT`, `PRODUCTION`, or `STAGING` when staging is active. Use consistent, distinct colors with readable text and adequate contrast in supported themes; keep it visible on narrow screens. Derive the label from explicit deployment-environment configuration, not build mode or hostname alone.
- In owner/developer admin views, also show the [project phase](phases.md), such as `RELEASE: beta`; final `PRODUCTION` has no suffix. Use visible, accessible labels **Environment** and **Project phase**. Keep display-safe phase values synchronized through authorized delivery; customer-admin views need no lifecycle display. Neither badge controls deployment or access.
- Use shared components for the page shell, header, sections, field groups, checkbox rows, and actions. Keep primary action placement clear without redundant controls; project-specific patterns belong in `docs/internal/`.
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
| Failure | Show a useful error and next step, preserve the draft safely, and allow correction or appropriate retry. A timeout or unknown outcome is not success; retries must not duplicate effects when the original result is uncertain. |

- Readiness must reflect typing, clearing, selection, paste, and autofill. Validation must be timely without interrupting every keystroke. Server-only checks run on submission, never as an impossible prerequisite for enabling the button. Validation and authorization remain enforced server-side.
- Keep pending, success, and failure distinguishable through text, not just color or motion. Announce asynchronous status changes without stealing focus; associate field errors and keep them available until resolved.
- Native page navigation, including established WordPress flows, can provide progress feedback without an extra spinner. The destination must still communicate the outcome; a refresh alone is not proof of a successful save. Autosave needs equivalent saving/saved/error feedback. Exceptions require justification in project documentation.

## Credential fields, where applicable

- Mask secret inputs by default; provide an accessible, keyboard-operable eye toggle for the entered draft. Allow paste/password managers and appropriate autocomplete; the toggle must not submit the form.
- Represent a saved credential with fixed `********` and "Saved", based on server confirmation. Show "Not configured" otherwise. The display must contain neither the secret nor its length and must never be submitted as a replacement.
- Keep Replace/Remove explicit: unchanged means keep, cancellation discards the draft, and successful saving clears it. Failed saves never claim success. Do not fetch stored secrets just to populate the field; login passwords use change/reset.
- Application-specific credential request formats, components, and state diagrams belong in `docs/internal/`.

Credential storage and server-side enforcement follow [security.md](security.md).
