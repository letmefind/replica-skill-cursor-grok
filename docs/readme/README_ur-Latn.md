<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · **Roman Urdu** · [Română](README_ro.md)

# Cursor aur Grok Bot ke liye Replica skills

</div>

Giyarah skills jo ek app kya karti hai usay dobara banati hain, aur ek skill, `replica`, jo unhein silsile mein rakhti hai. Muft, MIT. Python 3.8 aur standard library ke ilawa kuch install karne ko nahi.

Kaam saaf kamre wala hai. Skills features dekhte hain aur yeh ke koi un se kaise guzarta hai, phir sab kuch naye siray se likhte hain. Target ka code, logo, lafz, ya content nahi lete. Barik lafz neeche hain, aur skills unhein dohrate hain.

## Credit

Tareeqa, templates, aur chhe Python tools Jake Schincariol ke hain:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Yeh repository us pack ka letmefind wala port hai, Cursor ke liye aur Grok Bot ke liye. Skill ka matan https://github.com/letmefind/replica-skill se liya gaya, jo upar wali repository ka fork hai.

Usi author ke doosre packs: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Barah

| skill | kya karta hai |
| --- | --- |
| `replica` | Silsila, har qadam kaun si files parhta aur likhta hai, aur agla qadam kaun sa hai. |
| `replica-recon` | Screens, flows, hisse, data model, feature ki jadwal. Aam safhe, screenshots, store ki listing, aur aapka apna account. |
| `replica-architect` | Stack, database ka schema, aur API. |
| `replica-design` | Rang ke role, type, fasle, hisse, tokens ki surat mein, aap ke apne assets ke sath. |
| `replica-build` | App, screen dar screen, recon ke nakshay se. |
| `replica-backend` | Sign-in, database, payments, aur jornay. |
| `replica-test` | Har flow, click karke aur test karke. |
| `replica-diff` | Ek barabari ka number, aur jo abhi bhi kami hai. |
| `replica-entrepreneur` | Asli users ko jo napasand hai, usay sudhaar aur ek position ke zaavie mein. |
| `replica-brand` | Aapka apna naam aur brand, phir bachi hui cheezon ki jhaaru. |
| `replica-launch` | Landing page, qeemat, aur store ki listing. |
| `replica-deploy` | Zinda, aap ke domain par, jab pehle wali jaanch guzar jaye. |

Is silsile mein chalayen:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Ek appointment wali app, jismain aap link bhejte hain aur koi waqt book karta hai, aise chalti hai.

1. **replica-recon** help center, qeemat ka safha, store ki listing, aur aam walkthroughs parhta hai. Aap apne account mein click karte hain. Nikalta hai `replica/recon.md` aur `replica/features.csv`. Partner wala bazaar daire se bahar hai: woh unka network hai, koi feature nahi.
2. **replica-architect** ek sada, managed stack chunta hai, schema likhta hai (ek constraint ke sath taake do mehman ek hi slot na lein), aur build ko booking ke flow ke gird tartib deta hai.
3. **replica-design** screenshots ko tokens mein napta hai: rang ke role, type, fasle, tareekh ka picker, slot ka button. Khule icons, khula font, aap ke apne alfaaz.
4. **replica-build** pehle khol banata hai, phir booking ka flow, phir har screen us ki halaton ke sath, aur chalte chalte `features.csv` par nishan lagata hai.
5. **replica-backend** sign-up, provider ki apni API se calendar aap ki keys ke sath, test mode mein payment, aur yaad dilane wali email jorta hai.
6. **replica-test** flows se plan likhta hai, khush raaste aur kinaro ke liye end-to-end tests, aur bugs shiddat ke hisaab se, jab tak koi S1 ya S2 khula na rahe.
7. **replica-diff** number deta hai. Zaroori cheez ki kami ka matlab hai: nahi chhoot sakta.
8. **replica-entrepreneur** asli reviews parhta hai, sirf asli. Har quote us line se copy hota hai jo aap ne di, us line ke URL ke sath.
9. **replica-brand** naam tab rakhta hai jab trademark aur domain ki jaanch sach mein chal chuki ho, phir daraKht jhaarta hai jab tak asal ka kuch na bache.
10. **replica-launch** us zaavie ke gird landing page likhta hai, aam qeemat ke safhe ke muqable qeemat lagata hai (jis tareekh par parha, woh likhta hai), aur store ki listing check karta hai.
11. **replica-deploy** pehle wali jaanch chalata hai, aur jab aap kahen ke chalo, tab chhorta hai.

Koi bhi ek skill alag chal sakti hai. Jo app aap ne abhi shuru nahi ki, us par replica-entrepreneur yeh tay karne ka seedha tareeqa hai ke banana chahiye ya nahi.

## Cursor ke liye install

Cursor project ki skills `.cursor/skills/<name>/SKILL.md` aur `.agents/skills/<name>/SKILL.md` se leta hai, aur aap ke user ke liye `~/.cursor/skills/` aur `~/.agents/skills/` se. Folder ka naam skill ka naam hai. Sarname mein `name` aur `description` lazmi hain, aur `name` folder se milna chahiye.

