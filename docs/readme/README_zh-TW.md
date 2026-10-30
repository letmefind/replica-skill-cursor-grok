<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · **繁體中文** · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# 給 Cursor 與 Grok Bot 的 Replica skills

</div>

十一項 skill 用來重做一款應用實際做的事，再加上一項 skill，`replica`，負責把順序排好。免費，MIT 授權。除了 Python 3.8 和標準函式庫，沒有別的要裝。

做法是淨室。這些 skill 研究功能，以及一個人怎樣走完這些功能，然後全部重寫。它們不取目標的程式碼、標誌、文案或內容。細則在文末，skill 裡也會再寫一遍。

## 出處

方法、範本和六個 Python 工具出自 Jake Schincariol：

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

這個儲存庫是 letmefind 把那套包裝到 Cursor 和 Grok Bot 的結果。skill 正文取自 https://github.com/letmefind/replica-skill，也就是上面那個儲存庫的一個 fork。

同一作者的其他套件：[Arena](https://github.com/Jakeschincariol/arena-skill)、
[X](https://github.com/Jakeschincariol/x-agent-skill)、
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill)、
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill)。

## 十二項

| skill | 做什麼 |
| --- | --- |
| `replica` | 順序、每一步讀哪些檔案、寫哪些檔案，以及下一步該跑哪一項。 |
| `replica-recon` | 畫面、流程、元件、資料模型、功能表。來源是公開頁面、截圖、商店頁，以及你自己的帳號。 |
| `replica-architect` | 技術堆疊、資料庫結構和 API。 |
| `replica-design` | 顏色角色、字體、間距、元件，寫成 token，素材用你自己的。 |
| `replica-build` | 照偵察圖，一屏一屏把應用做出來。 |
| `replica-backend` | 登入、資料庫、付款和外部串接。 |
| `replica-test` | 每條流程都點一遍，並寫成測試。 |
| `replica-diff` | 給出對齊分數，以及還缺什麼。 |
| `replica-entrepreneur` | 把真實使用者討厭的地方寫成改動，並找出定位角度。 |
| `replica-brand` | 取一個你自己的名字和品牌，再掃一遍殘留。 |
| `replica-launch` | 落地頁、定價和商店文案。 |
| `replica-deploy` | 預檢通過之後，在你自己的網域上線。 |

按這個順序跑：

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

以預約類應用為例：你發出一個連結，對方選一個時間來訂。過程是這樣。

1. **replica-recon** 讀說明中心、定價頁、商店頁和公開的操作示範。你用自己的帳號點一遍。產出是 `replica/recon.md` 和 `replica/features.csv`。合作方市集不在範圍內：那是他們的網路，不是一項功能。
2. **replica-architect** 選一套樸素、託管的技術堆疊，寫出資料結構（包括一條約束，避免兩位訪客訂到同一個時段），並圍繞預約流程安排建置順序。
3. **replica-design** 把截圖量成 token：顏色角色、字體、間距、日期選擇器、時段按鈕。圖示用開放的，字型用開放的，文案用你自己的。
4. **replica-build** 先做外殼，再做預約流程，再做每一屏及其狀態，並順手勾掉 `features.csv`。
5. **replica-backend** 加上註冊、用你自己的金鑰走提供方官方 API 的日曆、測試模式的付款，以及提醒郵件。
6. **replica-test** 按流程寫測試計畫，為順利路徑和邊界寫端對端測試，並按嚴重程度記缺陷，直到沒有未關閉的 S1 或 S2。
7. **replica-diff** 評分。缺了必須有的功能，就不能發布。
8. **replica-entrepreneur** 只讀真實評價。每一句引文都來自你提供的一列，並帶上那一列的 URL。
9. **replica-brand** 在商標和網域檢查真正跑過之後再取名，然後掃整棵目錄，直到原作的痕跡不剩。
10. **replica-launch** 圍繞這個角度寫落地頁，對照公開定價頁定價（寫上讀到該頁的日期），並檢查商店文案。
11. **replica-deploy** 跑預檢。你說可以上，它才發布。

任何一項都可以單獨跑。還沒動手做的應用，先跑 replica-entrepreneur，是判斷值不值得做的一種穩妥辦法。

## 在 Cursor 裡安裝

