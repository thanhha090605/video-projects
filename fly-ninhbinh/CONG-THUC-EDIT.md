# Công thức edit video Fly Ninh Bình

Rút ra từ 1 video mẫu `mau/Download.mp4` (24 giây). Video mẫu được tải về từ TikTok nên chỉ có độ phân giải 576×1024 và dính logo TikTok. Hai thứ đó **không** thuộc phong cách, không làm theo.
Claude đọc file này mỗi khi dựng video cho kênh Fly Ninh Bình. Có góp ý nào thì sửa thẳng vào đây.

---

## 1. Thông số xuất video

| Mục | Giá trị |
|---|---|
| Khung hình | Dọc 9:16, **1080×1920** |
| Tốc độ khung hình | **60 fps** (video gốc iPhone 60 fps 4K; DJI 59.94 fps) |
| Định dạng | MP4, H.264, chất lượng cao |
| Độ dài | **khoảng 20–25 giây** |
| Âm thanh | **Chỉ nhạc nền**, bỏ hẳn tiếng gốc (tiếng động cơ dù lượn rất ồn). Độ to khoảng −10 đến −12 LUFS |
| Nhạc | Bài trong `nhạc nền /`, bắt đầu từ giây 0, mờ dần ở 1 giây cuối |

## 2. Khung thương hiệu cố định

- **File dùng:** `TAG FNB.png`, cỡ 1080×1920 nền trong suốt. **Phủ lên toàn bộ khung hình suốt video**, không dịch chuyển.
- **Nội dung tag:** `NINH BÌNH 🪂`, nhãn vàng `NGẮM TRỌN DI SẢN`, logo Fly Ninh Bình mờ ở góc phải. Tag nằm ở trên vạch hồng thứ hai (y ≤ 318).

## 3. Vùng đặt chữ

Kênh này dùng **cùng guideline với Fly Sapa** (`Guidelines_Template_-_Anthony_Smith.png`), nên toạ độ giống hệt:

| Vùng | Ngang (x) | Dọc (y) |
|---|---|---|
| Khung an toàn chung | 220 → 855 | 324 → 1568 |
| Vùng giữa, **nơi đặt chữ chính của kênh này** | 220 → 855 | 568 → 1232 |
| Giới hạn đáy | — | không thấp hơn 1568 |

- Video mẫu đặt câu mở đầu ở **y ≈ 770** và các cụm chữ hai dòng ở **y ≈ 1020 → 1170**. Cả hai đều nằm trong vùng giữa, cứ giữ như vậy.
- Trong video mẫu, cụm cuối `bình luận "Fly Ninh Bình"` bị tràn ra ngoài vạch ngang (rộng khoảng 800px). Từ giờ, **chữ dài quá 635px thì giảm cỡ** cho vừa khoảng 220 → 855.

## 4. Font chữ

Kênh này có chữ tiếng Việt nên **không dùng Poppins**, vì Poppins không có dấu tiếng Việt.

| Dùng cho | Font (trong `chung/fonts/`) |
|---|---|
| Dòng trên của cụm chữ, câu mở đầu | **Be Vietnam Pro** SemiBold / Bold |
| Dòng dưới viết tay | **Great Vibes**, gần như y hệt font trong video mẫu |

## 5. Kiểu video: "Mỗi cảnh một điểm bán hàng"

Video gồm 6 cảnh, mỗi cảnh khoảng 3 giây, **cắt theo nhịp nhạc**. Mỗi cảnh đi kèm một cụm chữ nói lên một lý do nên bay.

