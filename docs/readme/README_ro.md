<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · **Română**

# Skill-uri Replica pentru Cursor și Grok Bot

</div>

Unsprezece skill-uri care refac ceea ce face o aplicație, plus un skill, `replica`, care le ține în ordine. Gratuit, MIT. În afară de Python 3.8 și biblioteca standard, nu ai ce instala.

Lucrul e de cameră curată. Skill-urile studiază funcțiile și drumul unui om prin ele, apoi scriu totul din nou. Nu iau codul, sigla, textul sau conținutul țintei. Litera mică e jos, iar skill-urile o repetă.

## Sursa

Metoda, șabloanele și cele șase unelte Python sunt ale lui Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Acest depozit este portul letmefind al acelui pachet, pentru Cursor și pentru Grok Bot. Textul skill-urilor a fost luat din https://github.com/letmefind/replica-skill, un fork al depozitului de mai sus.

Alte pachete ale aceluiași autor: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Cele douăsprezece

| skill | ce face |
| --- | --- |
| `replica` | Ordinea, fișierele pe care le citește și le scrie fiecare pas, și ce pas urmează. |
| `replica-recon` | Ecrane, fluxuri, piese, model de date, matrice de funcții. Pagini publice, capturi, fișe de magazin și contul tău. |
| `replica-architect` | Stiva, schema bazei și API. |
| `replica-design` | Roluri de culoare, literă, spațiere, piese, ca tokeni, cu materialele tale. |
| `replica-build` | Aplicația, ecran cu ecran, din harta de recunoaștere. |
| `replica-backend` | Autentificare, bază, plăți și legături. |
| `replica-test` | Fiecare flux, parcurs cu clicuri și testat. |
| `replica-diff` | Un scor de paritate și ce mai lipsește. |
| `replica-entrepreneur` | Ce urăsc utilizatorii reali, transformat în corecturi și un unghi de poziție. |
| `replica-brand` | Un nume și o marcă ale tale, apoi o măturare a resturilor. |
| `replica-launch` | Pagină de aterizare, preț și fișa din magazin. |
| `replica-deploy` | În aer, pe domeniul tău, după ce trece verificarea dinainte. |

Rulează-le în ordinea asta:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

O aplicație de programări, de felul în care trimiți un link și cineva rezervă o oră, merge așa.

1. **replica-recon** citește centrul de ajutor, pagina de prețuri, fișa din magazin și parcursurile publice. Tu dai clic prin contul tău. Ies `replica/recon.md` și `replica/features.csv`. O piață de parteneri e în afara subiectului: e rețeaua lor, nu o funcție.
2. **replica-architect** alege o stivă banală și gestionată, scrie schema (inclusiv o constrângere ca doi oaspeți să nu ia același interval) și ordonează construcția în jurul fluxului de rezervare.
3. **replica-design** măsoară capturile în tokeni: roluri de culoare, literă, spațiere, selectorul de dată, butonul de interval. Pictograme deschise, un font deschis, cuvintele tale.
4. **replica-build** construiește coaja, apoi fluxul de rezervare, apoi fiecare ecran cu stările lui, și bifează `features.csv` pe parcurs.
5. **replica-backend** adaugă înscrierea, calendarul prin API-ul propriu al furnizorului cu cheile tale, plățile în mod de probă și mailul de aducere aminte.
6. **replica-test** scrie un plan din fluxuri, teste de la un capăt la altul pentru drumul fericit și margini, și defecte după gravitate până nu mai rămâne niciun S1 sau S2 deschis.
7. **replica-diff** dă nota. Dacă lipsește ceva obligatoriu, nu se poate publica.
8. **replica-entrepreneur** citește recenzii reale și numai recenzii reale. Fiecare citat e copiat dintr-un rând pe care l-ai dat tu, cu URL-ul acelui rând.
9. **replica-brand** îi dă un nume după ce verificările de marcă și de domeniu au rulat cu adevărat, apoi mătură arborele până nu mai rămâne nimic din original.
10. **replica-launch** scrie pagina de aterizare în jurul unghiului, pune prețurile față de pagina publică de prețuri (cu data la care a fost citită) și verifică fișa din magazin.
11. **replica-deploy** rulează verificarea dinainte și, când spui să meargă, publică.

Poți rula oricare skill de unul singur. replica-entrepreneur, pe o aplicație pe care n-ai început-o, e un fel chibzuit de a hotărî dacă o construiești.

## Instalare pentru Cursor

Cursor încarcă skill-urile unui proiect din `.cursor/skills/<name>/SKILL.md` și `.agents/skills/<name>/SKILL.md`, iar pentru utilizatorul tău din `~/.cursor/skills/` și `~/.agents/skills/`. Numele dosarului este numele skill-ului. `name` și `description` din preambul sunt obligatorii, iar `name` trebuie să se potrivească cu dosarul.

