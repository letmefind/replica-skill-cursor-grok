<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · **한국어** · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Cursor와 Grok Bot을 위한 Replica skills

</div>

앱이 하는 일을 다시 만드는 skill 열한 개와, 그 순서를 지키는 skill `replica` 하나. 무료이고 MIT입니다. Python 3.8과 표준 라이브러리 말고 설치할 것은 없습니다.

작업은 클린룸입니다. skill은 기능과, 사람이 그 기능을 어떻게 지나가는지를 본 다음 전부 새로 씁니다. 대상의 코드, 로고, 문장, 내용은 가져오지 않습니다. 세칙은 맨 아래에 있고, skill도 같은 말을 반복합니다.

## 출처

방법, 템플릿, 여섯 개의 Python 도구는 Jake Schincariol의 것입니다.

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

이 저장소는 그 묶음을 Cursor와 Grok Bot용으로 옮긴 letmefind의 port입니다. skill 본문은 위 저장소의 fork인 https://github.com/letmefind/replica-skill 에서 가져왔습니다.

같은 저자의 다른 묶음: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## 열둘

| skill | 하는 일 |
| --- | --- |
| `replica` | 순서, 각 단계가 읽고 쓰는 파일, 다음에 돌릴 단계. |
| `replica-recon` | 화면, 흐름, 구성 요소, 데이터 모델, 기능 표. 공개 페이지, 스크린샷, 스토어 목록, 본인 계정. |
| `replica-architect` | 스택, 데이터베이스 스키마, API. |
| `replica-design` | 색 역할, 글꼴, 간격, 구성 요소를 토큰으로. 자산은 본인 것. |
| `replica-build` | 정찰 지도를 따라 화면마다 앱을 만든다. |
| `replica-backend` | 인증, 데이터베이스, 결제, 연동. |
| `replica-test` | 모든 흐름을 직접 눌러 보고 테스트한다. |
| `replica-diff` | 일치 점수와, 아직 빠진 것. |
| `replica-entrepreneur` | 실제 사용자가 싫어하는 점을 고침과 포지션의 각도로 바꾼다. |
| `replica-brand` | 자기 이름과 브랜드를 정한 뒤 남은 흔적을 훑는다. |
| `replica-launch` | 랜딩 페이지, 가격, 스토어 소개. |
| `replica-deploy` | 사전 점검을 통과한 뒤 자기 도메인에 올린다. |

이 순서로 돌립니다.

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

링크를 보내면 상대가 시간을 잡는, 그런 예약 앱이라면 이렇게 갑니다.

1. **replica-recon**은 도움말, 가격 페이지, 스토어 목록, 공개된 사용 설명을 읽습니다. 본인 계정은 직접 눌러 봅니다. 나오는 파일은 `replica/recon.md`와 `replica/features.csv`입니다. 파트너 장터는 범위 밖입니다. 그것은 그들의 네트워크이지, 기능이 아닙니다.
2. **replica-architect**는 수수한 관리형 스택을 고르고 스키마를 씁니다. 손님 둘이 같은 시간을 잡지 못하게 하는 제약도 넣습니다. 만드는 순서는 예약 흐름을 중심으로 잡습니다.
3. **replica-design**은 스크린샷을 재서 토큰으로 만듭니다. 색 역할, 글꼴, 간격, 날짜 선택, 시간 버튼. 아이콘은 열린 것, 글꼴도 열린 것, 말은 자기 말입니다.
4. **replica-build**는 껍데기를 만들고, 이어서 예약 흐름을, 그다음 각 화면과 상태를 만들며 `features.csv`에 표시합니다.
5. **replica-backend**은 가입, 본인 키로 쓰는 제공자 공식 API의 달력, 테스트 모드 결제, 알림 메일을 더합니다.
6. **replica-test**는 흐름으로 계획을 쓰고, 잘 되는 길과 가장자리에 끝까지 가는 테스트를 두며, 심각도별로 결함을 남겨 S1이나 S2가 열려 있지 않을 때까지 갑니다.
7. **replica-diff**가 점수를 매깁니다. 꼭 있어야 하는 것이 빠지면 내보낼 수 없습니다.
8. **replica-entrepreneur**는 실제 리뷰만 읽습니다. 인용은 직접 준 행에서 그대로 베끼고, 그 행의 URL을 붙입니다.
9. **replica-brand**는 상표와 도메인 확인을 실제로 돌린 뒤에 이름을 붙이고, 원본이 하나도 남지 않을 때까지 트리를 훑습니다.
10. **replica-launch**는 그 각도로 랜딩 페이지를 쓰고, 공개 가격 페이지와 맞춰 가격을 정하며(읽은 날짜를 적고), 스토어 소개를 검사합니다.
11. **replica-deploy**는 사전 점검을 돌리고, 올리라고 말할 때 배포합니다.

skill은 하나만 따로 돌려도 됩니다. 아직 시작하지 않은 앱에서 replica-entrepreneur를 돌리는 것은, 만들지 말지를 정하는 괜찮은 방법입니다.

## Cursor에 설치

Cursor는 프로젝트에서 `.cursor/skills/<name>/SKILL.md`와 `.agents/skills/<name>/SKILL.md`로, 사용자 쪽에서는 `~/.cursor/skills/`와 `~/.agents/skills/`로 skill을 읽습니다. 폴더 이름이 skill 이름입니다. 프론트매터의 `name`과 `description`은 필수이고, `name`은 폴더와 같아야 합니다.

