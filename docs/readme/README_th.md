<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · **ไทย** · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Replica skills สำหรับ Cursor และ Grok Bot

</div>

สิบเอ็ด skill ที่สร้างสิ่งที่แอปทำขึ้นใหม่ บวกอีกหนึ่ง skill คือ `replica` ที่รักษาลำดับให้ตรง ฟรี ใช้สัญญาอนุญาต MIT นอกจาก Python 3.8 กับไลบรารีมาตรฐานแล้วไม่มีอะไรต้องติดตั้ง

งานนี้เป็นห้องสะอาด skill ศึกษาฟีเจอร์และทางที่คนเดินผ่านฟีเจอร์เหล่านั้น แล้วเขียนทุกอย่างใหม่ทั้งหมด ไม่เอาโค้ด โลโก้ ข้อความ หรือเนื้อหาของเป้าหมาย ตัวหนังสือเล็กอยู่ท้ายหน้า และ skill ก็ย้ำข้อความเดียวกัน

## ที่มา

วิธีทำ เทมเพลต และเครื่องมือ Python หกตัวเป็นของ Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

ที่เก็บนี้คือพอร์ตของ letmefind สำหรับ Cursor และสำหรับ Grok Bot ข้อความของ skill นำมาจาก https://github.com/letmefind/replica-skill ซึ่งเป็น fork ของที่เก็บด้านบน

ชุดอื่นของผู้เขียนคนเดียวกัน: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## สิบสองตัว

| skill | สิ่งที่ทำ |
| --- | --- |
| `replica` | ลำดับ ไฟล์ที่แต่ละขั้นอ่านและเขียน และขั้นถัดไปที่ควรเรียก |
| `replica-recon` | หน้าจอ ลำดับการใช้งาน ชิ้นส่วน โมเดลข้อมูล ตารางฟีเจอร์ จากหน้าสาธารณะ ภาพหน้าจอ หน้าร้าน และบัญชีของคุณเอง |
| `replica-architect` | สแตก สคีมาฐานข้อมูล และ API |
| `replica-design` | บทบาทของสี ตัวอักษร ระยะห่าง ชิ้นส่วน ในรูปโทเคน พร้อมทรัพย์สินของคุณเอง |
| `replica-build` | ตัวแอป ทีละหน้าจอ จากแผนที่สำรวจ |
| `replica-backend` | การเข้าสู่ระบบ ฐานข้อมูล การชำระเงิน และการเชื่อมต่อ |
| `replica-test` | ทุกเส้นทาง คลิกจนครบและทดสอบ |
| `replica-diff` | คะแนนความตรงกัน และสิ่งที่ยังขาด |
| `replica-entrepreneur` | สิ่งที่ผู้ใช้จริงไม่ชอบ เปลี่ยนเป็นการแก้และมุมวางตำแหน่ง |
| `replica-brand` | ชื่อและแบรนด์ของคุณเอง แล้วกวาดสิ่งที่เหลือ |
| `replica-launch` | หน้าแรก ราคา และข้อความในร้าน |
| `replica-deploy` | ขึ้นจริง บนโดเมนของคุณ หลังการตรวจก่อนปล่อยผ่าน |

เรียกตามลำดับนี้:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

แอปนัดหมายแบบที่คุณส่งลิงก์แล้วอีกฝ่ายจองเวลา เดินแบบนี้

