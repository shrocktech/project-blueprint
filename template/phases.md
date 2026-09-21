# Project Phases

Read the current phase, subphase, and active plan in [AGENTS.md](AGENTS.md) when starting or resuming work. These describe project focus; issue statuses, work stages, branches, and deployment environments remain separate.

| Phase | Subphases and focus | Ready to advance when |
| --- | --- | --- |
| `DEVELOPMENT` | `specs`: agree audience, scope, workflows, acceptance criteria, APIs/vendors, and issue plan. `setup`: configure and verify selected services, tools, and application skeleton. `build`: implement, test, and document. | The agreed first version passes internal acceptance checks. |
| `RELEASE` | `offering`: finalize website, packages, pricing, and policies. `beta`: gather invited-user feedback. `validation`: resolve launch blockers and verify readiness. | The offer matches the product, critical journeys work, and the owner authorizes public opening. |
| `LAUNCH` | `open`: open access and publish the release. `feedback`: assess actual customer use. `stabilize`: resolve significant early problems. | An agreed period of real use meets reliability criteria; support, recovery, and releases work routinely. |
| `PRODUCTION` | No subphases. Continue marketing, growth, support, maintenance, and approved feature releases. | Final ongoing phase; an empty backlog is not required. |

The user directs transitions. Accept natural wording: “specification” means `DEVELOPMENT: specs`; “move to setup” selects `DEVELOPMENT: setup`. Clarify only ambiguous intent. Verify each subphase's listed work and applicable phase-exit criteria; recommend advancement briefly with evidence and remaining decisions, then await approval without repeated nudges. An explicit transition needs no second confirmation. Continue independent approved work while awaiting a decision; do not silently skip unresolved requirements.

Record approved transitions in `AGENTS.md` and the relevant issue. Store the living specification in private `docs/internal/specification.md` or link an existing plan under [documentation.md](documentation.md). Phases guide priorities; authorized work may overlap. Future features do not reset the whole product from `PRODUCTION`.

Parent labels are uppercase, subphases lowercase: `DEVELOPMENT: specs`, `RELEASE: beta`, `LAUNCH: feedback`, then only `PRODUCTION`. Admin presentation follows [design.md](design.md). Phase changes do not authorize deployment or public access; private beta and public opening follow [launch.md](launch.md). Offering work uses [marketing.md](marketing.md) and [pricing.md](pricing.md).
