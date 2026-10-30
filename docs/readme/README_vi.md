<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · **Tiếng Việt** · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Replica skills cho Cursor và Grok Bot

</div>

Mười một skill dựng lại việc một ứng dụng làm, cộng một skill, `replica`, giữ chúng đúng thứ tự. Miễn phí, MIT. Ngoài Python 3.8 và thư viện chuẩn thì không có gì phải cài.

Cách làm là phòng sạch. Các skill xem tính năng và đường một người đi qua chúng, rồi viết lại toàn bộ. Chúng không lấy mã, logo, lời, hay nội dung của mục tiêu. Chữ nhỏ ở cuối, và các skill nhắc lại.

## Nguồn

Phương pháp, mẫu, và sáu công cụ Python là của Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Kho này là bản chuyển của letmefind cho Cursor và cho Grok Bot. Lời của skill lấy từ https://github.com/letmefind/replica-skill, một fork của kho ở trên.

Các gói khác của cùng tác giả: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Mười hai

| skill | việc nó làm |
| --- | --- |
| `replica` | Thứ tự, tệp mỗi bước đọc và viết, và bước nào chạy tiếp. |
| `replica-recon` | Màn hình, luồng, thành phần, mô hình dữ liệu, bảng tính năng. Trang công khai, ảnh chụp, trang cửa hàng, và tài khoản của bạn. |
| `replica-architect` | Chồng kỹ thuật, lược đồ cơ sở dữ liệu, và API. |
| `replica-design` | Vai trò màu, chữ, khoảng cách, thành phần, dưới dạng token, với tài sản của bạn. |
| `replica-build` | Ứng dụng, từng màn hình, từ bản đồ trinh sát. |
| `replica-backend` | Đăng nhập, cơ sở dữ liệu, thanh toán, và kết nối. |
| `replica-test` | Mọi luồng, bấm qua và kiểm thử. |
| `replica-diff` | Điểm tương đồng, và phần còn thiếu. |
| `replica-entrepreneur` | Điều người dùng thật ghét, thành bản sửa và một góc định vị. |
| `replica-brand` | Tên và thương hiệu của riêng bạn, rồi quét phần còn sót. |
| `replica-launch` | Trang đích, giá, và lời trên cửa hàng. |
| `replica-deploy` | Lên sóng, trên tên miền của bạn, sau khi kiểm tra trước qua. |

Chạy theo thứ tự này:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Một ứng dụng đặt lịch, kiểu bạn gửi một liên kết và người kia chọn giờ, đi như sau.

1. **replica-recon** đọc trung tâm trợ giúp, trang giá, trang cửa hàng, và các hướng dẫn công khai. Bạn tự bấm trong tài khoản của mình. Ra `replica/recon.md` và `replica/features.csv`. Một chợ đối tác nằm ngoài phạm vi: đó là mạng của họ, không phải một tính năng.
2. **replica-architect** chọn một chồng kỹ thuật nhàm và được quản lý, viết lược đồ (kể cả một ràng buộc để hai khách không đặt cùng một khung giờ), và xếp việc dựng quanh luồng đặt lịch.
3. **replica-design** đo ảnh chụp thành token: vai trò màu, chữ, khoảng cách, bộ chọn ngày, nút khung giờ. Biểu tượng mở, một phông mở, lời của bạn.
4. **replica-build** dựng cái vỏ, rồi luồng đặt lịch, rồi từng màn hình với các trạng thái, và đánh dấu `features.csv` khi đi.
5. **replica-backend** thêm đăng ký, lịch qua API của chính nhà cung cấp bằng khóa của bạn, thanh toán ở chế độ thử, và thư nhắc.
6. **replica-test** viết kế hoạch từ các luồng, kiểm thử đầu cuối cho đường thuận và các mép, và lỗi theo mức nặng cho đến khi không còn S1 hay S2 mở.
7. **replica-diff** chấm điểm. Thiếu phần bắt buộc nghĩa là chưa phát hành được.
8. **replica-entrepreneur** đọc đánh giá thật và chỉ đánh giá thật. Mỗi câu trích được chép từ một dòng bạn đưa, kèm URL của dòng đó.
9. **replica-brand** đặt tên sau khi việc kiểm tra nhãn hiệu và tên miền đã chạy thật, rồi quét cây cho đến khi không còn gì của bản gốc.
10. **replica-launch** viết trang đích quanh góc đó, đặt giá đối với trang giá công khai (kèm ngày đã đọc), và soát lời trên cửa hàng.
11. **replica-deploy** chạy kiểm tra trước và, khi bạn bảo đi, thì phát hành.

Bạn có thể chạy riêng bất kỳ skill nào. replica-entrepreneur, trên một ứng dụng bạn chưa bắt đầu, là cách hợp lý để quyết định có dựng hay không.

## Cài cho Cursor

Cursor nạp skill của dự án từ `.cursor/skills/<name>/SKILL.md` và `.agents/skills/<name>/SKILL.md`, và cho người dùng từ `~/.cursor/skills/` cùng `~/.agents/skills/`. Tên thư mục là tên skill. `name` và `description` trong phần đầu là bắt buộc, và `name` phải khớp thư mục.

