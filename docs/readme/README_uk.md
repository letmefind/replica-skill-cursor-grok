<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · **Українська** · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Навички Replica для Cursor і Grok Bot

</div>

Одинадцять навичок, які наново збирають те, що робить застосунок, і одна навичка, `replica`, яка тримає їх у порядку. Безкоштовно, MIT. Окрім Python 3.8 і стандартної бібліотеки ставити нічого.

Робота чиста: навички дивляться на функції і на те, як людина через них проходить, а потім пишуть усе заново. Код, знак, текст і вміст цілі вони не беруть. Застереження внизу, і навички їх повторюють.

## Звідки

Метод, шаблони і шість інструментів на Python зробив Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Цей репозиторій є портом того набору від letmefind для Cursor і для Grok Bot. Текст навичок узято з https://github.com/letmefind/replica-skill, форка репозиторію вище.

Інші набори того самого автора: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Дванадцять

| навичка | що робить |
| --- | --- |
| `replica` | Порядок, які файли читає і пише кожен крок, і який крок запускати. |
| `replica-recon` | Екрани, потоки, частини, модель даних, таблиця функцій. Відкриті сторінки, знімки, картки крамниці і власний обліковий запис. |
| `replica-architect` | Стек, схема бази і API. |
| `replica-design` | Ролі кольору, шрифт, відступи, частини, у вигляді токенів, зі своїми матеріалами. |
| `replica-build` | Застосунок, екран за екраном, за картою розвідки. |
| `replica-backend` | Вхід, база, платежі й інтеграції. |
| `replica-test` | Кожен потік, пройдений кліками і тестами. |
| `replica-diff` | Оцінка збігу і те, чого ще бракує. |
| `replica-entrepreneur` | Те, що справжні люди не люблять, у вигляді правок і кута позиціонування. |
| `replica-brand` | Власне ім'я і власний бренд, потім вимітання залишків. |
| `replica-launch` | Посадкова сторінка, ціни і картка крамниці. |
| `replica-deploy` | Наживо, на власному домені, після попередньої перевірки. |

Запускай у такому порядку:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Застосунок для запису, де ділишся посиланням і хтось бере час, іде так.

1. **replica-recon** читає довідку, сторінку цін, картку крамниці і відкриті огляди. Власним обліковим записом клікаєш ти. На виході `replica/recon.md` і `replica/features.csv`. Партнерський майданчик поза межами: це їхня мережа, а не функція.
2. **replica-architect** бере нудний керований стек, пише схему (включно з обмеженням, щоб двоє гостей не зайняли один слот) і вибудовує збірку навколо потоку запису.
3. **replica-design** міряє знімки в токени: ролі кольору, шрифт, відступи, вибір дати, кнопка слота. Відкриті значки, відкритий шрифт, свої слова.
4. **replica-build** збирає оболонку, потім потік запису, потім кожен екран із його станами і по ходу позначає `features.csv`.
5. **replica-backend** додає реєстрацію, календар через власний API постачальника з твоїми ключами, платежі в тестовому режимі і лист-нагадування.
6. **replica-test** пише план за потоками, наскрізні тести для вдалого шляху і країв, і дефекти за тяжкістю, поки не лишиться відкритих S1 чи S2.
7. **replica-diff** ставить оцінку. Немає обов'язкового: випускати не можна.
8. **replica-entrepreneur** читає справжні відгуки і тільки справжні. Кожна цитата скопійована з рядка, який дав ти, разом із URL цього рядка.
9. **replica-brand** дає ім'я після того, як перевірки торговельної марки і домену справді пройшли, і мете дерево, поки від оригіналу нічого не лишиться.
10. **replica-launch** пише посадкову навколо кута, ставить ціни проти відкритої сторінки цін (з датою, коли її читали) і перевіряє картку крамниці.
11. **replica-deploy** жене попередню перевірку і, коли ти кажеш «можна», випускає.

Будь-яку навичку можна запустити окремо. replica-entrepreneur на застосунку, який ти ще не починав, розумний спосіб вирішити, чи варто його робити.

## Встановлення для Cursor

Cursor бере навички проєкту з `.cursor/skills/<name>/SKILL.md` і `.agents/skills/<name>/SKILL.md`, а для користувача з `~/.cursor/skills/` і `~/.agents/skills/`. Ім'я теки і є ім'я навички. У шапці обов'язкові `name` і `description`, і `name` має збігатися з текою.

