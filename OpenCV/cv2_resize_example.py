# https://wikidocs.net/231854

"""
cv2.resize: 이미지 크기 변경

cv2.resize() 함수는 이미지의 크기를 조절하기 위해 사용됩니다. 이 함수는 원본 이미지와 새로운 크기를 입력으로 받아들이며, 새로운 크기에 맞게 이미지를 조절한 후 반환합니다.

함수 시그니처는 다음과 같습니다:

cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
여기서 각 인자는 다음을 의미합니다:

src: 크기를 조절하려는 원본 이미지입니다.
dsize: 새로운 이미지의 크기입니다. (width, height) 형식의 튜플로 지정할 수 있습니다.
dst: 선택적으로, 크기를 조절한 이미지를 저장할 곳을 지정합니다. 이 인자를 생략하면 함수가 새로운 이미지를 반환합니다.
fx: 선택적으로 가로 방향 크기의 배율 요인입니다.
fy: 선택적으로 세로 방향 크기의 배율 요인입니다.
interpolation: 선택적으로 크기 조절에 사용할 보간법을 지정합니다. 기본값은 cv2.INTER_LINEAR로, 선형 보간법을 사용합니다. 다른 옵션으로는 cv2.INTER_NEAREST, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4 등이 있습니다.
예를 들어, 이미지를 절반 크기로 줄이려면 다음과 같이 사용할 수 있습니다:
"""

import cv2

# 이미지 파일을 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 새로운 크기를 지정합니다.
#new_width = int(image.shape[1] / 2)
#new_height = int(image.shape[0] / 2)
new_width = int(image.shape[1] * 2)
new_height = int(image.shape[0] * 2)
new_size = (new_width, new_height)

# 이미지의 크기를 변경합니다.
resized_image = cv2.resize(image, new_size)

# 이미지를 파일로 저장합니다.
cv2.imwrite(r'd:\work\GeoData\lena_saved2.jpg', resized_image)


# 변경된 이미지를 출력합니다.
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




"""
이 함수를 사용하여 이미지의 크기를 조절하여 다양한 이미지 처리 작업을 수행할 수 있습니다.

마지막 편집일시 : 2024년 2월 25일 8:00 오후
"""