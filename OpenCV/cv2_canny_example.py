# https://wikidocs.net/231466

"""
cv2.Canny: 엣지 검출

cv2.Canny() 함수는 이미지에서 엣지를 검출하는 데 사용됩니다. 이 함수는 Canny 엣지 검출 알고리즘을 구현한 것으로, 이미지에서 강한 엣지를 검출하여 이미지의 윤곽을 찾는 데 널리 사용됩니다.

함수 시그니처는 다음과 같습니다:

edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
여기서 각 인자는 다음을 의미합니다:

image: 입력 이미지입니다. 보통 그레이스케일 이미지를 사용합니다.
threshold1: 엣지 검출에서 사용되는 최소 임계값입니다. 이 값보다 낮은 그라디언트 값은 엣지로 간주되지 않습니다.
threshold2: 엣지 검출에서 사용되는 최대 임계값입니다. 이 값보다 높은 그라디언트 값은 확실한 엣지로 간주됩니다.
edges: 선택적으로 출력 엣지 이미지입니다.
apertureSize: 선택적으로 소벨 연산자에 사용되는 커널 크기를 지정합니다. 기본값은 3입니다.
L2gradient: 선택적으로 그라디언트 크기를 계산할 때 사용할 방법을 지정합니다. 기본값은 False이며, 그라디언트 크기를 계산할 때 L1 norm을 사용합니다. True로 설정하면 L2 norm을 사용합니다.
이 함수는 엣지가 포함된 이미지를 반환합니다.

예를 들어:
"""

import cv2

# 이미지를 그레이스케일로 읽어들입니다.
#image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
#image = cv2.imread(r'd:\work\GeoData\lena_gray.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r'd:\work\GeoData\baseball-player.jpg', cv2.IMREAD_GRAYSCALE)

# Canny 엣지 검출을 수행합니다.
edges = cv2.Canny(image, 100, 200)

# 엣지가 포함된 이미지를 출력합니다.
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
위 코드는 'image.jpg' 이미지를 그레이스케일로 읽어들인 후 Canny 엣지 검출 알고리즘을 적용하여 엣지가 포함된 이미지를 출력합니다.
마지막 편집일시 : 2024년 2월 25일 10:29 오후
"""