<div align="center">

[English](../../README.md) · **简体中文** · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# 面向 Cursor 与 Grok Bot 的 Replica skills

</div>

十一项 skill 用来重做一款应用实际做的事，再加上一项 skill，`replica`，负责把它们排好顺序。免费，MIT 许可。除了 Python 3.8 和标准库，没有别的要装。

做法是净室。这些 skill 研究功能，以及一个人怎样走完这些功能，然后全部重写。它们不取目标的代码、标志、文案或内容。细则在文末，skill 里也会再写一遍。

## 出处

方法、模板和六个 Python 工具出自 Jake Schincariol：

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

本仓库是 letmefind 把那套包移植到 Cursor 和 Grok Bot 的结果。skill 正文取自 https://github.com/letmefind/replica-skill，即上面那个仓库的一个 fork。

同一作者的其他套件：[Arena](https://github.com/Jakeschincariol/arena-skill)、
[X](https://github.com/Jakeschincariol/x-agent-skill)、
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill)、
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill)。

## 十二项

| skill | 做什么 |
| --- | --- |
| `replica` | 顺序、每一步读哪些文件、写哪些文件，以及下一步该跑哪一项。 |
| `replica-recon` | 界面、流程、组件、数据模型、功能表。来源是公开页面、截图、商店页，以及你自己的账号。 |
| `replica-architect` | 技术栈、数据库结构和 API。 |
| `replica-design` | 颜色角色、字体、间距、组件，写成 token，素材用你自己的。 |
| `replica-build` | 按侦察图，一屏一屏把应用做出来。 |
| `replica-backend` | 登录、数据库、支付和外部接入。 |
| `replica-test` | 每条流程都点一遍，并写成测试。 |
| `replica-diff` | 给出对齐分数，以及还缺什么。 |
| `replica-entrepreneur` | 把真实用户讨厌的地方写成改动，并找出定位角度。 |
| `replica-brand` | 起一个你自己的名字和品牌，再扫一遍残留。 |
| `replica-launch` | 落地页、定价和商店文案。 |
| `replica-deploy` | 预检通过之后，在你自己的域名上线。 |

按这个顺序跑：

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

以预约类应用为例：你发出一个链接，对方选一个时间来订。过程是这样。

1. **replica-recon** 读帮助中心、定价页、商店页和公开的操作演示。你用自己的账号点一遍。产出是 `replica/recon.md` 和 `replica/features.csv`。合作方市场不在范围内：那是他们的网络，不是一项功能。
2. **replica-architect** 选一套朴素、托管的技术栈，写出数据结构（包括一条约束，避免两位访客订到同一个时段），并围绕预约流程安排构建顺序。
3. **replica-design** 把截图量成 token：颜色角色、字体、间距、日期选择器、时段按钮。图标用开放的，字体用开放的，文案用你自己的。
4. **replica-build** 先做外壳，再做预约流程，再做每一屏及其状态，并顺手勾掉 `features.csv`。
5. **replica-backend** 加上注册、用你自己的密钥走提供方官方 API 的日历、测试模式的支付，以及提醒邮件。
6. **replica-test** 按流程写测试计划，为顺利路径和边界写端到端测试，并按严重程度记缺陷，直到没有未关闭的 S1 或 S2。
7. **replica-diff** 打分。缺了必须有的功能，就不能发布。
8. **replica-entrepreneur** 只读真实评价。每一句引文都来自你提供的一行，并带上那一行的 URL。
9. **replica-brand** 在商标和域名检查真正跑过之后再取名，然后扫整棵目录，直到原作的痕迹不剩。
10. **replica-launch** 围绕这个角度写落地页，对照公开定价页定价（写上读到该页的日期），并检查商店文案。
11. **replica-deploy** 跑预检。你说可以上，它才发布。

任何一项都可以单独跑。还没动手做的应用，先跑 replica-entrepreneur，是判断值不值得做的一种稳妥办法。

## 在 Cursor 里安装

Cursor 从项目里的 `.cursor/skills/<name>/SKILL.md` 和 `.agents/skills/<name>/SKILL.md` 加载 skill，也会从你用户目录的 `~/.cursor/skills/` 和 `~/.agents/skills/` 加载。文件夹名就是 skill 名。前言里的 `name` 和 `description` 必填，而且 `name` 必须和文件夹一致。

