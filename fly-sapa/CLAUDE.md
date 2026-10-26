# Kênh Fly Sapa

Đây là dự án riêng của kênh **Fly Sapa** (dù lượn ở Sapa, khách quốc tế, chữ tiếng Anh).
Người dùng không biết code: trả lời bằng tiếng Việt, ngắn gọn, tự chạy lệnh. Hướng dẫn chung nằm ở `../CLAUDE.md`.

## Trước khi dựng video

**Luôn đọc `CONG-THUC-EDIT.md` trước.** File này chứa toàn bộ phong cách của kênh:
- Kiểu A: có lời thoại, phụ đề karaoke.
- Kiểu B: caption, chữ phản ứng, cảnh cuối có thể chia đôi màn hình.

## Tài nguyên của kênh

- `TAG FSP HIGHEST IN SAPA.png`: tag thương hiệu, phủ kín khung hình.
- `Guidelines_Template_-_Anthony_Smith.png`: vùng đặt chữ.
- `mau/`: video mẫu. `goc/`, `moi/`: video cần dựng. `xuat/`: thành phẩm.
- `scripts/dung_thu_IMG_1170.py`: khuôn dựng Kiểu B. Video mới thì **copy file này thành file mới** rồi sửa `SEGMENTS`, `REACTIONS`, `HOOK`.
- `scripts/xuat_capcut.py`: xuất bộ nguyên liệu (đoạn cắt, .srt, tag) để người dùng tự chỉnh trong CapCut.

Chạy file lệnh từ thư mục này:
`~/video-tools/whisper-venv/bin/python -I scripts/<tên file>.py`

## Dùng chung (thư mục `../chung/`)

- `../chung/fonts/`: Poppins (tiếng Anh) và Be Vietnam Pro (khi cần tiếng Việt).
- `../chung/sfx/`: âm thanh hiệu ứng.

## Quy trình "dựng video mới"

1. Bóc lời video trong `moi/` (faster-whisper, model medium) và xem khung hình.
2. Chọn Kiểu A hoặc Kiểu B theo công thức, đề xuất các đoạn cắt.
3. Dựng, rồi phủ guideline lên khung hình để kiểm tra vùng chữ.
4. Xuất ra `xuat/` và gửi video cho người dùng xem.
5. Người dùng góp ý điều gì cần nhớ lâu dài thì ghi vào `CONG-THUC-EDIT.md`.
