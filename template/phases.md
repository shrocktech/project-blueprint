# Project Phases

Read the current phase, subphase, and active plan in [AGENTS.md](AGENTS.md) when starting or resuming work. These describe project focus; issue statuses, work stages, branches, and deployment environments remain separate.

Ten stops in fixed order; the stop number is display-only and never typed in transitions.

| Phase | Subphases and focus | Ready to advance when |
| --- | --- | --- |
| `DEVELOPMENT` | **1** `planning`: agree specifications: audience, scope, workflows, acceptance criteria, APIs/vendors, data/security requirements, and issue plan; establish the approved [brand foundation](design.md#brand-foundation-and-settings) before styled UI; finish by configuring and verifying services, tools, and the application skeleton. **2** `build`: implement, test, and document under the light [checks by phase](security.md#checks-by-phase). **3** `security`: install and run the full check set, then review, fix, and retest under [security.md](security.md). | The first version passes internal acceptance checks and the full security review. |
| `RELEASE` | **4** `offering`: finalize website, packages, pricing, and policies. **5** `beta`: gather invited-user feedback. **6** `validation`: resolve launch blockers, recheck affected security controls and final data-handling claims. | The offer matches the product, critical journeys and security checks pass, and the owner authorizes public opening. |
| `LAUNCH` | **7** `open`: open access and publish the release. **8** `feedback`: assess actual customer use. **9** `stabilize`: resolve significant early problems. | An agreed period of real use meets reliability criteria; support, recovery, and releases work routinely. |
| `PRODUCTION` | **10** No subphases. Continue marketing, growth, support, maintenance, and approved feature releases. | Final ongoing phase; an empty backlog is not required. |

The user directs transitions. Accept natural wording: “planning” means `DEVELOPMENT: planning`; “move to security” selects `DEVELOPMENT: security`. If a request such as “move to production” could mean phase or deployment, clarify which; never infer deployment authorization. Verify each subphase's work and applicable phase-exit criteria; recommend advancement with evidence and remaining decisions, then await approval without repeated nudges. Explicit transitions need no second confirmation. Continue independent approved work while awaiting a decision; do not silently skip unresolved requirements.

Record approved transitions in `AGENTS.md` and the relevant issue. Store the living specification in private `docs/internal/specification.md` or link an existing plan under [documentation.md](documentation.md). Phases guide priorities; authorized work may overlap. Future features do not reset the whole product from `PRODUCTION`.

Record and display parents uppercase, subphases lowercase, prefixed by the stop number out of ten: `2/10 · DEVELOPMENT: build`, `5/10 · RELEASE: beta`, then `10/10 · PRODUCTION`. Phases are not GitHub issue labels or Project fields; the admin footer shows the current stop under [design.md](design.md#environment-and-phase-display). Phase changes do not authorize deployment or public access; private beta and public opening follow [launch.md](launch.md). Commercial work follows [offering.md](offering.md), including after launch.