本安装脚本使用 `.cursor/skills`（项目）和 `~/.cursor/skills`（`--global`）。项目里的 skill 随仓库走。`~/.cursor/skills/` 里的用户 skill 留在那台机器上，直到你在 Settings, Agents 里打开 Cloud Agents 的同步。希望某个仓库的每一次 Cloud Agent 运行都能看到的 skill，应放进该仓库的 `.cursor/skills/`。

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

再跑一次会替换 Replica 的文件夹和 `replica-tools/`，同一位置的其他 skill 不动。

在对话里输入 `/`，选 `replica` 或 `replica-recon`。这会把 skill 附到一条消息上。若要整段会话都用它，把它开成 Custom Mode：macOS 上是 Option+Enter，Windows 上是 Alt+Enter。

模板留在 skill 文件夹里。Python 工具只有一份共享副本。安装之后，它们在 skill 文件夹旁边的 `replica-tools/`。如果是从这个仓库的检出目录跑，把 `REPLICA_HOME` 设成该检出目录，skill 就会用那里的 `tools/`。Python 3.8 或更新版本。不需要用 pip 安装任何东西。

## 在 Grok Bot 里安装

把下面这段当作整条消息发出去：

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

之后的步骤写在 [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md)。简要说：把本仓库克隆到 `/home/box/replica-skill`（可用 `REPLICA_HOME` 改路径），运行 `grok-bot/install.sh`，再把 `grok-bot/skills/*/SKILL.md` 里的每个文件存成一项 skill。名称、说明和正文都按原文复制。Grok Bot 的一项 skill 就是这一个文件。工具和模板留在磁盘上，skill 用绝对路径调用，例如 `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`。

一个项目的研究笔记放在 `/workspace/<project-slug>/replica/`。一旦某一步开始写应用，`replica/` 就放进你的代码仓库。代码改动交给该 GitHub 仓库上的 Cursor cloud coding agent，任务里要带上它需要的 `replica/` 文件。登录、付款、购买域名、输入正式密钥，都由你自己做。

## 工具

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

它们都不访问网络。`imgdiff.py` 比的是版式，不是颜色，所以换品牌不会被算成差距。`parity.py` 给 must、should、could 加权，partial 算一半，你故意跳过的行不计分。`reviews.py` 丢掉没有链接的行。`sweep.py` 在原作的名称、域名或颜色还留在目录树里时，拦住发布。`listing.py` 检查商店限制，并拒绝你的商店文案里出现原作名称。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## 目录

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

你的项目文件放在 `replica/`，不要放进本仓库。

## 细则

**它重做的是功能和交互方式，而且是净室。** 它研究应用做什么、人怎样走完，然后全部重写。它不复制目标的源代码、专有素材、标志、商标、文案或私有 API。

**它只读你被允许读的东西。** 公开页面和你自己的账号。它不在登录后面抓取，不违反网站条款，不登录别人的账号，也不绕过付费墙。如果你的账号条款禁止用它来做竞品，skill 会说明这一点，并只使用公开来源。

**发布之前先换品牌。** 新名称、新配色、新标志、新文案。清扫不干净，replica-deploy 不上线。

**「克隆任何应用」指的是功能和流程。** 不是内容、关系网络，也不是应用自己持有的许可。音乐应用的播放器、播放列表和分享可以重做。它的曲库不能克隆。

**不保证克隆得一模一样。** 预约工具是数周的工作。电子表格引擎不是。动手之前 replica-recon 会估规模，replica-diff 会给你一个数字。

**创业这项 skill 不编造。** 没有虚构的评价、引文或数字。每条说法都有链接，并写明样本量。

**出售之前先核对。** 跑 replica-brand 列出的商标检查，读你用过的每项服务的条款，牵涉到钱就在发布前找律师谈。这不是法律意见。

## 许可

MIT。原始著作权属于 Jake Schincariol。这次移植为 letmefind 加了一行著作权。见 [LICENSE](../../LICENSE)。
