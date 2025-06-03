# https://wikidocs.net/231464

"""
03-3 Opencv-python: 컴퓨터 비전 처리 라이브러리
opencv-python1은 컴퓨터 비전과 관련된 작업을 위한 강력하고 다양한 기능을 제공하는 라이브러리, OpenCV (Open Source Computer Vision Library)의 Python 바인딩입니다. OpenCV는 원래 C++로 개발되었지만, opencv-python 패키지를 통해 Python에서도 그 기능을 손쉽게 사용할 수 있습니다.

OpenCV의 주요 기능:
이미지 처리: 이미지의 기본적인 처리 작업(읽기, 쓰기, 변환)부터 복잡한 처리(필터링, 특징 추출, 이미지 복원 등)까지 지원합니다.
비디오 처리: 비디오 파일 읽기 및 쓰기, 비디오 스트림 처리, 객체 추적 등의 기능을 제공합니다.
컴퓨터 비전: 얼굴 인식, 객체 탐지, 광학 문자 인식(OCR), 패턴 인식 등 다양한 컴퓨터 비전 관련 작업을 수행할 수 있습니다.
기계 학습: OpenCV는 기본적인 기계 학습 알고리즘(예: k-최근접 이웃, SVM, 의사결정 트리 등)을 제공하며, 이미지 데이터와 함께 사용할 수 있습니다.
실시간 컴퓨터 비전: 카메라 스트림을 실시간으로 처리하고, 객체 탐지, 얼굴 인식, 동작 인식 등을 수행할 수 있습니다.
예제 코드:
"""

import cv2

# 이미지 읽기
#image = cv2.imread('example.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 이미지를 회색조로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 저장
#cv2.imwrite('gray_example.jpg', gray_image)
cv2.imwrite(r'd:\work\GeoData\lena_gray.jpg', gray_image)

# 이미지 표시
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
이 코드에서는 OpenCV를 사용하여 이미지를 읽고, 회색조로 변환한 다음 저장하고 표시하는 방법을 보여줍니다.

opencv-python은 이미지 및 비디오 데이터를 다루는 응용 프로그램에서 널리 사용되며, 연구, 프로토타이핑, 제품 개발 등 다양한 분야에서 활용됩니다. 그 강력한 기능과 높은 유연성으로 인해 컴퓨터 비전과 관련된 많은 프로젝트에서 필수적인 도구로 여겨집니다.

API 가이드
상세 API guide는 아래 웹 사이트를 참고 바랍니다.

https://opencv-python.readthedocs.io/
https://github.com/opencv/opencv-python ↩
"""