Цей встановлювач використовує `.cursor/skills` (проєкт) і `~/.cursor/skills` (`--global`). Навички проєкту їдуть разом із репозиторієм. Користувацькі навички в `~/.cursor/skills/` лишаються на тій машині, поки не ввімкнеш синхронізацію для Cloud Agents у Settings, Agents. Навичка, яка має бути на кожному запуску Cloud Agent для репозиторію, лежить у `.cursor/skills/` цього репозиторію.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Повторний запуск замінює теки Replica і `replica-tools/` і не чіпає решту навичок на місці.

У чаті набери `/` і вибери `replica` або `replica-recon`. Навичка прикріпиться до одного повідомлення. Щоб вона трималася всю сесію, почни її як Custom Mode: Option+Enter на macOS або Alt+Enter на Windows.

Шаблони лишаються в теці навички. Інструменти на Python лежать однією спільною копією. Після встановлення вони в `replica-tools/` поруч із теками навичок. Із копії цього репозиторію постав `REPLICA_HOME` на цю копію, і навички візьмуть `tools/` звідти. Python 3.8 або новіший. Через pip ставити нічого.

## Встановлення для Grok Bot

Надішли це цілком, як усе повідомлення:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Подальші кроки в [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Коротко: склонуй цей репозиторій у `/home/box/replica-skill` (шлях змінює `REPLICA_HOME`), запусти `grok-bot/install.sh` і збережи кожен файл із `grok-bot/skills/*/SKILL.md` як навичку. Ім'я, опис і текст копіюються дослівно. Навичка Grok Bot і є цей один файл. Інструменти і шаблони лишаються на диску, навички кличуть їх абсолютним шляхом, наприклад `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Нотатки дослідження проєкту лежать у `/workspace/<project-slug>/replica/`. Щойно крок пише сам застосунок, `replica/` живе у твоєму репозиторії з кодом. Зміни коду віддаються Cursor cloud coding agent на тому репозиторії GitHub, завданням, у яке входять потрібні файли `replica/`. Вхід, оплата, купівля домену і введення бойових ключів лишаються за тобою.

## Інструменти

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Жоден не ходить у мережу. `imgdiff.py` порівнює розкладку, а не колір, тож зміна бренду тобі не в мінус. `parity.py` зважує must, should і could, рахує partial за половину і не оцінює рядок, який ти пропустив навмисно. `reviews.py` викидає рядок без посилання. `sweep.py` тримає випуск, поки в дереві лишаються ім'я, домен або кольори оригіналу. `listing.py` перевіряє межі крамниці і відхиляє ім'я оригіналу у твоїй картці.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Розкладка

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

Файли твого проєкту клади в `replica/`, не в цей репозиторій.

## Застереження

**Він наново збирає функції і прийоми інтерфейсу, чисто.** Дивиться, що робить застосунок і як люди через нього йдуть, потім пише все заново. Вихідний код цілі, її закриті матеріали, знаки, торговельні марки, текст і закриті API він не копіює.

**Він читає лише те, що тобі можна читати.** Відкриті сторінки і власний обліковий запис. Він не збирає дані за входом і проти правил сайту, не входить у чужий обліковий запис і не проходить платну стіну. Якщо правила твого облікового запису забороняють будувати на ньому конкурента, навичка так і каже і лишається на відкритих джерелах.

**Перед випуском він змінює бренд.** Нове ім'я, нова палітра, новий знак, нові слова. replica-deploy не випускає, поки вимітання не чисте.

**«Клонувати будь-який застосунок» означає функції і потік.** Не вміст, не мережу і не ліцензії, якими володіє застосунок. Програвач, списки і спільний доступ музичного застосунку зібрати можна. Його каталог клонувати не можна.

**Обіцянки ідеального клону немає.** Інструмент запису це тижні. Рушій таблиці ні. replica-recon оцінює розмір до старту, replica-diff дає число.

**Навичка про справу не вигадує.** Жодних вигаданих відгуків, цитат і чисел. У кожного твердження є посилання, і розмір вибірки названо.

**Перевір, перш ніж продавати.** Прожени перевірки торговельної марки, які перелічує replica-brand, прочитай правила всього, чим користувався, і поговори з юристом до випуску, якщо на кону гроші. Це не юридична консультація.

## Ліцензія

MIT. Вихідні права в Jake Schincariol. Порт додає рядок прав для letmefind. Див. [LICENSE](../../LICENSE).
