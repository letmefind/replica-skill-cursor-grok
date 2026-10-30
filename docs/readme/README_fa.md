<div align="center" dir="rtl">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · **فارسی** · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# مهارت‌های Replica برای Cursor و Grok Bot

</div>

<div dir="rtl">

یازده مهارت که کار یک برنامه را از نو می‌سازند، به‌اضافهٔ مهارت `replica` که
ترتیب‌شان را نگه می‌دارد. رایگان، با پروانهٔ MIT. جز پایتون ۳.۸ و کتابخانهٔ
استاندارد، چیزی برای نصب نیست.

روش کار اتاق‌پاک است. مهارت‌ها قابلیت‌ها و مسیر کاربر را می‌خوانند و همه‌چیز
را از نو می‌نویسند. کد برنامهٔ هدف، لوگو، متن و محتوایش مال این کار نیست.
حرف آخر حقوقی پایین همین صفحه است و خود مهارت‌ها هم همان را تکرار می‌کنند.

## اعتبار

روش، قالب‌ها و شش ابزار پایتون را Jake Schincariol نوشته است:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

این مخزن اقتباس letmefind از همان بسته است، برای Cursor و برای Grok Bot.
متن مهارت‌ها از فورک زیر برداشته شده است:

https://github.com/letmefind/replica-skill

