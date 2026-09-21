# Project Phases

Read the current phase, subphase, and active plan in [AGENTS.md](AGENTS.md) when starting or resuming work. These describe project focus; issue statuses, work stages, branches, and deployment environments remain separate.

| Phase | Subphases and focus | Ready to advance when |
| --- | --- | --- |
| `DEVELOPMENT` | `planning`: agree specifications: audience, scope, workflows, acceptance criteria, APIs/vendors, data/security requirements, and issue plan; finish by configuring and verifying services, tools, and the application skeleton. `build`: implement, test, and document. `security`: review, fix, and retest under [security.md](security.md). | The first version passes internal acceptance checks and the security review. |
| `RELEASE` | `offering`: finalize website, packages, pricing, and policies. `beta`: gather invited-user feedback. `validation`: resolve launch blockers, recheck affected security controls and final data-handling claims. | The offer matches the product, critical journeys and security checks pass, and the owner authorizes public opening. |
| `LAUNCH` | `open`: open access and publish the release. `feedback`: assess actual customer use. `stabilize`: resolve significant early problems. | An agreed period of real use meets reliability criteria; support, recovery, and releases work routinely. |
| `PRODUCTION` | No subphases. Continue marketing, growth, support, maintenance, and approved feature releases. | Final ongoing phase; an empty backlog is not required. |

The user directs transitions. Accept natural wording: “planning” means `DEVELOPMENT: planning`; “move to security” selects `DEVELOPMENT: security`. If a request such as “move to production” could mean phase or deployment, clarify which; never infer deployment authorization. Verify each subphase's work and applicable phase-exit criteria; recommend advancement with evidence and remaining decisions, then await approval without repeated nudges. Explicit transitions need no second confirmation. Continue independent approved work while awaiting a decision; do not silently skip unresolved requirements.

Record approved transitions in `AGENTS.md` and the relevant issue. Store the living specification in private `docs/internal/specification.md` or link an existing plan under [documentation.md](documentation.md). Phases guide priorities; authorized work may overlap. Future features do not reset the whole product from `PRODUCTION`.

Record and display parents uppercase, subphases lowercase: `DEVELOPMENT: planning`, `RELEASE: beta`, `LAUNCH: feedback`, then only `PRODUCTION`. Phases are not GitHub issue labels or Project fields. Admin presentation follows [design.md](design.md). Phase changes do not authorize deployment or public access; private beta and public opening follow [launch.md](launch.md). Commercial work follows [offering.md](offering.md), including after launch.
