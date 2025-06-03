# https://wikidocs.net/231861

"""
cv2.getRotationMatrix2D: 이미지의 회전 변환 매트릭스 생성

cv2.getRotationMatrix2D() 함수는 이미지의 회전 변환 매트릭스를 생성하는 데 사용됩니다. 이 함수를 사용하면 지정된 각도로 이미지를 회전시킬 수 있습니다.

함수 시그니처는 다음과 같습니다:

retval = cv2.getRotationMatrix2D(center, angle, scale)
여기서 각 인자는 다음을 의미합니다:

center: 회전의 중심점입니다. 일반적으로 이미지의 중심점을 사용합니다. (x, y) 형식의 튜플로 지정됩니다.
angle: 회전 각도입니다. 반시계 방향으로의 양수 각도이며, 시계 방향으로의 음수 각도입니다.
scale: 선택적으로 회전 후 이미지의 크기를 조절하기 위한 배율입니다. 기본값은 1입니다.
이 함수는 회전 변환 매트릭스를 반환합니다. 이 매트릭스는 cv2.warpAffine() 함수와 함께 사용하여 이미지를 회전시킬 때 사용됩니다.

예를 들어, 이미지를 45도 회전시키는 방법은 다음과 같습니다: (y축이 )
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

마지막 편집일시 : 2024년 11월 8일 10:45 오후
"""