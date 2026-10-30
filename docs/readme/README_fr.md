<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · **Français** · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Skills Replica pour Cursor et Grok Bot

</div>

Onze skills qui reconstruisent ce que fait une application, plus un skill, `replica`, qui tient l'ordre. Gratuit, MIT, et rien à installer à part Python 3.8 et la bibliothèque standard.

Le travail est en salle blanche. Les skills étudient les fonctions et le chemin d'une personne à travers elles, puis réécrivent tout. Ils ne prennent pas le code, le logo, le texte ni le contenu de la cible. Les mentions légales sont en bas, et les skills les répètent.

## Crédit

La méthode, les modèles et les six outils Python sont de Jake Schincariol :

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Ce dépôt est le port de letmefind pour Cursor et pour Grok Bot. Le texte des skills vient de https://github.com/letmefind/replica-skill, un fork du dépôt ci-dessus.

Autres paquets du même auteur : [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Les douze

| skill | ce qu'il fait |
| --- | --- |
| `replica` | L'ordre, les fichiers que chaque étape lit et écrit, et quelle étape lancer. |
| `replica-recon` | Écrans, parcours, composants, modèle de données, matrice de fonctions. Pages publiques, captures, fiches de store et votre propre compte. |
| `replica-architect` | Stack, schéma de base de données et API. |
| `replica-design` | Rôles de couleur, typo, espacements, composants, en tokens, avec vos propres assets. |
| `replica-build` | L'application, écran par écran, à partir de la carte de recon. |
| `replica-backend` | Auth, base de données, paiements et intégrations. |
| `replica-test` | Chaque parcours, cliqué et testé. |
| `replica-diff` | Un score de parité, et ce qui manque encore. |
| `replica-entrepreneur` | Ce que détestent les vrais utilisateurs, tourné en correctifs et en angle de positionnement. |
| `replica-brand` | Un nom et une marque à vous, puis un balayage des restes. |
| `replica-launch` | Page d'accueil, prix et fiche de store. |
| `replica-deploy` | En ligne, sur votre propre domaine, une fois la prévérification passée. |

Dans cet ordre :

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Une application de rendez-vous, du genre où l'on partage un lien et quelqu'un réserve un créneau, se déroule ainsi.

1. **replica-recon** lit le centre d'aide, la page de prix, la fiche du store et les parcours publics. Vous cliquez dans votre propre compte. Il en sort `replica/recon.md` et `replica/features.csv`. Une place de marché de partenaires est hors sujet : c'est leur réseau, pas une fonction.
2. **replica-architect** choisit une stack simple et gérée, écrit le schéma (y compris une contrainte pour que deux invités ne réservent pas le même créneau) et ordonne la construction autour du parcours de réservation.
3. **replica-design** mesure les captures en tokens : rôles de couleur, typo, espacements, le sélecteur de date, le bouton de créneau. Icônes libres, police libre, vos propres mots.
4. **replica-build** construit la coque, puis le parcours de réservation, puis chaque écran avec ses états, et coche `features.csv` au fur et à mesure.
5. **replica-backend** ajoute l'inscription, le calendrier via l'API officielle du fournisseur avec vos clés, les paiements en mode test et le courriel de rappel.
6. **replica-test** écrit un plan à partir des parcours, des tests de bout en bout pour le chemin heureux et les bords, et des bugs par gravité jusqu'à ce qu'aucun S1 ni S2 ne reste ouvert.
7. **replica-diff** le note. Un must-have manquant veut dire : pas publiable.
8. **replica-entrepreneur** lit de vrais avis, et seulement de vrais avis. Chaque citation est copiée d'une ligne que vous avez fournie, avec l'URL de cette ligne.
9. **replica-brand** le nomme, après que les vérifications de marque et de domaine ont vraiment été faites, puis balaie l'arbre jusqu'à ce qu'il ne reste rien de l'original.
10. **replica-launch** écrit la page d'accueil autour de l'angle, fixe les prix face à la page publique de tarifs (avec la date de lecture) et contrôle la fiche du store.
11. **replica-deploy** lance la prévérification et, quand vous dites d'y aller, publie.

On peut lancer n'importe quel skill seul. replica-entrepreneur, sur une application que vous n'avez pas encore commencée, est une façon raisonnable de décider s'il faut la construire.

## Installer pour Cursor

Cursor charge les skills d'un projet depuis `.cursor/skills/<name>/SKILL.md` et `.agents/skills/<name>/SKILL.md`, et pour votre utilisateur depuis `~/.cursor/skills/` et `~/.agents/skills/`. Le nom du dossier est le nom du skill. `name` et `description` dans le frontmatter sont obligatoires, et `name` doit correspondre au dossier.

Cet installeur utilise `.cursor/skills` (projet) et `~/.cursor/skills` (`--global`). Les skills de projet voyagent avec le dépôt. Ceux de `~/.cursor/skills/` restent sur cette machine jusqu'à ce que vous activiez la synchro pour Cloud Agents dans Settings, Agents. Un skill que vous voulez à chaque exécution de Cloud Agent sur un dépôt va dans `.cursor/skills/` de ce dépôt.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Le relancer remplace les dossiers Replica et `replica-tools/`, et laisse les autres skills en place.

Dans le chat, tapez `/` et choisissez `replica` ou `replica-recon`. Cela attache le skill à un message. Pour le garder toute la session, ouvrez-le en Custom Mode : Option+Enter sur macOS, Alt+Enter sur Windows.

Les modèles restent dans le dossier du skill. Les outils Python sont en un seul exemplaire. Après l'installation, ils sont dans `replica-tools/` à côté des dossiers de skills. Depuis un checkout de ce dépôt, réglez `REPLICA_HOME` sur ce checkout et les skills utilisent `tools/` là. Python 3.8 ou plus récent. Rien à installer avec pip.

## Installer pour Grok Bot

Envoyez ceci, comme message entier :

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

La suite est dans [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). En bref : clonez ce dépôt vers `/home/box/replica-skill` (`REPLICA_HOME` change le chemin), lancez `grok-bot/install.sh`, puis enregistrez chaque fichier de `grok-bot/skills/*/SKILL.md` comme skill. Le nom, la description et le corps sont copiés tels quels. Un skill Grok Bot, c'est ce seul fichier. Les outils et les modèles restent sur le disque et les skills les appellent par chemin absolu, par exemple `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Les notes de recherche d'un projet vivent dans `/workspace/<project-slug>/replica/`. Dès qu'une étape écrit l'application, `replica/` vit dans votre dépôt de code. Les changements de code sont confiés à un Cursor cloud coding agent sur ce dépôt GitHub, sous forme d'une tâche qui inclut les fichiers `replica/` nécessaires. Vous vous connectez, vous payez, vous achetez le domaine et vous saisissez les clés live vous-même.

## Outils

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Aucun n'utilise le réseau. `imgdiff.py` compare la disposition, pas la couleur, pour qu'un changement de marque ne joue pas contre vous. `parity.py` pondère must, should et could, compte partial pour moitié et ne note pas une ligne que vous avez écartée exprès. `reviews.py` écarte toute ligne sans lien. `sweep.py` bloque un lancement tant que le nom, le domaine ou les couleurs de l'original sont encore dans l'arbre. `listing.py` vérifie les limites du store et refuse le nom de l'original dans votre fiche.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Agencement

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

Les fichiers de votre projet vont dans `replica/`, pas dans ce dépôt.

## Mentions

**Il reconstruit les fonctions et les parcours d'usage, en salle blanche.** Il étudie ce que fait l'application et comment les gens s'y déplacent, puis réécrit tout. Il ne copie pas le code source, les assets propriétaires, les logos, les marques, le texte ni les API privées de la cible.

**Il ne lit que ce que vous avez le droit de lire.** Pages publiques et votre propre compte. Il ne moissonne pas derrière une connexion ni contre les conditions d'un site, n'entre pas dans le compte de quelqu'un d'autre et ne franchit pas un paywall. Si les conditions de votre compte interdisent de s'en servir pour construire un concurrent, le skill le dit et s'en tient aux sources publiques.

**Il change de marque avant le lancement.** Nouveau nom, nouvelle palette, nouveau logo, nouveaux mots. replica-deploy ne publie pas tant que le balayage n'est pas propre.

**« Cloner n'importe quelle application » veut dire les fonctions et le flux.** Pas le contenu, le réseau ni les licences qu'une application possède. On peut reconstruire le lecteur, les playlists et le partage d'une application de musique. Pas son catalogue.

**Pas de promesse d'un clone parfait.** Un outil de réservation, c'est des semaines. Un moteur de tableur, non. replica-recon donne la taille avant de commencer, et replica-diff vous donne un nombre.

**Le skill entrepreneur n'invente rien.** Pas d'avis, de citations ni de chiffres inventés. Chaque affirmation a un lien, et la taille de l'échantillon est indiquée.

**Vérifiez avant de vendre.** Lancez les contrôles de marque listés par replica-brand, lisez les conditions de tout ce que vous avez utilisé, et parlez à un avocat avant le lancement s'il y a de l'argent en jeu. Ceci n'est pas un conseil juridique.

## Licence

MIT. Le copyright d'origine est celui de Jake Schincariol. Le port ajoute une ligne pour letmefind. Voir [LICENSE](../../LICENSE).