1. **replica-recon** อ่านศูนย์ช่วยเหลือ หน้าราคา หน้าร้าน และคำอธิบายสาธารณะ คุณคลิกผ่านบัญชีของตัวเองเอง ผลลัพธ์คือ `replica/recon.md` และ `replica/features.csv` ตลาดของพาร์ตเนอร์อยู่นอกขอบเขต นั่นคือเครือข่ายของเขา ไม่ใช่ฟีเจอร์
2. **replica-architect** เลือกสแตกที่เรียบและมีคนดูแล เขียนสคีมา (รวมข้อจำกัดไม่ให้แขกสองคนจองช่องเดียวกัน) แล้วจัดลำดับการสร้างรอบเส้นทางการจอง
3. **replica-design** วัดภาพหน้าจอเป็นโทเคน: บทบาทของสี ตัวอักษร ระยะห่าง ตัวเลือกวันที่ ปุ่มช่องเวลา ไอคอนแบบเปิด ฟอนต์แบบเปิด คำของคุณเอง
4. **replica-build** สร้างเปลือก แล้วเส้นทางการจอง แล้วทุกหน้าจอพร้อมสถานะ และติ๊ก `features.csv` ไปด้วย
5. **replica-backend** เพิ่มการสมัคร ปฏิทินผ่าน API ของผู้ให้บริการด้วยคีย์ของคุณ การชำระเงินในโหมดทดสอบ และอีเมลเตือน
6. **replica-test** เขียนแผนจากเส้นทาง ทดสอบตั้งแต่ต้นจนจบทั้งทางที่ราบรื่นและขอบ และเก็บบั๊กตามความรุนแรงจนกว่าจะไม่มี S1 หรือ S2 ที่ยังเปิด
7. **replica-diff** ให้คะแนน ของที่ต้องมีถ้าขาด แปลว่ายังปล่อยไม่ได้
8. **replica-entrepreneur** อ่านรีวิวจริง และเฉพาะรีวิวจริง ทุกประโยคคัดลอกจากแถวที่คุณให้มา พร้อม URL ของแถวนั้น
9. **replica-brand** ตั้งชื่อหลังจากตรวจเครื่องหมายการค้าและโดเมนได้รันจริง แล้วกวาดต้นไม้จนกว่าจะไม่เหลือของต้นฉบับ
10. **replica-launch** เขียนหน้าแรกตามมุมนั้น ตั้งราคาเทียบหน้าสาธารณะ (พร้อมวันที่ที่อ่าน) และตรวจข้อความในร้าน
11. **replica-deploy** รันการตรวจก่อนปล่อย และเมื่อคุณบอกให้ไป จึงปล่อย

เรียก skill ตัวใดตัวหนึ่งเดี่ยวๆ ได้ replica-entrepreneur บนแอปที่คุณยังไม่ได้เริ่ม เป็นทางที่สมเหตุสมผลในการตัดสินใจว่าจะสร้างหรือไม่

## ติดตั้งสำหรับ Cursor

Cursor โหลด skill ของโปรเจกต์จาก `.cursor/skills/<name>/SKILL.md` และ `.agents/skills/<name>/SKILL.md` และสำหรับผู้ใช้จาก `~/.cursor/skills/` กับ `~/.agents/skills/` ชื่อโฟลเดอร์คือชื่อ skill `name` และ `description` ในส่วนหัวจำเป็น และ `name` ต้องตรงกับโฟลเดอร์

สคริปต์ติดตั้งนี้ใช้ `.cursor/skills` (โปรเจกต์) และ `~/.cursor/skills` (`--global`) skill ของโปรเจกต์เดินไปกับที่เก็บ skill ของผู้ใช้ใน `~/.cursor/skills/` อยู่บนเครื่องนั้นจนกว่าคุณจะเปิดการซิงก์สำหรับ Cloud Agents ที่ Settings, Agents skill ที่อยากให้ทุกครั้งที่ Cloud Agent รันบนที่เก็บหนึ่งเห็น ให้อยู่ใน `.cursor/skills/` ของที่เก็บนั้น

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

รันซ้ำจะแทนที่โฟลเดอร์ Replica และ `replica-tools/` และไม่แตะ skill อื่นที่อยู่ตรงนั้น

ในแชท พิมพ์ `/` แล้วเลือก `replica` หรือ `replica-recon` นั่นแนบ skill เข้ากับข้อความเดียว ถ้าอยากให้คงทั้งเซสชัน ให้เริ่มเป็น Custom Mode: Option+Enter บน macOS หรือ Alt+Enter บน Windows

เทมเพลตอยู่กับโฟลเดอร์ของ skill เครื่องมือ Python มีชุดเดียวที่ใช้ร่วมกัน หลังติดตั้งจะอยู่ใน `replica-tools/` ข้างโฟลเดอร์ skill จากสำเนาของที่เก็บนี้ ให้ตั้ง `REPLICA_HOME` ไปที่สำเนานั้น แล้ว skill จะใช้ `tools/` ที่นั่น Python 3.8 หรือใหม่กว่า ไม่มีอะไรต้องติดตั้งด้วย pip

## ติดตั้งสำหรับ Grok Bot

ส่งข้อความนี้ทั้งก้อน เป็นข้อความทั้งฉบับ:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

ขั้นตอนถัดไปอยู่ใน [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md) โดยย่อ: clone ที่เก็บนี้ไปที่ `/home/box/replica-skill` (เปลี่ยนได้ด้วย `REPLICA_HOME`) รัน `grok-bot/install.sh` แล้วบันทึกแต่ละไฟล์ใน `grok-bot/skills/*/SKILL.md` เป็น skill ชื่อ คำอธิบาย และเนื้อหาถูกคัดลอกตรงตัว skill ของ Grok Bot คือไฟล์นั้นไฟล์เดียว เครื่องมือและเทมเพลตอยู่บนดิสก์ และ skill เรียกด้วยพาธสัมบูรณ์ เช่น `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`

