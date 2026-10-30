<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · **Türkçe** · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Cursor ve Grok Bot için Replica skills

</div>

Bir uygulamanın ne yaptığını yeniden kuran on bir skill, bir de onları sırada tutan skill: `replica`. Ücretsiz, MIT. Python 3.8 ve standart kütüphane dışında kurulacak bir şey yok.

İş temiz oda. Skill'ler özellikleri ve bir kişinin içlerinden nasıl geçtiğini inceler, sonra her şeyi yeniden yazar. Hedefin kodunu, logosunu, metnini, içeriğini almazlar. Küçük yazı en altta ve skill'ler onu tekrarlar.

## Kaynak

Yöntem, şablonlar ve altı Python aracı Jake Schincariol'a aittir:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Bu depo, o paketin Cursor ve Grok Bot için letmefind tarafından yapılmış portudur. Skill metni, yukarıdaki deponun bir fork'u olan https://github.com/letmefind/replica-skill adresinden alındı.

Aynı yazarın diğer paketleri: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## On iki

| skill | ne yapar |
| --- | --- |
| `replica` | Sıra, her adımın okuduğu ve yazdığı dosyalar, sıradaki adım. |
| `replica-recon` | Ekranlar, akışlar, parçalar, veri modeli, özellik tablosu. Açık sayfalar, ekran görüntüleri, mağaza kayıtları ve kendi hesabın. |
| `replica-architect` | Yığın, veritabanı şeması ve API. |
| `replica-design` | Renk rolleri, yazı, aralık, parçalar; token olarak, kendi varlıklarınla. |
| `replica-build` | Uygulama, keşif haritasından, ekran ekran. |
| `replica-backend` | Kimlik, veritabanı, ödemeler ve bağlantılar. |
| `replica-test` | Her akış, tıklanarak ve test edilerek. |
| `replica-diff` | Bir eşlik puanı ve hâlâ eksik olan. |
| `replica-entrepreneur` | Gerçek kullanıcıların nefret ettiği şeyler, düzeltmeye ve bir konum açısına. |
| `replica-brand` | Kendi adın ve markan, sonra kalanları süpürme. |
| `replica-launch` | Açılış sayfası, fiyat ve mağaza metni. |
| `replica-deploy` | Ön kontrol geçince, kendi alan adında yayında. |

Bu sırayla çalıştır:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Bir bağlantı paylaşıp birinin saat seçtiği türden bir randevu uygulaması şöyle gider.

1. **replica-recon** yardım merkezini, fiyat sayfasını, mağaza kaydını ve açık anlatımları okur. Kendi hesabında sen tıklarsın. Çıkanlar `replica/recon.md` ve `replica/features.csv` olur. Bir ortak pazarı kapsam dışıdır: o onların ağıdır, bir özellik değil.
2. **replica-architect** sıkıcı, yönetilen bir yığın seçer, şemayı yazar (iki konuğun aynı aralığı alamaması için bir kısıt dahil) ve kurulumu randevu akışının çevresine dizer.
3. **replica-design** ekran görüntülerini token'a ölçer: renk rolleri, yazı, aralık, tarih seçici, aralık düğmesi. Açık simgeler, açık bir yazı tipi, kendi sözlerin.
4. **replica-build** önce kabuğu, sonra randevu akışını, sonra her ekranı durumlarıyla kurar ve giderken `features.csv` dosyasını işaretler.
5. **replica-backend** kaydı, kendi anahtarlarınla sağlayıcının kendi API'sinden takvimi, deneme kipinde ödemeyi ve anımsatma postasını ekler.
6. **replica-test** akışlardan bir plan yazar, mutlu yol ve kenarlar için uçtan uca testler koyar, hataları şiddete göre tutar, açık S1 veya S2 kalmayana kadar.
7. **replica-diff** puanlar. Olmazsa olmaz eksikse, yayınlanamaz.
8. **replica-entrepreneur** gerçek yorumları, yalnızca gerçek yorumları okur. Her alıntı, senin verdiğin bir satırdan, o satırın URL'siyle kopyalanır.
9. **replica-brand** marka ve alan adı kontrolleri gerçekten koştuktan sonra ad koyar, sonra özgün olandan hiçbir şey kalmayana kadar ağacı süpürür.
10. **replica-launch** açılış sayfasını açının çevresine yazar, fiyatı açık fiyat sayfasıyla karşılaştırır (okunduğu tarihiyle) ve mağaza metnini denetler.
11. **replica-deploy** ön kontrolü çalıştırır ve sen geç de, o zaman yayınlar.

Herhangi bir skill'i tek başına da çalıştırabilirsin. Henüz başlamadığın bir uygulamada replica-entrepreneur, kurup kurmamaya karar vermenin makul bir yoludur.

## Cursor için kurulum

Cursor, skill'leri projede `.cursor/skills/<name>/SKILL.md` ve `.agents/skills/<name>/SKILL.md` yollarından, senin kullanıcın için `~/.cursor/skills/` ve `~/.agents/skills/` yollarından yükler. Klasör adı skill adıdır. Ön bilgideki `name` ve `description` zorunludur ve `name` klasörle aynı olmalıdır.

