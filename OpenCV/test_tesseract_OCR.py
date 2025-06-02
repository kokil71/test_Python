# Tesseract-OCR를 Python에서 사용하는 방법에 대한 예제와 샘플 코드가 있습니다.
# # OCR : Optical Character Recognition
# [Python에서 Tesseract-OCR 설치 및 사용 방법](https://playground.naragara.com/954/)  
# [Tesseract를 이용한 OCR(광학 문자 판독) 예제](https://m.blog.naver.com/hn03049/221957851802)  
# [파이썬 Tesseract OCR - 이미지에서 문자 추출](https://blog.naver.com/PostView.naver?blogId=dsz08082&logNo=222655962994)  
# 테서랙트 사용자 매뉴얼 : https://tesseract-ocr.github.io/tessdoc/
# 출력 품질 향상 : https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html#rescaling
# 버전 4.00+에 대한 훈련된 데이터 파일 : https://tesseract-ocr.github.io/tessdoc/Data-Files.html
# 알파 채널 : https://www.techopedia.com/definition/1945/alpha-channel
# 테서랙트를 초기화할 수 없습니다. : https://stackoverflow.com/questions/14800730/could-not-initialize-tesseract
# Tesseract와 OpenCV를 이용한 딥러닝 기반 OCR 텍스트 인식: https://learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/
# cv2-tools 2.4.0 : https://pypi.org/project/cv2-tools/
# 이 링크들에서 **설치 방법, 기본 사용법, OCR 적용 예제** 등을 확인할 수 있습니다.  혹시 특정 기능을 구현하고 싶다면 알려주세요! 

# https://playground.naragara.com/954/

from PIL import Image
import cv2
import pytesseract
import matplotlib.pyplot as plt


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"   

"""
#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\lotto.png"), lang='kor', config='--psm 7 --oem 0')
#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\lotto.png"), lang='kor', config='--psm 6 --oem 0')
#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\lotto.png"), lang='kor', config='--psm 3 --oem 0')
str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\lotto.png"), lang='kor')
print(str)

#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_4-6.png"), lang='kor', config='--psm 7 --oem 0')
#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_4-6.png"), lang='kor', config='--psm 6 --oem 0')
#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_4-6.png"), lang='kor', config='--psm 3 --oem 0')
str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_4-6.png"), lang='kor')
print(str)

str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_6-2.png"), lang='kor')
print(str)


str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\명함.png"), lang='kor')
print(str)
str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\명함.png"), lang='eng')
print(str)

str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\명함.png"), lang='kor+eng')
print(str)


str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\img_7-2.png"), lang='kor+eng')
print(str)
"""

# [ 원본 이미지의 그레이 처리 작업 후 문자열 추출 테스트 ] 
#imPath = r"d:\work\GeoData\lotto.png"
#imPath = r"d:\work\GeoData\명함.png"
imPath = r"d:\work\GeoData\namecard.png"
#imPath = r"d:\work\GeoData\ocr_test.jpg"
#imPath = r"d:\work\GeoData\ocr_test.png"

# Define config parameters.
# '-l eng' for using the English language
# '--oem 1' sets the OCR Engine Mode to LSTM only.

#config = ('-l kor --oem 1 --psm 3')
config = ('-l kor+eng --oem 3 --psm 4')

# Read image from disk
#img = cv2.imread(imPath, cv2.COLOR_BGR2GRAY)
img = cv2.imread(imPath, 1)
#image_base = Image.open(imPath)
#img = cv2.imread(image_base, 1)
#cv2.imshow("orignal", img)
plt.imshow(img)
plt.show()

str = pytesseract.image_to_string(img, config=config)
print(str)
print('이미지 그레이처리')
img_gray = cv2.imread(imPath, cv2.COLOR_BGR2GRAY)
img_gray = cv2.imread(imPath, cv2.IMREAD_GRAYSCALE)
#cv2.imshow("grayscale", img_gray)
plt.imshow(img_gray)
plt.show()

str = pytesseract.image_to_string(img, config=config)
print(str)


#str = pytesseract.image_to_string(Image.open(r"d:\work\GeoData\ocr_test.jpg"), lang='kor+eng')
#print(str)

cv2.waitKey(0)
cv2.destroyAllWindows()