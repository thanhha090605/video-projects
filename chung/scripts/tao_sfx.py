"""Tạo bộ âm thanh hiệu ứng cơ bản bằng ffmpeg (không cần tải gì về) vào chung/sfx/.

Chạy:  ~/video-tools/whisper-venv/bin/python -I chung/scripts/tao_sfx.py
Có file hiệu ứng thật (.wav/.mp3) thì cứ bỏ vào chung/sfx/ với cùng tên để thay thế.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FFMPEG = os.path.expanduser("~/video-tools/bin/ffmpeg")
SFX = os.path.join(ROOT, "chung/sfx")

# tên file: (thời lượng giây, biểu thức kênh trái | kênh phải, bộ lọc thêm)
SOUNDS = {
    # Tiếng gió vút: nhiễu, to dần rồi tắt nhanh, lướt từ trái sang phải
    "whoosh.wav": (0.6,
                   "(random(0)*2-1)*pow(sin(PI*t/0.6),3)*(1-t/0.6)|(random(1)*2-1)*pow(sin(PI*t/0.6),3)*(t/0.6)",
                   "highpass=f=300,lowpass=f=5000,volume=1.6"),
    # Tiếng "bụp" khi chữ hiện: âm cao trượt xuống, tắt rất nhanh
    "pop.wav": (0.15, "0.8*sin(2*PI*t*(1100-3000*t))*exp(-30*t)|0.8*sin(2*PI*t*(1100-3000*t))*exp(-30*t)", None),
    # Tiếng dội trầm: âm trầm tụt xuống + chút tiếng nổ ngắn
    "impact.wav": (1.4,
                   "0.9*sin(2*PI*t*(70-25*t))*exp(-3.5*t)+0.5*(random(0)*2-1)*exp(-30*t)|"
                   "0.9*sin(2*PI*t*(70-25*t))*exp(-3.5*t)+0.5*(random(1)*2-1)*exp(-30*t)",
                   "lowpass=f=2500"),
}


def main():
    os.makedirs(SFX, exist_ok=True)
    for name, (dur, expr, extra) in SOUNDS.items():
        af =f"aevalsrc='{expr}':s=44100:d={dur}"
        cmd = [FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i", af]
        if extra:
            cmd += ["-af", extra]
        cmd += [os.path.join(SFX, name)]
        subprocess.run(cmd, check=True)
        print("ok", name)


if __name__ == "__main__":
    main()
