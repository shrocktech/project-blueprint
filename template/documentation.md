# Documentation and Changelog Rules

Read alongside [AGENTS.md](AGENTS.md) and [git-workflow.md](git-workflow.md).

## Documentation audiences and sources

| Folder | Audience and use |
| --- | --- |
| `docs/internal/` | Private technical reference for developers and agents; always maintained. |
| `docs/public/` | Customer-facing guides when external documentation is needed; source for the public documentation site or app help. |
| `docs/admin/` | Optional administrator guides when the product has distinct administration tasks; source for its administrator documentation. |

Create public/admin sets only when needed and give each a README index. Administrator guides explain tasks such as configuration, user management, and supported maintenance; implementation details remain internal.

Applicable customer policies use `docs/public/legal/` under [legal.md](legal.md).

- Maintain `docs/internal/` as the authoritative technical documentation for developers and agents, with `docs/internal/README.md` as its index. Cover current behavior, architecture, setup, configuration, interfaces, data flows, operations, and troubleshooting as relevant. Read the Markdown directly in the private repository or locally; no GitHub Wiki or publishing process is required.
- Update affected pages with every issue that changes how the application works. Documentation is part of the implementation, not a later cleanup task. Do not mark the issue complete or move to the next task with required documentation outstanding.
- Use Mermaid or other useful diagrams freely to explain structure and behavior. Keep editable diagram sources with the docs and verify they render in the intended viewer.
- Commit affected documentation alongside the implementation and verify its integration into `develop`, including working links and assets. Documentation completion requires current source files, not a separate wiki synchronization or publication.
- Keep technical docs private. A folder name does not restrict access: never place internal docs in a public repository. If the application repository is public, keep `docs/internal/` in a separate private documentation repository, reference corresponding changes without exposing private details, and verify both merges before completion. Exclude internal docs from application bundles and public hosting output even when source code is private.
- Derive public and administrator guides from the technical docs, adapting them for their audience. Once a set exists, update its affected drafts with each issue before completion. Publish only documentation matching the released version from `main` through the authorized release process.
- Build public documentation from `docs/public/` and administrator documentation from `docs/admin/`, with explicitly selected assets for each. Never publish the entire `docs/` tree. Record each enabled set's source, destination, build command, and intended audience in project setup notes; verify the resulting output and links.
- `docs/admin/` is an audience designation, not access control. Keep restricted administrator sources in a private repository and serve their output through the existing authenticated administrator area or other authorized private delivery. Verify unauthorized users cannot access restricted pages or assets. Publicly publish admin guides only when approved for public readers.
- Public builds must include only explicitly approved public pages and assets. Never copy or publish internal docs wholesale. Review public text, diagrams, links, and assets for internal-only details and secrets. Keep unreleased features out of published documentation. Use an approved hosting path consistent with the project's cost and privacy constraints.

## Changelog

- Do not maintain a changelog during initial development or internal prereleases. Create `CHANGELOG.md` during final go-live preparation and publish it with the first public launch; summarize the initial release without reconstructing every development commit. Follow [launch.md](launch.md) for launch preparation.
- After go-live, add meaningful user-facing changes to an `Unreleased` section as part of each applicable issue. Internal-only changes need no public entry.
- For every subsequent public release, finalize the applicable entries under the version and release date, including breaking changes and migration steps when relevant. Keep remaining unreleased work separate.
- Link the changelog from the documentation index and, once available, the public docs. Keep public changelog entries and release notes consistent and free of internal-only information.
