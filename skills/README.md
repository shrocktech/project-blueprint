# Reusable Skills

| Skill | When to use |
| --- | --- |
| [adopt-existing](adopt-existing/SKILL.md) | Adopting or updating the blueprint in an existing application |
| [issue-interview](issue-interview/SKILL.md) | A requested walkthrough of pending user decisions/setup |
| [interface-design](interface-design/SKILL.md) | Compact page/form layouts, action feedback, and rendered UI verification |
| [pricing-research](pricing-research/SKILL.md) | Comparable products, pricing/packaging, and refund recommendations |
| [legal-review](legal-review/SKILL.md) | Terms/privacy preparation and review for the project's jurisdictions |

Read only the applicable skill. These are portable source packages, not automatically installed or activated by copying `template/`.

During adoption, install relevant skills using the target agent's supported mechanism and verify discovery. If unavailable, retain the blueprint checkout and record accessible local `SKILL.md` paths in the target's `AGENTS.md` for explicit reading. Record the blueprint revision; apply later updates deliberately while preserving local additions.

Inside each skill, plain filenames such as `git-workflow.md` refer to the target project's instructions, not files beside the installed skill. During initial adoption, consult the blueprint's template equivalents until those files are merged. Confirm the target repository before any mutation.

Keep application-specific configuration and domains in that project's appropriate docs, not these reusable skills.

For product-specific skills, follow [current product references](../template/packages.md#current-product-references): project conventions belong in skills; current vendor details come through Context7 or official documentation. Required Graphify tooling follows [project setup](../template/project.md#graphify). WordPress projects also require the [official WordPress skills](../template/project.md#wordpress-skills).