Yeh installer `.cursor/skills` (project) aur `~/.cursor/skills` (`--global`) istemal karta hai. Project ki skills repository ke sath chalti hain. `~/.cursor/skills/` ki user skills us machine par rehti hain jab tak aap Settings, Agents mein Cloud Agents ki sync na chala dein. Jo skill aap har Cloud Agent run par us repository ke liye chahte hain, woh us repository ke `.cursor/skills/` mein honi chahiye.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Dobara chalane se Replica ke folders aur `replica-tools/` badal jate hain, aur wahan ki doosri skills apni jagah rehti hain.

Chat mein `/` likhen aur `replica` ya `replica-recon` chunen. Yeh skill ek message se jud jati hai. Poori session ke liye rakhne ko use Custom Mode ki tarah shuru karein: macOS par Option+Enter, Windows par Alt+Enter.

Templates skill ke folder mein rehti hain. Python tools ek hi shared copy hain. Install ke baad woh skill folders ke bagal `replica-tools/` mein hoti hain. Is repository ki checkout se `REPLICA_HOME` us checkout par set karein, to skills wahan ki `tools/` istemal karti hain. Python 3.8 ya us se naya. pip se kuch install nahi.

## Grok Bot ke liye install

Yeh, poora message banakar bhejein:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Us ke baad ke qadam [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md) mein hain. Mukhtasar: is repository ko `/home/box/replica-skill` par clone karein (`REPLICA_HOME` raasta badal deta hai), `grok-bot/install.sh` chalayen, phir `grok-bot/skills/*/SKILL.md` ki har file ko skill ki tarah save karein. Naam, description, aur jism jyon ka tyon copy hota hai. Grok Bot ki skill wohi ek file hai. Tools aur templates disk par rehti hain, aur skills unhein mutlaq raaste se bulati hain, maslan `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Ek project ke research notes `/workspace/<project-slug>/replica/` par hote hain. Jab koi qadam khud application likhne lage, `replica/` aap ke code repository mein hota hai. Code ki tabdeeli us GitHub repository par Cursor cloud coding agent ko di jati hai, aise kaam ki surat mein jismein zaroori `replica/` files shamil hon. Sign-in, adaigi, domain kharidna, aur zinda keys likhna aap khud karte hain.

## Tools

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Koi bhi network istemal nahi karti. `imgdiff.py` layout muqabla karta hai, rang nahi, is liye rebrand aap ke khilaf nahi gina jata. `parity.py` must, should, aur could ko wazan deta hai, partial ko aadha ginta hai, aur jis line ko aap jaan bujh kar chhor dein usay number nahi deta. `reviews.py` bina link wali line phenk deta hai. `sweep.py` launch rokta hai jab tak asal ka naam, domain, ya rang daraKht mein hon. `listing.py` store ki haden check karta hai aur aap ki listing mein asal ka naam radd karta hai.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Tarkib

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

Aap ke project ki files `replica/` mein jati hain, is repository mein nahi.

## Barik lafz

**Yeh kaam aur istemal ke tareeqe dobara banata hai, saaf kamre mein.** Dekhta hai app kya karti hai aur log us se kaise guzarte hain, phir sab kuch naye siray se likhta hai. Target ka source code, band assets, logos, trademarks, lafz, ya private API copy nahi karta.

**Sirf woh parhta hai jo aap ko parhne ki ijazat hai.** Aam safhe aur aapka apna account. Login ke peeche nahi khodta, site ki sharton ke khilaf nahi jata, kisi aur ke account mein nahi jata, aur paid deewar ke paar nahi nikalta. Agar aap ke account ki sharten competitor banane se rokti hon, skill yeh keh deti hai aur aam zariyon par rehti hai.

**Launch se pehle brand badalta hai.** Naya naam, naya rang, naya logo, naye alfaaz. Jab tak jhaaru saaf na ho, replica-deploy nahi chhorta.

**"Koi bhi app clone karo" ka matlab features aur flow hai.** Content nahi, network nahi, aur woh licences nahi jo app ke paas hon. Music app ka player, playlists, aur sharing dobara ban sakte hain. Uska catalogue clone nahi ho sakta.

**Mukammal clone ka wada nahi.** Booking ka tool hafte ka kaam hai. Spreadsheet ka engine nahi. Shuru karne se pehle replica-recon size batata hai, aur replica-diff ek number deta hai.

**Karobar wali skill kuch nahi gharti.** Banayi hui reviews, quotes, ya numbers nahi. Har daawe ka link hai, aur sample ka size likha hota hai.

**Bechne se pehle dekhen.** Jo trademark checks replica-brand likhta hai unhein chalayen, jo cheez istemal ki us ki sharten parhen, aur agar paisa beech mein ho to launch se pehle wakeel se baat karein. Yeh qanooni mashwara nahi.

## Licence

MIT. Asal copyright Jake Schincariol ki hai. Port letmefind ke liye ek copyright line jorta hai. Dekhen [LICENSE](../../LICENSE).