Trình cài này dùng `.cursor/skills` (dự án) và `~/.cursor/skills` (`--global`). Skill của dự án đi cùng kho. Skill người dùng trong `~/.cursor/skills/` ở lại máy đó cho đến khi bạn bật đồng bộ cho Cloud Agents trong Settings, Agents. Skill muốn có trên mỗi lần Cloud Agent chạy cho một kho thì thuộc về `.cursor/skills/` của kho đó.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Chạy lại sẽ thay các thư mục Replica và `replica-tools/`, và để yên các skill khác ở đó.

Trong khung chat, gõ `/` rồi chọn `replica` hoặc `replica-recon`. Việc đó gắn skill vào một tin. Muốn giữ cả phiên, hãy mở nó như Custom Mode: Option+Enter trên macOS, hoặc Alt+Enter trên Windows.

Mẫu ở lại trong thư mục skill. Công cụ Python là một bản dùng chung. Sau khi cài, chúng nằm trong `replica-tools/` cạnh các thư mục skill. Từ một bản lấy của kho này, đặt `REPLICA_HOME` vào bản lấy đó và các skill sẽ dùng `tools/` ở đó. Python 3.8 hoặc mới hơn. Không có gì để cài bằng pip.

## Cài cho Grok Bot

Gửi đúng đoạn này, như cả tin nhắn:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Các bước sau đó nằm trong [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Ngắn gọn: clone kho này vào `/home/box/replica-skill` (đổi bằng `REPLICA_HOME`), chạy `grok-bot/install.sh`, rồi lưu mỗi tệp trong `grok-bot/skills/*/SKILL.md` thành một skill. Tên, mô tả, và thân được chép nguyên văn. Một skill của Grok Bot là đúng tệp đó. Công cụ và mẫu ở trên đĩa, skill gọi chúng bằng đường dẫn tuyệt đối, ví dụ `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Ghi chú nghiên cứu của một dự án nằm ở `/workspace/<project-slug>/replica/`. Khi một bước bắt đầu viết ứng dụng, `replica/` nằm trong kho mã của bạn. Thay đổi mã được giao cho một Cursor cloud coding agent trên kho GitHub đó, bằng một việc có kèm các tệp `replica/` mà nó cần. Bạn tự đăng nhập, trả tiền, mua tên miền, và gõ khóa thật.

## Công cụ

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Không công cụ nào dùng mạng. `imgdiff.py` so bố cục, không so màu, nên đổi thương hiệu không bị tính vào bạn. `parity.py` đặt trọng số cho must, should, và could, tính partial bằng một nửa, và không chấm dòng bạn cố ý bỏ. `reviews.py` bỏ mọi dòng không có liên kết. `sweep.py` chặn phát hành khi tên, tên miền, hoặc màu của bản gốc còn trong cây. `listing.py` kiểm giới hạn cửa hàng và từ chối tên bản gốc trong lời của bạn.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Bố cục

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

Tệp dự án của bạn để trong `replica/`, không để trong kho này.

## Chữ nhỏ

**Nó dựng lại chức năng và cách dùng, theo phòng sạch.** Nó xem ứng dụng làm gì và người ta đi qua thế nào, rồi viết lại toàn bộ. Nó không chép mã nguồn, tài sản riêng, logo, nhãn hiệu, lời, hay API riêng của mục tiêu.

**Nó chỉ đọc thứ bạn được phép đọc.** Trang công khai và tài khoản của bạn. Nó không cào phía sau đăng nhập hay trái điều khoản của trang, không đăng nhập tài khoản của người khác, và không vượt tường trả phí. Nếu điều khoản tài khoản của bạn cấm dùng nó để làm đối thủ, skill nói rõ và chỉ bám nguồn công khai.

**Nó đổi thương hiệu trước khi phát hành.** Tên mới, bảng màu mới, logo mới, lời mới. replica-deploy không đưa lên cho đến khi lần quét sạch.

**«Nhân bản ứng dụng nào cũng được» nghĩa là tính năng và luồng.** Không phải nội dung, mạng lưới, hay các giấy phép mà ứng dụng nắm. Bạn có thể dựng lại trình phát, danh sách phát, và chia sẻ của một ứng dụng nhạc. Bạn không thể nhân bản danh mục của nó.

**Không hứa một bản sao hoàn hảo.** Một công cụ đặt lịch là vài tuần. Một động cơ bảng tính thì không. replica-recon ước kích thước trước khi bạn bắt đầu, và replica-diff cho bạn một con số.

**Skill về việc kinh doanh không bịa.** Không đánh giá, câu trích, hay con số bịa. Mọi nhận định có một liên kết, và cỡ mẫu được ghi.

**Kiểm trước khi bán.** Chạy các kiểm tra nhãn hiệu mà replica-brand liệt kê, đọc điều khoản của mọi thứ bạn dùng, và nói với luật sư trước khi phát hành nếu có tiền trong cuộc. Đây không phải tư vấn pháp lý.

## Giấy phép

MIT. Bản quyền gốc là của Jake Schincariol. Bản chuyển thêm một dòng bản quyền cho letmefind. Xem [LICENSE](../../LICENSE).
