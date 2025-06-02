# https://yunwoong.tistory.com/73?category=902345
# https://colab.research.google.com/drive/1b7NP8D4p2MjukF935WWu6rY3OeSTxPo1?usp=sharing#scrollTo=lhcdsPom5PdK

# Detection OCR - 영수증, 명함

# 그림, 표, 바코드 등을 포함한 복잡한 구조의 이미지인 경우에서는 OCR 결과가 좋지 않습니다. 원하는 영역만 추출하여 OCR을 수행하면 좋을 것 같은데..
# 하지만 이미지에서 내가 원하는 영역을 정확하게 파악하고 출력하는 것은 쉬운 일이 아닙니다.
# 다양한 이미지에서 원하는 영역만 추출하여 OCR을 수행하거나 OCR결과에서 원하는 값을 찾는 방법에 대해 소개합니다. 

# 이미지에서 원하는 영역만 추출하여 OCR을 수행하거나 OCR결과에서 원하는 값을 찾는 방법에 대해 정리합니다.

#########################################################################################################################
# scan ocr module
#########################################################################################################################

# Install the necessary packages
# > sudo apt install tesseract-ocr
# > sudo apt-get install tesseract-ocr-kor
# > pip install pytesseract

# Import Packages
from imutils.perspective import four_point_transform
from imutils.contours import sort_contours
import matplotlib.pyplot as plt
import pytesseract
import imutils
import cv2
import re
import requests
import numpy as np

# Function to display images in Jupyter Notebooks and Google Colab
# Colab에서 이미지를 확인하기위한 Function
def plt_imshow(title='image', img=None, figsize=(8 ,5)):
    plt.figure(figsize=figsize)

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

# [이전 자료][scan_ocr_link]에서 설명한 Scan 이미지로 변환하는 방법을 Function으로 만들어 사용하도록 하겠습니다.
def make_scan_image(image, width, ksize=(5,5), min_threshold=75, max_threshold=200):
    image_list_title = []
    image_list = []

    org_image = image.copy()
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

    findCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영역으로 판단하고 break
        if len(approx) == 4:
            findCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 오류
    if findCnt is None:
        raise Exception(("Could not find outline."))

    output = image.copy()
    cv2.drawContours(output, [findCnt], -1, (0, 255, 0), 2)

    image_list_title.append("Outline")
    image_list.append(output)

    # 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
    transform_image = four_point_transform(org_image, findCnt.reshape(4, 2) * ratio)

    plt_imshow(image_list_title, image_list)
    plt_imshow("Transform", transform_image)

    return transform_image

# Load Image - 영수증 ======================================================================================
url = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
plt_imshow("orignal image", org_image)

receipt_image = make_scan_image(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100)

# 수정된 이미지를 OCR로 수행하면 아래와 같은 결과가 나옵니다.
options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt_image, cv2.COLOR_BGR2RGB), lang="eng", config=options)

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")


"""
# Load Image - 명함
url = 'https://user-images.githubusercontent.com/69428232/148511583-651cbe19-29ba-4b60-97b5-22c2829d56d9.jpg'           # NameCard
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
plt_imshow("orignal image", org_image)

receipt_image = make_scan_image(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100)

# 수정된 이미지를 OCR로 수행하면 아래와 같은 결과가 나옵니다.
options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt_image, cv2.COLOR_BGR2RGB), lang="eng", config=options)

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")
"""

#########################################################################################################################
# 이미지 처리 기술과 OpenCV 라이브러리를 사용하여 입력 이미지에서 원하는 텍스트를 추출 하는 방법
#########################################################################################################################

# 그림, 표, 바코드 등을 포함한 복잡한 구조의 이미지인 경우에서는 OCR 결과가 좋지 않습니다. 따라서 원하는 영역만 추출하여 OCR을 수행하면 좋을 것 같은데..
# 하지만 이미지에서 내가 원하는 영역을 정확하게 파악하고 출력하는 것은 쉬운 일이 아닙니다.

#1. 이미지 연산을 통한 영역 추출
# - 그레이스케일로 변환
# - 노이즈를 줄이기 위해 가우시안블러 적용
# - 흐릿한 Grayscale 이미지에 blackhat 모노폴리 연산을 적용 (blackhat연산은 밝은 배경(영수증의 배경)에서 어두운 영역(텍스트)을 드러내기 위해 사용됩니다.)
# - 닫힘 연산을 통해 끊어져보이는 객체를 연결하여 Grouping합니다.
gray = cv2.cvtColor(receipt_image, cv2.COLOR_BGR2GRAY)
(H, W) = gray.shape

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 20))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 21))

gray = cv2.GaussianBlur(gray, (11, 11), 0)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

grad = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
grad = np.absolute(grad)
(minVal, maxVal) = (np.min(grad), np.max(grad))
grad = (grad - minVal) / (maxVal - minVal)
grad = (grad * 255).astype("uint8")

