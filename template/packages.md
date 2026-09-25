# Package Selection

Read alongside [AGENTS.md](AGENTS.md), [security.md](security.md), and [updates.md](updates.md).

Evaluate packages for approved requirements; preserve working custom code and established frameworks. Blueprint adoption uses the `adopt-existing` skill, not package upgrades.

- Before building substantial functionality, check the project's existing components and research established packages. Prefer a suitable, lightweight, actively maintained open-source solution over writing equivalent functionality from scratch.
- Evaluate current maintenance and release history, adoption, maintainer responsiveness, security advisories, documentation, license compatibility, runtime support, size, and transitive dependencies. Popularity and frequent releases are useful signals, not guarantees; a mature package need not release every week.
- Choose the smallest solution that meets the requirement. Distinguish a library from a separately hosted service: webmail, for example, can involve authentication, storage, and operational responsibilities beyond adding a UI component.
- Use a supported stable version, honor project constraints, and commit the appropriate lockfile. Verify the official package/repository identity before installation. Avoid prereleases unless the task specifically requires them.
- Make routine selections autonomously within approved scope. Briefly record the chosen package, source link, reason, and meaningful tradeoffs in the issue and private docs; do not require the owner to compare every library.
- Ask only when a choice introduces a material product, licensing, cost, data-handling, or architecture decision that existing instructions do not settle. Provide a recommendation and useful alternatives.
- Prefer custom code when existing options are unsuitable, unmaintained, incompatible, or heavier than the problem warrants. Document the reason and maintenance responsibility. Remove unused dependencies when relevant to the task.
- Include selected dependencies in the maintenance coverage described in [updates.md](updates.md). No package is guaranteed to remain maintained; reassess when support ends or credible security concerns arise.

## Current product references

For supported libraries, frameworks, SDKs, APIs, CLI tools, and cloud products, prefer [Context7](https://context7.com/docs) for current documentation matching the project's actual version. Use the available MCP or CLI integration; resolve the correct library and version, using a verified exact library ID when known. Follow [Context7's reference guidance](https://context7.com/docs/tips).

Follow project architecture and conventions and use applicable official/product-specific skills or tools. Consult official vendor docs when Context7 is unavailable, incomplete, lacks the needed version, or authoritative provider details are required. Vendor documentation determines actual API behavior; project rules determine intended use. Resolve conflicts explicitly, and do not rely on model memory for version-sensitive details when current sources are available.

Keep product-specific skills focused on project conventions and workflows, with brief reference links and known Context7 IDs where useful, rather than copied vendor documentation.