Bu kurucu `.cursor/skills` (proje) ve `~/.cursor/skills` (`--global`) kullanır. Proje skill'leri depo ile birlikte gider. `~/.cursor/skills/` içindeki kullanıcı skill'leri, Settings, Agents altında Cloud Agents için eşitlemeyi açana kadar o makinede kalır. Bir deponun her Cloud Agent çalışmasında görünmesini istediğin skill, o deponun `.cursor/skills/` klasörüne aittir.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Yeniden çalıştırmak Replica klasörlerini ve `replica-tools/` dizinini değiştirir, oradaki diğer skill'lere dokunmaz.

Sohbette `/` yaz ve `replica` ya da `replica-recon` seç. Bu, skill'i tek bir iletiye bağlar. Oturum boyunca kalsın diye Custom Mode olarak başlat: macOS'ta Option+Enter, Windows'ta Alt+Enter.

Şablonlar skill klasöründe kalır. Python araçları tek bir ortak kopyadır. Kurulumdan sonra skill klasörlerinin yanında `replica-tools/` içindedirler. Bu deponun bir kopyasından çalışırken `REPLICA_HOME` değerini o kopyaya ayarla; skill'ler oradaki `tools/` yolunu kullanır. Python 3.8 veya daha yeni. pip ile kurulacak bir şey yok.

## Grok Bot için kurulum

Bunu, iletinin tamamı olarak gönder:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Sonraki adımlar [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md) içindedir. Kısa hali: bu depoyu `/home/box/replica-skill` konumuna clone et (`REPLICA_HOME` yolu değiştirir), `grok-bot/install.sh` betiğini çalıştır, sonra `grok-bot/skills/*/SKILL.md` altındaki her dosyayı bir skill olarak kaydet. Ad, açıklama ve gövde olduğu gibi kopyalanır. Bir Grok Bot skill'i o tek dosyadır. Araçlar ve şablonlar diskte kalır, skill'ler onları mutlak yolla çağırır. Örnek: `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Bir projenin araştırma notları `/workspace/<project-slug>/replica/` altındadır. Bir adım uygulamayı yazmaya başlayınca `replica/` senin kod depondadır. Kod değişiklikleri, o GitHub deposundaki bir Cursor cloud coding agent'a, ihtiyaç duyduğu `replica/` dosyalarını içeren bir görev olarak verilir. Giriş yapmak, ödemek, alan adını almak ve canlı anahtarları yazmak sana aittir.

## Araçlar

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Hiçbiri ağı kullanmaz. `imgdiff.py` rengi değil yerleşimi karşılaştırır, bu yüzden marka değişimi aleyhine yazılmaz. `parity.py` must, should ve could için ağırlık verir, partial'ı yarım sayar ve bilerek atladığın satırı puanlamaz. `reviews.py` bağlantısız satırı atar. `sweep.py`, özgün ad, alan adı veya renkler ağaçta durduğu sürece yayını durdurur. `listing.py` mağaza sınırlarını denetler ve kaydında özgün adı reddeder.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Yerleşim

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

Proje dosyaların `replica/` içine gider, bu depoya değil.

## Küçük yazı

**İşlevi ve kullanım kalıplarını, temiz odada yeniden kurar.** Uygulamanın ne yaptığını ve insanların içinden nasıl geçtiğini inceler, sonra her şeyi yeniden yazar. Hedefin kaynak kodunu, özel varlıklarını, logolarını, markalarını, metnini veya özel API'lerini kopyalamaz.

**Yalnızca okumana izin verileni okur.** Açık sayfalar ve kendi hesabın. Bir girişin arkasını taramaz, bir sitenin koşullarına karşı gitmez, başkasının hesabına girmez ve bir ödeme duvarını aşmaz. Hesabının koşulları rakip kurmak için kullanmayı yasaklıyorsa, skill bunu söyler ve açık kaynaklarda kalır.

**Yayından önce markayı değiştirir.** Yeni ad, yeni palet, yeni logo, yeni sözler. Süpürme temiz olmadan replica-deploy yayınlamaz.

**«Her uygulamayı klonla» özellik ve akış demektir.** İçerik, ağ veya bir uygulamanın sahip olduğu lisanslar değil. Bir müzik uygulamasının çaları, listeleri ve paylaşımı yeniden kurulabilir. Kataloğu klonlanamaz.

**Kusursuz bir klon vaadi yok.** Bir randevu aracı haftalar sürer. Bir hesap tablosu motoru sürmez. replica-recon başlamadan boyutu söyler, replica-diff bir sayı verir.

**Girişim skill'i uydurmaz.** Uydurma yorum, alıntı veya sayı yok. Her iddianın bir bağlantısı vardır ve örneklem büyüklüğü yazılır.

**Satmadan önce kontrol et.** replica-brand'in saydığı marka kontrollerini çalıştır, kullandığın her şeyin koşullarını oku ve ortada para varsa yayından önce bir avukatla konuş. Bu hukuki tavsiye değildir.

## Lisans

MIT. Özgün telif Jake Schincariol'a aittir. Port, letmefind için bir telif satırı ekler. Bkz. [LICENSE](../../LICENSE).
