<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · **Italiano**
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Skill Replica per Cursor e Grok Bot

</div>

Undici skill che ricostruiscono ciò che fa un'applicazione, più uno skill, `replica`, che tiene l'ordine. Gratis, MIT, e non c'è da installare nulla oltre a Python 3.8 e alla libreria standard.

Il lavoro è in camera bianca. Gli skill studiano le funzioni e il percorso di una persona attraverso di esse, poi riscrivono tutto. Non prendono il codice, il logo, il testo o i contenuti del bersaglio. Le note legali sono in fondo, e gli skill le ripetono.

## Credito

Il metodo, i modelli e i sei strumenti Python sono di Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Questo repository è il port di letmefind per Cursor e per Grok Bot. Il testo degli skill è stato preso da https://github.com/letmefind/replica-skill, un fork del repository sopra.

Altri pacchetti dello stesso autore: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## I dodici

| skill | che cosa fa |
| --- | --- |
| `replica` | L'ordine, i file che ogni passo legge e scrive, e quale passo eseguire. |
| `replica-recon` | Schermate, flussi, componenti, modello dei dati, matrice delle funzioni. Pagine pubbliche, screenshot, schede dello store e il tuo account. |
| `replica-architect` | Stack, schema del database e API. |
| `replica-design` | Ruoli di colore, tipo, spazi, componenti, come token, con i tuoi asset. |
| `replica-build` | L'applicazione, schermata per schermata, dalla mappa di recon. |
| `replica-backend` | Accesso, database, pagamenti e integrazioni. |
| `replica-test` | Ogni flusso, percorso a clic e testato. |
| `replica-diff` | Un punteggio di parità, e ciò che manca ancora. |
| `replica-entrepreneur` | Ciò che odiano gli utenti veri, trasformato in correzioni e in un angolo di posizionamento. |
| `replica-brand` | Un nome e un marchio tuoi, poi una spazzata di ciò che resta. |
| `replica-launch` | Pagina di atterraggio, prezzi e scheda dello store. |
| `replica-deploy` | Online, sul tuo dominio, dopo che il controllo preliminare è passato. |

In quest'ordine:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Un'applicazione per gli appuntamenti, di quelle in cui condividi un link e qualcuno prenota un orario, va così.

1. **replica-recon** legge il centro assistenza, la pagina dei prezzi, la scheda dello store e i percorsi pubblici. Tu clicchi nel tuo account. Ne escono `replica/recon.md` e `replica/features.csv`. Un marketplace di partner è fuori: è la loro rete, non una funzione.
2. **replica-architect** sceglie uno stack semplice e gestito, scrive lo schema (compreso un vincolo perché due ospiti non prenotino lo stesso slot) e ordina la costruzione intorno al flusso di prenotazione.
3. **replica-design** misura gli screenshot in token: ruoli di colore, tipo, spazi, il selettore di data, il pulsante dello slot. Icone aperte, un font aperto, le tue parole.
4. **replica-build** costruisce il guscio, poi il flusso di prenotazione, poi ogni schermata con i suoi stati, e spunta `features.csv` man mano.
5. **replica-backend** aggiunge l'iscrizione, il calendario tramite l'API ufficiale del fornitore con le tue chiavi, i pagamenti in modalità di prova e l'email di promemoria.
6. **replica-test** scrive un piano dai flussi, test end-to-end per il percorso felice e i bordi, e bug per gravità finché non resta aperto nessun S1 o S2.
7. **replica-diff** assegna il punteggio. Un must-have mancante vuol dire: non si pubblica.
8. **replica-entrepreneur** legge recensioni vere e solo recensioni vere. Ogni citazione è copiata da una riga che hai fornito tu, con l'URL di quella riga.
9. **replica-brand** gli dà un nome, dopo che i controlli su marchio e dominio sono stati davvero eseguiti, e spazza l'albero finché non resta nulla dell'originale.
10. **replica-launch** scrive la pagina di atterraggio intorno all'angolo, mette i prezzi di fronte alla pagina pubblica dei prezzi (con la data in cui è stata letta) e controlla la scheda dello store.
11. **replica-deploy** esegue il controllo preliminare e, quando dici di andare, pubblica.

Si può eseguire un solo skill. replica-entrepreneur, su un'applicazione che non hai ancora iniziato, è un modo ragionevole per decidere se costruirla.

## Installazione per Cursor

Cursor carica gli skill di un progetto da `.cursor/skills/<name>/SKILL.md` e `.agents/skills/<name>/SKILL.md`, e per il tuo utente da `~/.cursor/skills/` e `~/.agents/skills/`. Il nome della cartella è il nome dello skill. `name` e `description` nel frontmatter sono obbligatori, e `name` deve coincidere con la cartella.

