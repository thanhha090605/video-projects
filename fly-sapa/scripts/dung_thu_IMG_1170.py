"""Dựng thử fly-sapa/goc/IMG_1170.MOV theo fly-sapa/CONG-THUC-EDIT.md (Kiểu B: caption + chữ phản ứng).

Chạy (trong thư mục kênh):  ~/video-tools/whisper-venv/bin/python -I scripts/dung_thu_IMG_1170.py
Kết quả: fly-sapa/xuat/IMG_1170_kieuB.mp4
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # video-projects/
KENH = os.path.join(ROOT, "fly-sapa")
FFMPEG = os.path.expanduser("~/video-tools/bin/ffmpeg")
SRC = os.path.join(KENH, "goc/IMG_1170.MOV")
TAG = os.path.join(KENH, "TAG FSP HIGHEST IN SAPA.png")
GUIDE = os.path.join(KENH, "Guidelines_Template_-_Anthony_Smith.png")
FONTS = os.path.join(ROOT, "chung/fonts")
ASS = os.path.join(KENH, "xuat/IMG_1170_kieuB.ass")
OUT = os.path.join(KENH, "xuat/IMG_1170_kieuB.mp4")

XF = 0.25  # thời lượng chuyển cảnh loé trắng (giây)

# Các đoạn cắt từ video gốc (giây bắt đầu, giây kết thúc)
SEGMENTS = [
    (3.0, 9.0),     # "Wow! So these are all normally rice fields!"
    (29.6, 38.9),   # nhào lộn: "Woohoo!", "That was amazing!"
    (67.6, 79.9),   # tiếp đất: "Legs up!", "Woohoo!", "Yay!"
    (85.0, 89.2),   # ăn mừng: "Oh yeah!", "That was awesome!"  + kêu gọi đặt vé
]

# Chữ phản ứng: (giây trong video gốc, giây kết thúc, chữ, x, y)  — y phải nằm trong 568..1232
REACTIONS = [
    (3.2, 6.8, "wow!! these are all rice fields", 540, 1150),
    (30.0, 31.4, "woohoo!", 700, 900),
    (34.0, 38.8, "that was amazing!", 540, 1150),
    (67.6, 69.5, "legs up, legs up!", 540, 1150),
    (76.7, 78.2, "woohoo!", 690, 880),
    (79.0, 79.9, "yay!", 400, 900),
    (85.2, 87.0, "oh yeah!", 690, 1000),
    (87.5, 89.2, "that was awesome!", 540, 1150),
]

HOOK = "POV: YOUR FIRST\\NFLIGHT OVER SAPA'S\\NRICE TERRACES"
CTA_1 = "Book your flight:"
CTA_2 = "FLYSAPA.COM"


def seg_offsets():
    """Vị trí bắt đầu của mỗi đoạn trên dòng thời gian video thành phẩm."""
    offs, t = [], 0.0
    for i, (a, b) in enumerate(SEGMENTS):
        offs.append(t)
        t += (b - a) - (XF if i < len(SEGMENTS) - 1 else 0)
    return offs, t


def src_to_out(ts):
    offs, _ = seg_offsets()
    for (a, b), o in zip(SEGMENTS, offs):
        if a <= ts <= b:
            return o + (ts - a)
    raise ValueError(f"{ts}s không nằm trong đoạn nào")


def ass_time(t):
    h, rem = divmod(max(t, 0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def letter_fly_in(text, start_ms=0, step_ms=45, dur_ms=220):
    """Từng chữ cái hiện dần và trượt lên — giống chữ bay vào ở mẫu W3."""
    out = []
    for i, ch in enumerate(text):
        t0 = start_ms + i * step_ms
        out.append(
            "{\\alpha&HFF&\\fscy40\\t(%d,%d,\\alpha&H00&\\fscy100)}%s" % (t0, t0 + dur_ms, ch)
        )
    return "".join(out)


def build_ass(total):
    offs, _ = seg_offsets()
    cta_start = offs[-1] + 0.3
    lines = [
        "[Script Info]",
        "ScriptType: v4.00+",
        "PlayResX: 1080",
        "PlayResY: 1920",
        "WrapStyle: 0",
        "ScaledBorderAndShadow: yes",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding",
        # Caption chính: dải vàng (y 476..562), ngang 220..855
        "Style: Hook,Poppins ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,"
        "0,0,0,0,100,100,0,0,1,2,3,8,220,225,476,1",
        # Chữ phản ứng: vùng giữa
        "Style: React,Poppins SemiBold,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,"
        "0,0,0,0,100,100,0,0,1,3,0,5,220,225,0,1",
        # Kêu gọi đặt vé: vùng giữa, phía trên
        "Style: Cta1,Poppins Bold,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,"
        "0,0,0,0,100,100,0,0,1,2,3,8,220,225,0,1",
        "Style: Cta2,Poppins ExtraBold,96,&H004FD8FF,&H004FD8FF,&H00000000,&H90000000,"
        "0,0,0,0,100,100,0,0,1,3,3,8,220,225,0,1",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    lines.append(
        f"Dialogue: 0,{ass_time(0)},{ass_time(cta_start)},Hook,,0,0,0,,{{\\fad(150,200)}}{HOOK}"
    )
    for a, b, text, x, y in REACTIONS:
        lines.append(
            f"Dialogue: 1,{ass_time(src_to_out(a))},{ass_time(src_to_out(b))},React,,0,0,0,,"
            f"{{\\pos({x},{y})\\fad(80,120)}}{text}"
        )
    lines.append(
        f"Dialogue: 2,{ass_time(cta_start)},{ass_time(total)},Cta1,,0,0,0,,"
        f"{{\\pos(540,600)}}{letter_fly_in(CTA_1)}"
    )
    lines.append(
        f"Dialogue: 2,{ass_time(cta_start + 0.5)},{ass_time(total)},Cta2,,0,0,0,,"
        f"{{\\pos(540,684)}}{letter_fly_in(CTA_2, step_ms=55)}"
    )
    with open(ASS, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def build_filter():
    parts = []
    for i, (a, b) in enumerate(SEGMENTS):
        parts.append(
            f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=60,"
            f"eq=saturation=1.18:contrast=1.04,format=yuv420p,settb=1/60000[v{i}]"
        )
        parts.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=44100[a{i}]")
    offs, _ = seg_offsets()
    vprev, aprev = "v0", "a0"
    for i in range(1, len(SEGMENTS)):
        off = offs[i]
        parts.append(f"[{vprev}][v{i}]xfade=transition=fadewhite:duration={XF}:offset={off:.3f}[vx{i}]")
        parts.append(f"[{aprev}][a{i}]acrossfade=d={XF}[ax{i}]")
        vprev, aprev = f"vx{i}", f"ax{i}"
    parts.append("[1:v]scale=1080:1920:flags=lanczos,format=rgba[tag]")
    parts.append(f"[{vprev}][tag]overlay=0:0:format=auto[vt]")
    parts.append(f"[vt]ass={ASS}:fontsdir={FONTS},format=yuv420p[vout]")
    parts.append(f"[{aprev}]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[aout]")
    return ";".join(parts)


def main():
    _, total = seg_offsets()
    build_ass(total)
    cmd = [
        FFMPEG, "-hide_banner", "-y",
        "-i", SRC, "-loop", "1", "-i", TAG,
        "-filter_complex", build_filter(),
        "-map", "[vout]", "-map", "[aout]",
        "-t", f"{total:.3f}", "-r", "60",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "192k", "-ac", "2",
        "-movflags", "+faststart", OUT,
    ]
    print(f"Thời lượng: {total:.2f}s")
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
