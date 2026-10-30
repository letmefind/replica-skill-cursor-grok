<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · **日本語** · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Cursor と Grok Bot 向けの Replica skills

</div>

アプリが何をするかを作り直す十一の skill に、順番を保つ skill `replica` が一つ加わります。無料、MIT。入れるものは Python 3.8 と標準ライブラリだけです。

やり方はクリーンルームです。skill は機能と、人がそれをどう辿るかを見て、すべてを新しく書きます。対象のコード、ロゴ、文面、中身は取りません。末尾の但し書きを、skill 自身も繰り返します。

## 出典

手法、テンプレート、六つの Python ツールは Jake Schincariol のものです。

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

このリポジトリは、その一式を Cursor と Grok Bot 向けに移した letmefind の port です。skill の本文は、上のリポジトリの fork である https://github.com/letmefind/replica-skill から取りました。

同じ作者の別パック: [Arena](https://github.com/Jakeschincariol/arena-skill)、
[X](https://github.com/Jakeschincariol/x-agent-skill)、
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill)、
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill)。

## 十二

| skill | すること |
| --- | --- |
| `replica` | 順番、各段階が読むファイルと書くファイル、次に走らせる段階。 |
| `replica-recon` | 画面、流れ、部品、データモデル、機能表。公開ページ、スクリーンショット、ストアの掲載、自分のアカウント。 |
| `replica-architect` | スタック、データベースのスキーマ、API。 |
| `replica-design` | 色の役割、書体、間隔、部品をトークンにし、素材は自分のものを使う。 |
| `replica-build` | 偵察の地図から、画面ごとにアプリを作る。 |
| `replica-backend` | 認証、データベース、決済、外部連携。 |
| `replica-test` | すべての流れを実際にクリックし、テストする。 |
| `replica-diff` | 一致の点数と、まだ足りないもの。 |
| `replica-entrepreneur` | 本物の利用者が嫌う点を直しとポジションの角度に変える。 |
| `replica-brand` | 自分の名前とブランドを付け、残りかすを掃く。 |
| `replica-launch` | ランディングページ、価格、ストアの掲載文。 |
| `replica-deploy` | 事前確認を通したあと、自分のドメインで公開する。 |

この順で走らせます。

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

リンクを渡すと相手が時間を予約する、あの種の予定アプリだと、こう進みます。

1. **replica-recon** はヘルプ、料金ページ、ストアの掲載、公開されている操作説明を読みます。自分のアカウントは自分でクリックします。出てくるのは `replica/recon.md` と `replica/features.csv` です。提携先のマーケットは範囲外です。あれは相手のネットワークであって、機能ではありません。
2. **replica-architect** は地味なマネージドのスタックを選び、スキーマを書きます（二人の客が同じ枠を取れない制約を含む）。構築の順は予約の流れを中心に置きます。
3. **replica-design** はスクリーンショットを測ってトークンにします。色の役割、書体、間隔、日付の選択、枠のボタン。アイコンはオープンなもの、フォントもオープンなもの、言葉は自分のものです。
4. **replica-build** は外枠を作り、次に予約の流れ、次に各画面とその状態を作り、進むたびに `features.csv` に印を付けます。
5. **replica-backend** は登録、自分の鍵で使う提供元公式 API のカレンダー、テストモードの決済、リマインドのメールを足します。
6. **replica-test** は流れから計画を書き、うまくいく道と端の両方にエンドツーエンドのテストを置き、重大度で不具合を残し、S1 も S2 も開いたままにしないところまで進めます。
7. **replica-diff** が点数を付けます。必須が欠けていれば、出せません。
8. **replica-entrepreneur** は本物のレビューだけを読みます。引用は、自分が出した行からそのまま写し、その行の URL を付けます。
9. **replica-brand** は商標とドメインの確認を実際に走らせてから名前を付け、元のものが何も残らないまで木を掃きます。
10. **replica-launch** はその角度でランディングページを書き、公開の料金ページと突き合わせて価格を置き（読んだ日付を残す）、ストアの掲載文を検査します。
11. **replica-deploy** は事前確認を走らせ、出せと言うまで公開しません。

skill はどれか一つだけでも走らせられます。まだ手を付けていないアプリで replica-entrepreneur を走らせるのは、作るかどうかを決める筋のよいやり方です。

## Cursor へのインストール

Cursor は、プロジェクトでは `.cursor/skills/<name>/SKILL.md` と `.agents/skills/<name>/SKILL.md` から、利用者個人では `~/.cursor/skills/` と `~/.agents/skills/` から skill を読みます。フォルダ名が skill 名です。フロントマターの `name` と `description` は必須で、`name` はフォルダと一致させます。