Acest instalator folosește `.cursor/skills` (proiect) și `~/.cursor/skills` (`--global`). Skill-urile de proiect călătoresc cu depozitul. Skill-urile de utilizator din `~/.cursor/skills/` rămân pe mașina aceea până pornești sincronizarea pentru Cloud Agents în Settings, Agents. Un skill pe care îl vrei la fiecare rulare de Cloud Agent pentru un depozit stă în `.cursor/skills/` al acelui depozit.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

O rulare din nou înlocuiește dosarele Replica și `replica-tools/`, și lasă celelalte skill-uri la locul lor.

În chat, tastează `/` și alege `replica` sau `replica-recon`. Asta lipește skill-ul de un mesaj. Ca să rămână toată sesiunea, pornește-l ca Custom Mode: Option+Enter pe macOS, sau Alt+Enter pe Windows.

Șabloanele rămân în dosarul skill-ului. Uneltele Python sunt o singură copie comună. După instalare stau în `replica-tools/`, lângă dosarele skill-urilor. Dintr-o copie a acestui depozit, pune `REPLICA_HOME` pe acea copie și skill-urile folosesc `tools/` de acolo. Python 3.8 sau mai nou. Nimic de instalat cu pip.

## Instalare pentru Grok Bot

Trimite asta, ca întregul mesaj:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Pașii de după sunt în [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Pe scurt: clonează acest depozit în `/home/box/replica-skill` (schimbi calea cu `REPLICA_HOME`), rulează `grok-bot/install.sh`, apoi salvează fiecare fișier din `grok-bot/skills/*/SKILL.md` ca skill. Numele, descrierea și corpul se copiază întocmai. Un skill Grok Bot este acel singur fișier. Uneltele și șabloanele rămân pe disc, iar skill-urile le cheamă cu cale absolută, de pildă `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Notele de cercetare ale unui proiect stau în `/workspace/<project-slug>/replica/`. Când un pas începe să scrie aplicația, `replica/` trăiește în depozitul tău de cod. Schimbările de cod sunt date unui Cursor cloud coding agent pe acel depozit GitHub, ca o sarcină care cuprinde fișierele `replica/` de care are nevoie. Tu te autentifici, plătești, cumperi domeniul și tastezi cheile vii.

## Unelte

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Niciuna nu folosește rețeaua. `imgdiff.py` compară așezarea, nu culoarea, așa că o schimbare de marcă nu se pune împotriva ta. `parity.py` ponderează must, should și could, numără partial ca jumătate și nu punctează un rând pe care l-ai sărit intenționat. `reviews.py` aruncă orice rând fără legătură. `sweep.py` ține publicarea cât timp numele, domeniul sau culorile originalului sunt încă în arbore. `listing.py` verifică limitele magazinului și respinge numele originalului în fișa ta.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Așezare

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

Fișierele proiectului tău merg în `replica/`, nu în acest depozit.

## Litera mică

**Reface funcționalitatea și tiparele de folosire, în cameră curată.** Studiază ce face aplicația și cum trec oamenii prin ea, apoi scrie totul din nou. Nu copiază codul sursă al țintei, materialele închise, siglele, mărcile, textul sau API-urile private.

**Citește doar ce ai voie să citești.** Pagini publice și contul tău. Nu răzuiește în spatele unei autentificări și nici împotriva termenilor unui site, nu intră în contul altcuiva și nu trece de un perete de plată. Dacă termenii contului tău interzic să-l folosești ca să construiești un concurent, skill-ul o spune și rămâne la surse publice.

**Schimbă marca înainte de publicare.** Nume nou, paletă nouă, siglă nouă, cuvinte noi. replica-deploy nu publică până măturarea nu e curată.

**«Clonează orice aplicație» înseamnă funcțiile și fluxul.** Nu conținutul, rețeaua sau licențele pe care le deține o aplicație. Poți reface playerul, listele și partajarea unei aplicații de muzică. Nu poți clona catalogul.

**Nicio promisiune de clonă perfectă.** O unealtă de rezervări înseamnă săptămâni. Un motor de foaie de calcul nu. replica-recon măsoară mărimea înainte să începi, iar replica-diff îți dă un număr.

**Skill-ul de întreprindere nu inventează.** Fără recenzii, citate sau numere născocite. Fiecare afirmație are o legătură, iar mărimea eșantionului e scrisă.

**Verifică înainte să vinzi.** Rulează verificările de marcă pe care le enumeră replica-brand, citește termenii a tot ce ai folosit și vorbește cu un avocat înainte de publicare dacă sunt bani în joc. Asta nu e sfat juridic.

## Licență

MIT. Dreptul de autor original este al lui Jake Schincariol. Portul adaugă o linie de drept de autor pentru letmefind. Vezi [LICENSE](../../LICENSE).
