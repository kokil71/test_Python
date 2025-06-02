# https://yunwoong.tistory.com/72?category=902345
# https://colab.research.google.com/drive/1Uz9N7BbVX6qNrpRGHGOcZuW0XY00a1iw#scrollTo=lEoKE7QYjrRH

# Scan OCR - 영수증, 명함 등 사각형 형태의 Boundary 있을 경우 회전을 통하여 이미지 수정, 차 번호 인식은 어려움
# 이미지를 Scan한 이미지로 변경하여 OCR을 수행합니다.

#Import Packages
from imutils.perspective import four_point_transform
import matplotlib.pyplot as plt
import pytesseract
import imutils
import cv2
import re
import requests
import numpy as np

#Function to display images in Jupyter Notebooks and Google Colab
#Colab에서 이미지를 확인하기위한 Function
def plt_imshow(title='image', img=None, figsize=(8 ,5)):
    #plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

def kko_run_tesseract_ocr(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100, lang='eng'):
    #plt_imshow("orignal image", org_image)

    image = org_image.copy()
    #image = imutils.resize(image, width=500)
    image = imutils.resize(image, width=width)
    ratio = org_image.shape[1] / float(image.shape[1])

    # 이미지를 grayscale로 변환하고 blur를 적용
    # 모서리를 찾기위한 이미지 연산
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
    blurred = cv2.GaussianBlur(gray, ksize, 0)
    #edged = cv2.Canny(blurred, 75, 200)
    edged = cv2.Canny(blurred, min_threshold, max_threshold)

    plt_imshow(['gray', 'blurred', 'edged'], [gray, blurred, edged])

    #Contour란 같은 값을 가진 곳을 연결한 선이라고 생각하면 됩니다. 이미지의 외곽선을 검출하기 위해 사용합니다.
    #cv2.findContours(image, mode, method, contours=None, hierarchy=None, offset=None) -> contours
    # - image: 입력 이미지. non-zero 픽셀을 객체로 간주함  
    # - mode: 외곽선 검출 모드. cv2.RETR_로 시작하는 상수  
    # - method: 외곽선 근사화 방법. cv2.CHAIN_APPROX_로 시작하는 상수

    # contours를 찾아 크기순으로 정렬
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    receiptCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영수증 영역으로 판단하고 break
        if len(approx) == 4:
            receiptCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 오류
    if receiptCnt is None:
        raise Exception(("Could not find receipt outline."))

    output = image.copy()
    cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)
    plt_imshow("Receipt Outline", output)

    # 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
    receipt = four_point_transform(org_image, receiptCnt.reshape(4, 2) * ratio)
    plt_imshow("Receipt Transform", receipt)

    #config = ('-l kor+eng --oem 3 --psm 4')
    options = "--psm 4"
    #options = "-l " + lang + " --psm 4"
    text = pytesseract.image_to_string(cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB), lang=lang, config=options)

    # OCR결과 출력
    print("[INFO] OCR결과:")
    print("==================")
    print(text)
    print("\n")

# ksize 값 확인
# ksize는 커널 크기를 지정하는 튜플 (width, height) 형식으로 설정해야 합니다. 예를 들어, (5, 5)와 같은 값이 필요합니다.
# - 만약 ksize가 단일 숫자라면, (3, 3)처럼 튜플로 변경해 주세요.
# min_threshold 및 max_threshold 값 확인
# - cv2.Canny()의 임계값(min_threshold, max_threshold)은 보통 0~255 범위 내의 값이어야 합니다. 예를 들어:
# - 너무 낮거나 높은 값을 설정하면 엣지 검출이 제대로 안 될 수 있으므로 적절한 값을 선택하세요.
def run_tesseract_ocr(image, width, ksize=(5,5), min_threshold=75, max_threshold=200, lang='eng'):
    plt_imshow("orignal image", image)

    image_list_title = []
    image_list = []

    image = imutils.resize(image, width=width)
    ratio = org_image.shape[1] / float(image.shape[1])

    # 이미지를 grayscale로 변환하고 blur를 적용
    # 모서리를 찾기위한 이미지 연산
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, ksize, 0)
    edged = cv2.Canny(blurred, min_threshold, max_threshold)

    image_list_title = ['gray', 'blurred', 'edged']
    image_list = [gray, blurred, edged]

    # contours를 찾아 크기순으로 정렬
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    receiptCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영수증 영역으로 판단하고 break
        if len(approx) == 4:
            receiptCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 오류
    if receiptCnt is None:
        raise Exception(("Could not find receipt outline."))

    output = image.copy()
    cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)

    image_list_title.append("Receipt Outline")
    image_list.append(output)

    # 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
    receipt = four_point_transform(org_image, receiptCnt.reshape(4, 2) * ratio)

    plt_imshow(image_list_title, image_list)
    plt_imshow("Receipt Transform", receipt)

    options = "--psm 4"

    text = pytesseract.image_to_string(cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB), lang=lang, config=options)

    # OCR결과 출력
    print("[INFO] OCR결과:")
    print("==================")
    print(text)    

"""
#Image Load - Lotto
url = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'          # Lotto

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 

plt_imshow("orignal image", org_image)

image = org_image.copy()
image = imutils.resize(image, width=500)
ratio = org_image.shape[1] / float(image.shape[1])

# 이미지를 grayscale로 변환하고 blur를 적용
# 모서리를 찾기위한 이미지 연산
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 200)

plt_imshow(['gray', 'blurred', 'edged'], [gray, blurred, edged])

# contours를 찾아 크기순으로 정렬
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

receiptCnt = None

# 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영수증 영역으로 판단하고 break
	if len(approx) == 4:
		receiptCnt = approx
		break

# 만약 추출한 윤곽이 없을 경우 오류
if receiptCnt is None:
	raise Exception(("Could not find receipt outline."))

output = image.copy()
cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)
plt_imshow("Receipt Outline", output)

# 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
receipt = four_point_transform(org_image, receiptCnt.reshape(4, 2) * ratio)
plt_imshow("Receipt Transform", receipt)

options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB), config=options)

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")
"""


# 옵션값을 변경하며 OCR을 수행하면서, 인식율이 좋은 각 수치를 찾습니다.
#image : 원본 이미지
#width : resize width
#ksize : 가우시안 커널 크기
#min_threshold : Canny 알고리즘의 마지막 단계인 Hysteresis를 수행하기 위한 임계값 1
#max_threshold : Canny 알고리즘의 마지막 단계인 Hysteresis를 수행하기 위한 임계값 2
#lang : Tesseract OCR 언어



#Image Load - 영수증
url = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'          # Lotto

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)  
plt_imshow("orignal image", org_image)

run_tesseract_ocr(org_image, width=500, ksize=(5, 5), min_threshold=75, max_threshold=200, lang='eng')

#Image Load - 명함
url = 'https://user-images.githubusercontent.com/69428232/148511583-651cbe19-29ba-4b60-97b5-22c2829d56d9.jpg'           # NameCard

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
plt_imshow("orignal image", org_image)

run_tesseract_ocr(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100, lang='kor+eng')

# Image Load - Car License
imPath = r"d:\work\GeoData\car2.jpg"
image_nparray = np.asarray(bytearray(open(imPath, "rb").read()), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
plt_imshow("orignal image", org_image)

run_tesseract_ocr(org_image, width=500, ksize=(5, 5), min_threshold=75, max_threshold=200, lang='kor+eng')

