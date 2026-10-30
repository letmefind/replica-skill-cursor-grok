<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · **Deutsch** · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Replica-Skills für Cursor und Grok Bot

</div>

Elf Skills, die nachbauen, was eine App tut, plus ein Skill, `replica`, der die Reihenfolge hält. Kostenlos, MIT, und außer Python 3.8 mit der Standardbibliothek ist nichts zu installieren.

Die Arbeit ist Clean-Room. Die Skills sehen sich die Funktionen an und den Weg, den eine Person durch sie nimmt, und schreiben danach alles neu. Code, Logo, Text und Inhalte des Ziels nehmen sie nicht. Das Kleingedruckte steht unten, und die Skills wiederholen es.

## Herkunft

Methode, Vorlagen und die sechs Python-Werkzeuge stammen von Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Dieses Repository ist der Port von letmefind für Cursor und für Grok Bot. Der Skill-Text kommt aus https://github.com/letmefind/replica-skill, einem Fork des Repositorys oben.

Weitere Pakete desselben Autors: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Die zwölf

| Skill | was er tut |
| --- | --- |
| `replica` | Reihenfolge, welche Dateien jeder Schritt liest und schreibt, und welcher Schritt als Nächstes kommt. |
| `replica-recon` | Bildschirme, Abläufe, Bausteine, Datenmodell, Funktionsmatrix. Öffentliche Seiten, Screenshots, Store-Einträge und das eigene Konto. |
| `replica-architect` | Stack, Datenbankschema und API. |
| `replica-design` | Farbrollen, Schrift, Abstände, Bausteine, als Tokens, mit eigenen Assets. |
| `replica-build` | Die App, Bildschirm für Bildschirm, aus der Recon-Karte. |
| `replica-backend` | Anmeldung, Datenbank, Zahlungen und Anbindungen. |
| `replica-test` | Jeder Ablauf, durchgeklickt und getestet. |
| `replica-diff` | Ein Paritätswert, und was noch fehlt. |
| `replica-entrepreneur` | Was echte Nutzer hassen, umgesetzt in Korrekturen und einen Positionierungswinkel. |
| `replica-brand` | Ein eigener Name und eine eigene Marke, danach eine Suche nach Resten. |
| `replica-launch` | Landingpage, Preise und der Store-Text. |
| `replica-deploy` | Live, auf der eigenen Domain, nachdem die Vorprüfung bestanden ist. |

In dieser Reihenfolge:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Eine Termin-App, von der Art, bei der man einen Link teilt und jemand eine Zeit bucht, läuft so.

1. **replica-recon** liest das Hilfe-Center, die Preisseite, den Store-Eintrag und öffentliche Rundgänge. Du klickst dich durch dein eigenes Konto. Heraus kommen `replica/recon.md` und `replica/features.csv`. Ein Partner-Marktplatz liegt außerhalb: das ist deren Netzwerk, keine Funktion.
2. **replica-architect** wählt einen langweiligen, verwalteten Stack, schreibt das Schema (einschließlich einer Bedingung, damit zwei Gäste nicht denselben Slot buchen) und ordnet den Bau um den Buchungsablauf.
3. **replica-design** misst Screenshots in Tokens: Farbrollen, Schrift, Abstände, die Datumsauswahl, den Slot-Button. Offene Icons, eine offene Schrift, eigene Worte.
4. **replica-build** baut die Hülle, dann den Buchungsablauf, dann jeden Bildschirm mit seinen Zuständen, und hakt `features.csv` dabei ab.
5. **replica-backend** ergänzt die Registrierung, den Kalender über die eigene API des Anbieters mit deinen Schlüsseln, Zahlungen im Testmodus und Erinnerungsmails.
6. **replica-test** schreibt einen Plan aus den Abläufen, Ende-zu-Ende-Tests für den guten Weg und die Ränder, und Fehler nach Schwere, bis kein S1 oder S2 mehr offen ist.
7. **replica-diff** bewertet es. Fehlende Must-haves heißen: nicht auslieferbar.
8. **replica-entrepreneur** liest echte Bewertungen und nur echte. Jedes Zitat ist aus einer Zeile kopiert, die du geliefert hast, mit der URL dieser Zeile.
9. **replica-brand** benennt es, nachdem Marken- und Domain-Prüfungen wirklich gelaufen sind, und durchsucht den Baum, bis nichts vom Original übrig ist.
10. **replica-launch** schreibt die Landingpage um den Winkel, setzt Preise gegen die öffentliche Preisseite (mit dem Datum, an dem sie gelesen wurde) und prüft den Store-Text.
11. **replica-deploy** führt die Vorprüfung aus und liefert aus, wenn du sagst, dass es losgeht.

Jeden Skill kann man für sich laufen lassen. replica-entrepreneur, auf einer App, die du noch nicht angefangen hast, ist ein vernünftiger Weg zu entscheiden, ob du bauen sollst.

## Installation für Cursor

Cursor lädt Skills im Projekt aus `.cursor/skills/<name>/SKILL.md` und `.agents/skills/<name>/SKILL.md`, und für dich persönlich aus `~/.cursor/skills/` und `~/.agents/skills/`. Der Ordnername ist der Skill-Name. `name` und `description` in der Präambel sind Pflicht, und `name` muss zum Ordner passen.

