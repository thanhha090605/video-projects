# Video projects — dựng video tự động cho nhiều kênh

Người dùng không biết code. Trả lời bằng tiếng Việt, ngắn gọn, tự chạy lệnh.

## Cách tổ chức: mỗi kênh là một dự án riêng

- `fly-sapa/`, `fly-ninhbinh/`…: mỗi thư mục là **một dự án độc lập** của một kênh. Người dùng mở phiên Claude ngay trong thư mục kênh để làm video cho kênh đó. Mỗi kênh có:
  - `CLAUDE.md`: hướng dẫn riêng của kênh
  - `CONG-THUC-EDIT.md`: công thức edit. **Luôn đọc trước khi dựng.**
  - `scripts/`: file lệnh dựng video của kênh, dùng làm khuôn cho video mới
  - `.claude/settings.json`: cho phép dùng `../chung/` và `~/video-tools/`
  - Tag và guideline của kênh
  - `mau/`: video mẫu. `goc/`, `moi/`: video cần dựng. `xuat/`: thành phẩm
- `chung/`: dùng chung cho mọi kênh
  - `fonts/`: Poppins (không có dấu tiếng Việt), Be Vietnam Pro, Great Vibes, Bebas Neue
  - `sfx/`: âm thanh hiệu ứng (`whoosh`, `pop`, `impact`), tạo bằng `scripts/tao_sfx.py`
  - `scripts/`: chỉ chứa công cụ dùng chung

## Thêm kênh mới

1. Tạo thư mục `<ten-kenh>/` với `mau/ goc/ moi/ xuat/ scripts/ .claude/`.
2. Copy `.claude/settings.json` từ một kênh có sẵn.
3. Phân tích video trong `mau/`, viết `CONG-THUC-EDIT.md` và `CLAUDE.md` riêng.
4. Lấy khuôn dựng của kênh có phong cách gần nhất, copy vào `scripts/` rồi sửa.

## Công cụ (đã cài sẵn)

- ffmpeg / ffprobe: `~/video-tools/bin/` (macOS, Apple Silicon)
- Python: `~/video-tools/whisper-venv/bin/python`, có faster-whisper (model `medium` đã tải về máy), Pillow (đo độ rộng chữ), numpy
- ffmpeg không có fontconfig: khi in chữ, luôn truyền `fontsdir=` (với filter `ass`) hoặc `fontfile=` (với `drawtext`)
- Không vẽ được emoji màu bằng ffmpeg

## Quy tắc chung

- Chữ phải nằm trong vùng guideline của kênh. Trước khi giao video, phủ guideline lên vài khung hình để kiểm tra.
- Không xoá hay ghi đè file trong `mau/` và `goc/`.
