# https://joyhong.tistory.com/79
# Tesseract로 OCR 하기

from PIL import Image 
from pytesseract import * 

filename = r"D:\work\GeoData\sample.jfif" 
image = Image.open(filename)
text = image_to_string(image, lang="kor") 

with open(r"D:\work\GeoData\sample.txt", "w") as f: 
    f.write(text) 