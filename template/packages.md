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
