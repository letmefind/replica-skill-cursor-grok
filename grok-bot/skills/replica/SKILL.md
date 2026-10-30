---
name: replica
description: 'Runs the Replica pack in order: recon, architect, design, build, backend, test, diff, entrepreneur, brand, launch, deploy. Use when the user wants to clone an app, asks where to start, or asks which step is next. Each step reads what the previous one wrote under replica/.'
---

# replica

Eleven skills rebuild what an app does. This one is the map. Run them in
order. Each one reads what the last one wrote.

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

You can run any skill on its own. If the files it needs are missing, stop and
run the earlier skill. The replica-entrepreneur skill, used on an app you are
only thinking about, is a fair way to decide whether to build.

Open a step by using the skill with that name.

## On this computer

`REPLICA_HOME` defaults to `/home/box/replica-skill`. Tools are in
`${REPLICA_HOME:-/home/box/replica-skill}/tools/`. Templates sit next to the
Cursor copies of the skills, under
`${REPLICA_HOME:-/home/box/replica-skill}/cursor/skills/<name>/`.

Ask for a short project slug if you do not have one.

Research steps write `/workspace/<project-slug>/replica/`. That covers
replica-recon, replica-architect, the token and component work in
replica-design, replica-entrepreneur, the name and voice work in
replica-brand, and the launch documents in replica-launch.

Build steps use `replica/` inside the user's code repository. Writing code
is always handed to a Cursor cloud coding agent on the user's GitHub
repository. The task must stand on its own: paste the rules and steps from
the skill, and include the relevant `replica/` files. Do not edit the
repository yourself. This covers replica-build, replica-backend, Playwright
and code fixes in replica-test, the primitives in replica-design, string and
token edits in replica-brand, the landing page in the repository, and the
build and test commands in replica-deploy.

The user signs in, passes 2FA, pays, buys domains, and types cards and live
keys. You never do those. You never send a message or an email unless the
user has explicitly asked for that exact send.

| step | where `replica/` lives | who writes code |
| --- | --- | --- |
| replica-recon | `/workspace/<project-slug>/replica/` | nobody |
| replica-architect | `/workspace/<project-slug>/replica/` | nobody |
| replica-design | specs under `/workspace/<project-slug>/replica/design/`; primitives in the repository | Cursor cloud coding agent for the primitives |
| replica-build | the repository | Cursor cloud coding agent |
| replica-backend | the repository | Cursor cloud coding agent |
| replica-test | drafts under `/workspace/<project-slug>/replica/`; specs in the repository | Cursor cloud coding agent for Playwright and fixes; desktop browser for a manual pass of a preview |
| replica-diff | files from a read-only checkout, reports beside them | Cursor cloud coding agent only if code must change |
| replica-entrepreneur | `/workspace/<project-slug>/replica/` | Cursor cloud coding agent only to append rows already in the repository's matrix |
| replica-brand | strategy under `/workspace/<project-slug>/replica/`; code in the repository | Cursor cloud coding agent for the edits the sweep finds |
| replica-launch | documents under `/workspace/<project-slug>/replica/launch/`; the page in the repository | Cursor cloud coding agent for the page |
| replica-deploy | `replica/deploy.md` under `/workspace/<project-slug>/replica/`, then committed in the repository | Cursor cloud coding agent for build and test commands |

## What each skill reads and writes

Paths are relative to the directory in the table above.

| skill | reads | writes |
| --- | --- | --- |
| replica-recon | public pages, screenshots, store listings, help docs, the user's own account | `replica/recon.md`, `replica/features.csv`, `replica/screens/` |
| replica-architect | `replica/recon.md`, `replica/features.csv` | `replica/architecture.md`, `replica/schema.sql` or the first migration |
| replica-design | `replica/recon.md`, `replica/screens/` | `replica/design/tokens.json`, `tokens.css`, the Tailwind mapping, `replica/design/components.md`, the UI primitives |
| replica-build | `replica/recon.md`, `replica/architecture.md`, `replica/design/` | the app, the `clone` column in `replica/features.csv`, `replica/build-log.md`, `replica/clone-screens/` |
| replica-backend | `replica/architecture.md`, `replica/schema.sql` | migrations, server code, `.env.example`, `replica/backend.md` |
| replica-test | the flows in `replica/recon.md` | `replica/test-plan.md`, `replica/bugs.md`, `e2e/` |
| replica-diff | `replica/features.csv`, `replica/screens/`, `replica/clone-screens/`, open bugs | `replica/parity.md`, `replica/diffs/` |
| replica-entrepreneur | public reviews | `replica/reviews.csv`, `replica/feedback.md`, `replica/fixes.md`, new rows in `replica/features.csv` |
| replica-brand | `replica/fixes.md`, the codebase, the design tokens | `replica/brand.md`, `replica/brand.json`, updated tokens and strings |
| replica-launch | `replica/fixes.md`, `replica/brand.md`, `replica/brand.json`, `replica/feedback.md` | `replica/launch/` (`landing.md`, `pricing.md`, `listing.json`, `launch-plan.md`) and the landing page |
| replica-deploy | everything in `replica/` | `replica/deploy.md`, then the live site once the user says go |

Public research (recon, reviews, pricing, name and domain checks) uses web
search and opening URLs. The user's own account uses the desktop browser.
The user handles sign-in.

## Routing

- No `replica/recon.md`, and the user wants a clone: replica-recon.
- Recon exists, no architecture: replica-architect.
- Architecture exists, no design tokens: replica-design.
- Tokens exist, and the screens are not built: replica-build.
- Screens still use fake data, or the user asks for auth, the database, payments, email, or an integration: replica-backend.
- A flow is built and the user wants it tested, or backend just finished: replica-test.
- Tests have been run, or the user asks how close the clone is: replica-diff.
- Parity is in decent shape, or the user asks what people hate: replica-entrepreneur.
- A fix list and an angle exist, or the user asks for a name: replica-brand. Always before launch.
- Brand files exist, or the user asks for a landing page, pricing, or a store listing: replica-launch.
- Launch files exist, or the user asks to ship: replica-deploy. Nothing goes live without the user's go, and the sweep must be clean.

If the user names a step, run that skill, then stop and go back when an input file is missing.

## Rules for every step

The skill you route to has the full rules. These are the ones that never loosen:

- Rebuild functionality and UX patterns, clean-room. Not the target's source, logos, icons, illustrations, photos, sounds, licensed fonts, copy, or content.
- Public sources and the user's own account only. The user signs in, passes 2FA, and pays. Never ask for a password. Never get past a paywall or a login by a trick.
- Official public APIs only, with the user's own keys. Never the original app's private endpoints.
- The user creates accounts, buys domains, and types cards and live keys. The agent does not.
- No invented reviews, quotes, counts, or testimonials.
- Rebrand before launch. replica-deploy does not ship until the sweep is clean.
- Test the clone, not the original. Never load-test, fuzz, script, or hammer the original app.
