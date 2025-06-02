# https://yunwoong.tistory.com/58
# https://colab.research.google.com/drive/1xrLV_Q7w202B4iXGYWPM7QFCwXnRsKQ_#scrollTo=BEQaAwRHQwYM

# 영수증, 명함

#import sys
#sys.stdout.reconfigure(encoding='utf-8')

#3. Google Drive Mount / Test Image Load
#이미지가 존재하는 Google Drive Mount
#편의를 위해 URL로 이미지를 Load 하여 수행하겠습니다

import cv2
# from google.colab import drive
# drive.mount('/content/drive')

# %cd drive/MyDrive/Colab Notebooks/Tesseract_OCR
# path = './asset/images/ocr_test.png'
# org_image = cv2.imread(path)

#Mounted at /content/drive
#/content/drive/MyDrive/Colab Notebooks/Tesseract_OCR

import requests
import numpy as np

url = 'https://user-images.githubusercontent.com/69428232/148318703-ef6bd43f-ec4f-42f5-a336-3b584a662982.jpg'

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

#4. Recognition
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

rgb_image = cv2.cvtColor(org_image, cv2.COLOR_BGR2RGB)

# 테스트 하려는 이미지는 한글, 영어, 숫자가 혼합된 이미지 입니다.

plt.figure(figsize=(8, 5))

plt.subplot(1, 1, 1)
plt.imshow(rgb_image)
plt.title('RGB Image')
plt.xticks([]), plt.yticks([])

#plt.show()

#KeyError: 'PNG' 오류 발생이 되었다면 pytesseract, Pillow 설치 후 설치된 버전이 적용되지 않았기때문입니다.
#런타임 재수행하시면 정상수행이 됩니다.

# use Tesseract to OCR the image
# text= pytesseract.image_to_data(rgb_image, output_type=Output.DICT, lang='kor+eng')
# print(text.keys())
text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
#print(text)

#5. additional examples
#한가지 추가적인 예를 하나 살표보겠습니다.
#우리가 인식하고자 하는 이미지는 사실 그렇게 깨끗하지 않습니다. 다양한 음영과 노이즈가 존재하죠.

url = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image2 = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
rgb_image2 = cv2.cvtColor(org_image2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 5))

plt.subplot(1, 1, 1)
plt.imshow(rgb_image2)
plt.title('additional example image')
plt.xticks([]), plt.yticks([])

#plt.show()




#import pytesseract
#import cv2 
#import matplotlib.pyplot as plt

#테스트 하려는 이미지는 한글, 영어, 숫자가 혼합된 이미지 입니다.
path = r"d:\work\GeoData\ocr_test.jpg"
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#config = ('-l kor+eng --oem 3 --psm 4')

# use Tesseract to OCR the image 
text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
#text = pytesseract.image_to_string(rgb_image, config=config)
print(text)

# Terminal 에서 한글 깨지는 것

# 파일 인코딩 확인: print(text) 실행 전에 text.encode('utf-8') 또는 text.encode('utf-8').decode('utf-8')을 추가해 인코딩 문제를 방지할 수 있습니다.
#text = text.encode('utf-8')
#text = text.encode('utf-8').decode('utf-8')
print(text)
# 콘솔 설정 변경: Windows의 경우, chcp 65001 명령어를 실행해 UTF-8 인코딩을 활성화한 후 다시 시도해 보세요.
#chcp 65001
# 코드 수정: sys.stdout.reconfigure(encoding='utf-8')를 추가하면 출력 시 UTF-8 인코딩을 사용할 수 있습니다.
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
#print(text)