<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · **Bahasa Indonesia** · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Replica skills untuk Cursor dan Grok Bot

</div>

Sebelas skill yang membangun ulang apa yang dilakukan sebuah aplikasi, plus satu skill, `replica`, yang menjaga urutannya. Gratis, MIT. Selain Python 3.8 dan pustaka standar, tidak ada yang perlu dipasang.

Pekerjaannya ruang bersih. Skill mempelajari fitur dan jalan seseorang melewatinya, lalu menulis semuanya dari awal. Mereka tidak mengambil kode, logo, teks, atau isi target. Cetakan kecil ada di bawah, dan skill mengulanginya.

## Sumber

Metode, templat, dan enam alat Python adalah karya Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Repositori ini adalah port letmefind dari paket itu, untuk Cursor dan untuk Grok Bot. Teks skill diambil dari https://github.com/letmefind/replica-skill, sebuah fork dari repositori di atas.

Paket lain dari penulis yang sama: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Dua belas

| skill | yang dikerjakan |
| --- | --- |
| `replica` | Urutan, berkas yang dibaca dan ditulis tiap langkah, dan langkah mana yang dijalankan. |
| `replica-recon` | Layar, alur, bagian, model data, matriks fitur. Halaman publik, tangkapan layar, daftar toko, dan akun Anda sendiri. |
| `replica-architect` | Tumpukan, skema basis data, dan API. |
| `replica-design` | Peran warna, huruf, jarak, bagian, sebagai token, dengan aset Anda sendiri. |
| `replica-build` | Aplikasinya, layar demi layar, dari peta pengintaian. |
| `replica-backend` | Masuk, basis data, pembayaran, dan integrasi. |
| `replica-test` | Setiap alur, diklik sampai selesai dan diuji. |
| `replica-diff` | Skor kesetaraan, dan apa yang masih kurang. |
| `replica-entrepreneur` | Hal yang dibenci pengguna sungguhan, dijadikan perbaikan dan sudut posisi. |
| `replica-brand` | Nama dan merek milik Anda, lalu sapuan sisa. |
| `replica-launch` | Halaman pendaratan, harga, dan teks toko. |
| `replica-deploy` | Tayang, di domain Anda sendiri, setelah pemeriksaan awal lulus. |

Jalankan dengan urutan ini:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Aplikasi janji temu, yang tautannya Anda bagi lalu seseorang memesan waktu, berjalan seperti ini.

1. **replica-recon** membaca pusat bantuan, halaman harga, daftar toko, dan penelusuran publik. Anda mengklik lewat akun sendiri. Yang keluar adalah `replica/recon.md` dan `replica/features.csv`. Pasar mitra di luar lingkup: itu jaringan mereka, bukan sebuah fitur.
2. **replica-architect** memilih tumpukan yang biasa dan dikelola, menulis skema (termasuk batasan agar dua tamu tidak memesan slot yang sama), dan menyusun pembangunan di seputar alur pemesanan.
3. **replica-design** mengukur tangkapan layar menjadi token: peran warna, huruf, jarak, pemilih tanggal, tombol slot. Ikon terbuka, font terbuka, kata-kata Anda sendiri.
4. **replica-build** membangun kerangka, lalu alur pemesanan, lalu setiap layar beserta keadaannya, dan menandai `features.csv` sambil berjalan.
5. **replica-backend** menambahkan pendaftaran, kalender lewat API milik penyedia dengan kunci Anda, pembayaran dalam mode uji, dan surel pengingat.
6. **replica-test** menulis rencana dari alur, uji ujung ke ujung untuk jalan yang mulus dan tepinya, serta cacat menurut tingkat keparahan sampai tidak ada S1 atau S2 yang terbuka.
7. **replica-diff** memberi skor. Yang wajib hilang berarti belum layak terbit.
8. **replica-entrepreneur** membaca ulasan sungguhan dan hanya ulasan sungguhan. Setiap kutipan disalin dari baris yang Anda berikan, beserta URL baris itu.
9. **replica-brand** menamainya setelah pemeriksaan merek dagang dan domain benar-benar dijalankan, lalu menyapu pohon sampai tidak ada sisa dari yang asli.
10. **replica-launch** menulis halaman pendaratan di seputar sudut itu, memasang harga terhadap halaman harga publik (dengan tanggal saat halaman itu dibaca), dan memeriksa teks toko.
11. **replica-deploy** menjalankan pemeriksaan awal dan, ketika Anda bilang jalan, menerbitkan.

Skill mana pun bisa dijalankan sendiri. replica-entrepreneur, pada aplikasi yang belum Anda mulai, adalah cara yang masuk akal untuk memutuskan apakah perlu dibangun.

## Pasang untuk Cursor

Cursor memuat skill proyek dari `.cursor/skills/<name>/SKILL.md` dan `.agents/skills/<name>/SKILL.md`, serta untuk pengguna Anda dari `~/.cursor/skills/` dan `~/.agents/skills/`. Nama folder adalah nama skill. `name` dan `description` di bagian depan wajib ada, dan `name` harus cocok dengan folder.