| Cảnh | Thời gian | Hình ảnh | Chữ |
|---|---|---|---|
| 1. Mở đầu | 0 → 5,5s | Cảnh rộng: dù được thổi phồng và cất cánh trên cánh đồng, núi đá vôi phía sau | Câu trích dẫn trong ngoặc kép, chữ thường, 3 dòng, ở y ≈ 770. Câu đang dùng: `"khi mục tiêu là` / `được trải nghiệm thì` / `chẳng có gì là thất bại"` (câu trong mẫu: "bay một chuyến sẽ đỡ đau tim hơn yêu một người nên tuổi trẻ thì cứ bay đi") |
| 2. Khách | 5,5 → 8,3s | Khách cười to, quay selfie trên xe dù | `dù lượn` / *Ninh Bình* |
| 3. Trên không | 8,3 → 11,7s | Khách bay ngang qua, nhìn cảnh | `Ngắm trọn di sản` / *Tràng An & Hoa Lư* |
| 4. An toàn | 11,7 → 14,5s | Cánh dù nhỏ trên nền trời xanh | `Phi công` / *có chứng chỉ bay* |
| 5. Toàn cảnh | 14,5 → 17,4s | Góc nhìn từ trên cao: ruộng xanh, cánh dù cam nhỏ | `bảo hiểm & GoPro quay` / *xuyên suốt hành trình bay* |
| 6. Kêu gọi | 17,4 → 24s | Cánh dù cam bay trên làng quê, cảnh rộng | `Ưu đãi 5%` / *bình luận "Fly Ninh Bình"* |

### Kiểu chữ của cụm hai dòng

