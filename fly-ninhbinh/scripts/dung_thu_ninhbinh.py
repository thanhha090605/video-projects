"""Dựng thử video Fly Ninh Bình từ fly-ninhbinh/goc/ theo fly-ninhbinh/CONG-THUC-EDIT.md
(kiểu "mỗi cảnh một điểm bán hàng", chữ 2 dòng, nhạc nền + tiếng bụp, dội trầm, chuyển cảnh theo phách).

Chạy (trong thư mục kênh):  ~/video-tools/whisper-venv/bin/python -I scripts/dung_thu_ninhbinh.py
Kết quả: fly-ninhbinh/xuat/ninhbinh_thu_01.mp4
"""
import os
import subprocess
import sys

from PIL import ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # video-projects/
KENH = os.path.join(ROOT, "fly-ninhbinh")
FFMPEG = os.path.expanduser("~/video-tools/bin/ffmpeg")
FONTS = os.path.join(ROOT, "chung/fonts")
TAG = os.path.join(KENH, "TAG FNB.png")
MUSIC = os.path.join(KENH, "nhạc nền /cho tôi lang thang.MP4")
ASS = os.path.join(KENH, "xuat/ninhbinh_thu_01.ass")
OUT = os.path.join(KENH, "xuat/ninhbinh_thu_01.mp4")

# Vùng chữ theo guideline: x 220..855
TEXT_W = 635
FONT_TOP = ("Be Vietnam Pro SemiBold", "BeVietnamPro-SemiBold.ttf")
FONT_SCRIPT = ("Great Vibes", "GreatVibes-Regular.ttf")

WHITE = "&H00FFFFFF&"
CREAM = "&H00A6E3F3&"  # #F3E3A6

# Nhạc ~92 BPM, phách đầu ở 0,116s; cắt cảnh mỗi 5 nửa-phách (3,25s)
BEAT0, HALF = 0.116, 0.65
CUTS = [BEAT0 + HALF * k for k in (8, 13, 18, 23, 28, 36)]  # 5,32 · 8,57 · 11,82 · 15,07 · 18,32 · 23,52

# (file, giây bắt đầu, tâm cắt ngang cho cảnh quay ngang (0..1) hoặc None, dòng trên, dòng dưới, màu dòng dưới)
SCENES = [
    ("goc/IMG_7432.MOV", 15.0, None, None, None, None),  # cánh dù cam bung lên lúc bình minh
    ("goc/IMG_7155.MOV", 17.6, None, "dù lượn", "Ninh Bình", WHITE),
    ("goc/DJI 07.mp4", 1.5, 0.49, "Ngắm trọn di sản", "Tràng An & Hoa Lư", WHITE),
    ("goc/DJI 07.mp4", 10.0, 0.46, "Phi công", "có chứng chỉ bay", CREAM),
    ("goc/IMG_7155.MOV", 24.0, None, "bảo hiểm & GoPro quay", "xuyên suốt hành trình bay", CREAM),
    ("goc/IMG_7432.MOV", 23.5, None, "Ưu đãi 5%", "bình luận|Fly Ninh Bình", WHITE),
]
HOOK = ["“khi mục tiêu là", "được trải nghiệm thì", "chẳng có gì là thất bại”"]

# Chuyển cảnh tại mỗi điểm cắt (tên hiệu ứng xfade của ffmpeg), căn giữa đúng phách nhạc
XF = 0.4
TRANSITIONS = ["fadewhite", "circleopen", "smoothleft", "fade", "fadewhite"]  # không dùng slideup

# Âm thanh hiệu ứng (chung/sfx/, tạo bằng tao_sfx.py): (file, âm lượng)
SFX_DIR = os.path.join(ROOT, "chung/sfx")
POP, IMPACT = ("pop.wav", 0.3), ("impact.wav", 0.7)  # không dùng tiếng vút khi chuyển cảnh

HLG_TO_SDR = ("zscale=t=linear:npl=203,format=gbrpf32le,tonemap=hable:desat=0,"
              "zscale=p=bt709:t=bt709:m=bt709:r=tv,format=yuv420p")


def fit(text, font, size, maxw=TEXT_W):
    """Giảm cỡ chữ cho tới khi dòng chữ rộng không quá maxw px."""
    ft = ImageFont.truetype(os.path.join(FONTS, font[1]), size)
    w = ft.getlength(text)
    return size if w <= maxw else int(size * maxw / w)


