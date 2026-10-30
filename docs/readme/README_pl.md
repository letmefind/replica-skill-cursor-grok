<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · **Polski** · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Umiejętności Replica dla Cursor i Grok Bot

</div>

Jedenaście umiejętności, które odtwarzają to, co robi aplikacja, plus jedna, `replica`, która trzyma je w kolejności. Za darmo, MIT. Poza Pythonem 3.8 i biblioteką standardową nie ma czego instalować.

Praca jest czysta. Umiejętności oglądają funkcje i drogę, którą człowiek przez nie przechodzi, a potem piszą wszystko od nowa. Nie biorą kodu, znaku, tekstu ani treści celu. Drobny druk jest na dole, a umiejętności go powtarzają.

## Źródło

Metodę, szablony i sześć narzędzi w Pythonie napisał Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

To repozytorium jest portem tego zestawu od letmefind, dla Cursor i dla Grok Bot. Tekst umiejętności wzięto z https://github.com/letmefind/replica-skill, forka repozytorium powyżej.

Inne zestawy tego samego autora: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Dwanaście

| umiejętność | co robi |
| --- | --- |
| `replica` | Kolejność, pliki, które każdy krok czyta i zapisuje, oraz który krok uruchomić. |
| `replica-recon` | Ekrany, przepływy, części, model danych, macierz funkcji. Strony publiczne, zrzuty, karty sklepu i własne konto. |
| `replica-architect` | Stos, schemat bazy i API. |
| `replica-design` | Role koloru, pismo, odstępy, części, jako tokeny, z własnymi materiałami. |
| `replica-build` | Aplikacja, ekran po ekranie, z mapy rozpoznania. |
| `replica-backend` | Logowanie, baza, płatności i integracje. |
| `replica-test` | Każdy przepływ, przeklikany i przetestowany. |
| `replica-diff` | Ocena zgodności i to, czego jeszcze brakuje. |
| `replica-entrepreneur` | To, czego prawdziwi ludzie nie lubią, jako poprawki i kąt pozycjonowania. |
| `replica-brand` | Własna nazwa i własna marka, potem zamiatanie resztek. |
| `replica-launch` | Strona wejściowa, ceny i karta sklepu. |
| `replica-deploy` | Na żywo, na własnej domenie, po przejściu kontroli wstępnej. |

Uruchamiaj w tej kolejności:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Aplikacja do umawiania, taka, w której wysyłasz link i ktoś rezerwuje godzinę, idzie tak.

1. **replica-recon** czyta centrum pomocy, stronę cen, kartę sklepu i publiczne przejścia. Po własnym koncie klikasz ty. Wychodzą `replica/recon.md` i `replica/features.csv`. Rynek partnerów jest poza zakresem: to ich sieć, nie funkcja.
2. **replica-architect** wybiera nudny, zarządzany stos, pisze schemat (wraz z ograniczeniem, żeby dwóch gości nie wzięło tego samego slotu) i układa budowę wokół przepływu rezerwacji.
3. **replica-design** mierzy zrzuty na tokeny: role koloru, pismo, odstępy, wybór daty, przycisk slotu. Otwarte ikony, otwarty font, własne słowa.
4. **replica-build** buduje skorupę, potem przepływ rezerwacji, potem każdy ekran z jego stanami i po drodze odhacza `features.csv`.
5. **replica-backend** dodaje rejestrację, kalendarz przez własne API dostawcy z twoimi kluczami, płatności w trybie testowym i mail z przypomnieniem.
6. **replica-test** pisze plan z przepływów, testy od końca do końca dla szczęśliwej drogi i brzegów, oraz błędy według wagi, aż nie zostanie otwarte S1 ani S2.
7. **replica-diff** wystawia ocenę. Brak rzeczy koniecznej znaczy: nie do wydania.
8. **replica-entrepreneur** czyta prawdziwe recenzje i tylko prawdziwe. Każdy cytat jest skopiowany z wiersza, który podałeś, razem z URL tego wiersza.
9. **replica-brand** nadaje nazwę po tym, jak kontrole znaku towarowego i domeny naprawdę poszły, i zamiata drzewo, aż z oryginału nic nie zostanie.
10. **replica-launch** pisze stronę wejściową wokół kąta, ustawia ceny wobec publicznej strony cen (z datą, kiedy ją czytano) i sprawdza kartę sklepu.
11. **replica-deploy** odpala kontrolę wstępną i, kiedy powiesz, że można, wydaje.

Każdą umiejętność da się uruchomić osobno. replica-entrepreneur na aplikacji, której jeszcze nie zacząłeś, to rozsądny sposób, żeby zdecydować, czy ją budować.

## Instalacja dla Cursor

Cursor ładuje umiejętności projektu z `.cursor/skills/<name>/SKILL.md` i `.agents/skills/<name>/SKILL.md`, a dla użytkownika z `~/.cursor/skills/` i `~/.agents/skills/`. Nazwa folderu jest nazwą umiejętności. W nagłówku `name` i `description` są wymagane, a `name` musi pasować do folderu.

