# Design Standards

Apply these defaults to new UI when compatible with the established stack. Preserve existing frameworks, components, icons, and custom code; replacement needs explicit permission.

- For new projects, use the latest stable Tailwind CSS, verifying the version at installation.
- For compatible React projects, use shadcn/ui, Lucide icons, and shadcn-admin as the dashboard starting point. Other stacks use maintained native solutions under [packages.md](packages.md).
- WordPress keeps its theme/plugin UI and established Bootstrap/Tabler; blueprint adoption never introduces a replacement framework.
- Reuse components and keep interfaces simple, accessible, and consistent. Respect lockfiles; upgrades follow [updates.md](updates.md).

## Credential fields, where applicable

- Mask secret inputs by default; provide an accessible, keyboard-operable eye toggle for the entered draft. Allow paste/password managers and appropriate autocomplete; the toggle must not submit the form.
- Represent a saved credential with fixed `********` and "Saved", based on server confirmation. Show "Not configured" otherwise. The display must contain neither the secret nor its length and must never be submitted as a replacement.
- Keep Replace/Remove explicit: unchanged means keep, cancellation discards the draft, and successful saving clears it. Failed saves never claim success. Do not fetch stored secrets just to populate the field; login passwords use change/reset.
- This file defines the credential UI states. Put application-specific request formats, components, and state diagrams in `docs/internal/`; verify accessibility and saved/replacement/cancel/error/removal behavior when implemented.

Credential storage and server-side enforcement follow [security.md](security.md).
