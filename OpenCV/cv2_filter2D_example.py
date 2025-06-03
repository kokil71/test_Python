#https://wikidocs.net/231851

"""
cv2.filter2D: 이미지 2차원 필터링

cv2.filter2D1는 OpenCV 라이브러리에서 제공하는 함수로, 사용자가 정의한 커널(또는 필터)를 이미지에 적용하여 2차원 필터링을 수행하는 기능을 제공합니다. 이 함수는 이미지의 세부 사항을 강조하거나, 이미지를 흐리게 하는 등 다양한 이미지 처리 효과를 구현할 수 있습니다.

기본 사용법:
dst = cv2.filter2D(src, ddepth, kernel, anchor, delta, borderType)
여기서 각 매개변수는 다음과 같은 의미를 가집니다:

src: 입력 이미지입니다. 보통 numpy 배열로 표현됩니다.
ddepth: 결과 이미지의 깊이(비트 단위)입니다. -1로 지정하면 입력 이미지와 동일한 깊이를 사용합니다.
kernel: 필터링에 사용될 커널입니다. numpy 배열로 정의되며, 일반적으로 부동소수점 값으로 구성됩니다.
anchor: 선택적으로 커널의 중심을 지정하는 점입니다. 기본값은 (-1, -1)로, 커널의 중심을 사용합니다.
delta: 필터링된 픽셀에 추가적으로 더해질 값. 기본값은 0입니다.
borderType: 이미지 가장자리 픽셀을 확장하는 방식을 결정합니다. 예를 들어, cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, cv2.BORDER_WRAP 등이 있습니다. 좀 더 자세한 내용은 "opencv의 borderType 에 대하여" 섹션을 참고해주세요.
사용 예제:
"""

import cv2
import numpy as np

# 원본 이미지 로드
#src = cv2.imread('image.jpg')
src = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 사용자 정의 커널 생성 (예: 평균 필터)
kernel = np.ones((5, 5), np.float32) / 25

# filter2D 함수를 사용하여 이미지 필터링
dst = cv2.filter2D(src, -1, kernel)

# 결과 이미지 출력
cv2.imshow('Filtered Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
이 예제에서는 5x5 크기의 평균 필터를 이미지에 적용하여 흐릿한 효과를 만듭니다. cv2.filter2D 함수는 다양한 종류의 사용자 정의 필터를 적용할 때 유용하며, 이미지의 세부 사항을 강조하거나 경계를 감지하는 등 다양한 이미지 처리 작업에 사용될 수 있습니다.

https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04, https://www.geeksforgeeks.org/python-opencv-filter2d-function/ ↩

마지막 편집일시 : 2024년 2월 25일 11:00 오후
"""
