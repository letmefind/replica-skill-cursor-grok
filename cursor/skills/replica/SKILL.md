---
name: replica
description: 'Runs the Replica pack in order: recon, architect, design, build, backend, test, diff, entrepreneur, brand, launch, deploy. Use when the user wants to clone an app, asks where to start, or asks which step is next. Each step reads what the previous one wrote under replica/.'
---

# replica

Eleven skills rebuild what an app does. This one is the map. Run them in
order. Each one reads what the last one wrote, in a `replica/` folder in the
project.

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

You can run any skill on its own. If the files it needs are missing, stop and
run the earlier skill. The replica-entrepreneur skill, used on an app you are
only thinking about, is a fair way to decide whether to build.

## Invoking skills

In Cursor, type `/` in chat and choose the skill by name. That attaches it to
one message. To keep a skill active for the whole session, start it as a
Custom Mode: Option+Enter on macOS, or Alt+Enter on Windows. You can also
name the skill in an ordinary message when the request matches its description.

## What each skill reads and writes

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