このインストーラが使うのは `.cursor/skills`（プロジェクト）と `~/.cursor/skills`（`--global`）です。プロジェクトの skill はリポジトリと一緒に動きます。`~/.cursor/skills/` の利用者 skill は、Settings, Agents で Cloud Agents の同期を入れるまで、そのマシンに残ります。あるリポジトリの Cloud Agent の実行のたびに見せたい skill は、そのリポジトリの `.cursor/skills/` に置きます。

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

もう一度走らせると Replica のフォルダと `replica-tools/` は置き換わり、そこにある他の skill はそのままです。

チャットで `/` と打ち、`replica` か `replica-recon` を選びます。skill はそのメッセージ一つに付きます。セッションのあいだ付けたままにするには、Custom Mode として始めます。macOS は Option+Enter、Windows は Alt+Enter です。

テンプレートは skill のフォルダに残します。Python ツールは共有の一式です。インストール後は skill のフォルダの隣の `replica-tools/` にあります。このリポジトリのチェックアウトから使うときは、`REPLICA_HOME` をそのチェックアウトにすると、skill はそこの `tools/` を使います。Python は 3.8 以降。pip で入れるものはありません。

## Grok Bot へのインストール

次の文を、メッセージそのものとして送ります。

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

そのあとの手順は [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md) にあります。短く言うと、このリポジトリを `/home/box/replica-skill` に clone し（`REPLICA_HOME` で変えられる）、`grok-bot/install.sh` を走らせ、`grok-bot/skills/*/SKILL.md` の各ファイルを skill として保存します。名前、説明、本文はそのまま写します。Grok Bot の skill はそのファイル一つです。ツールとテンプレートはディスクに残り、skill は絶対パスで呼びます。例は `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"` です。

プロジェクトの調査メモは `/workspace/<project-slug>/replica/` に置きます。アプリケーションを書き始める段階からは、`replica/` は自分のコードのリポジトリにあります。コードの変更は、その GitHub リポジトリ上の Cursor cloud coding agent に渡し、必要な `replica/` のファイルをタスクに含めます。ログイン、支払い、ドメインの購入、本番の鍵の入力は自分で行います。

## ツール

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

どれもネットワークを使いません。`imgdiff.py` は色ではなく配置を比べるので、ブランドを変えても不利になりません。`parity.py` は must、should、could に重みを付け、partial は半分に数え、わざと飛ばした行は採点しません。`reviews.py` はリンクのない行を落とします。`sweep.py` は、元の名前、ドメイン、色が木に残っているあいだ公開を止めます。`listing.py` はストアの制限を見て、掲載文に元の名前があれば拒みます。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## 配置

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

自分のプロジェクトのファイルは `replica/` に置き、このリポジトリには入れません。

## 但し書き

**作り直すのは機能と操作の型で、クリーンルームです。** アプリが何をし、人がどう辿るかを見て、すべてを新しく書きます。対象のソース、専有の素材、ロゴ、商標、文面、非公開の API はコピーしません。

**読んでよいものだけを読みます。** 公開ページと自分のアカウントです。ログインの向こうを掻き集めず、サイトの規約に逆らうことをせず、他人のアカウントに入らず、有料の壁を越えません。自分のアカウントの規約が競合を作る使い方を禁じていれば、skill はその旨を言い、公開の情報に留まります。

**公開の前にブランドを変えます。** 新しい名前、新しい配色、新しいロゴ、新しい言葉です。掃きがきれいになるまで、replica-deploy は出しません。

**「どのアプリでもクローン」が指すのは機能と流れです。** 中身でも、ネットワークでも、アプリが持っている許諾でもありません。音楽アプリの再生、プレイリスト、共有は作り直せます。カタログはクローンできません。

**完全な複製は約束しません。** 予約の道具は数週間です。表計算のエンジンはそうではありません。始める前に replica-recon が大きさを見積もり、replica-diff が数字を出します。

**起業の skill は作りません。** 架空のレビュー、引用、数字はありません。主張にはリンクがあり、標本の大きさも書きます。

**売る前に確かめてください。** replica-brand が挙げる商標の確認を走らせ、使ったものの規約を読み、金が関わるなら公開の前に弁護士に相談してください。これは法律上の助言ではありません。

## ライセンス

MIT。原著作者は Jake Schincariol です。この port は letmefind の著作権表示を一行足します。[LICENSE](../../LICENSE) を見てください。
