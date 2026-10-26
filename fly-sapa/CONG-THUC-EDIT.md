# Công thức edit video Fly Sapa

Rút ra từ 3 video mẫu trong `mau/` (`1005 sapa fix.mp4`, `W2 4_2.mp4`, `W3 5.mp4`).
Claude đọc file này mỗi khi dựng video mới. Có góp ý nào thì sửa thẳng vào đây.

---

## 1. Thông số xuất video (cả 3 mẫu giống nhau)

| Mục | Giá trị |
|---|---|
| Khung hình | Dọc 9:16, **1080×1920** |
| Tốc độ khung hình | **60 fps** |
| Định dạng | MP4, H.264, chất lượng cao (~14 Mbps) | 
| Âm thanh | AAC, 44.1 kHz, stereo |
| Độ dài | **17–45 giây** |
| Độ to âm thanh | Khoảng −14 LUFS (mức chuẩn của TikTok/Reels) |
| Khoảng lặng | Không có. Âm thanh chạy liên tục từ đầu đến cuối |

## 2. Khung thương hiệu cố định (luôn có, suốt cả video)

- **File dùng:** `TAG FSP HIGHEST IN SAPA.png`. Đây là ảnh nền trong suốt cỡ 2160×3840.
- **Cách dùng:** thu nhỏ về 1080×1920 rồi **phủ lên toàn bộ khung hình**, giữ nguyên vị trí, không dịch chuyển hay co giãn riêng.
- **Nội dung tag:** chữ `HIGHEST IN SAPA 🪂` và nhãn vàng `1.750 Meters` ở góc trên trái, logo Fly SAPA mờ ở góc trên phải. Tag nằm trong khoảng y ≈ 100–318.
- Với cảnh cuối chia đôi màn hình (Kiểu B), tag chỉ phủ ở nửa trên, đúng như mẫu W2.

## 2b. Vùng đặt chữ — theo `Guidelines_Template_-_Anthony_Smith.png`

Mọi chữ thêm vào (phụ đề, caption, chú thích, kêu gọi hành động) **phải nằm trong các vùng dưới đây**, để không bị nút và chữ của TikTok/Reels che mất. Toạ độ tính theo pixel trên khung 1080×1920.

| Vùng | Ngang (x) | Dọc (y) | Dùng cho |
|---|---|---|---|
| **Khung an toàn chung** | 220 → 855 (giữa vạch xanh trong và vạch đỏ trong) | 324 → 1568 | Không chữ nào được vượt ra ngoài khung này |
| Dải hồng | — | 258 → 318 | Đáy của tag thương hiệu. Không đặt chữ khác ở đây |
| **Dải vàng: caption chính / hook** | 220 → 855 | **476 → 562** | Câu caption Kiểu B (`POV: …`, `Forever and ever…`). Dòng đầu bắt đầu từ vạch vàng trên. Nếu chữ dài thì được tràn xuống tới y ≈ 680 |
| **Vùng giữa** | 220 → 855 | 568 → 1232 | Kêu gọi đặt vé (`Book your flight: FLYSAPA.COM`), chú thích cảm xúc, chữ phản ứng |
| **Dải xanh: phụ đề** | 220 → 855 | **1391 → 1508** | Phụ đề karaoke Kiểu A, 1 dòng, căn giữa |
| Giới hạn đáy | — | 1568 (vạch đỏ dưới) | Không chữ nào thấp hơn vạch này |

Ghi chú khi so với mẫu:
- Phụ đề của video Sapa (y ≈ 1490) và caption của W3 nằm đúng vùng. Từ giờ cứ theo đúng như vậy.
- Khối `COMMENT "FLY SAPA" GET SPECIAL VOUCHERS` trong mẫu Sapa bị tràn xuống dưới vạch đỏ 1568. Từ giờ, khối này phải nằm trọn trong **vùng giữa** (568 → 1232).
- Chữ dài quá 635px (khoảng 220 → 855) thì xuống dòng hoặc giảm cỡ chữ. Không bao giờ cho chữ chạm ra ngoài.

## 3. Kiểu cảnh quay

- Cảnh quay từ gậy selfie / camera 360 (Insta360, GoPro), góc rộng, hơi cong ở viền.
- Màu tươi, rực, trời xanh, ruộng bậc thang. Không chỉnh màu kiểu "phim".
- Rất ít cắt: mỗi cảnh dài 5–15 giây. Giữ khoảnh khắc thật, không cắt vụn.

## 4. Hai kiểu video

### Kiểu A — "Câu chuyện có lời thoại" (mẫu: `1005 sapa fix`, 45 giây)
Dùng khi video có hội thoại thật giữa phi công và khách.

- **Âm thanh:** giữ tiếng nói thật ở phần hội thoại (0–28s). Khi hết thoại (lúc đang bay) thì để nhạc và tiếng cười. Âm lượng to, khoảng −10 LUFS.
- **Phụ đề kiểu karaoke:**
  - Chữ **IN HOA, trắng, đậm**, 3–4 chữ mỗi dòng, chỉ 1 dòng.
  - Từ đang được nói thì **đổi nền xanh dương** (ô chữ nhật bo nhẹ sau chữ).
  - Vị trí: khoảng **70% chiều cao**, tính từ trên xuống (phần dưới khung, trên vùng nút của TikTok).
