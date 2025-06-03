# https://wikidocs.net/231856

"""
cv2.imwrite: 이미지 파일 저장

cv2.imwrite() 함수는 OpenCV 라이브러리를 사용하여 이미지를 파일로 저장하는 함수입니다. 이 함수는 이미지와 저장할 파일의 경로를 입력으로 받아들이며, 지정된 경로에 이미지를 저장합니다.

함수 시그니처는 다음과 같습니다:

cv2.imwrite(filename, img[, params])
여기서 각 인자는 다음을 의미합니다:

filename: 저장할 이미지 파일의 경로입니다.
img: 저장할 이미지입니다. NumPy 배열로 표현됩니다.
params: 선택적으로, 파일 저장 옵션을 지정합니다. 예를 들어, 이미지 품질 설정이나 포맷 설정 등을 지정할 수 있습니다.
예를 들어:
"""

import cv2

# 이미지 파일을 읽어들입니다.
#image = cv2.imread('image.jpg')
image = cv2.imread(r'd:\work\GeoData\lena.jpg')

# 이미지를 파일로 저장합니다.
cv2.imwrite(r'd:\work\GeoData\lena_saved.jpg', image)

"""
위 코드는 'image.jpg'로부터 이미지를 읽어들인 후, 'saved_image.jpg'라는 파일로 이미지를 저장합니다.

이 함수를 사용하여 OpenCV를 통해 이미지를 처리하고 나서 결과를 파일로 저장할 수 있습니다.

마지막 편집일시 : 2024년 2월 25일 8:01 오후
"""