Pemasang ini memakai `.cursor/skills` (proyek) dan `~/.cursor/skills` (`--global`). Skill proyek ikut bersama repositori. Skill pengguna di `~/.cursor/skills/` tinggal di mesin itu sampai Anda menyalakan sinkronisasi untuk Cloud Agents di Settings, Agents. Skill yang ingin ada pada setiap jalan Cloud Agent untuk sebuah repositori diletakkan di `.cursor/skills/` repositori itu.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Menjalankannya lagi mengganti folder Replica dan `replica-tools/`, dan membiarkan skill lain di tempatnya.

Di obrolan, ketik `/` lalu pilih `replica` atau `replica-recon`. Itu menempelkan skill pada satu pesan. Agar tetap sepanjang sesi, mulai sebagai Custom Mode: Option+Enter di macOS, atau Alt+Enter di Windows.

Templat tetap di folder skill. Alat Python adalah satu salinan bersama. Setelah dipasang, alat itu ada di `replica-tools/` di samping folder skill. Dari salinan repositori ini, setel `REPLICA_HOME` ke salinan itu dan skill memakai `tools/` di sana. Python 3.8 atau lebih baru. Tidak ada yang dipasang lewat pip.

## Pasang untuk Grok Bot

Kirim ini, sebagai seluruh pesan:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Langkah setelah itu ada di [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Versi pendek: clone repositori ini ke `/home/box/replica-skill` (ubah dengan `REPLICA_HOME`), jalankan `grok-bot/install.sh`, lalu simpan tiap berkas di `grok-bot/skills/*/SKILL.md` sebagai skill. Nama, deskripsi, dan isi disalin apa adanya. Skill Grok Bot adalah berkas yang satu itu. Alat dan templat tinggal di disk, dan skill memanggilnya dengan jalur mutlak, misalnya `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Catatan riset sebuah proyek ada di `/workspace/<project-slug>/replica/`. Begitu sebuah langkah menulis aplikasinya, `replica/` ada di repositori kode Anda. Perubahan kode diserahkan ke Cursor cloud coding agent pada repositori GitHub itu, sebagai tugas yang menyertakan berkas `replica/` yang dibutuhkan. Anda sendiri yang masuk, membayar, membeli domain, dan mengetik kunci yang hidup.

## Alat

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Tidak satu pun memakai jaringan. `imgdiff.py` membandingkan tata letak, bukan warna, jadi ganti merek tidak dihitung merugikan Anda. `parity.py` memberi bobot pada must, should, dan could, menghitung partial sebagai setengah, dan tidak menilai baris yang Anda lewati dengan sengaja. `reviews.py` membuang baris tanpa tautan. `sweep.py` menahan terbit selama nama, domain, atau warna yang asli masih ada di pohon. `listing.py` memeriksa batas toko dan menolak nama yang asli di daftar Anda.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Tata letak

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

Berkas proyek Anda masuk ke `replica/`, bukan ke repositori ini.

## Cetakan kecil

**Ia membangun ulang fungsi dan pola pemakaian, dengan ruang bersih.** Ia mempelajari apa yang dilakukan aplikasi dan bagaimana orang melewatinya, lalu menulis semuanya dari awal. Ia tidak menyalin kode sumber target, aset tertutup, logo, merek dagang, teks, atau API pribadi.

**Ia hanya membaca yang boleh Anda baca.** Halaman publik dan akun Anda sendiri. Ia tidak mengeruk di balik login atau melawan ketentuan situs, tidak masuk ke akun orang lain, dan tidak melewati dinding berbayar. Jika ketentuan akun Anda melarang memakainya untuk membangun pesaing, skill mengatakan itu dan tetap pada sumber publik.

**Ia mengganti merek sebelum terbit.** Nama baru, palet baru, logo baru, kata baru. replica-deploy tidak menerbitkan sampai sapuan bersih.

**«Klon aplikasi apa pun» berarti fitur dan alurnya.** Bukan isinya, jaringannya, atau lisensi yang dimiliki aplikasi. Pemutar, daftar putar, dan berbagi dari aplikasi musik bisa dibangun ulang. Katalognya tidak bisa diklon.

**Tidak ada janji klon yang sempurna.** Alat pemesanan adalah hitungan minggu. Mesin lembar kerja bukan. replica-recon menakar ukurannya sebelum Anda mulai, dan replica-diff memberi angka.

**Skill usaha tidak mengarang.** Tidak ada ulasan, kutipan, atau angka yang dibuat-buat. Setiap klaim punya tautan, dan ukuran sampel ditulis.

**Periksa sebelum menjual.** Jalankan pemeriksaan merek dagang yang dicantumkan replica-brand, baca ketentuan segala yang Anda pakai, dan bicara dengan pengacara sebelum terbit jika ada uang yang dipertaruhkan. Ini bukan nasihat hukum.

## Lisensi

MIT. Hak cipta asli adalah milik Jake Schincariol. Port ini menambah satu baris hak cipta untuk letmefind. Lihat [LICENSE](../../LICENSE).
