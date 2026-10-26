# Video Projects — dựng video dù lượn tự động bằng AI

Workflow dựng video ngắn dọc (TikTok / Reels / Shorts) cho các kênh dù lượn **Fly Sapa** và **Fly Ninh Bình**.
Mọi bước đều do [Claude Code](https://claude.com/claude-code) thực hiện bằng **ffmpeg + Python**: người dùng chỉ cần bỏ video vào thư mục và nhắn yêu cầu bằng tiếng Việt.

> Repo này **không chứa video, nhạc và font** (quá nặng hoặc có bản quyền). Xem mục [Cài đặt](#cài-đặt) để chuẩn bị lại trên máy mới.

---

## Ý tưởng chính

1. **Học từ video mẫu:** Claude phân tích các video đã dựng mà bạn thích. Claude đo nhịp cắt, bóc lời, chụp khung hình, đo âm lượng, rồi viết lại thành **công thức edit** (`CONG-THUC-EDIT.md`).
2. **Mỗi kênh là một dự án riêng:** mỗi kênh có công thức, tag thương hiệu, guideline vùng chữ và khuôn dựng riêng. Font và âm thanh hiệu ứng thì các kênh dùng chung.
3. **Dựng theo công thức:** Claude chọn cảnh, cắt, phủ tag, thêm chữ đúng vùng guideline, thêm nhạc và hiệu ứng, rồi xuất video 1080×1920, 60 fps.
4. **Góp ý → công thức tốt hơn:** điều gì bạn muốn nhớ lâu dài (ví dụ "bỏ tiếng vút khi chuyển cảnh") sẽ được ghi vào công thức, nên các video sau tự áp dụng.

## Cấu trúc

```
video-projects/
├── CLAUDE.md                 # Quy tắc chung cho Claude + cách thêm kênh mới
├── README.md
├── chung/                    # Dùng chung mọi kênh
│   ├── fonts/                # (không lưu trên GitHub, tải bằng scripts/tai_font.sh)
│   ├── sfx/                  # Âm thanh hiệu ứng tự tạo: whoosh, pop, impact
│   └── scripts/
│       ├── tai_font.sh       # Tải font miễn phí từ Google Fonts
│       └── tao_sfx.py        # Tạo lại âm thanh hiệu ứng bằng ffmpeg
├── fly-sapa/                 # Dự án kênh Fly Sapa (chữ tiếng Anh)
│   ├── CLAUDE.md             # Hướng dẫn riêng của kênh
│   ├── CONG-THUC-EDIT.md     # Công thức edit
│   ├── .claude/settings.json # Cho phép dùng ../chung và ~/video-tools
│   ├── TAG FSP HIGHEST IN SAPA.png
│   ├── Guidelines_Template_-_Anthony_Smith.png
│   ├── scripts/
│   │   ├── dung_thu_IMG_1170.py   # Khuôn dựng Kiểu B (caption + chữ phản ứng)
│   │   └── xuat_capcut.py         # Xuất đoạn cắt + .srt + tag để chỉnh trong CapCut
│   └── mau/ goc/ moi/ xuat/       # Video (chỉ có trên máy)
└── fly-ninhbinh/             # Dự án kênh Fly Ninh Bình (chữ tiếng Việt)
    ├── CLAUDE.md
    ├── CONG-THUC-EDIT.md
    ├── .claude/settings.json
    ├── TAG FNB.png
    ├── Guidelines_Template_-_Anthony_Smith.png
    ├── scripts/dung_thu_ninhbinh.py  # Khuôn dựng: 6 cảnh theo phách nhạc, chữ 2 dòng, chuyển cảnh, SFX
    ├── nhạc nền /                    # (chỉ có trên máy)
    └── mau/ goc/ moi/ xuat/
```

### Các thư mục video của mỗi kênh

| Thư mục | Để gì |
|---|---|
| `mau/` | Video **đã dựng hoàn chỉnh** để Claude học phong cách |
| `moi/` | Video **quay thô mới**, đang chờ dựng |
| `goc/` | Kho video thô đã dựng xong hoặc để dành |
| `xuat/` | Video **thành phẩm** |

## Phong cách hai kênh (tóm tắt, chi tiết trong `CONG-THUC-EDIT.md`)

### Fly Sapa
- Tag `HIGHEST IN SAPA` + nhãn `1.750 Meters` phủ suốt video.
- **Kiểu A:** giữ lời thoại thật, phụ đề karaoke in hoa (từ đang nói có nền xanh), chú thích cảm xúc nghiêng (`*tear`, `*pinky promise`). Kết video bằng `COMMENT "FLY SAPA"`.
- **Kiểu B:** caption `POV: …` ở dải trên, chữ phản ứng nhỏ (`woohoo!`, `that was amazing!`), chuyển cảnh loé trắng, cảnh cuối có thể chia đôi màn hình, kết video bằng `Book your flight: FLYSAPA.COM`.
- Font: Poppins.

### Fly Ninh Bình
- Tag `NINH BÌNH` + nhãn `NGẮM TRỌN DI SẢN`.
- **"Mỗi cảnh một điểm bán hàng":** 6 cảnh cắt đúng phách nhạc, mỗi cảnh một cụm chữ 2 dòng: chữ đậm Be Vietnam Pro ở trên, chữ viết tay Great Vibes ở dưới.
- Chuyển cảnh: loé trắng → mở vòng tròn → trượt trái → hoà tan → loé trắng. **Không** dùng hiệu ứng trượt lên.
- Âm thanh: chỉ nhạc nền, thêm tiếng "bụp" khi chữ hiện và tiếng dội trầm ở cảnh ưu đãi. **Không** dùng tiếng vút.
- Video iPhone quay HDR được chuyển sang SDR. Video drone quay ngang được cắt lấy khung dọc.

## Vùng đặt chữ (guideline)

Cả hai kênh dùng chung guideline 1080×1920. Toạ độ tính theo pixel:

| Vùng | x | y |
|---|---|---|
| Khung an toàn chung | 220 → 855 | 324 → 1568 |
| Dải vàng (caption chính) | 220 → 855 | 476 → 562 |
| Vùng giữa (chữ chính, kêu gọi) | 220 → 855 | 568 → 1232 |
| Dải xanh (phụ đề karaoke) | 220 → 855 | 1391 → 1508 |

Trước khi giao video, Claude phủ guideline lên vài khung hình để kiểm tra không chữ nào lọt ra ngoài. Chữ dài thì tự giảm cỡ hoặc xuống dòng (đo bằng Pillow).

## Cài đặt

Dành cho máy **macOS chip Apple Silicon**:

1. **ffmpeg / ffprobe**: tải bản static build cho macOS arm64 (ví dụ từ [martin-riedl.de](https://ffmpeg.martin-riedl.de)) vào `~/video-tools/bin/`, hoặc `brew install ffmpeg`.
2. **Python + thư viện:**
   ```bash
   python3 -m venv ~/video-tools/whisper-venv
   ~/video-tools/whisper-venv/bin/pip install faster-whisper pillow
   ```
   Lần đầu bóc lời, model `medium` (~1,5 GB) sẽ tự tải về.
3. **Font:** `sh chung/scripts/tai_font.sh`
4. **Âm thanh hiệu ứng** (nếu cần tạo lại): `~/video-tools/whisper-venv/bin/python -I chung/scripts/tao_sfx.py`
5. Bỏ video mẫu, video gốc và nhạc nền vào thư mục của từng kênh.

> `.claude/settings.json` của mỗi kênh đang ghi đường dẫn tuyệt đối `/Users/haley/...`. Nếu dùng trên máy khác, hãy sửa lại cho đúng.

## Cách dùng hằng ngày

1. Kéo clip quay thô vào `<kênh>/moi/`.
2. Trong app Claude, mở phiên mới ở thư mục của kênh (ví dụ `fly-ninhbinh/`).
3. Nhắn: **"dựng video mới"**.
4. Xem video trong `xuat/`, rồi góp ý bằng lời (ví dụ "chữ to hơn", "bỏ cảnh 3") để Claude sửa.
5. Muốn tự chỉnh tay trong CapCut thì nhắn **"xuất bộ CapCut"**: Claude xuất các đoạn cắt, phụ đề `.srt`, tag và font.

## Thêm kênh mới

Nhắn **"tạo kênh mới tên …"**. Các bước đã được ghi trong `CLAUDE.md` gốc:
1. Tạo thư mục kênh.
2. Phân tích video mẫu.
3. Viết `CONG-THUC-EDIT.md` và `CLAUDE.md` riêng.
4. Lấy khuôn dựng của kênh có phong cách gần nhất làm khởi đầu.

## Giới hạn hiện tại

- **Emoji màu:** ffmpeg không vẽ được.
- **Hiệu ứng phức tạp** kiểu CapCut / After Effects (sticker động, chữ bay lượn) chỉ làm được ở mức đơn giản.
- **Âm thanh hiệu ứng** là loại tự tạo, khá cơ bản. Có file thật thì bỏ vào `chung/sfx/` với cùng tên để thay thế.
- **Nhạc:** Claude không tự chọn nhạc hay được. Claude chỉ đo được nhịp (BPM) và độ to.
