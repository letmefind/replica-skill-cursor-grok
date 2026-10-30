<div align="center">

**English** · [简体中文](docs/readme/README_zh.md) · [繁體中文](docs/readme/README_zh-TW.md) · [日本語](docs/readme/README_ja.md) · [한국어](docs/readme/README_ko.md) · [Türkçe](docs/readme/README_tr.md) · [Русский](docs/readme/README_ru.md) · [Tiếng Việt](docs/readme/README_vi.md) · [ไทย](docs/readme/README_th.md) · [Deutsch](docs/readme/README_de.md) · [Español](docs/readme/README_es.md) · [Français](docs/readme/README_fr.md) · [Українська](docs/readme/README_uk.md) · [Polski](docs/readme/README_pl.md) · [Português (Brasil)](docs/readme/README_pt-BR.md) · [العربية](docs/readme/README_ar.md) · [فارسی](docs/readme/README_fa.md) · [Bahasa Indonesia](docs/readme/README_id.md) · [Italiano](docs/readme/README_it.md)
· [Ελληνικά](docs/readme/README_el.md) · [മലയാളം](docs/readme/README_ml.md) · [Roman Urdu](docs/readme/README_ur-Latn.md) · [Română](docs/readme/README_ro.md)

# Replica skills for Cursor and Grok Bot

</div>

Eleven skills that rebuild what an app does, plus one skill, `replica`, that
keeps them in order. Free, MIT, nothing to install beyond Python 3.8 and the
standard library.

The work is clean-room. The skills study features and how a person moves
through them, then write everything fresh. They do not take the target's
code, logo, copy, or content. The fine print is at the bottom, and the skills
repeat it.

## Credit

The method, the templates, and the six Python tools are by Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

This repository is letmefind's port of that pack for Cursor and for Grok Bot.
The skill text was taken from https://github.com/letmefind/replica-skill,
a fork of the repository above.

Other packs from the same author: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## The twelve

| skill | what it does |
| --- | --- |
| `replica` | Order, the files each step reads and writes, and which step to run. |
| `replica-recon` | Screens, flows, components, data model, feature matrix. Public pages, screenshots, store listings, and your own account. |
| `replica-architect` | Stack, database schema, and API. |
| `replica-design` | Colour roles, type, spacing, components, as tokens, with your own assets. |
| `replica-build` | The app, screen by screen, from the recon map. |
| `replica-backend` | Auth, database, payments, and integrations. |
| `replica-test` | Every flow, clicked through and tested. |
| `replica-diff` | A parity score, and what is still missing. |
| `replica-entrepreneur` | What real users hate, turned into fixes and a positioning angle. |
| `replica-brand` | A name and a brand of your own, then a sweep for leftovers. |
| `replica-launch` | Landing page, pricing, and the store listing. |
| `replica-deploy` | Live, on your own domain, after the preflight passes. |

Run them in this order:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

A scheduling app, the kind where you share a link and someone books a time,
goes like this.

1. **replica-recon** reads the help center, the pricing page, the store
   listing, and public walkthroughs. You click through your own account.
   Out come `replica/recon.md` and `replica/features.csv`. A partner
   marketplace is out of scope: that is their network, not a feature.
2. **replica-architect** picks a boring managed stack, writes the schema
   (including a constraint so two guests cannot book the same slot), and
   orders the build around the booking flow.
3. **replica-design** measures screenshots into tokens: colour roles, type,
   spacing, the date picker, the slot button. Open icons, an open font, your
   own words.
4. **replica-build** builds the shell, then the booking flow, then every
   screen with its states, and ticks `features.csv` as it goes.
5. **replica-backend** adds sign-up, calendar access through the provider's
   own API with your keys, payments in test mode, and reminder email.
6. **replica-test** writes a plan from the flows, end-to-end tests for the
   happy paths and the edges, and bugs by severity until no S1 or S2 is open.
7. **replica-diff** scores it. Missing must-haves means not shippable.
8. **replica-entrepreneur** reads real reviews and only real reviews. Every
   quote is copied from a row you supplied, with that row's URL.
9. **replica-brand** names it, after the trademark and domain checks are
   actually run, then sweeps the tree until nothing of the original is left.
10. **replica-launch** writes the landing page around the angle, prices
    against the public pricing page (with the date it was read), and lints
    the store listing.
11. **replica-deploy** runs the preflight and, when you say go, ships.

