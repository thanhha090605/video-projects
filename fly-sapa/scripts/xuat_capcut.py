"""Xuất bộ nguyên liệu để tự chỉnh trong CapCut, từ cùng kịch bản với dung_thu_IMG_1170.py.

Chạy (trong thư mục kênh):  ~/video-tools/whisper-venv/bin/python -I scripts/xuat_capcut.py
Kết quả: fly-sapa/xuat/capcut_IMG_1170/
"""
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dung_thu_IMG_1170 as kb  # noqa: E402

OUT_DIR = os.path.join(kb.KENH, "xuat/capcut_IMG_1170")

VIDEO_ARGS = [
    "-r", "60", "-c:v", "libx264", "-preset", "medium", "-crf", "16",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2", "-movflags", "+faststart",
]
LOOK = "scale=1080:1920:flags=lanczos,fps=60,eq=saturation=1.18:contrast=1.04,format=yuv420p"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:])
        sys.exit(r.returncode)


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(path, items):
    # CapCut đặt phụ đề trên một track, nên dòng trước phải kết thúc trước khi dòng sau bắt đầu
    items = sorted(items)
    items = [(a, min(b, items[i + 1][0] - 0.05) if i + 1 < len(items) else b, t)
             for i, (a, b, t) in enumerate(items)]
    with open(path, "w", encoding="utf-8") as f:
        for i, (a, b, text) in enumerate(items, 1):
            f.write(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{text}\n\n")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    offs, total = kb.seg_offsets()

    # 1. Từng đoạn cắt riêng, chưa có chữ, chưa có tag
    for i, (a, b) in enumerate(kb.SEGMENTS, 1):
        run([kb.FFMPEG, "-y", "-ss", str(a), "-to", str(b), "-i", kb.SRC, "-vf", LOOK, *VIDEO_ARGS,
             os.path.join(OUT_DIR, f"doan_{i:02d}.mp4")])

    # 2. Video đã ghép sẵn 4 đoạn + chuyển cảnh loé trắng, chưa có chữ và tag
    parts = []
    for i, (a, b) in enumerate(kb.SEGMENTS):
        parts.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,{LOOK},settb=1/60000[v{i}]")
        parts.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=44100[a{i}]")
    vprev, aprev = "v0", "a0"
    for i in range(1, len(kb.SEGMENTS)):
        parts.append(f"[{vprev}][v{i}]xfade=transition=fadewhite:duration={kb.XF}:offset={offs[i]:.3f}[vx{i}]")
        parts.append(f"[{aprev}][a{i}]acrossfade=d={kb.XF}[ax{i}]")
        vprev, aprev = f"vx{i}", f"ax{i}"
    parts.append(f"[{aprev}]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[aout]")
    run([kb.FFMPEG, "-y", "-i", kb.SRC, "-filter_complex", ";".join(parts),
         "-map", f"[{vprev}]", "-map", "[aout]", *VIDEO_ARGS,
         os.path.join(OUT_DIR, "video_ghep_san_khong_chu.mp4")])

    # 3. Phụ đề .srt, khớp thời gian với video_ghep_san_khong_chu.mp4
    cta_start = offs[-1] + 0.3
    write_srt(os.path.join(OUT_DIR, "chu_phan_ung.srt"),
              [(kb.src_to_out(a), kb.src_to_out(b), text) for a, b, text, _x, _y in kb.REACTIONS])
    write_srt(os.path.join(OUT_DIR, "caption_va_keu_goi.srt"), [
        (0, cta_start, kb.HOOK.replace("\\N", " ")),
        (cta_start, total, f"{kb.CTA_1}\n{kb.CTA_2}"),
    ])

    # 4. Tag thương hiệu cỡ 1080x1920, guideline, font
    run([kb.FFMPEG, "-y", "-i", kb.TAG, "-vf", "scale=1080:1920:flags=lanczos",
         os.path.join(OUT_DIR, "tag_fly_sapa_1080x1920.png")])
    shutil.copy(kb.GUIDE,
                os.path.join(OUT_DIR, "guideline_1080x1920.png"))
    font_dir = os.path.join(OUT_DIR, "fonts")
    os.makedirs(font_dir, exist_ok=True)
    for name in ("Poppins-ExtraBold.ttf", "Poppins-Bold.ttf", "Poppins-SemiBold.ttf"):
        shutil.copy(os.path.join(kb.FONTS, name), font_dir)
    print(f"Xong: {OUT_DIR}  (tổng {total:.2f}s)")


if __name__ == "__main__":
    main()
