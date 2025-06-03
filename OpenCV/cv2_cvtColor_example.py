# https://wikidocs.net/231860

"""
cv2.cvtColor: 이미지의 색 공간 (color space) 변환

cv2.cvtColor() 함수는 이미지의 색상 공간을 변환하는 데 사용됩니다. 이 함수를 사용하여 이미지를 다양한 색상 공간으로 변환할 수 있습니다.

함수 시그니처는 다음과 같습니다:

dst = cv2.cvtColor(src, code, dst, dstCn)
여기서 각 인자는 다음을 의미합니다:

src: 입력 이미지입니다.
code: 변환하려는 색상 공간을 지정하는 플래그입니다. 일반적으로 cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV 등이 사용됩니다. 입력 이미지의 색상 공간과 목표 색상 공간 사이의 변환 방법을 결정합니다. 150여개의 변환 코드가 존재하며 Color Space Conversions 페이지에서 직접 필요한 코드를 찾아 사용하시면 됩니다.
dst: 선택적으로 출력 이미지입니다. 입력 이미지와 동일한 크기와 타입을 가져야 합니다.
dstCn: 선택적으로 출력 이미지의 채널 수를 지정합니다.
이 함수는 변환된 결과 이미지를 반환합니다.

예를 들어, BGR 색상 공간에서 그레이스케일로 변환하는 방법은 다음과 같습니다:
"""

import cv2

# 이미지를 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# BGR 색상 공간에서 그레이스케일로 변환합니다.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 결과 이미지를 출력합니다.
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg' 이미지를 읽어들인 후 BGR 색상 공간에서 그레이스케일로 변환한 후 결과 이미지를 출력합니다.

마지막 편집일시 : 2024년 2월 25일 10:49 오후
"""