You can run any one skill on its own. replica-entrepreneur, on an app you
have not started, is a reasonable way to decide whether to build.

## Install for Cursor

Cursor loads skills from a project at `.cursor/skills/<name>/SKILL.md` and
`.agents/skills/<name>/SKILL.md`, and for your user at `~/.cursor/skills/`
and `~/.agents/skills/`. The folder name is the skill name. `name` and
`description` in the frontmatter are required, and `name` must match the
folder.

This installer uses `.cursor/skills` (project) and `~/.cursor/skills`
(`--global`). Project skills travel with the repository. User skills in
`~/.cursor/skills/` stay on that machine until you turn on sync for Cloud
Agents under Settings, Agents. A skill you want on every Cloud Agent run for
a repository belongs in that repository's `.cursor/skills/`.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Running it again replaces the Replica folders and `replica-tools/`, and
leaves any other skills in place.

In chat, type `/` and choose `replica` or `replica-recon`. That attaches the
skill to one message. To keep it for the whole session, start it as a Custom
Mode: Option+Enter on macOS, or Alt+Enter on Windows.

Templates stay in the skill folder. The Python tools are one shared copy.
After install they are in `replica-tools/` beside the skill folders. From a
checkout of this repository, set `REPLICA_HOME` to the checkout and the
skills use `tools/` there. Python 3.8 or newer. Nothing to pip install.

## Install for Grok Bot

Send this, as the whole message:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

The steps after that are in [grok-bot/INSTALL.md](grok-bot/INSTALL.md). Short
version: clone this repository to `/home/box/replica-skill` (override with
`REPLICA_HOME`), run `grok-bot/install.sh`, then save each file in
`grok-bot/skills/*/SKILL.md` as a skill. The name, the description, and the
body are copied verbatim. A Grok Bot skill is that one file. The tools and
templates stay on disk and the skills call them by absolute path, for example
`python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Research notes for a project live at `/workspace/<project-slug>/replica/`.
Once a step is writing the application, `replica/` lives in your code
repository. Code changes are handed to a Cursor cloud coding agent on that
GitHub repository, as a task that includes the `replica/` files it needs.
You sign in, pay, buy the domain, and type live keys yourself.

## Tools

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

None of them use the network. `imgdiff.py` compares layout, not colour, so a
rebrand does not count against you. `parity.py` weights must, should, and
could, counts partial as half, and will not score a row you skipped on
purpose. `reviews.py` drops any row without a link. `sweep.py` blocks a
launch while the original's name, domain, or colours are still in the tree.
`listing.py` checks store limits and rejects the original's name in your listing.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Layout

```
tools/                 contrast.py, parity.py, imgdiff.py, reviews.py, sweep.py, listing.py, themes.json
cursor/skills/         twelve SKILL.md folders, templates beside the skills that use them
cursor/install.sh
grok-bot/skills/       the same twelve skills, one SKILL.md each
grok-bot/install.sh
grok-bot/INSTALL.md
tests/
scripts/validate.py
```

Your project files go in `replica/`, not in this repository.

## Fine print

**It rebuilds functionality and UX patterns, clean-room.** It studies what
the app does and how people move through it, then writes everything fresh.
It does not copy the target's source code, proprietary assets, logos,
trademarks, copy, or private APIs.

**It only reads what you are allowed to read.** Public pages and your own
account. It does not scrape behind a login or against a site's terms, does
not log into anyone else's account, and does not get past a paywall. If your
account's terms forbid using it to build a competitor, the skill says so and
sticks to public sources.

**It rebrands before launch.** New name, new palette, new logo, new words.
replica-deploy does not ship until the sweep is clean.

**"Clone any app" means the features and the flow.** Not the content, the
network, or the licences an app owns. You can rebuild a music app's player,
playlists, and sharing. You cannot clone its catalogue.

**No promise of a perfect clone.** A booking tool is weeks. A spreadsheet
engine is not. replica-recon sizes it before you start, and replica-diff
gives you a number.

**The entrepreneur skill does not invent.** No made-up reviews, quotes, or
numbers. Every claim has a link, and the sample size is stated.

**Check before you sell.** Run the trademark checks replica-brand lists,
read the terms of anything you used, and talk to a lawyer before launch if
there is money on the line. This is not legal advice.

## License

MIT. The original copyright is Jake Schincariol's. The port adds a copyright
line for letmefind. See [LICENSE](LICENSE).