- **Dòng trên:** Be Vietnam Pro SemiBold, cỡ khoảng 60, **trắng**, có bóng đen mờ. Chữ thường, viết hoa chữ đầu nếu là câu.
- **Dòng dưới:** Great Vibes, cỡ khoảng 100, **chồng sát lên dòng trên** (hai dòng gần chạm nhau), có bóng mờ.
  - Tên địa danh và lời kêu gọi (*Ninh Bình*, *Tràng An & Hoa Lư*, *bình luận "Fly Ninh Bình"*): màu **trắng**.
  - Lời cam kết (*có chứng chỉ bay*, *xuyên suốt hành trình bay*): màu **vàng kem nhạt** (#F3E3A6).
- **Vị trí:** căn giữa, y ≈ 1020 → 1170.
- **Chuyển chữ:** chữ cũ mờ dần, chữ mới hiện dần (khoảng 0,3 giây), đúng lúc cắt cảnh.

### Kiểu chữ câu mở đầu

- Be Vietnam Pro SemiBold, cỡ khoảng 40, trắng, viền đen mỏng, đặt trong ngoặc kép, căn giữa ở y ≈ 770.

### Chuyển cảnh và âm thanh hiệu ứng (bạn yêu cầu thêm, mẫu gốc không có)

- **Chuyển cảnh:** dài 0,4 giây, **căn giữa đúng điểm cắt** (trùng phách nhạc). Thứ tự hiệu ứng:
  1. loé trắng
  2. mở vòng tròn
  3. trượt mượt sang trái
  4. hoà tan (hai cảnh mờ dần vào nhau)
  5. loé trắng (vào cảnh kêu gọi lúc bình minh)
- **Không dùng hiệu ứng zoom vào giữa:** khi giữa khung là cánh dù, màn hình biến thành mảng màu trơn.
- **Không dùng hiệu ứng trượt lên** (bạn yêu cầu bỏ).
- **Chữ khi chuyển cảnh:** chữ cũ tắt trước điểm cắt 0,05 giây, chữ mới hiện sau điểm cắt 0,15 giây (hiện dần 0,25 giây, tắt dần 0,2 giây). Như vậy hai cụm chữ không bao giờ đè lên nhau.
- **Âm thanh hiệu ứng** (file trong `chung/sfx/`, tạo bằng `chung/scripts/tao_sfx.py`):
  - **Không dùng tiếng vút khi chuyển cảnh** (bạn yêu cầu bỏ). File `whoosh.wav` vẫn còn trong `chung/sfx/` nếu sau này cần.
  - **Tiếng bụp** (`pop.wav`, âm lượng 0,3): khi mỗi cụm chữ hiện ra.
  - **Tiếng dội trầm** (`impact.wav`, âm lượng 0,7): ngay khi vào cảnh kêu gọi "Ưu đãi 5%".
  - Đây là âm thanh tự tạo, khá đơn giản. Có file hiệu ứng thật thì bỏ vào `chung/sfx/` **cùng tên** để thay thế.

### Hình ảnh

- Màu tươi: trời xanh đậm, ruộng xanh lá rực, cánh dù cam nổi bật. Có thể tăng nhẹ độ bão hoà.
- Cảnh quay iPhone 4K dọc: thu nhỏ về 1080×1920.
- Cảnh DJI quay ngang (2720×1530): **cắt lấy phần giữa** thành khung dọc. Chọn phần có cánh dù hoặc chủ thể.
- Video gốc iPhone quay ở chế độ HDR (10-bit). Khi xuất phải chuyển sang màu thường (SDR) để không bị bệt màu.

## 6. Quy trình dựng một video mới

1. Xem các video trong `goc/` hoặc `moi/`, chọn 6 cảnh khớp với 6 vai trò ở mục 5.
2. Cắt mỗi cảnh khoảng 3 giây (riêng cảnh 1 khoảng 5,5 giây, cảnh 6 khoảng 6 giây). Ưu tiên cắt trúng nhịp nhạc.
3. Chuyển về 1080×1920, 60 fps, màu SDR.
4. Phủ `TAG FNB.png`.
5. Thêm chữ theo mục 5. Kiểm tra bằng guideline, không chữ nào lọt ra ngoài.
6. Thay toàn bộ âm thanh bằng nhạc nền, mờ dần ở cuối.
7. Xuất ra `xuat/`.

## 6b. Thông số từ bản dựng thử đầu tiên (chờ bạn duyệt)

- **File lệnh:** `scripts/dung_thu_ninhbinh.py` → `xuat/ninhbinh_thu_01.mp4` (23,5 giây).
- **Cắt theo nhịp nhạc:** bài "cho tôi lang thang" có nhịp khoảng 92 BPM, phách đầu ở 0,12s. Cắt cảnh mỗi 3,25 giây (5 nửa phách): 5,32 · 8,57 · 11,82 · 15,07 · 18,32 · kết thúc 23,52.
- **Cỡ chữ:** dòng trên 80, chữ viết tay 150, câu mở đầu khoảng 41–52. Chữ tự giảm cỡ để không vượt độ rộng 635px.
- **Chữ viết tay quá dài:** xuống thành 2 dòng, khoảng cách dòng bằng 0,62 lần cỡ chữ. Dấu `|` trong chữ đánh dấu chỗ được phép xuống dòng, ví dụ `bình luận|Fly Ninh Bình`.
- **Vị trí:** đáy dòng trên ở y = 1000, dòng viết tay bắt đầu ở y = 960 (chồng sát lên dòng trên).
- **Viền:** viền đen mờ (độ dày 4, độ nhoè 6) để chữ đọc được trên nền trời sáng.
- **Tên thương hiệu:** không bọc "Fly Ninh Bình" trong ngoặc kép, vì ngoặc làm chữ dài thêm và bị thu nhỏ.
- **Thiếu cảnh khách cận mặt:** video gốc không có cảnh này, nên cảnh 2 dùng cảnh dù vàng cất cánh thay thế.

## 7. Cần chuẩn bị thêm

- [x] Tag `TAG FNB.png`
- [x] Guideline (giống Fly Sapa)
- [x] Nhạc nền `nhạc nền /cho tôi lang thang.MP4`. Nhạc trong video mẫu là một bài khác, có lời.
- [ ] Font chính thức nếu có. Tạm dùng Be Vietnam Pro + Great Vibes.
- [ ] Thêm video mẫu nếu có. Hiện mới có 1 video, càng nhiều mẫu thì công thức càng chính xác.
