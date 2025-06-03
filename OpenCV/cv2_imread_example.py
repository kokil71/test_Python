# https://wikidocs.net/231853

"""
cv2.imread: 이미지 파일 읽기
cv2.imread() 함수는 OpenCV 라이브러리에서 이미지 파일을 읽어들이는 함수입니다. 이 함수는 이미지 파일의 경로를 인자로 받아들이고, 해당 이미지를 NumPy 배열 형태로 반환합니다. 예를 들어:
"""

import cv2

# 이미지 파일을 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 이미지를 출력합니다.
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imread()

"""
함수는 이미지 파일을 NumPy 배열 형태인 ndarray로 반환합니다. 따라서 해당 함수로 이미지를 읽어들이면 NumPy의 ndarray 객체로 반환됩니다. 이러한 형태로 반환된 이미지는 NumPy 배열의 다양한 기능을 활용하여 이미지 처리 및 분석 작업을 수행할 수 있습니다.

마지막 편집일시 : 2024년 2월 25일 8:00 오후
"""