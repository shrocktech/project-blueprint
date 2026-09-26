# Design Standards

Apply these defaults to new UI when compatible with the established stack. Preserve existing frameworks, components, icons, and custom code; replacement needs explicit permission.

- For new projects, use the latest stable Tailwind CSS, verifying the version at installation.
- For compatible React projects, use shadcn/ui and shadcn-admin as the dashboard starting point; choose icons below. Other stacks use maintained native solutions under [packages.md](packages.md).
- WordPress keeps its theme/plugin UI and established Bootstrap/Tabler; blueprint adoption never introduces a replacement framework.
- Interfaces must be simple, accessible, and consistent. Respect lockfiles; upgrades follow [updates.md](updates.md).
- Draw on [Impeccable](https://github.com/pbakaus/impeccable) principles: clear visual hierarchy, purposeful typography and spacing, restrained decoration, responsive layouts, and complete interaction states. Apply them within the project's established design system and accessibility requirements; project rules take precedence over stylistic preferences. The skill is optional; this reference does not install it.

## Desktop, tablet, and mobile

Every web UI must work on desktop, tablet, and mobile, including customer pages, administration, and critical forms. Use fluid layouts and content-driven breakpoints within the established framework. Keep essential content and actions available at every size; shrinking the desktop page or hiding features is not a responsive implementation.

Record a repeatable coverage matrix in project docs. Default viewport examples below are CSS pixels, not required layout breakpoints; add the project's supported sizes and test just above/below actual breakpoints and at intermediate widths.

| View | Representative coverage |
| --- | --- |
| Mobile | 375 × 812, plus a narrow 320-pixel width; portrait and landscape, touch input |
| Tablet | 768 × 1024 and 1024 × 768; touch input and both orientations |
| Desktop | 1440 × 900 and a wider 1920 × 1080 view; mouse and keyboard |

- Verify navigation, menus, dialogs, tables, images, long content, forms, and feedback states. Prevent clipped controls, overlaps, accidental page-wide horizontal scrolling, and fixed headers/footers obscuring content or focused fields. Wide tables may scroll inside a clearly usable contained region.
- Preserve logical reading/focus order, readable text, zoom/reflow, and usable touch targets. Essential actions must work without hover. Check keyboard operation as well as touch, orientation changes, and retention of entered form data.
- Use the required [Playwright tooling](project.md#playwright) and `interface-design` skill to inspect rendered results and exercise meaningful journeys across the matrix. Cover Chromium, Firefox, and WebKit as appropriate to supported browsers, including mobile Chromium and WebKit emulation for phone coverage. A resized desktop viewport alone does not verify touch/mobile behavior.
- Record the candidate, routes/states, browser and viewport/device settings, assertions, visual evidence, fixes, and gaps privately. Fix responsive regressions before completion and verify critical journeys across all three device classes before release. Emulation is not physical-device testing; verify hardware-specific behavior on an actual device when needed and report unavailable checks honestly.

## Navigation and route changes

During development, change navigation and routes directly. Do not add redirects from retired URLs, legacy route aliases, or compatibility shims to preserve an earlier development layout. Imagined bookmarks, external links, SEO history, or possible future users are not requirements; adding such compatibility requires an explicit owner instruction.

- Update menus, internal links, route definitions, generated URLs, tests, and relevant docs to the intended destination. Remove obsolete routes and associated development-only forwarding within the changed scope; do not leave redirect chains or silently send unknown URLs to a replacement page or home page.
- Verify current links reach their intended URLs directly and retired routes return the application's appropriate not-found behavior without forwarding. Check affected browser journeys under [project.md](project.md#playwright).
- Keep functional authentication, HTTPS enforcement, and required native platform flows tied to their actual requirements. This navigation rule does not authorize removing them or disrupting verified live URLs during adoption. Record actual published-route obligations for an existing live project; a development environment alone does not make those obligations disposable. Do not invent them for an unreleased project.

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
- After server confirmation, show saved credentials as fixed `********` and "Saved" by default; absent credentials show "Not configured".
- For saved API keys, show the first four and last four characters around fixed `********`, for example `abcd********wxyz — Saved`, subject to the preview rules in [security.md](security.md). Use the fixed mask when no preview is available. Saved indicators never reveal the full value or actual length, become editable values, or get submitted as replacements; the eye toggle reveals only the entered draft.
- Keep Replace/Remove explicit: unchanged means keep, cancellation discards the draft, and successful saving clears it. Failed saves never claim success. Do not fetch stored secrets just to populate the field; login passwords use change/reset.
- Application-specific credential request formats, components, and state diagrams belong in `docs/internal/`.

Credential storage and server-side enforcement follow [security.md](security.md).