이 설치 스크립트는 `.cursor/skills`(프로젝트)와 `~/.cursor/skills`(`--global`)를 씁니다. 프로젝트 skill은 저장소와 함께 갑니다. `~/.cursor/skills/`의 사용자 skill은 Settings, Agents에서 Cloud Agents 동기화를 켜기 전까지 그 기계에 남습니다. 어떤 저장소의 Cloud Agent가 돌 때마다 보이게 할 skill은 그 저장소의 `.cursor/skills/`에 둡니다.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

다시 실행하면 Replica 폴더와 `replica-tools/`는 바뀌고, 그 자리에 있는 다른 skill은 그대로입니다.

채팅에서 `/`를 치고 `replica` 또는 `replica-recon`을 고릅니다. skill은 그 메시지 하나에 붙습니다. 세션 내내 쓰려면 Custom Mode로 시작합니다. macOS는 Option+Enter, Windows는 Alt+Enter입니다.

템플릿은 skill 폴더에 둡니다. Python 도구는 공유본 하나입니다. 설치 뒤에는 skill 폴더 옆의 `replica-tools/`에 있습니다. 이 저장소를 받아 둔 곳에서 쓰려면 `REPLICA_HOME`을 그 체크아웃으로 두면, skill이 그곳의 `tools/`를 씁니다. Python 3.8 이상. pip로 설치할 것은 없습니다.

## Grok Bot에 설치

다음을 메시지 전체로 보냅니다.

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

그다음 단계는 [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md)에 있습니다. 짧게 말하면, 이 저장소를 `/home/box/replica-skill`에 clone하고(`REPLICA_HOME`으로 바꿉니다), `grok-bot/install.sh`를 실행한 뒤 `grok-bot/skills/*/SKILL.md`의 각 파일을 skill로 저장합니다. 이름, 설명, 본문은 그대로 복사합니다. Grok Bot skill은 그 파일 하나입니다. 도구와 템플릿은 디스크에 남고, skill은 절대 경로로 부릅니다. 예는 `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`입니다.

프로젝트의 조사 노트는 `/workspace/<project-slug>/replica/`에 둡니다. 애플리케이션을 쓰는 단계부터 `replica/`는 본인 코드 저장소에 있습니다. 코드 변경은 그 GitHub 저장소의 Cursor cloud coding agent에게 맡기고, 필요한 `replica/` 파일을 작업에 넣습니다. 로그인, 결제, 도메인 구매, 실제 키 입력은 직접 합니다.

## 도구

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

어느 것도 네트워크를 쓰지 않습니다. `imgdiff.py`는 색이 아니라 배치를 비교하므로, 브랜드를 바꿔도 손해로 치지 않습니다. `parity.py`는 must, should, could에 가중치를 두고, partial은 반으로 세며, 일부러 건너뛴 행은 채점하지 않습니다. `reviews.py`는 링크가 없는 행을 버립니다. `sweep.py`는 원본의 이름, 도메인, 색이 트리에 남아 있는 동안 출시를 막습니다. `listing.py`는 스토어 제한을 보고, 소개에 원본 이름이 있으면 거절합니다.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## 배치

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

프로젝트 파일은 `replica/`에 두고, 이 저장소에는 넣지 않습니다.

## 세칙

**다시 만드는 것은 기능과 사용 방식이고, 클린룸입니다.** 앱이 무엇을 하는지, 사람이 어떻게 지나가는지를 본 다음 전부 새로 씁니다. 대상의 소스, 독점 자산, 로고, 상표, 문장, 비공개 API는 복사하지 않습니다.

**읽어도 되는 것만 읽습니다.** 공개 페이지와 본인 계정입니다. 로그인 뒤를 긁지 않고, 사이트 약관에 거스르지 않으며, 다른 사람 계정에 들어가지 않고, 유료 벽을 넘지 않습니다. 본인 계정 약관이 경쟁 제품을 만드는 용도를 금하면, skill은 그렇게 말하고 공개된 자료에 머뭅니다.

**출시 전에 브랜드를 바꿉니다.** 새 이름, 새 색, 새 로고, 새 말입니다. 훑기가 깨끗해지기 전에는 replica-deploy가 올리지 않습니다.

**「어떤 앱이든 복제」가 뜻하는 것은 기능과 흐름입니다.** 내용도, 네트워크도, 앱이 가진 사용권도 아닙니다. 음악 앱의 재생기, 재생 목록, 공유는 다시 만들 수 있습니다. 목록 자체는 복제할 수 없습니다.

**똑같은 복제를 약속하지 않습니다.** 예약 도구는 몇 주입니다. 스프레드시트 엔진은 그렇지 않습니다. 시작 전에 replica-recon이 크기를 가늠하고, replica-diff가 숫자를 줍니다.

**창업 skill은 지어내지 않습니다.** 만든 리뷰, 인용, 숫자는 없습니다. 주장마다 링크가 있고, 표본 크기도 적습니다.

**팔기 전에 확인하세요.** replica-brand가 적은 상표 확인을 돌리고, 쓴 것의 약관을 읽고, 돈이 걸리면 출시 전에 변호사와 이야기하세요. 이것은 법률 조언이 아닙니다.

## 라이선스

MIT. 원저작권은 Jake Schincariol의 것입니다. 이 port는 letmefind의 저작권 한 줄을 더합니다. [LICENSE](../../LICENSE)를 보세요.
