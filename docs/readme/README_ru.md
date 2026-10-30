<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · **Русский** · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Навыки Replica для Cursor и Grok Bot

</div>

Одиннадцать навыков, которые заново собирают то, что делает приложение, и один навык, `replica`, который держит их в порядке. Бесплатно, MIT. Кроме Python 3.8 и стандартной библиотеки ставить нечего.

Работа чистая: навыки смотрят на функции и на то, как человек через них проходит, а потом пишут всё заново. Код, знак, текст и содержимое цели они не берут. Оговорки внизу, и навыки их повторяют.

## Откуда

Метод, шаблоны и шесть инструментов на Python сделал Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Этот репозиторий: порт того набора от letmefind для Cursor и для Grok Bot. Текст навыков взят из https://github.com/letmefind/replica-skill, форка репозитория выше.

Другие наборы того же автора: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Двенадцать

| навык | что делает |
| --- | --- |
| `replica` | Порядок, какие файлы читает и пишет каждый шаг, и какой шаг запускать. |
| `replica-recon` | Экраны, потоки, части, модель данных, таблица функций. Открытые страницы, снимки, карточки магазина и свой аккаунт. |
| `replica-architect` | Стек, схема базы и API. |
| `replica-design` | Роли цвета, шрифт, отступы, части, в виде токенов, со своими материалами. |
| `replica-build` | Приложение, экран за экраном, по карте разведки. |
| `replica-backend` | Вход, база, платежи и интеграции. |
| `replica-test` | Каждый поток, пройденный кликами и тестами. |
| `replica-diff` | Оценка совпадения и то, чего ещё нет. |
| `replica-entrepreneur` | То, что реальные люди не любят, в виде правок и угла позиционирования. |
| `replica-brand` | Своё имя и свой бренд, затем выметание остатков. |
| `replica-launch` | Посадочная страница, цены и карточка магазина. |
| `replica-deploy` | В эфире, на своём домене, после предварительной проверки. |

Запускай в таком порядке:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Приложение для записи, где делишься ссылкой и кто-то берёт время, идёт так.

1. **replica-recon** читает справку, страницу цен, карточку магазина и открытые обходы. По своему аккаунту кликаешь ты. На выходе `replica/recon.md` и `replica/features.csv`. Партнёрская площадка вне рамок: это их сеть, а не функция.
2. **replica-architect** берёт скучный управляемый стек, пишет схему (включая ограничение, чтобы два гостя не заняли один слот) и выстраивает сборку вокруг потока записи.
3. **replica-design** мерит снимки в токены: роли цвета, шрифт, отступы, выбор даты, кнопка слота. Открытые значки, открытый шрифт, свои слова.
4. **replica-build** собирает оболочку, потом поток записи, потом каждый экран с его состояниями и по ходу отмечает `features.csv`.
5. **replica-backend** добавляет регистрацию, календарь через собственный API поставщика с твоими ключами, платежи в тестовом режиме и письмо-напоминание.
6. **replica-test** пишет план по потокам, сквозные тесты для удачного пути и краёв, и дефекты по тяжести, пока не останется открытых S1 или S2.
7. **replica-diff** ставит оценку. Нет обязательного: выпускать нельзя.
8. **replica-entrepreneur** читает настоящие отзывы и только настоящие. Каждая цитата скопирована из строки, которую дал ты, вместе с URL этой строки.
9. **replica-brand** даёт имя после того, как проверки товарного знака и домена реально прошли, и метёт дерево, пока от оригинала ничего не останется.
10. **replica-launch** пишет посадочную вокруг угла, ставит цены против открытой страницы цен (с датой, когда её читали) и проверяет карточку магазина.
11. **replica-deploy** гоняет предварительную проверку и, когда ты говоришь «можно», выпускает.

Любой навык можно запустить отдельно. replica-entrepreneur на приложении, которое ты ещё не начинал, разумный способ решить, стоит ли его делать.

## Установка для Cursor

Cursor берёт навыки проекта из `.cursor/skills/<name>/SKILL.md` и `.agents/skills/<name>/SKILL.md`, а для пользователя из `~/.cursor/skills/` и `~/.agents/skills/`. Имя папки и есть имя навыка. В шапке обязательны `name` и `description`, и `name` должен совпадать с папкой.

