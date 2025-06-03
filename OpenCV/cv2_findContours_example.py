# https://wikidocs.net/231859

"""
cv2.findContours: 이미지 윤곽선 찾기

cv2.findContours() 함수는 이미지에서 윤곽선을 찾는 데 사용됩니다. 이 함수는 이진화된 이미지에서 객체의 외곽을 찾아내고, 외곽선을 구성하는 점들을 반환합니다.

함수 시그니처는 다음과 같습니다:

contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
여기서 각 인자는 다음을 의미합니다:

image: 윤곽선을 찾을 입력 이미지입니다. 보통 그레이스케일 또는 이진화된 이미지를 사용합니다.
mode: 윤곽선을 찾는 방법을 지정하는 플래그입니다. 주로 사용되는 값으로는 cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_TREE 등이 있습니다.
method: 윤곽선 근사화 방법을 지정하는 플래그입니다. 주로 사용되는 값으로는 cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_TC89_L1, cv2.CHAIN_APPROX_TC89_KCOS 등이 있습니다.
contours: 선택적으로 검출된 윤곽선을 저장할 리스트입니다.
hierarchy: 선택적으로 윤곽선의 계층 구조를 저장할 배열입니다.
offset: 선택적으로 윤곽선의 좌표를 변환할 때 사용되는 오프셋입니다.
이 함수는 검출된 윤곽선을 나타내는 리스트인 contours와, 윤곽선의 계층 구조를 나타내는 배열인 hierarchy를 반환합니다.

예를 들어:
"""

import cv2

# 이미지를 그레이스케일로 읽어들입니다.
#image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
#image = cv2.imread(r'd:\work\GeoData\lena.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r'd:\work\GeoData\baseball-player.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지를 이진화합니다.
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 윤곽선을 찾습니다.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 찾은 윤곽선을 이미지에 그립니다.
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# 결과 이미지를 출력합니다.
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg' 이미지를 읽어들인 후 이진화하여 윤곽선을 찾고, 검출된 윤곽선을 초록색으로 그린 후 결과 이미지를 출력합니다.

마지막 편집일시 : 2024년 2월 25일 8:03 오후
"""