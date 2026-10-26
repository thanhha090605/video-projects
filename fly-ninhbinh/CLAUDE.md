# Kênh Fly Ninh Bình

Đây là dự án riêng của kênh **Fly Ninh Bình** (dù lượn có động cơ ở Ninh Bình, chữ tiếng Việt).
Người dùng không biết code: trả lời bằng tiếng Việt, ngắn gọn, tự chạy lệnh. Hướng dẫn chung nằm ở `../CLAUDE.md`.

## Trước khi dựng video

**Luôn đọc `CONG-THUC-EDIT.md` trước.** Kênh dùng kiểu "mỗi cảnh một điểm bán hàng":
- 6 cảnh, cắt theo phách nhạc.
- Cụm chữ 2 dòng: Be Vietnam Pro ở dòng trên, Great Vibes viết tay ở dòng dưới.
- Chỉ dùng nhạc nền, kèm tiếng "bụp" khi chữ hiện và tiếng dội trầm ở cảnh ưu đãi.

Những thứ người dùng **đã yêu cầu bỏ**, không được thêm lại:
- tiếng vút khi chuyển cảnh
- hiệu ứng chuyển cảnh trượt lên

## Tài nguyên của kênh

- `TAG FNB.png`: tag thương hiệu, phủ kín khung hình.
- `Guidelines_Template_-_Anthony_Smith.png`: vùng đặt chữ (giống Fly Sapa).
- `nhạc nền /`: nhạc nền. Lưu ý tên thư mục có dấu cách ở cuối.
- `mau/`: video mẫu. `goc/`, `moi/`: video cần dựng. `xuat/`: thành phẩm.
- `scripts/dung_thu_ninhbinh.py`: khuôn dựng video. Video mới thì **copy file này thành file mới** rồi sửa `SCENES`, `HOOK`, `CUTS` (cắt theo phách nhạc), `TRANSITIONS`.

Chạy file lệnh từ thư mục này:
`~/video-tools/whisper-venv/bin/python -I scripts/<tên file>.py`

## Dùng chung (thư mục `../chung/`)

- `../chung/fonts/`: Be Vietnam Pro và Great Vibes. **Không dùng Poppins**, vì Poppins không có dấu tiếng Việt.
- `../chung/sfx/`: `pop.wav`, `impact.wav` (tạo lại bằng `../chung/scripts/tao_sfx.py`).

## Lưu ý kỹ thuật

- Video iPhone quay HDR (HLG): phải chuyển sang SDR. Khuôn dựng đã có sẵn bước này (`HLG_TO_SDR`).
- Video DJI quay ngang: cắt lấy khung dọc quanh chủ thể (tham số tâm cắt trong `SCENES`).
- Khi đổi nhạc thì phải đo lại nhịp (BPM, phách đầu) để tính lại `CUTS`.

## Quy trình "dựng video mới"

1. Xem khung hình các video trong `moi/` (hoặc `goc/`), chọn 6 cảnh theo 6 vai trò trong công thức.
2. Dựng, rồi phủ guideline lên khung hình để kiểm tra không chữ nào lọt ra ngoài vùng.
3. Xuất ra `xuat/` và gửi video cho người dùng xem.
4. Người dùng góp ý điều gì cần nhớ lâu dài thì ghi vào `CONG-THUC-EDIT.md`.
