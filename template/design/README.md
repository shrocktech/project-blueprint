# Project design guide

| Design decision | Project choice and canonical source |
| --- | --- |
| Identity, audience and voice | Record the approved direction and examples. |
| Colors, typography and spacing | List their roles and link the actual CSS, design tokens or framework theme file. |
| Logo, artwork and components | Link approved assets, mockups and representative components. |
| UI foundation | Record CSS framework, component library, icon family, button variants/sizes/shape and links to their shared implementations. |
| Approved exceptions | Record the decision, scope and owner. |

## Design interview

Use this interview for a new interface or an owner-requested redesign. First inspect `materials/`, `design/`, standing preferences and any working application. Reuse settled decisions; ask one brief unanswered question at a time, recommending a direction and accepting “use your judgment.”

1. **Do you have mockups, wireframes or brand references to follow?** Summarize what was found and confirm which materials express the intended direction.
2. **Is there a website or application whose design you like?** Identify the specific qualities to borrow: navigation, typography, colors, spacing or controls. Adapt references to the project's identity and respect asset licenses.
3. **Would you like a custom design proposal?** Recommend a coordinated CSS framework, component library, icon family and button system, starting from standing preferences, the established stack and the [design-check defaults](#design-checks). Ask only about meaningful unresolved choices or reasons to differ. References and custom choices can be combined; skip questions already answered.

For redesigns, establish the affected screens and what should improve, retaining useful components and working behavior. Design planning is scoped work: it does not reset the product lifecycle, repeat the setup interview or authorize replacing the stack. Explain any material replacement before seeking that decision.

Present a small visual sample (two or three alternatives when useful) showing navigation, typography, buttons and fields, including relevant interaction states and themes. Obtain approval of the direction before styled implementation, then maintain the choices in this guide and link canonical tokens and shared components. Clearly distinguish drafts under `design/` from approved choices. Build or extend the needed shared controls before expanding feature screens; add consistent variants there rather than styling each screen independently. Routine refinements within the approved direction use existing autonomy rules.

Selected [UI UX Pro Max and DesignLang](../standards/optional-tools.md#design-planning-tools) support recommendations, reference extraction and drift checks. Existing tools can complete the interview without them. Implement and verify through `interface-design`, [browser iteration](#browser-iteration) and phase-appropriate [device checks](#desktop-tablet-and-mobile).

## Design checks

Apply these defaults to new UI when compatible with the established stack. Preserve existing frameworks, components, icons, and custom code; replacement needs explicit permission.

- For new projects, use the latest stable Tailwind CSS, verifying the version at installation.
- For compatible React projects, use shadcn/ui and shadcn-admin as the dashboard starting point; choose icons below. Other stacks use maintained native solutions under [packages.md](../standards/packages.md).
- WordPress keeps its theme/plugin UI and established Bootstrap/Tabler; blueprint adoption never introduces a replacement framework.
- Keep interfaces simple and consistent. For web accessibility, target [WCAG 2.2 Level AA](https://www.w3.org/TR/WCAG22/#conformance-reqs). Check applicable Level A and AA criteria for affected user flows, including keyboard use, focus, contrast and reflow. Record specific gaps found during verification. Respect lockfiles; upgrades follow [updates.md](../standards/updates.md).
- Draw on [Impeccable](https://github.com/pbakaus/impeccable) principles: clear visual hierarchy, purposeful typography and spacing, restrained decoration, responsive layouts, and complete interaction states. Apply them within the project's established design system and accessibility requirements; project rules take precedence over stylistic preferences. The skill is optional; this reference does not install it.
- For public-facing landing, marketing, portfolio, and product pages, use [TASTE](https://github.com/leonxlnx/taste-skill) as a design reference: build the visual direction from verified subject matter, organize sections around claims and evidence, and critique rendered screenshots before refining. Follow [TASTE setup and scope](../standards/optional-tools.md#taste); its default skill is not for dashboards or application forms.
- Preserve brand tokens, readable content, familiar controls, and accessible navigation over aesthetic quotas or bans. Image counts, motion counts, headline line limits, random directions, and bans on icons, borders, colors, or cards are not acceptance criteria. Use purposeful motion with reduced-motion and script-failure fallbacks; do not add interactions merely to satisfy a visual score. Verify media rights and attribution separately from the skill's license; never invent product facts, prices, endorsements, or customer proof. Synthetic content belongs only in clearly identified prototypes, with approved real content before publication under [offering.md](../standards/offering.md).

## Browser iteration

For UI implementation and refinement in projects with Impeccable selected, use its [browser iteration workflow](https://impeccable.style/tutorials/iterate-live/) on the authorized local application. Verify the installed skill supports [Live Mode](https://impeccable.style/docs/live/), currently beta, and record its version and verified launch/cleanup procedure with project tooling. Preserve the approved brand, shared components and canonical tokens. Projects without selected or working Impeccable use the existing Playwright visual iteration loop and record any setup gap.

- Start the existing development server and use the installed agent's supported invocation (`/impeccable live`, or `$impeccable live` in Codex). Open the application URL and keep the agent session active. For a precise request, `impeccable generate` can target an element directly; use Live Mode selection/annotations when useful. Generate alternatives only when they help resolve a visual choice, then compare them in the page and refine within the authorized scope.
- Accept the chosen result into its canonical source, inspect the diff and discard unused variations. Agents may choose routine refinements within approved design decisions; involve the owner for material identity/product decisions under existing autonomy rules. Follow source-mapping guidance for generated pages. A temporary browser preview does not establish a saved implementation.
- Finish or safely resume pending iterations; stop the helper and remove temporary preview/connection code before final checks. Reload the application to confirm the accepted source persists. Keep helper endpoints private and use synthetic data; explain any necessary CSP adjustment and obtain approval before modifying the policy under upstream setup guidance.
- Use the existing [Playwright setup](../standards/project.md#playwright), `interface-design` skill and [device coverage](#desktop-tablet-and-mobile) to inspect the saved result, exercise affected interactions and rerun relevant tests at the scope required by [checks by phase](../standards/security.md#checks-by-phase). Record visual evidence, assertions and gaps privately. A pleasing variation alone does not establish functional, accessibility or responsive correctness.

## Brand foundation and settings

During `DEVELOPMENT: planning`, establish an owner-approved brand foundation before styled UI implementation. Inspect existing assets, guidelines, theme settings, tokens, components and installed design skills first; preserve an established identity and extend its canonical sources. Adoption does not authorize rebranding, framework replacement or duplicate tooling. Unstyled wireframes, research and independent technical work may proceed while brand decisions are pending. Scale the work to the project: a small application can use a concise essentials guide and approved wordmark; larger products may need fuller guidelines.

- Use the [project specification](../standards/phases.md) for audience, purpose and positioning; ask briefly about personality, voice or constraints only when unresolved during the [design interview](#design-interview). Record any explicitly approved provisional elements. Do not invent business facts, founder stories, endorsements or proof points.
- Maintain one versioned brand kit: context and voice; color roles and verified accessible combinations; fonts, weights, hierarchy, fallbacks and licenses; logo direction and approved variants/assets; imagery/icon guidance; usage examples and restrictions. A logo brief is not a finished logo. Record asset provenance and permitted use; use existing licensed resources or free suitable alternatives, with separate approval for purchases. Naming research is preliminary screening, not trademark clearance. Omit irrelevant print specifications rather than inventing them.
- Maintain this guide and its editable artwork in `design/`. Apply [workspace migration](../standards/documentation.md#workspace-migration) to existing kits. Link to framework-managed tokens, served assets and restricted external masters at their required locations. Index the kit from the private documentation and record its location, approval and settings route in `AGENTS.md`. Keep strategy, research and drafts private under [documentation.md](../standards/documentation.md); publish only approved assets. Translate approved choices into the established theme/tokens and shared components, linking their authoritative locations rather than hand-maintaining duplicate palettes. Optional design-system tools consume this foundation; Impeccable/TASTE refine within it. Verify representative components and pages through `interface-design` and the applicable device checks.
- Every application provides **Settings → Brand Guidelines**, or a clearly named equivalent in its existing settings area. Reuse an existing page where suitable. Show the approved logo variants, color swatches with values/roles, typography samples, imagery/icon rules, voice examples, approval/version and asset links at a glance. Include a living gallery of the actual shared controls and their supported variants, with disabled, loading and error examples where applicable; use harmless sample actions and synthetic data. Reuse these components directly so the gallery and feature screens cannot drift through separate implementations, and cover it with the existing Playwright checks. No separate gallery service is required. Render from this guide and the application’s actual theme values, directly or through a reproducibly generated view; distinguish approved values from drafts and identify where each value is maintained. Never expose private strategy or internal paths through public assets or customer views.
- Use the project's normal settings controls for editable brand fields, with a preview, validation, explicit save and confirmed persistence. For code-managed tokens/assets, provide a clear request-change action through the established project workflow rather than an editor that silently rewrites source. Sanitize text, validate asset uploads and supported values, verify contrast and font availability, and test saving, reloading and failure feedback. Apply the save/feedback rules below. Material identity changes need owner approval; retain the approved version for recovery and publish through [authorization](../standards/git-workflow.md#authorization).

[Cofoundy Brand Skills](https://github.com/cofoundy/brand-skills) is an optional aid for generating the kit, not a prerequisite for satisfying these rules. Offer it during setup only where existing tools/guidelines leave a need. When selected, inspect and pin a reviewed upstream commit and install project-scoped through supported discovery, preserving its [MIT license and notices](https://github.com/cofoundy/brand-skills/blob/main/LICENSE). Start with context, audience/positioning as needed, then identity, voice/messaging and guidelines; use naming only when needed. Include required initialization, router and shared references for the selected workflow; do not install portfolio management, rebranding or `brand-mod` by default.

Verify actual discovery and cross-skill/reference paths for the target agent; Claude-specific routing is not proof of support elsewhere. Review helper scripts before execution, validate generated YAML with a real parser (including punctuation in names/descriptions), and verify a representative kit can be saved and read back. The upstream discovery defaults may not find a private documentation location: explicitly configure/record the canonical path and pass it to each skill without duplicating the kit in a public root. Follow [updates.md](../standards/updates.md) for selected tooling; project instructions remain authoritative. Tool unavailability does not block creation with existing tools, but missing approval or assets remains explicit.

## Desktop, tablet, and mobile

Projects with a web-facing UI must support desktop, tablet, and mobile, including customer pages, administration, and critical forms. Projects without one follow the [Playwright not-applicable rule](../standards/project.md#playwright) and skip this matrix. Use fluid layouts and content-driven breakpoints within the established framework; keep essential content and actions available at every size.

Apply the verification scope in [checks by phase](../standards/security.md#checks-by-phase); design for all three device classes throughout development. Record a repeatable coverage matrix in project docs. Default viewport examples below are CSS pixels, not required layout breakpoints; add the project's supported sizes and test just above/below actual breakpoints and at intermediate widths.

| View | Representative coverage |
| --- | --- |
| Mobile | 375 × 812, plus a narrow 320-pixel width; portrait and landscape, touch input |
| Tablet | 768 × 1024 and 1024 × 768; touch input and both orientations |
| Desktop | 1440 × 900 and a wider 1920 × 1080 view; mouse and keyboard |

- Verify navigation, menus, dialogs, tables, images, long content, forms, and feedback states. Prevent clipped controls, overlaps, accidental page-wide horizontal scrolling, and fixed headers/footers obscuring content or focused fields. Wide tables may scroll inside a clearly usable contained region.
- Preserve logical reading/focus order, readable text, zoom/reflow, and usable touch targets. Essential actions must work without hover. Check keyboard operation as well as touch, orientation changes, and retention of entered form data.
- Use the required [Playwright tooling](../standards/project.md#playwright) and `interface-design` skill to inspect rendered results and exercise meaningful journeys across the matrix. Cover Chromium, Firefox, and WebKit as appropriate to supported browsers, including mobile Chromium and WebKit emulation for phone coverage. A resized desktop viewport alone does not verify touch/mobile behavior.
- Record the candidate, routes/states, browser and viewport/device settings, assertions, visual evidence, fixes, and gaps privately. Fix responsive regressions before completion and verify critical journeys across all three device classes before release. Verify hardware-specific behavior on physical devices when needed.

## Navigation and route changes

During development, change navigation and routes directly. Do not add redirects from retired URLs, legacy route aliases, or compatibility shims to preserve an earlier development layout. Imagined bookmarks, external links, SEO history, or possible future users are not requirements; adding such compatibility requires an explicit owner instruction.

- Update menus, internal links, route definitions, generated URLs, tests, and relevant docs to the intended destination. Remove obsolete routes and associated development-only forwarding within the changed scope; do not leave redirect chains or silently send unknown URLs to a replacement page or home page.
- Verify current links reach their intended URLs directly and retired routes return the application's appropriate not-found behavior without forwarding. Check affected browser journeys under [project.md](../standards/project.md#playwright).
- Keep functional authentication, HTTPS enforcement, and required native platform flows tied to their actual requirements. This navigation rule does not authorize removing them or disrupting verified live URLs during adoption. Record actual published-route obligations for an existing live project; a development environment alone does not make those obligations disposable. Do not invent them for an unreleased project.

## Icons

- Favor icons with labels in menus, features, and checkout where space allows. Keep one coherent general UI set: the established library or stack-appropriate [Lucide](https://lucide.dev/), [Heroicons](https://heroicons.com/), or [Bootstrap Icons](https://icons.getbootstrap.com/), with consistent sizing, style, and meaning.
- Default to muted monochrome with adequate contrast in supported themes; muted never means disabled. Accent/status colors need non-color cues.
- Provider/payment marks must follow asset licenses and brand-use terms. Prefer permitted muted variants, otherwise a generic icon with the provider name. Payment/security icons must reflect supported methods and actual features, never unverified security, guarantees, or certification.
- Keep visible labels where practical. Icon-only controls and collapsed navigation need accessible names and discoverable text on focus/hover. Hide decorative icons from assistive technology and include them within their label's button/link target.

## Page and form layout

- Use a compact title/action row for application pages, with useful content directly below. Avoid oversized headers and decorative empty space in settings and administration screens.
- Use shared components for the page shell, header, sections, field groups, checkbox rows, and actions. Keep primary action placement clear without redundant controls; project-specific patterns belong in `docs/internal/`.
- Put two or three related short fields in a row when they fit comfortably; give long or complex controls more width. Stack on narrow screens and preserve logical reading/tab order. Do not force unrelated fields into columns.
- Use the existing spacing scale for page padding, field gaps, and sections. Align labels, control edges, and actions consistently; keep helper/error text associated with its field without displacing neighboring controls unnecessarily.
- Center checkboxes, radios, and icons beside single-line text; align controls to the first line of wrapping labels. Associate labels with controls and make the label clickable.
- Keep density comfortable: readable text, visible focus, usable hit targets, and layouts that reflow when zoomed. Compactness must not hide labels or clip content.

Use the `interface-design` skill at its recorded location for layout planning and rendered verification. Follow [AGENTS.md](../AGENTS.md) for skill discovery.

## Environment and phase display

Owner/developer admin layouts have a persistent footer whose left side shows the environment and current [project phase](../standards/phases.md) with its stop number, in small muted text with adequate contrast in supported themes:

```text
Environment: DEVELOPMENT · Phase: 2/10 · DEVELOPMENT: build
```

- Environment is `DEVELOPMENT`, `PRODUCTION`, or `STAGING` when staging is active, derived from explicit deployment-environment configuration, not build mode or hostname alone. Give each a consistent, distinct color.
- Phase comes from one configuration value (for example `APP_PHASE`) that the agent updates through authorized delivery at each recorded transition; never hardcode it in templates. `10/10 · PRODUCTION` has no subphase.
- Keep the footer visible on narrow screens without obscuring content or focused fields. Customer-facing pages and customer-admin views show neither value. Neither value controls deployment or access.

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

- Mask new secret drafts by default. Use one directly editable field with an accessible, keyboard-operable eye toggle and a Save button. Allow paste/password managers and appropriate autocomplete; the eye must not submit the form. Do not add Replace/Remove controls or routine explanatory notes beneath the field; retain necessary validation and saving/error feedback under the action-state rules above.
- After server confirmation, mask saved integration passwords entirely with asterisks. For saved API/secret keys, show the first four and last four characters with one asterisk per hidden character: a 40-character key has 32 asterisks between its visible ends. Use a monospaced display and in-field horizontal scrolling when necessary, not a shortened mask or page overflow. Apply the preview safeguards in [security.md](../standards/security.md); unsuitable keys use a fully masked display. An absent credential has an empty input.
- Keep the saved display separate from the replacement draft. Typing/pasting starts a replacement rather than appending to the mask; unchanged or empty input preserves the saved credential. Never submit display asterisks as a replacement or infer a placeholder solely from its characters. Successful saving clears the submitted draft and restores the confirmed masked display, preserving any newer unsaved edits; failed saving preserves the draft without claiming success. Leaving without saving discards the draft.
- The eye reveals/hides the entered draft or, on explicit activation, the saved recoverable integration credential under [security.md](../standards/security.md). Merely loading settings never retrieves the full stored secret. Application login passwords remain hashed and use change/reset; their eye reveals only the newly entered password.
- Application-specific credential request formats, components, and state diagrams belong in `docs/internal/`.

Credential storage and server-side enforcement follow [security.md](../standards/security.md).