def script_lines(text, size=150, min_size=115):
    """Dòng viết tay: giữ 1 dòng nếu vừa khung ở cỡ đủ to, nếu không thì bẻ làm 2 dòng.
    Dấu | trong chữ đánh dấu chỗ được phép xuống dòng (không thì tự chọn chỗ cân nhất)."""
    one = text.replace("|", " ")
    fs = fit(one, FONT_SCRIPT, size)
    words = one.split()
    if fs >= min_size or len(words) < 2:
        return [one], fs
    if "|" in text:
        parts = [p.strip() for p in text.split("|", 1)]
    else:
        best = min(range(1, len(words)),
                   key=lambda k: abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
        parts = [" ".join(words[:best]), " ".join(words[best:])]
    return parts, min(fit(p, FONT_SCRIPT, size) for p in parts)


def ass_time(t):
    h, rem = divmod(max(t, 0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def build_ass(total):
    starts = [0.0] + CUTS[:-1]
    lines = [
        "[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920",
        "WrapStyle: 2", "ScaledBorderAndShadow: yes", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding",
        # Viền đen mờ toả ra (\blur) thay cho bóng đổ, giống mẫu
        f"Style: Top,{FONT_TOP[0]},80,&H00FFFFFF,&H00FFFFFF,&H50000000,&H00000000,"
        "0,0,0,0,100,100,0,0,1,4,0,2,0,0,0,1",
        f"Style: Script,{FONT_SCRIPT[0]},150,&H00FFFFFF,&H00FFFFFF,&H50000000,&H00000000,"
        "0,0,0,0,100,100,0,0,1,4,0,8,0,0,0,1",
        f"Style: Hook,{FONT_TOP[0]},52,&H00FFFFFF,&H00FFFFFF,&H40000000,&H00000000,"
        "0,0,0,0,100,100,0,0,1,3,0,5,0,0,0,1",
        "", "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    fade = "\\fad(250,200)\\blur6"
    # Câu mở đầu: 3 dòng, căn giữa ở y ≈ 770
    hook_fs = min(fit(t, FONT_TOP, 52) for t in HOOK)
    hook = "\\N".join(HOOK)
    lines.append(f"Dialogue: 0,{ass_time(0.2)},{ass_time(CUTS[0] - 0.05)},Hook,,0,0,0,,"
                 f"{{\\pos(540,770)\\fs{hook_fs}{fade}}}{hook}")
    # Cụm chữ: dòng trên đáy ở y=1000, dòng viết tay chồng sát bên dưới (1 hoặc 2 dòng), đáy < 1232
    for (_f, _s, _c, top, script, color), a, b in zip(SCENES, starts, CUTS):
        if not top:
            continue
        # chữ cũ tắt ngay trước điểm cắt, chữ mới hiện sau khi chuyển cảnh xong một nửa
        a, b = a + 0.15, (b - 0.05 if b < total else total)
        parts, sfs = script_lines(script)
        lines.append(f"Dialogue: 1,{ass_time(a)},{ass_time(b)},Top,,0,0,0,,"
                     f"{{\\pos(540,1000)\\fs{fit(top, FONT_TOP, 80)}{fade}}}{top}")
        for k, part in enumerate(parts):
            y = 960 + k * int(sfs * 0.62)
            lines.append(f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Script,,0,0,0,,"
                         f"{{\\pos(540,{y})\\fs{sfs}\\1c{color}{fade}}}{part}")
    with open(ASS, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def sfx_events():
    """(giây, file, âm lượng): bụp khi chữ hiện, dội trầm ở cảnh kêu gọi."""
    ev = [(0.2, *POP)]
    for i, cut in enumerate(CUTS[:-1]):
        if SCENES[i + 1][3]:
            ev.append((cut + 0.12, *POP))
    ev.append((CUTS[-2], *IMPACT))
    return ev


def main():
    total = CUTS[-1]
    build_ass(total)
    n = len(SCENES)

    # Mỗi cảnh lấy dư XF/2 ở hai đầu để chuyển cảnh nằm giữa điểm cắt (đúng phách)
    seg_start = [0.0] + [c - XF / 2 for c in CUTS[:-1]]
    seg_end = [c + XF / 2 for c in CUTS[:-1]] + [total]

    cmd = [FFMPEG, "-hide_banner", "-y"]
    parts = []
    for i, (src, ss, cx, *_) in enumerate(SCENES):
        length = seg_end[i] - seg_start[i]
        ss = ss - (XF / 2 if i else 0)
        cmd += ["-ss", f"{ss:.3f}", "-t", f"{length:.3f}", "-i", os.path.join(KENH, src)]
        if cx is None:  # iPhone dọc 4K HDR (HLG)
            chain = f"scale=1080:1920:flags=lanczos,{HLG_TO_SDR},eq=saturation=1.22:contrast=1.05"
        else:  # DJI ngang 2720x1530: cắt lấy khung dọc quanh tâm cx
            chain = (f"crop=860:1530:'min(max({cx}*iw-430,0),iw-860)':0,"
                     "scale=1080:1920:flags=lanczos,eq=saturation=1.15:contrast=1.04")
        parts.append(f"[{i}:v]{chain},fps=60,setsar=1,format=yuv420p,"
                     f"trim=duration={length:.3f},setpts=PTS-STARTPTS[v{i}]")
    prev = "v0"
    for i in range(1, n):
        parts.append(f"[{prev}][v{i}]xfade=transition={TRANSITIONS[i - 1]}:duration={XF}:"
                     f"offset={seg_start[i]:.3f}[x{i}]")
        prev = f"x{i}"

    cmd += ["-loop", "1", "-i", TAG, "-i", MUSIC]
    parts.append(f"[{n}:v]scale=1080:1920,format=rgba[tag]")
    parts.append(f"[{prev}][tag]overlay=0:0:format=auto[vt]")
    parts.append(f"[vt]ass={ASS}:fontsdir={FONTS},format=yuv420p[vout]")

    # Nhạc nền + âm thanh hiệu ứng
    parts.append(f"[{n + 1}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample=44100,"
                 "aformat=channel_layouts=stereo[music]")
    mix = ["[music]"]
    for k, (t, name, vol) in enumerate(sfx_events()):
        cmd += ["-i", os.path.join(SFX_DIR, name)]
        idx = n + 2 + k
        ms = int(max(t, 0) * 1000)
        parts.append(f"[{idx}:a]aresample=44100,aformat=channel_layouts=stereo,"
                     f"volume={vol},adelay={ms}|{ms}[s{k}]")
        mix.append(f"[s{k}]")
    parts.append("".join(mix) + f"amix=inputs={len(mix)}:duration=first:normalize=0,"
                 f"afade=t=out:st={total - 1:.3f}:d=1,loudnorm=I=-11:TP=-1:LRA=11,aresample=44100[aout]")
    cmd += [
        "-filter_complex", ";".join(parts), "-map", "[vout]", "-map", "[aout]",
        "-t", f"{total:.3f}", "-r", "60",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high",
        "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
        "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-movflags", "+faststart", OUT,
    ]
    print(f"Thời lượng: {total:.2f}s")
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
