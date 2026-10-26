#!/bin/sh
# Tải các font miễn phí (Google Fonts, giấy phép OFL) mà các kênh đang dùng vào chung/fonts/.
# Chạy:  sh chung/scripts/tai_font.sh
set -e
cd "$(dirname "$0")/../fonts"
B=https://raw.githubusercontent.com/google/fonts/main/ofl
for p in \
  poppins/Poppins-SemiBold.ttf poppins/Poppins-Bold.ttf poppins/Poppins-ExtraBold.ttf \
  bevietnampro/BeVietnamPro-SemiBold.ttf bevietnampro/BeVietnamPro-Bold.ttf bevietnampro/BeVietnamPro-ExtraBold.ttf \
  greatvibes/GreatVibes-Regular.ttf bebasneue/BebasNeue-Regular.ttf
do
  curl -fsSL -o "$(basename "$p")" "$B/$p" && echo "ok $(basename "$p")"
done
