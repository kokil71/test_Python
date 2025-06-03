# https://wikidocs.net/231862

"""
cv2.warpAffine: 이미지 아핀 변환

cv2.warpAffine() 함수는 이미지에 아핀 변환을 적용하는 데 사용됩니다. 이 함수를 사용하면 이미지를 이동, 회전, 크기 조정 등의 변환을 적용할 수 있습니다.



아핀 변환의 예 (출처: https://en.wikipedia.org/wiki/Affine_transformation)

함수 시그니처는 다음과 같습니다:

dst = cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
여기서 각 인자는 다음을 의미합니다:


src: 입력 이미지입니다.
M: 아핀 변환 매트릭스입니다. 이 매트릭스는 회전, 이동, 크기 조정 등의 변환을 나타냅니다.
dsize: 결과 이미지의 크기입니다. (width, height) 형식의 튜플로 지정됩니다.
dst: 선택적으로 출력 이미지입니다. 입력 이미지와 동일한 크기와 타입을 가져야 합니다.
flags: 선택적으로 보간법을 지정하는 플래그입니다. 기본값은 cv2.INTER_LINEAR로, 선형 보간법을 사용합니다.
borderMode: 선택적으로 가장자리 픽셀 처리 방법을 지정합니다.
borderValue: 선택적으로 가장자리 픽셀의 값을 지정합니다.
이 함수는 아핀 변환을 적용한 결과 이미지를 반환합니다.

예를 들어, 이미지를 45도 회전시키는 방법은 다음과 같습니다:
"""

import cv2

# 이미지를 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 이미지의 중심점을 계산합니다.
center = (image.shape[1] // 2, image.shape[0] // 2)

# 회전 매트릭스를 생성합니다.
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# 이미지를 회전시킵니다.
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# 결과 이미지를 출력합니다.
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg' 이미지를 읽어들인 후 이미지의 중심점을 계산하고, 45도 각도로 이미지를 회전시킨 후 결과 이미지를 출력합니다.

마지막 편집일시 : 2024년 2월 25일 10:25 오후
"""