Этот установщик использует `.cursor/skills` (проект) и `~/.cursor/skills` (`--global`). Навыки проекта едут вместе с репозиторием. Пользовательские навыки в `~/.cursor/skills/` остаются на той машине, пока не включишь синхронизацию для Cloud Agents в Settings, Agents. Навык, который должен быть на каждом запуске Cloud Agent для репозитория, кладут в `.cursor/skills/` этого репозитория.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Повторный запуск заменяет папки Replica и `replica-tools/` и не трогает остальные навыки на месте.

В чате набери `/` и выбери `replica` или `replica-recon`. Навык прикрепится к одному сообщению. Чтобы он держался всю сессию, начни его как Custom Mode: Option+Enter на macOS или Alt+Enter на Windows.

Шаблоны остаются в папке навыка. Инструменты на Python лежат одной общей копией. После установки они в `replica-tools/` рядом с папками навыков. Из копии этого репозитория поставь `REPLICA_HOME` на эту копию, и навыки возьмут `tools/` оттуда. Python 3.8 или новее. Через pip ставить нечего.

## Установка для Grok Bot

Отправь это целиком, как всё сообщение:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Дальнейшие шаги в [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Коротко: склонируй этот репозиторий в `/home/box/replica-skill` (путь меняет `REPLICA_HOME`), запусти `grok-bot/install.sh` и сохрани каждый файл из `grok-bot/skills/*/SKILL.md` как навык. Имя, описание и текст копируются дословно. Навык Grok Bot и есть этот один файл. Инструменты и шаблоны остаются на диске, навыки зовут их абсолютным путём, например `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Заметки исследования проекта лежат в `/workspace/<project-slug>/replica/`. Как только шаг пишет само приложение, `replica/` живёт в твоём репозитории с кодом. Изменения кода отдаются Cursor cloud coding agent на том репозитории GitHub, задачей, в которую входят нужные файлы `replica/`. Вход, оплата, покупка домена и ввод боевых ключей остаются за тобой.

## Инструменты

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Ни один не ходит в сеть. `imgdiff.py` сравнивает раскладку, а не цвет, так что смена бренда тебе не в минус. `parity.py` взвешивает must, should и could, считает partial за половину и не оценивает строку, которую ты пропустил нарочно. `reviews.py` выбрасывает строку без ссылки. `sweep.py` держит выпуск, пока в дереве остаются имя, домен или цвета оригинала. `listing.py` проверяет пределы магазина и отвергает имя оригинала в твоей карточке.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Раскладка

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

Файлы твоего проекта клади в `replica/`, не в этот репозиторий.

## Оговорки

**Он заново собирает функции и приёмы интерфейса, чисто.** Смотрит, что делает приложение и как люди через него идут, потом пишет всё заново. Исходный код цели, её закрытые материалы, знаки, товарные знаки, текст и закрытые API он не копирует.

**Он читает только то, что тебе можно читать.** Открытые страницы и свой аккаунт. Он не собирает данные за входом и против правил сайта, не входит в чужой аккаунт и не проходит платную стену. Если правила твоего аккаунта запрещают строить на нём конкурента, навык так и говорит и остаётся на открытых источниках.

**Перед выпуском он меняет бренд.** Новое имя, новая палитра, новый знак, новые слова. replica-deploy не выпускает, пока выметание не чистое.

**«Клонировать любое приложение» значит функции и поток.** Не содержимое, не сеть и не лицензии, которыми владеет приложение. Плеер, списки и общий доступ музыкального приложения собрать можно. Его каталог клонировать нельзя.

**Обещания идеального клона нет.** Инструмент записи это недели. Движок таблицы нет. replica-recon оценивает размер до старта, replica-diff даёт число.

**Навык про дело не выдумывает.** Никаких придуманных отзывов, цитат и чисел. У каждого утверждения есть ссылка, и размер выборки назван.

**Проверь, прежде чем продавать.** Прогони проверки товарного знака, которые перечисляет replica-brand, прочитай правила всего, чем пользовался, и поговори с юристом до выпуска, если на кону деньги. Это не юридическая консультация.

## Лицензия

MIT. Исходные права у Jake Schincariol. Порт добавляет строку прав для letmefind. См. [LICENSE](../../LICENSE).
