
from unicodedata import normalize
filename_mac = "ºÙÀÓ1. 2020³â SW¸¶¿¡½ºÆ®·Î°úÁ¤ Á¦11±â ¿¬¼ö»ý Á¦Ãâ¼­·ù ¾È³»"
#filename_mac = "123째징4568_20250529_142207"
filename_nfc = normalize('NFC', filename_mac)
filename_cp949 = filename_nfc.encode('ISO-8859-1').decode('cp949')
print(filename_cp949)

"""
filename = r"c:\work\GeoData\한글파일이름.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write("내용입니다.")
"""

from PIL import Image
import cv2

# OpenCV 이미지
img_out = cv2.imread(r"d:\work\GeoData\car1.jpg")  # BGR 형식

# BGR → RGB 변환
img_rgb = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)

# PIL 이미지로 변환
img_pil = Image.fromarray(img_rgb)

# 한글 파일명으로 저장
save_path = r"d:\work\GeoData\사진_샘플.jpg"
img_pil.save(save_path)