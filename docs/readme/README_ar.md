<div align="center" dir="rtl">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · **العربية** · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# مهارات Replica لـ Cursor و Grok Bot

</div>

<div dir="rtl">

إحدى عشرة مهارة تعيد بناء ما يفعله التطبيق، ومهارة واحدة، `replica`، تحفظ ترتيبها. مجانية، برخصة MIT. لا شيء يُثبَّت سوى Python 3.8 والمكتبة القياسية.

العمل غرفة نظيفة. تدرس المهارات الوظائف وطريقة مرور الشخص خلالها، ثم تكتب كل شيء من جديد. لا تأخذ شيفرة الهدف ولا شعاره ولا نصه ولا محتواه. التفاصيل في الأسفل، والمهارات تعيدها.

## المصدر

المنهج والقوالب وأدوات Python الست من عمل Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

هذا المستودع هو نقل letmefind لتلك الحزمة إلى Cursor وإلى Grok Bot. نص المهارات مأخوذ من https://github.com/letmefind/replica-skill، وهو تفريع للمستودع أعلاه.

حزم أخرى للمؤلف نفسه: [Arena](https://github.com/Jakeschincariol/arena-skill)،
[X](https://github.com/Jakeschincariol/x-agent-skill)،
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill)،
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## الاثنتا عشرة

| المهارة | ما تفعله |
| --- | --- |
| `replica` | الترتيب، والملفات التي يقرأها كل خطوة ويكتبها، والخطوة التي تُشغَّل. |
| `replica-recon` | الشاشات، والمسارات، والأجزاء، ونموذج البيانات، وجدول الوظائف. صفحات علنية، ولقطات، وصفحات المتجر، وحسابك أنت. |
| `replica-architect` | المكدس، ومخطط قاعدة البيانات، و API. |
| `replica-design` | أدوار اللون، والخط، والمسافات، والأجزاء، على شكل رموز، بأصولك أنت. |
| `replica-build` | التطبيق، شاشةً شاشة، من خريطة الاستطلاع. |
| `replica-backend` | الدخول، وقاعدة البيانات، والمدفوعات، والربط. |
| `replica-test` | كل مسار، بالنقر والاختبار. |
| `replica-diff` | درجة التطابق، وما يزال ناقصًا. |
| `replica-entrepreneur` | ما يكرهه المستخدمون الحقيقيون، يتحول إلى إصلاحات وزاوية تموضع. |
| `replica-brand` | اسم وعلامة من عندك، ثم كنس لما تبقّى. |
| `replica-launch` | صفحة الهبوط، والتسعير، ونص المتجر. |
| `replica-deploy` | على الهواء، على نطاقك، بعد اجتياز الفحص المسبق. |

شغّلها بهذا الترتيب:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

تطبيق مواعيد، من النوع الذي ترسل فيه رابطًا ويحجز أحدهم وقتًا، يسير هكذا.

1. **replica-recon** يقرأ مركز المساعدة وصفحة الأسعار وصفحة المتجر والجولات العلنية. أنت تنقر عبر حسابك. المخرجات `replica/recon.md` و `replica/features.csv`. سوق الشركاء خارج النطاق: تلك شبكتهم، وليست وظيفة.
2. **replica-architect** يختار مكدسًا عاديًا مُدارًا، ويكتب المخطط (بما فيه قيد يمنع ضيفين من حجز الفتحة نفسها)، ويرتّب البناء حول مسار الحجز.
3. **replica-design** يقيس اللقطات إلى رموز: أدوار اللون، والخط، والمسافات، ومحدد التاريخ، وزر الفتحة. أيقونات مفتوحة، وخط مفتوح، وكلامك أنت.
4. **replica-build** يبني الهيكل، ثم مسار الحجز، ثم كل شاشة بحالاتها، ويعلّم `features.csv` وهو يتقدم.
5. **replica-backend** يضيف التسجيل، والتقويم عبر API الخاص بالمزوّد بمفاتيحك، والمدفوعات في وضع الاختبار، وبريد التذكير.
6. **replica-test** يكتب خطة من المسارات، واختبارات من الطرف إلى الطرف للطريق السهل والحواف، وأعطالًا حسب الشدة حتى لا يبقى S1 أو S2 مفتوحًا.
7. **replica-diff** يضع الدرجة. نقص ما هو لازم يعني أنه غير قابل للنشر.
8. **replica-entrepreneur** يقرأ مراجعات حقيقية ومراجعات حقيقية فقط. كل اقتباس منسوخ من صف قدّمته أنت، مع عنوان ذلك الصف.
9. **replica-brand** يسمّيه بعد أن تُجرى فحوص العلامة والنطاق فعلًا، ثم يكنس الشجرة حتى لا يبقى شيء من الأصل.
10. **replica-launch** يكتب صفحة الهبوط حول الزاوية، ويضع الأسعار مقابل صفحة الأسعار العلنية (مع تاريخ قراءتها)، ويفحص نص المتجر.
11. **replica-deploy** يشغّل الفحص المسبق، وحين تقول انطلق، ينشر.

يمكن تشغيل أي مهارة وحدها. replica-entrepreneur على تطبيق لم تبدأه بعد طريق معقول لتقرر هل تبنيه.

## التثبيت لـ Cursor

يحمّل Cursor مهارات المشروع من `.cursor/skills/<name>/SKILL.md` و `.agents/skills/<name>/SKILL.md`، ولمستخدمك من `~/.cursor/skills/` و `~/.agents/skills/`. اسم المجلد هو اسم المهارة. `name` و `description` في الترويسة لازمان، ويجب أن يطابق `name` المجلد.

يستخدم مثبّت هذا المستودع `.cursor/skills` (للمشروع) و `~/.cursor/skills` (`--global`). مهارات المشروع تسافر مع المستودع. مهارات المستخدم في `~/.cursor/skills/` تبقى على تلك الآلة حتى تشغّل المزامنة لـ Cloud Agents من Settings, Agents. المهارة التي تريدها في كل تشغيل لـ Cloud Agent على مستودع توضع في `.cursor/skills/` لذلك المستودع.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

تشغيله مرة أخرى يستبدل مجلدات Replica و `replica-tools/`، ويترك المهارات الأخرى في مكانها.

في المحادثة اكتب `/` واختر `replica` أو `replica-recon`. ذلك يلصق المهارة برسالة واحدة. لإبقائها طول الجلسة ابدأها كـ Custom Mode: Option+Enter على macOS، أو Alt+Enter على Windows.

القوالب تبقى في مجلد المهارة. أدوات Python نسخة مشتركة واحدة. بعد التثبيت تكون في `replica-tools/` بجانب مجلدات المهارات. من نسخة هذا المستودع اضبط `REPLICA_HOME` على تلك النسخة، فتستخدم المهارات `tools/` هناك. Python 3.8 أو أحدث. لا شيء يُثبَّت بـ pip.

## التثبيت لـ Grok Bot

أرسل هذا، كنص الرسالة كلها:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

الخطوات بعدها في [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). باختصار: استنسخ هذا المستودع إلى `/home/box/replica-skill` (غيّر المسار بـ `REPLICA_HOME`)، شغّل `grok-bot/install.sh`، ثم احفظ كل ملف في `grok-bot/skills/*/SKILL.md` مهارة. الاسم والوصف والمتن تُنسخ كما هي. مهارة Grok Bot هي ذلك الملف الواحد. الأدوات والقوالب تبقى على القرص، والمهارات تناديها بمسار مطلق، مثل `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

ملاحظات البحث لمشروع تكون في `/workspace/<project-slug>/replica/`. حين تبدأ خطوة بكتابة التطبيق، يعيش `replica/` في مستودع شيفرتك. تغييرات الشيفرة تُسلَّم إلى Cursor cloud coding agent على مستودع GitHub ذاك، مهمةً تضم ملفات `replica/` التي يحتاجها. أنت من يسجّل الدخول ويدفع ويشتري النطاق ويكتب المفاتيح الحية.

## الأدوات

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

لا واحدة منها تستخدم الشبكة. `imgdiff.py` يقارن التخطيط لا اللون، فتغيير العلامة لا يُحسب عليك. `parity.py` يزن must و should و could، ويعدّ partial نصفًا، ولا يقيّم صفًا تخطيته عمدًا. `reviews.py` يسقط أي صف بلا رابط. `sweep.py` يمنع النشر ما دام اسم الأصل أو نطاقه أو ألوانه في الشجرة. `listing.py` يفحص حدود المتجر ويرفض اسم الأصل في نصك.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## التخطيط

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

ملفات مشروعك تذهب إلى `replica/`، لا إلى هذا المستودع.

## التفاصيل

**يعيد بناء الوظيفة وأنماط الاستخدام، في غرفة نظيفة.** يدرس ما يفعله التطبيق وكيف يمر الناس خلاله، ثم يكتب كل شيء من جديد. لا ينسخ شيفرة الهدف المصدرية ولا أصوله الخاصة ولا شعاراته ولا علاماته ولا نصه ولا واجهات API الخاصة.

**لا يقرأ إلا ما يُسمح لك بقراءته.** الصفحات العلنية وحسابك. لا يقشط خلف تسجيل الدخول ولا ضد شروط موقع، ولا يدخل حساب شخص آخر، ولا يتجاوز جدار الدفع. إن كانت شروط حسابك تمنع استخدامه لبناء منافس، تقول المهارة ذلك وتلتزم بالمصادر العلنية.

**يغيّر العلامة قبل النشر.** اسم جديد، ولوحة جديدة، وشعار جديد، وكلام جديد. replica-deploy لا ينشر حتى يكون الكنس نظيفًا.

**«استنساخ أي تطبيق» يعني الوظائف والمسار.** لا المحتوى، ولا الشبكة، ولا التراخيص التي يملكها التطبيق. يمكن إعادة بناء مشغّل تطبيق موسيقى وقوائم التشغيل والمشاركة. لا يمكن استنساخ فهرسه.

**لا وعد بنسخة مطابقة.** أداة حجز أسابيع. محرك جدول ليس كذلك. replica-recon يقدّر الحجم قبل أن تبدأ، و replica-diff يعطيك رقمًا.

**مهارة المشروع لا تخترع.** لا مراجعات ولا اقتباسات ولا أرقام مختلقة. لكل ادعاء رابط، وحجم العينة مكتوب.

**افحص قبل أن تبيع.** شغّل فحوص العلامة التي يسردها replica-brand، واقرأ شروط كل ما استخدمته، وكلّم محاميًا قبل النشر إن كان المال في الميزان. هذا ليس استشارة قانونية.

## الرخصة

MIT. حقوق النشر الأصلية لـ Jake Schincariol. النقل يضيف سطر حقوق لـ letmefind. انظر [LICENSE](../../LICENSE).

</div>