Ten instalator używa `.cursor/skills` (projekt) i `~/.cursor/skills` (`--global`). Umiejętności projektu jadą z repozytorium. Umiejętności użytkownika w `~/.cursor/skills/` zostają na tej maszynie, dopóki nie włączysz synchronizacji dla Cloud Agents w Settings, Agents. Umiejętność, która ma być przy każdym uruchomieniu Cloud Agent dla repozytorium, należy do `.cursor/skills/` tego repozytorium.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Ponowne uruchomienie podmienia foldery Replica i `replica-tools/`, a innych umiejętności w tym miejscu nie rusza.

W czacie wpisz `/` i wybierz `replica` albo `replica-recon`. To doczepia umiejętność do jednej wiadomości. Żeby została na całą sesję, zacznij ją jako Custom Mode: Option+Enter na macOS albo Alt+Enter na Windows.

Szablony zostają w folderze umiejętności. Narzędzia w Pythonie są jedną wspólną kopią. Po instalacji leżą w `replica-tools/` obok folderów umiejętności. Z kopii tego repozytorium ustaw `REPLICA_HOME` na tę kopię, a umiejętności wezmą stamtąd `tools/`. Python 3.8 albo nowszy. Nic do instalacji przez pip.

## Instalacja dla Grok Bot

Wyślij to jako całą wiadomość:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Dalsze kroki są w [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Krótko: sklonuj to repozytorium do `/home/box/replica-skill` (ścieżkę zmienia `REPLICA_HOME`), uruchom `grok-bot/install.sh`, potem zapisz każdy plik z `grok-bot/skills/*/SKILL.md` jako umiejętność. Nazwa, opis i treść są kopiowane dosłownie. Umiejętność Grok Bot to ten jeden plik. Narzędzia i szablony zostają na dysku, a umiejętności wołają je ścieżką bezwzględną, na przykład `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Notatki z badania projektu leżą w `/workspace/<project-slug>/replica/`. Gdy krok zaczyna pisać samą aplikację, `replica/` jest w twoim repozytorium z kodem. Zmiany kodu idą do Cursor cloud coding agent na tym repozytorium GitHub, jako zadanie, które zawiera potrzebne pliki `replica/`. Logujesz się, płacisz, kupujesz domenę i wpisujesz żywe klucze sam.

## Narzędzia

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Żadne nie używa sieci. `imgdiff.py` porównuje układ, nie kolor, więc zmiana marki nie liczy się przeciw tobie. `parity.py` waży must, should i could, liczy partial jako połowę i nie punktuje wiersza, który pominąłeś celowo. `reviews.py` odrzuca wiersz bez linku. `sweep.py` blokuje wydanie, dopóki nazwa, domena albo kolory oryginału są w drzewie. `listing.py` sprawdza limity sklepu i odrzuca nazwę oryginału w twojej karcie.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Układ

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

Pliki twojego projektu idą do `replica/`, nie do tego repozytorium.

## Drobny druk

**Odtwarza funkcje i wzorce obsługi, czysto.** Patrzy, co aplikacja robi i jak ludzie przez nią przechodzą, potem pisze wszystko od nowa. Nie kopiuje kodu źródłowego celu, jego zamkniętych materiałów, znaków, znaków towarowych, tekstu ani prywatnych API.

**Czyta tylko to, co wolno ci czytać.** Strony publiczne i własne konto. Nie zbiera za logowaniem ani wbrew zasadom strony, nie wchodzi na cudze konto i nie przechodzi paywalla. Jeśli zasady twojego konta zabraniają budować na nim konkurenta, umiejętność tak mówi i zostaje przy źródłach publicznych.

**Przed wydaniem zmienia markę.** Nowa nazwa, nowa paleta, nowy znak, nowe słowa. replica-deploy nie wydaje, dopóki zamiatanie nie jest czyste.

**«Sklonuj dowolną aplikację» znaczy funkcje i przepływ.** Nie treść, nie sieć i nie licencje, które aplikacja posiada. Odtwarzacz, listy i udostępnianie aplikacji muzycznej da się zbudować. Jej katalogu sklonować się nie da.

**Nie ma obietnicy idealnego klona.** Narzędzie do rezerwacji to tygodnie. Silnik arkusza to nie to. replica-recon szacuje rozmiar, zanim zaczniesz, a replica-diff daje liczbę.

**Umiejętność o przedsięwzięciu niczego nie zmyśla.** Żadnych zmyślonych recenzji, cytatów ani liczb. Każde twierdzenie ma link, a wielkość próby jest podana.

**Sprawdź, zanim sprzedasz.** Odpal kontrole znaku towarowego, które wymienia replica-brand, przeczytaj zasady wszystkiego, czego użyłeś, i pogadaj z prawnikiem przed wydaniem, jeśli w grze są pieniądze. To nie jest porada prawna.

## Licencja

MIT. Pierwotne prawa ma Jake Schincariol. Port dodaje linię praw dla letmefind. Zobacz [LICENSE](../../LICENSE).