grad = cv2.morphologyEx(grad, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

close_thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
close_thresh = cv2.erode(close_thresh, None, iterations=2)

plt_imshow(["Original", "Blackhat", "Gradient", "Rect Close", "Square Close"], [receipt_image, blackhat, grad, thresh, close_thresh], figsize=(16, 10))

# Grouping된 이미지를 좀 더 크게 보면 아래와 같습니다.
plt_imshow(["Square Close"], [close_thresh], figsize=(16, 10))

# Grouping 된 영역의 윤곽선을 찾고 그 윤곽선이 특정 조건 (Ex. 종횡비 등)에 만족하는 영역만 추출합니다.
cnts = cv2.findContours(close_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sort_contours(cnts, method="top-to-bottom")[0]

roi_list = []
roi_title_list = []

margin = 20
receipt_grouping = receipt_image.copy()

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w // float(h)

    if ar > 3.0 and ar < 6.5 and (W/2) < x:
        color = (0, 255, 0)
        roi = receipt_image[y - margin:y + h + margin, x - margin:x + w + margin]
        roi_list.append(roi)
        roi_title_list.append("Roi_{}".format(len(roi_list)))
    else:
        color = (0, 0, 255)

    cv2.rectangle(receipt_grouping, (x - margin, y - margin), (x + w + margin, y + h + margin), color, 2)
    cv2.putText(receipt_grouping, "".join(str(ar)), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, color, 2)

plt_imshow(["Grouping Image"], [receipt_grouping], figsize=(16, 10))

# 찾은 영역을 아래와 같습니다. 각 이미지를 OCR 수행합니다.
plt_imshow(roi_title_list, roi_list, figsize=(16, 10))

for roi in roi_list:
    gray_roi= cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    threshold_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    roi_text = pytesseract.image_to_string(threshold_roi)
    print(roi_text)

# 추출된 이미지만큼 OCR을 수행하면 성능이 많이 느리기 때문에 이미지를 Merge하여 OCR되는 횟수를 최소화합니다.
def mergeResize(img, row=300, col=200):
    IMG_COL = col #66

    # row값에 따른 col값 변경
    IMG_COL = int((row * IMG_COL)/row)

    IMG_ROW = row
    border_v = 0
    border_h = 0

    if (IMG_COL / IMG_ROW) >= (img.shape[0] / img.shape[1]):
        border_v = int((((IMG_COL / IMG_ROW) * img.shape[1]) - img.shape[0]) / 2)
    else:
        border_h = int((((IMG_ROW / IMG_COL) * img.shape[0]) - img.shape[1]) / 2)
    img = cv2.copyMakeBorder(img, top=border_v, bottom=border_v, left=0, right=border_h + border_h, borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255))
    img = cv2.resize(img, (IMG_ROW, IMG_COL))
    return img

for idx, roi in enumerate(roi_list):
  if idx == 0:
    mergeImg = mergeResize(roi)
  else:
    cropImg = mergeResize(roi)
    mergeImg = np.concatenate((mergeImg, cropImg), axis=0)

threshold_mergeImg = cv2.threshold(mergeImg, 150, 255, cv2.THRESH_BINARY)[1]
plt_imshow(["Merge Image"], [threshold_mergeImg])
merge_Img_text = pytesseract.image_to_string(threshold_mergeImg)
print(merge_Img_text)

# 2. 정규식을 통한 영역 추출
options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt_image, cv2.COLOR_BGR2RGB), config=options)

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")

# 전화번호, 가격, 합산가격 추출
phoneNums = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)         # 전화번호 추출
prices = re.findall(r"(?:NP )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)           # 가    격 추출
total_price = re.findall(r"(?:BAL )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)     # 합산가격 추출
print("전화번호 : {}".format(phoneNums))
print("가    격 : {}".format(prices))
print("합산가격 : {}".format(total_price))

"""
# Print text extracted from image
def pint_text_extracted_from_image(text, option):
    match option:
        case 1:
            # 전화번호, 가격, 합산가격 추출
            phoneNums = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)         # 전화번호 추출
            prices = re.findall(r"(?:NP )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)           # 가    격 추출
            total_price = re.findall(r"(?:BAL )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)     # 합산가격 추출 
            print("전화번호 : {}".format(phoneNums))
            print("가    격 : {}".format(prices))
            print("합산가격 : {}".format(total_price))
        case 2:
            tel = re.findall(r'(?:Tel )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
            mobile = re.findall(r'(?:Mobile )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)[0]
            addr = re.findall(r"[0-9\.\-+_]+\,.*", text)[0]
            print("유선전화 : {}".format(tel))
            print("휴대전화 : {}".format(mobile))
            print("이메일 : {}".format(emails))
            print("주소 : {}".format(addr))
        case _:
            print("")

# 정규식은 명함과 같은 이미지 OCR에 활용하면 좋을 것 같습니다. ===================================================
url = 'https://user-images.githubusercontent.com/69428232/155486780-55525c3c-8f5f-4313-8590-dd69d4ce4111.jpg'

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 

business_card_image = make_scan_image(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100)

options = "--psm 4"
text = pytesseract.image_to_string(business_card_image, config=options, lang='kor+eng')

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")

tel = re.findall(r'(?:Tel )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
mobile = re.findall(r'(?:Mobile )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)[0]
addr = re.findall(r"[0-9\.\-+_]+\,.*", text)[0]

# print("유선전화 : {}".format(tel))
# print("휴대전화 : {}".format(mobile))
# print("이메일 : {}".format(emails))
# print("주소 : {}".format(addr))

# Load Image - 영수증 ======================================================================================
url = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
org_image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR) 
plt_imshow("orignal image", org_image)

receipt_image = make_scan_image(org_image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100)

# 수정된 이미지를 OCR로 수행하면 아래와 같은 결과가 나옵니다.
options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt_image, cv2.COLOR_BGR2RGB), lang="eng", config=options)

# OCR결과 출력
print("[INFO] OCR결과:")
print("==================")
print(text)
print("\n")

# 전화번호, 가격, 합산가격 추출
#phoneNums = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)         # 전화번호 추출
#prices = re.findall(r"(?:NP )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)           # 가    격 추출
#total_price = re.findall(r"(?:BAL )([0-9\.\-+_]+\.[0-9\.\-+_]+)", text)     # 합산가격 추출
#print("전화번호 : {}".format(phoneNums))
#print("가    격 : {}".format(prices))
#print("합산가격 : {}".format(total_price))
"""