บันทึกการค้นคว้าของโปรเจกต์อยู่ที่ `/workspace/<project-slug>/replica/` เมื่อขั้นหนึ่งเริ่มเขียนตัวแอป `replica/` จะอยู่ในที่เก็บโค้ดของคุณ การเปลี่ยนโค้ดส่งให้ Cursor cloud coding agent บนที่เก็บ GitHub นั้น เป็นงานที่มีไฟล์ `replica/` ที่ต้องใช้ติดไปด้วย คุณลงชื่อเข้าใช้ จ่ายเงิน ซื้อโดเมน และพิมพ์คีย์จริงด้วยตัวเอง

## เครื่องมือ

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

ไม่มีตัวไหนใช้เครือข่าย `imgdiff.py` เทียบผัง ไม่เทียบสี ดังนั้นการเปลี่ยนแบรนด์ไม่ถูกนับเป็นโทษ `parity.py` ถ่วงน้ำหนัก must, should และ could นับ partial เป็นครึ่ง และไม่ให้คะแนนแถวที่คุณข้ามโดยตั้งใจ `reviews.py` ทิ้งแถวที่ไม่มีลิงก์ `sweep.py` กั้นการปล่อยตราบใดที่ชื่อ โดเมน หรือสีของต้นฉบับยังอยู่ในต้นไม้ `listing.py` ตรวจขีดจำกัดของร้าน และปฏิเสธชื่อต้นฉบับในข้อความของคุณ

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## ผัง

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

ไฟล์โปรเจกต์ของคุณอยู่ใน `replica/` ไม่ใช่ในที่เก็บนี้

## ตัวหนังสือเล็ก

**มันสร้างฟังก์ชันและรูปแบบการใช้งานใหม่ แบบห้องสะอาด** มันดูว่าแอปทำอะไรและคนเดินผ่านอย่างไร แล้วเขียนทุกอย่างใหม่ ไม่คัดลอกซอร์สโค้ด ทรัพย์สินเฉพาะ โลโก้ เครื่องหมายการค้า ข้อความ หรือ API ส่วนตัวของเป้าหมาย

**มันอ่านเฉพาะสิ่งที่คุณได้รับอนุญาตให้อ่าน** หน้าสาธารณะและบัญชีของคุณเอง มันไม่ขูดหลังการเข้าสู่ระบบหรือฝืนเงื่อนไขของไซต์ ไม่เข้าบัญชีของคนอื่น และไม่ข้ามกำแพงจ่ายเงิน ถ้าเงื่อนไขบัญชีของคุณห้ามใช้เพื่อสร้างคู่แข่ง skill จะบอกอย่างนั้นและยึดแหล่งสาธารณะ

**มันเปลี่ยนแบรนด์ก่อนปล่อย** ชื่อใหม่ จานสีใหม่ โลโก้ใหม่ คำใหม่ replica-deploy ไม่ปล่อยจนกว่าการกวาดจะสะอาด

**«โคลนแอปใดก็ได้» หมายถึงฟีเจอร์และเส้นทาง** ไม่ใช่เนื้อหา เครือข่าย หรือสัญญาอนุญาตที่แอปถืออยู่ เครื่องเล่น รายการเพลง และการแชร์ของแอปเพลงสร้างใหม่ได้ แคตตาล็อกของมันโคลนไม่ได้

**ไม่สัญญาว่าจะเหมือนทุกอย่าง** เครื่องมือจองคืองานหลายสัปดาห์ เอนจินสเปรดชีตไม่ใช่ replica-recon ประเมินขนาดก่อนคุณเริ่ม และ replica-diff ให้ตัวเลข

**skill ด้านธุรกิจไม่แต่งเรื่อง** ไม่มีรีวิว คำพูด หรือตัวเลขที่แต่งขึ้น ทุกข้ออ้างมีลิงก์ และขนาดตัวอย่างถูกเขียนไว้

**ตรวจก่อนขาย** รันการตรวจเครื่องหมายการค้าที่ replica-brand ระบุ อ่านเงื่อนไขของทุกอย่างที่คุณใช้ และคุยกับทนายก่อนปล่อยถ้ามีเงินอยู่ในเกม นี่ไม่ใช่คำแนะนำทางกฎหมาย

## สัญญาอนุญาต

MIT ลิขสิทธิ์เดิมเป็นของ Jake Schincariol พอร์ตนี้เพิ่มบรรทัดลิขสิทธิ์ให้ letmefind ดู [LICENSE](../../LICENSE)