- **Chú thích cảm xúc** (sticker chữ nhỏ cạnh mặt người): `*really nervous`, `*tear`, `*listen carefully`, `*pinky promise`, `*ready`.
  - Chữ thường, trắng, viền đen, **xoay nghiêng** theo hướng mặt, có dấu `*` ở đầu.
- **Cấu trúc câu chuyện:**
  1. **0–20s**, *Lo lắng trước khi bay:* khách sợ, phi công trấn an ("trust me", "pinky promise").
  2. **20–28s**, *Chạy đà, cất cánh:* khung hình rung, nhanh, hồi hộp ("run run run").
  3. **28–40s**, *Bay lên, vỡ oà:* khách cười to, thấy cảnh đẹp.
  4. **41–45s**, *Kêu gọi hành động:* cảnh rộng cánh dù trên trời, chữ giữa màn hình:
     `COMMENT` / `"FLY SAPA"` (xanh dương, viền trắng) / `GET SPECIAL VOUCHERS`.

### Kiểu B — "Nhạc + câu caption" (mẫu: `W2 4_2` 17 giây, `W3 5` 21 giây)
Dùng khi không có lời thoại đáng giữ.

- **Âm thanh:** nhạc nền trending. Giữ tiếng reo vui thật nếu có.
- **Một câu caption chính** đặt ở **1/3 trên**, giữa màn hình, giữ suốt phần thân video. Có emoji phía trên:
  - Ví dụ W2: `☁️🎀✨` / `Forever and ever a` / `"You only live once" girly`. Kiểu chữ trộn: font không chân đậm + font có chân nghiêng cho phần trong ngoặc kép.
  - Ví dụ W3: `✨🇻🇳🌞` / `POV: YOUR PILOT SAID LANDING WOULD BE AS LIGHT AS A FEATHER`. Chữ in hoa trắng, đậm.
- **Chữ phản ứng nhỏ** cạnh người (lấy từ câu nói thật lúc cuối, ví dụ W3 giây 12–17 "thank you, easy huh, yeah easy, so easy"): `whoooo`, `see?`, `thank you!!`, `yeah easy`, `so easy`. Chữ thường, trắng, viền đen.
- **Cấu trúc:** 1 cảnh chính khoảng 13–14 giây → **1 cú chuyển cảnh** → cảnh cuối 3–7 giây, kèm kêu gọi đặt vé.
- **Chuyển cảnh:** loé sáng (light leak) khoảng 0,3 giây (W2), hoặc cắt thẳng (W3).
- **Cảnh cuối chia đôi màn hình (cố ý, mẫu W2 từ giây 13):** cùng một cảnh bay đặt 2 lần, chồng **trên / dưới**, mỗi nửa cao 960px. Khung thương hiệu chỉ nằm ở nửa trên. Chữ kêu gọi đặt vé nằm **ngay đường ranh giữa hai nửa**.
- **Kêu gọi hành động cuối video:**
  - W2: `BOOK YOUR FLIGHT:` (chữ vàng nhạt) / `flysapa.com` (font có chân, trắng), đặt giữa màn hình, đè lên đường ranh của màn hình chia đôi.
  - W3: `Book your flight:` / `FLYSAPA.COM` (vàng), đặt ở 1/3 trên, **chữ bay vào từng chữ cái**.

## 5. Quy trình dựng một video mới

1. Xem video gốc trong `goc/` hoặc `moi/`: bóc lời, tìm cảnh hay nhất.
2. Chọn **Kiểu A** nếu có hội thoại cảm xúc, **Kiểu B** nếu chỉ có cảnh đẹp.
3. Cắt còn 17–45 giây theo cấu trúc ở trên.
4. Chuyển về khung dọc 1080×1920, 60 fps.
5. Gắn khung thương hiệu (mục 2).
6. Thêm phụ đề hoặc caption, chú thích cảm xúc, kêu gọi hành động. **Đặt chữ đúng vùng ở mục 2b.** Trước khi xuất, chụp vài khung hình có phủ guideline lên để kiểm tra không chữ nào lọt ra ngoài.
7. Cân âm thanh về khoảng −14 LUFS.
8. Xuất ra `xuat/`.

## 6. Cần chuẩn bị thêm

- [x] **Tag thương hiệu**: `TAG FSP HIGHEST IN SAPA.png`
- [x] **Guideline vùng chữ**: `Guidelines_Template_-_Anthony_Smith.png`
- [ ] **Font chữ** chính thức (file .ttf / .otf). Tạm thời dùng font miễn phí trong `chung/fonts/` (dùng chung mọi kênh):
  - **Poppins ExtraBold:** caption chính, chữ `FLYSAPA.COM`
  - **Poppins Bold:** `Book your flight:`
  - **Poppins SemiBold:** chữ phản ứng
  - **Bebas Neue:** dự phòng cho tiêu đề kiểu chữ cao, hẹp
- Cỡ chữ đang dùng, chờ bạn duyệt (khung 1080×1920): caption 64, chữ phản ứng 54, `Book your flight:` 62, `FLYSAPA.COM` 96.
- Bản dựng thử đầu tiên: `scripts/dung_thu_IMG_1170.py` → `xuat/IMG_1170_kieuB.mp4` (xuất bộ CapCut: `scripts/xuat_capcut.py`). Dùng làm khuôn cho các video sau.
- [ ] **Nhạc nền** cho Kiểu B.
