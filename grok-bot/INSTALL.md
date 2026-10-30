# Install the Replica skills on Grok Bot

Send this message:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Then do these steps, in order.

1. Clone the repository to `/home/box/replica-skill`, or update it if it is already there.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git /home/box/replica-skill
```

If that directory already exists:

```bash
git -C /home/box/replica-skill pull --ff-only
```

2. Run the installer. It updates the checkout when it can, and it prints the skills to save.

```bash
bash /home/box/replica-skill/grok-bot/install.sh
```

`REPLICA_HOME` overrides the directory. The default is `/home/box/replica-skill`.

3. For each file it lists (`grok-bot/skills/<name>/SKILL.md`), save one skill:

- **name:** the `name` value in the frontmatter. It matches the folder name.
- **description:** the `description` value. It is one line, inside single quotes. Take the text inside the quotes, and turn every doubled single quote (`''`) into one single quote.
- **body:** the markdown after the frontmatter, verbatim, from the `#` heading through the end of the file. Do not include the `---` block.

Do not paraphrase, shorten, translate, or merge skills. Save all twelve, including `replica`.

4. Tell the user the tools are at `/home/box/replica-skill/tools` and that the twelve skills are saved. Do not edit the user's code repositories as part of install. Do not buy anything, and do not send a message other than the confirmation they asked for.