Dieses Installationsskript benutzt `.cursor/skills` (Projekt) und `~/.cursor/skills` (`--global`). Projekt-Skills reisen mit dem Repository. Skills in `~/.cursor/skills/` bleiben auf diesem Rechner, bis du die Synchronisation für Cloud Agents unter Settings, Agents einschaltest. Ein Skill, den jeder Cloud-Agent-Lauf für ein Repository sehen soll, gehört in `.cursor/skills/` dieses Repositorys.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Ein zweiter Lauf ersetzt die Replica-Ordner und `replica-tools/` und lässt andere Skills an diesem Ort in Ruhe.

Im Chat `/` tippen und `replica` oder `replica-recon` wählen. Das hängt den Skill an eine Nachricht. Für die ganze Sitzung als Custom Mode starten: Option+Enter unter macOS, Alt+Enter unter Windows.

Vorlagen bleiben im Skill-Ordner. Die Python-Werkzeuge gibt es nur einmal. Nach der Installation liegen sie in `replica-tools/` neben den Skill-Ordnern. Aus einem Checkout dieses Repositorys setzt du `REPLICA_HOME` auf den Checkout, dann benutzen die Skills dort `tools/`. Python 3.8 oder neuer. Nichts per pip installieren.

## Installation für Grok Bot

Schick genau diese Nachricht:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Die Schritte danach stehen in [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Kurz: dieses Repository nach `/home/box/replica-skill` klonen (`REPLICA_HOME` überschreibt den Pfad), `grok-bot/install.sh` ausführen und jede Datei unter `grok-bot/skills/*/SKILL.md` als Skill speichern. Name, Beschreibung und Text werden wörtlich übernommen. Ein Grok-Bot-Skill ist diese eine Datei. Werkzeuge und Vorlagen bleiben auf der Platte, und die Skills rufen sie mit absolutem Pfad auf, zum Beispiel `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Recherche zu einem Projekt liegt unter `/workspace/<project-slug>/replica/`. Sobald ein Schritt die Anwendung schreibt, liegt `replica/` in deinem Code-Repository. Codeänderungen gehen an einen Cursor cloud coding agent auf diesem GitHub-Repository, als Auftrag, der die nötigen `replica/`-Dateien enthält. Anmelden, zahlen, die Domain kaufen und Live-Schlüssel eintippen tust du selbst.

## Werkzeuge

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Keines davon benutzt das Netz. `imgdiff.py` vergleicht das Layout, nicht die Farbe, damit ein Rebrand nicht gegen dich zählt. `parity.py` gewichtet must, should und could, zählt partial als halb und bewertet eine Zeile nicht, die du absichtlich ausgelassen hast. `reviews.py` wirft jede Zeile ohne Link weg. `sweep.py` blockiert einen Launch, solange Name, Domain oder Farben des Originals noch im Baum stehen. `listing.py` prüft die Store-Grenzen und lehnt den Namen des Originals in deinem Eintrag ab.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Aufbau

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

Deine Projektdateien gehören nach `replica/`, nicht in dieses Repository.

## Kleingedrucktes

**Es baut Funktionen und Bedienmuster nach, Clean-Room.** Es sieht, was die App tut und wie Menschen sich durch sie bewegen, und schreibt dann alles neu. Quellcode, proprietäre Assets, Logos, Marken, Texte oder private APIs des Ziels kopiert es nicht.

**Es liest nur, was du lesen darfst.** Öffentliche Seiten und dein eigenes Konto. Es kratzt nicht hinter einem Login und nicht gegen die Bedingungen einer Site, meldet sich nicht in fremden Konten an und kommt nicht an einer Paywall vorbei. Wenn die Bedingungen deines Kontos verbieten, damit einen Wettbewerber zu bauen, sagt der Skill das und bleibt bei öffentlichen Quellen.

**Vor dem Launch kommt ein Rebrand.** Neuer Name, neue Palette, neues Logo, neue Worte. replica-deploy liefert nicht aus, bevor der Sweep sauber ist.

**„Jede App klonen“ heißt die Funktionen und den Ablauf.** Nicht die Inhalte, das Netzwerk oder die Lizenzen, die eine App besitzt. Den Player, Playlists und das Teilen einer Musik-App kann man nachbauen. Den Katalog nicht.

**Kein Versprechen eines perfekten Klons.** Ein Buchungswerkzeug sind Wochen. Eine Tabellen-Engine ist es nicht. replica-recon sagt die Größe, bevor du anfängst, und replica-diff gibt dir eine Zahl.

**Der Entrepreneur-Skill erfindet nichts.** Keine erfundenen Bewertungen, Zitate oder Zahlen. Jede Behauptung hat einen Link, und die Stichprobengröße steht dabei.

**Prüfen, bevor du verkaufst.** Die Markenprüfungen aus replica-brand laufen lassen, die Bedingungen von allem lesen, was du benutzt hast, und mit einer Anwältin oder einem Anwalt sprechen, bevor du startest, wenn Geld im Spiel ist. Das ist keine Rechtsberatung.

## Lizenz

MIT. Das ursprüngliche Copyright liegt bei Jake Schincariol. Der Port ergänzt eine Zeile für letmefind. Siehe [LICENSE](../../LICENSE).