بسته‌های دیگر همان نویسنده: [Arena](https://github.com/Jakeschincariol/arena-skill)،
[X](https://github.com/Jakeschincariol/x-agent-skill)،
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill)،
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## دوازده مهارت

| مهارت | کارش |
| --- | --- |
| `replica` | ترتیب، فایل‌هایی که هر قدم می‌خواند و می‌نویسد، و این‌که نوبت کدام قدم است. |
| `replica-recon` | صفحه‌ها، جریان‌ها، قطعه‌ها، مدل داده، جدول قابلیت‌ها. از صفحهٔ عمومی، تصویر، فروشگاه، و حساب خودتان. |
| `replica-architect` | پشته، طرح پایگاه داده، و API. |
| `replica-design` | نقش رنگ، حروف، فاصله و قطعه‌ها، به‌صورت توکن، با دارایی خودتان. |
| `replica-build` | خود برنامه، صفحه به صفحه، از روی نقشهٔ recon. |
| `replica-backend` | ورود، پایگاه داده، پرداخت و اتصال‌ها. |
| `replica-test` | همهٔ جریان‌ها، با کلیک و با تست. |
| `replica-diff` | نمرهٔ برابری، و این‌که چه چیز هنوز جا مانده. |
| `replica-entrepreneur` | چیزی که کاربر واقعی از برنامه بدش می‌آید، تبدیل به اصلاح و زاویهٔ عرضه. |
| `replica-brand` | نام و هویت خودتان، بعد جاروب برای هرچه از اصل مانده. |
| `replica-launch` | صفحهٔ فرود، قیمت، و متن فروشگاه. |
| `replica-deploy` | انتشار روی دامنهٔ خودتان، بعد از بازبینی نهایی. |

ترتیب:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

مثالش یک برنامهٔ نوبت‌دهی است. لینک می‌فرستید، طرف وقت رزرو می‌کند.

1. **replica-recon** مرکز راهنما، صفحهٔ قیمت، صفحهٔ فروشگاه و ویدیوهای عمومی
   را می‌خواند. شما با حساب خودتان کلیک می‌کنید. خروجی `replica/recon.md` و
   `replica/features.csv` است. بازارچه‌ای که شریک‌های خودشان است بیرون از
   محدوده می‌ماند. آن شبکهٔ آن‌هاست، نه یک قابلیت.
2. **replica-architect** یک پشتهٔ ساده و مدیریت‌شده برمی‌دارد، طرح پایگاه را
   می‌نویسد (از جمله قیدی که دو مهمان یک وقت را با هم نگیرند) و ساخت را دور
   جریان رزرو می‌چیند.
3. **replica-design** از روی تصویر، توکن درمی‌آورد: نقش رنگ، اندازهٔ حروف،
   فاصله، انتخابگر تاریخ، دکمهٔ وقت. آیکون آزاد، قلم آزاد، حرف خودتان.
4. **replica-build** پوسته را می‌سازد، بعد جریان رزرو را، بعد هر صفحه را با
   حالت‌هایش، و ردیف‌های `features.csv` را تیک می‌زند.
5. **replica-backend** ثبت‌نام، تقویم از راه API رسمی همان سرویس با کلید
   خودتان، پرداخت در حالت آزمایش، و ایمیل یادآوری را اضافه می‌کند.
6. **replica-test** از روی جریان‌ها برنامهٔ تست می‌نویسد، مسیر خوشحال و
   لبه‌ها را تست می‌کند، و باگ را با شدت ثبت می‌کند تا S1 و S2 باز نماند.
7. **replica-diff** نمره می‌دهد. اگر قابلیت ضروری جا مانده باشد، آمادهٔ
   انتشار نیست.
8. **replica-entrepreneur** فقط نقد واقعی می‌خواند. هر نقل‌قول عین متن یک
   ردیف است که خودتان داده‌اید، با لینک همان ردیف.
9. **replica-brand** اسم می‌گذارد، بعد از این‌که جست‌وجوی علامت تجاری و دامنه
   واقعاً انجام شده باشد، و درخت کد را می‌گردد تا چیزی از اصل نماند.
10. **replica-launch** صفحهٔ فرود را دور همان زاویه می‌نویسد، قیمت را با صفحهٔ
    عمومی قیمت مقایسه می‌کند و تاریخ خواندن را می‌نویسد، و متن فروشگاه را
    بررسی می‌کند.
11. **replica-deploy** بازبینی نهایی را اجرا می‌کند و وقتی خودتان بگویید برو،
    منتشر می‌کند.

هر مهارت را تنهایی هم می‌شود اجرا کرد. replica-entrepreneur روی برنامه‌ای که
هنوز نساخته‌اید راه خوبی است برای این‌که بفهمید اصلاً ارزش ساختن دارد یا نه.

## نصب روی Cursor

Cursor مهارت را از این مسیرها برمی‌دارد: در پروژه
`.cursor/skills/<name>/SKILL.md` و `.agents/skills/<name>/SKILL.md`، و برای
خود کاربر `~/.cursor/skills/` و `~/.agents/skills/`. اسم پوشه همان اسم مهارت
است. در سربرگ، `name` و `description` لازم است و `name` باید با اسم پوشه یکی
باشد.

نصب‌کنندهٔ این مخزن `.cursor/skills` را برای پروژه می‌گذارد و با `--global`
می‌رود سراغ `~/.cursor/skills`. مهارت داخل مخزن همراه همان مخزن می‌رود.
مهارت سطح کاربر روی همان دستگاه می‌ماند تا در تنظیمات، بخش Agents، همگام‌سازی
با Cloud Agents را روشن کنید. اگر می‌خواهید هر بار که Cloud Agent روی یک
مخزن کار می‌کند مهارت را ببیند، بگذاریدش داخل `.cursor/skills/` همان مخزن.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

اجرای دوباره پوشه‌های Replica و `replica-tools/` را عوض می‌کند و به مهارت‌های
دیگر در همان مقصد دست نمی‌زند.

در گفتگو `/` را بزنید و `replica` یا `replica-recon` را انتخاب کنید. مهارت به
همان یک پیام وصل می‌شود. اگر می‌خواهید تا آخر جلسه بماند، به‌صورت Custom Mode
شروعش کنید: در مک Option+Enter، در ویندوز Alt+Enter.

قالب‌ها کنار همان مهارت می‌مانند. ابزارهای پایتون یک نسخهٔ مشترک‌اند. بعد از
نصب در `replica-tools/` کنار پوشهٔ مهارت‌ها هستند. اگر از خود این مخزن اجرا
می‌کنید، `REPLICA_HOME` را روی ریشهٔ مخزن بگذارید تا مهارت‌ها از `tools/`
استفاده کنند. پایتون ۳.۸ به بالا. بسته‌ای برای pip نیست.

## نصب روی Grok Bot

این متن را، همین‌طور که هست، بفرستید:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

قدم‌های بعدی در [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md) است. خلاصه: مخزن
را در `/home/box/replica-skill` کلون کنید (`REPLICA_HOME` مسیر را عوض می‌کند)،
`grok-bot/install.sh` را اجرا کنید، و هر فایل
`grok-bot/skills/*/SKILL.md` را به‌صورت یک مهارت ذخیره کنید. اسم، توضیح و
بدنه عین فایل کپی می‌شود. مهارت Grok Bot همین یک فایل است. ابزار و قالب روی
دیسک می‌مانند و مهارت با مسیر مطلق صدایشان می‌کند، مثلاً
`python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

یادداشت پژوهش هر پروژه در `/workspace/<project-slug>/replica/` است. از جایی
که نوبت نوشتن خود برنامه است، `replica/` داخل مخزن کد شماست. تغییر کد به یک
Cursor cloud coding agent روی همان مخزن گیت‌هاب سپرده می‌شود، با کاری که
فایل‌های `replica/` لازم را هم همراه دارد. ورود، پرداخت، خرید دامنه و وارد
کردن کلید زنده با خود شماست.

## ابزارها

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

هیچ‌کدام به شبکه وصل نمی‌شوند. `imgdiff.py` چیدمان را مقایسه می‌کند نه رنگ را،
تا تغییر هویت به ضررتان تمام نشود. `parity.py` به ضروری و مفید و اختیاری وزن
می‌دهد، نیمه را نصف حساب می‌کند، و ردیفی را که عمداً کنار گذاشته‌اید وارد نمره
نمی‌کند. `reviews.py` ردیف بی‌لینک را دور می‌ریزد. `sweep.py` تا وقتی نام یا
دامنه یا رنگ اصل در درخت مانده، جلوی انتشار را می‌گیرد. `listing.py` سقف
فروشگاه را چک می‌کند و نام برنامهٔ اصل را در متن شما خطا می‌گیرد.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## چیدمان

```
tools/                 contrast.py, parity.py, imgdiff.py, reviews.py, sweep.py, listing.py, themes.json
cursor/skills/         دوازده پوشه با SKILL.md، و قالب کنار مهارتی که لازم دارد
cursor/install.sh
grok-bot/skills/       همان دوازده مهارت، هر کدام فقط یک SKILL.md
grok-bot/install.sh
grok-bot/INSTALL.md
tests/
scripts/validate.py
```

فایل‌های پروژهٔ شما در `replica/` می‌ماند، نه در این مخزن.

## حرف آخر حقوقی

**قابلیت و الگوی استفاده را می‌سازد، اتاق‌پاک.** می‌بیند برنامه چه می‌کند و
آدم چطور از آن رد می‌شود، بعد همه‌چیز را از نو می‌نویسد. کد منبع، دارایی
اختصاصی، لوگو، علامت تجاری، متن و API خصوصی هدف را کپی نمی‌کند.

**فقط چیزی را می‌خواند که اجازه دارید بخوانید.** صفحهٔ عمومی و حساب خودتان.
پشت ورود را نمی‌خراشد، خلاف شرایط سایت نمی‌رود، به حساب کس دیگری وارد نمی‌شود،
و از دیوار پرداخت رد نمی‌شود. اگر شرایط حساب شما ساختن محصول رقیب را ممنوع
کرده باشد، همان را می‌گوید و به منبع عمومی برمی‌گردد.

**قبل از انتشار، نام و ظاهر عوض می‌شود.** نام تازه، پالت تازه، لوگو تازه،
حرف تازه. replica-deploy تا جاروب پاک نباشد منتشر نمی‌کند.

**«کلون هر برنامه» یعنی قابلیت و جریان کار.** نه محتوا، نه شبکهٔ کاربران، نه
مجوزی که خود برنامه دارد. پخش‌کننده و فهرست پخش و اشتراک‌گذاری یک برنامهٔ
موسیقی را می‌شود ساخت. کاتالوگش را نه.

**قول کلون بی‌نقص نمی‌دهد.** یک ابزار رزرو چند هفته است. موتور یک صفحهٔ گسترده
نه. replica-recon همان اول اندازه را می‌گوید و replica-diff یک عدد می‌دهد،
نه یک حس.

**مهارت کارآفرین از خودش چیزی درنمی‌آورد.** نقد و نقل‌قول و عدد ساختگی ممنوع.
هر ادعا لینک دارد و اندازهٔ نمونه نوشته می‌شود.

**قبل از فروختن بررسی کنید.** جست‌وجوهایی که replica-brand فهرست کرده، شرایط
هر سرویسی که به کار گرفته‌اید، و اگر پول در میان است حرف با وکیل. این متن
مشاورهٔ حقوقی نیست.

## پروانه

MIT. حق نشر اصلی برای Jake Schincariol است. برای این اقتباس یک خط حق نشر به
نام letmefind اضافه شده. متن در [LICENSE](../../LICENSE) است.

</div>