Questo installer usa `.cursor/skills` (progetto) e `~/.cursor/skills` (`--global`). Gli skill di progetto viaggiano con il repository. Quelli in `~/.cursor/skills/` restano su quella macchina finché non attivi la sincronizzazione per Cloud Agents in Settings, Agents. Uno skill che vuoi a ogni esecuzione di Cloud Agent su un repository va in `.cursor/skills/` di quel repository.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Eseguirlo di nuovo sostituisce le cartelle Replica e `replica-tools/`, e lascia stare gli altri skill.

Nella chat, scrivi `/` e scegli `replica` o `replica-recon`. Questo attacca lo skill a un messaggio. Per tenerlo per tutta la sessione, aprilo come Custom Mode: Option+Enter su macOS, Alt+Enter su Windows.

I modelli restano nella cartella dello skill. Gli strumenti Python sono una sola copia. Dopo l'installazione stanno in `replica-tools/` accanto alle cartelle degli skill. Da un checkout di questo repository, imposta `REPLICA_HOME` su quel checkout e gli skill usano `tools/` lì. Python 3.8 o più recente. Niente da installare con pip.

## Installazione per Grok Bot

Invia questo, come messaggio intero:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

I passi successivi sono in [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). In breve: clona questo repository in `/home/box/replica-skill` (`REPLICA_HOME` cambia il percorso), esegui `grok-bot/install.sh` e salva ogni file in `grok-bot/skills/*/SKILL.md` come skill. Nome, descrizione e corpo si copiano così come sono. Uno skill di Grok Bot è quel solo file. Strumenti e modelli restano sul disco e gli skill li chiamano con il percorso assoluto, per esempio `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Le note di ricerca di un progetto stanno in `/workspace/<project-slug>/replica/`. Quando un passo scrive l'applicazione, `replica/` sta nel tuo repository di codice. Le modifiche al codice vanno a un Cursor cloud coding agent su quel repository GitHub, come un compito che include i file `replica/` necessari. Accesso, pagamento, acquisto del dominio e chiavi live li fai tu.

## Strumenti

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Nessuno usa la rete. `imgdiff.py` confronta la disposizione, non il colore, così un rebrand non ti pesa contro. `parity.py` pesa must, should e could, conta partial come metà e non dà punteggio a una riga che hai lasciato fuori di proposito. `reviews.py` scarta ogni riga senza link. `sweep.py` blocca un lancio finché nome, dominio o colori dell'originale sono ancora nell'albero. `listing.py` controlla i limiti dello store e rifiuta il nome dell'originale nella tua scheda.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Disposizione

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

I file del tuo progetto vanno in `replica/`, non in questo repository.

## Note legali

**Ricostruisce funzioni e schemi d'uso, in camera bianca.** Studia che cosa fa l'applicazione e come le persone ci si muovono, poi riscrive tutto. Non copia il codice sorgente, gli asset proprietari, i logo, i marchi, il testo o le API private del bersaglio.

**Legge solo ciò che ti è permesso leggere.** Pagine pubbliche e il tuo account. Non raschia dietro un accesso né contro i termini di un sito, non entra nell'account di qualcun altro e non supera un paywall. Se i termini del tuo account vietano di usarlo per costruire un concorrente, lo skill lo dice e resta sulle fonti pubbliche.

**Cambia marca prima del lancio.** Nome nuovo, palette nuova, logo nuovo, parole nuove. replica-deploy non pubblica finché lo sweep non è pulito.

**«Clonare qualsiasi applicazione» vuol dire le funzioni e il flusso.** Non i contenuti, la rete o le licenze che un'applicazione possiede. Si può ricostruire il lettore, le playlist e la condivisione di un'app musicale. Non il suo catalogo.

**Nessuna promessa di un clone perfetto.** Uno strumento di prenotazione sono settimane. Un motore di fogli di calcolo no. replica-recon dà la dimensione prima di iniziare, e replica-diff ti dà un numero.

**Lo skill entrepreneur non inventa.** Niente recensioni, citazioni o numeri inventati. Ogni affermazione ha un link, e la dimensione del campione è indicata.

**Controlla prima di vendere.** Esegui i controlli sui marchi che elenca replica-brand, leggi i termini di tutto ciò che hai usato e parla con un avvocato prima del lancio se ci sono soldi in gioco. Questo non è un parere legale.

## Licenza

MIT. Il copyright originale è di Jake Schincariol. Il port aggiunge una riga per letmefind. Vedi [LICENSE](../../LICENSE).