Cursor 從專案裡的 `.cursor/skills/<name>/SKILL.md` 和 `.agents/skills/<name>/SKILL.md` 載入 skill，也會從你使用者目錄的 `~/.cursor/skills/` 和 `~/.agents/skills/` 載入。資料夾名稱就是 skill 名稱。前言裡的 `name` 和 `description` 必填，而且 `name` 必須和資料夾一致。

這個安裝腳本使用 `.cursor/skills`（專案）和 `~/.cursor/skills`（`--global`）。專案裡的 skill 隨儲存庫走。`~/.cursor/skills/` 裡的使用者 skill 留在那台機器上，直到你在 Settings, Agents 裡打開 Cloud Agents 的同步。希望某個儲存庫的每一次 Cloud Agent 執行都能看到的 skill，應放進該儲存庫的 `.cursor/skills/`。

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

再跑一次會替換 Replica 的資料夾和 `replica-tools/`，同一位置的其他 skill 不動。

在對話裡輸入 `/`，選 `replica` 或 `replica-recon`。這會把 skill 附到一則訊息上。若要整段工作階段都用它，把它開成 Custom Mode：macOS 上是 Option+Enter，Windows 上是 Alt+Enter。

範本留在 skill 資料夾裡。Python 工具只有一份共用複本。安裝之後，它們在 skill 資料夾旁邊的 `replica-tools/`。如果是從這個儲存庫的取出目錄跑，把 `REPLICA_HOME` 設成該取出目錄，skill 就會用那裡的 `tools/`。Python 3.8 或更新版本。不需要用 pip 安裝任何東西。

## 在 Grok Bot 裡安裝

把下面這段當作整則訊息送出去：

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

之後的步驟寫在 [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md)。簡要說：把本儲存庫複製到 `/home/box/replica-skill`（可用 `REPLICA_HOME` 改路徑），執行 `grok-bot/install.sh`，再把 `grok-bot/skills/*/SKILL.md` 裡的每個檔案存成一項 skill。名稱、說明和正文都按原文複製。Grok Bot 的一項 skill 就是這一個檔案。工具和範本留在磁碟上，skill 用絕對路徑呼叫，例如 `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`。

一個專案的研究筆記放在 `/workspace/<project-slug>/replica/`。一旦某一步開始寫應用，`replica/` 就放進你的程式碼儲存庫。程式碼改動交給該 GitHub 儲存庫上的 Cursor cloud coding agent，工作裡要帶上它需要的 `replica/` 檔案。登入、付款、購買網域、輸入正式金鑰，都由你自己做。

## 工具

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

它們都不存取網路。`imgdiff.py` 比的是版面，不是顏色，所以換品牌不會被算成差距。`parity.py` 給 must、should、could 加權，partial 算一半，你故意跳過的列不計分。`reviews.py` 丟掉沒有連結的列。`sweep.py` 在原作的名稱、網域或顏色還留在目錄樹裡時，擋住發布。`listing.py` 檢查商店限制，並拒絕你的商店文案裡出現原作名稱。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## 目錄

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

你的專案檔案放在 `replica/`，不要放進本儲存庫。

## 細則

**它重做的是功能和互動方式，而且是淨室。** 它研究應用做什麼、人怎樣走完，然後全部重寫。它不複製目標的原始碼、專有素材、標誌、商標、文案或私有 API。

**它只讀你被允許讀的東西。** 公開頁面和你自己的帳號。它不在登入後面抓取，不違反網站條款，不登入別人的帳號，也不繞過付費牆。如果你的帳號條款禁止用它來做競品，skill 會說明這一點，並只使用公開來源。

**發布之前先換品牌。** 新名稱、新配色、新標誌、新文案。清掃不乾淨，replica-deploy 不上線。

**「複製任何應用」指的是功能和流程。** 不是內容、關係網路，也不是應用自己持有的授權。音樂應用的播放器、播放清單和分享可以重做。它的曲庫不能複製。

**不保證複製得一模一樣。** 預約工具是數週的工作。試算表引擎不是。動手之前 replica-recon 會估規模，replica-diff 會給你一個數字。

**創業這項 skill 不編造。** 沒有虛構的評價、引文或數字。每條說法都有連結，並寫明樣本量。

**出售之前先核對。** 跑 replica-brand 列出的商標檢查，讀你用過的每項服務的條款，牽涉到錢就在發布前找律師談。這不是法律意見。

## 授權

MIT。原始著作權屬於 Jake Schincariol。這次移植為 letmefind 加了一行著作權。見 [LICENSE](../../LICENSE)。
