# https://wikidocs.net/231857

"""
cv2.threshold: 임계값 기준 이미지의 이진화

cv2.threshold() 함수는 이미지의 이진화를 수행하는 데 사용됩니다. 즉, 이미지를 흑백으로 변환하고 임계값 이상의 픽셀을 하나의 값으로, 이하의 픽셀을 다른 값으로 설정합니다.

함수 시그니처는 다음과 같습니다:

retval, dst = cv2.threshold(src, thresh, maxval, type[, dst])
여기서 각 인자는 다음을 의미합니다:

src: 입력 이미지로, 단일 채널 (그레이스케일) 이미지여야 합니다.
thresh: 임계값으로, 이 값을 기준으로 픽셀 값을 분류합니다.
maxval: 임계값 이상일 때 적용할 값입니다. 보통 255로 설정됩니다.
type: 임계값을 적용하는 방법을 지정하는 플래그입니다. 주요 유형으로는 cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV 등이 있습니다.
dst: 선택적으로 출력 이미지입니다. 원본 이미지와 동일한 크기와 타입을 가져야 합니다.
이 함수는 두 개의 반환 값을 갖습니다:

retval: 사용된 임계값입니다.
dst: 이진화된 결과 이미지입니다.
예를 들어:
"""

import cv2

# 이미지 파일을 그레이스케일로 읽어들입니다.
#image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r'd:\work\GeoData\lena.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지를 이진화합니다.
retval, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 이진화된 이미지를 출력합니다.
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg'를 그레이스케일로 읽어들인 후, 임계값을 127로 설정하여 이진화한 뒤 결과를 출력합니다.

마지막 편집일시 : 2024년 2월 25일 8:02 오후
"""