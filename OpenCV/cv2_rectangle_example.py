# https://wikidocs.net/231858

"""
cv2.rectangle: 이미지 상에 직사각형 그리기

cv2.rectangle() 함수는 이미지 상에 직사각형을 그리는 데 사용됩니다. 이 함수는 주어진 이미지나 이미지 배열에 사각형을 그리고자 할 때 유용하게 사용됩니다.

함수 시그니처는 다음과 같습니다:

cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
여기서 각 인자는 다음을 의미합니다:

img: 사각형을 그릴 이미지입니다.
pt1: 사각형의 왼쪽 상단 꼭지점 좌표입니다. (x, y) 형식의 튜플이어야 합니다.
pt2: 사각형의 오른쪽 하단 꼭지점 좌표입니다. (x, y) 형식의 튜플이어야 합니다.
color: 사각형의 색상입니다. (B, G, R) 형식의 튜플이나 스칼라 값으로 지정할 수 있습니다.
thickness: 선택적으로 사각형의 선 두께를 지정합니다. 기본값은 1입니다. 음수 값을 전달하면 내부를 채웁니다.
lineType: 선택적으로 선의 형태를 지정합니다. 기본값은 cv2.LINE_8입니다.
shift: 선택적으로 좌표값의 소수 부분을 비트 시프트할 양을 지정합니다.
예를 들어:
"""

import cv2

# 이미지를 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 사각형을 그릴 좌표를 설정합니다.
pt1 = (100, 100)
#pt2 = (300, 300)
pt2 = (300, 200)

# 사각형을 그립니다.
cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)

# 이미지를 화면에 표시합니다.
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg' 이미지에 (100, 100)에서 (300, 300)까지의 사각형을 그린 후, 결과 이미지를 화면에 표시합니다.

마지막 편집일시 : 2024년 2월 25일 8:03 오후
"""