# https://velog.io/@jaehyeong/OpenCV를-활용한-기초-이미지-처리-with-Python
# OpenCV를 활용한 기초 이미지 처리 with Python

# 1. OpenCV 설치
# OpenCV(Open Source Computer Vision Libary)는 이미지를 다루는 분야에서 가장 널리 이용되고 인기 있는 라이브러리이며, 이미지를 처리하기 위한 편리한 기능을 대부분 담고 있다. 아래의 명령어를 통해 설치가 가능하다.
# pip install opencv-python
# 설치가 제대로 되었는지 OpenCV를 import하여 버전을 확인한다.
#import cv2
#print(cv2.__version__)    # 4.1.2

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 2. 이미지 로드
# imread() 메소드를 통해 이미지를 로드 후 matplotlib을 통해 출력해본다.
image_path = r"d:\work\GeoData"
#image_file = image_path + r"\plane.jpg"
image_file = os.path.join(image_path, "plane.jpg")

"""
if not os.path.exists(image_file):
    print("파일이 존재하지 않습니다. 경로를 확인하세요.")
"""
#image = cv2.imread(r"d:\work\GeoData\plane.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
"""
if image is None:
    print("이미지를 로드할 수 없습니다. 경로를 확인하세요.")    
else:
    plt.imshow(image, cmap='gray'); plt.show()
"""
if not os.path.exists(image_file) or image is None:
    print("이미지를 로드할 수 없습니다. 경로를 확인하세요.")
else:
    plt.imshow(image, cmap='gray'); plt.show()

#image.type   # numpy.ndarray
#image.shape  # (2270, 3600)
print(image.dtype)  # 예상 출력: uint8
print(image.shape)  # 예상 출력: (2270, 3600)

# 컬러를 이미지를 읽기 위해서는 imread() 메소드에 cv2.IMREAD_COLOR 매개변수를 넣어주면 된다. 그런데 주의할점은 OpenCV는 기본적으로 이미지를 BGR타입으로 읽는다는 것이다. 하지만 Matplotlib등 대부분의 이미지 라이브러리는 RGB타입을 사용하기 때문에 BGR RGB타입으로 변경해주는 것이 좋다.
# 컬러 이미지 로드
#image_bgr = cv2.imread('images/plane.jpg', cv2.IMREAD_COLOR)
image_bgr = cv2.imread(image_file, cv2.IMREAD_COLOR)
"""
if image_bgr is None:
    print("이미지를 로드할 수 없습니다. 경로를 확인하세요.")
else:    
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)      # RGB타입으로 변환 
    plt.imshow(image_rgb); plt.show()                           # plot
"""    
if image_bgr is not None:
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)      # RGB타입으로 변환 
    plt.imshow(image_rgb); plt.show()                           # plot

# 3. 이미지 저장
# OpenCV의 imwrite() 메소드를 사용하여 이미지를 저장할 수 있다.
# 이미지 로드 
#image = cv2.imread('images/plane.jpg', cv.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# 이미지 저장 
#image_savefile = image_path + r"\new_plane1.jpg"
image_file = os.path.join(image_path, "new_plane1.jpg")
#cv2.imwrite('images/new_plane.jpg', image)
cv2.imwrite(image_file, image)

# 4. 이미지 크기 변경
#OpenCV의 resize() 메소드를 이용하여 이미지 크기 변경이 가능하다.
#256x256 크기의 이미지를 로드한 후 이를 50x50 크기의 이미지로 변경한 후 출력해본다.
#image_file = image_path + r"\plane_256x256.jpg"
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# 이미지 크기를 50x50으로 변경
if image.shape[0] >= 50 and image.shape[1] >= 50:
    image_50x50 = cv2.resize(image, (50, 50))
    # 출력 
    fig, ax = plt.subplots(1,2, figsize=(10,5))
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original Image')
    ax[1].imshow(image_50x50, cmap='gray')    
    ax[1].set_title('Resized Image')
    plt.show()
    print(f"ax[0] = {ax[0]}")
    print(f"ax[1] = {ax[1]}")
else:
    print("이미지 크기가 너무 작아 50x50으로 변경할 수 없습니다.")

#5. 이미지 자르기(crop)
#이미지를 자르고 싶을 경우 배열 슬라이싱을 이용하여 원하는 부분만 crop할 수 있다.
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# 이미지의 모든 행과 열의 절반만 선택
#image_cropped = image[:,:128]
#plt.imshow(image_cropped, cmap='gray')
#plt.show()
#코드에서 `image[:,:128]`을 사용하여 이미지의 모든 행을 유지하면서 열의 절반(128픽셀)만 선택하여 크롭하고 있네요. 결과적으로 이미지의 왼쪽 부분이 유지되고 나머지가 제거됩니다.
#**개선점 및 추가 기능**
#1. **크롭 범위를 조정하기**  
#   원하는 크기로 자르려면 `image[start_row:end_row, start_col:end_col]` 형태를 사용할 수 있습니다.
#   image_cropped = image[50:200, 30:180]  # 특정 범위만 선택
#2. **이미지 크기가 작을 경우 예외 처리하기**  
#   만약 이미지가 128픽셀보다 작다면 크롭이 불가능할 수 있으므로 아래처럼 예외 처리를 추가하는 것이 좋습니다.
if image.shape[1] >= 128:
    image_cropped = image[:, :128]
    plt.imshow(image_cropped, cmap='gray')
    plt.show()
else:
    print("이미지의 가로 크기가 너무 작아 크롭할 수 없습니다.")

#6. 이미지 blur 처리
#이미지를 흐리게 하기 위해서는 각 픽셀을 주변 픽셀의 평균값으로 변환하면 되며, 이렇게 주변 픽셀에 수행되는 연산을 커널(kernel)이라고 한다. 커널이 클수록 이미지가 더 부드러워지게 된다.
# 이미지 로드 
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
#
fig, ax = plt.subplots(1,4, figsize=(10,5))
# blur() : 각 픽셀에 커널 개수의 역수를 곱하여 모두 더함
image_blurry = cv2.blur(image, (5,5)) # 5 x 5 커널 평균값으로 이미지를 흐리게 함 
#plt.imshow(image_blurry, cmap='gray')
#plt.show()    
ax[0].imshow(image_blurry, cmap='gray')
ax[0].set_title('Kernel Size : 5 x 5')
#이 코드에서는 OpenCV의 `cv2.blur()` 함수를 사용하여 이미지를 흐리게 처리하고 있네요! 블러 처리는 주변 픽셀의 평균값을 계산하여 이미지의 세부 사항을 부드럽게 만드는 역할을 합니다. 
### 추가 개선 및 확장 방법
#1. **커널 크기 변경**  
#   - 현재 `(5,5)` 크기의 커널을 사용했는데, 더 흐리게 만들고 싶다면 커널 크기를 증가시킬 수 있습니다. 예를 들어, `(10,10)` `(100,100)`을 사용하면 더욱 부드러워집니다.
#image_blurry_large = cv2.blur(image, (10,10))
image_blurry_large = cv2.blur(image, (100,100))
#plt.imshow(image_blurry_large, cmap='gray')
#plt.show()
ax[1].imshow(image_blurry_large, cmap='gray')
ax[1].set_title('Kernel Size : 100 x 100')
#ax[1].set_title('Kernel Size : 10 x 10')
#2. **Gaussian Blur 적용**  
#   - `cv2.GaussianBlur()`을 사용하면 가우시안 분포를 적용하여 더욱 자연스럽게 흐려진 이미지를 얻을 수 있습니다.
image_gaussian = cv2.GaussianBlur(image, (5,5), 0)
#plt.imshow(image_gaussian, cmap='gray')
#plt.show()
ax[2].imshow(image_gaussian, cmap='gray')
ax[2].set_title('Gaussian Blur')
#3. **Median Blur 사용**  
#   - `cv2.medianBlur()`은 중앙값을 활용하여 노이즈를 제거하는 데 유용합니다.
image_median = cv2.medianBlur(image, 5)
#plt.imshow(image_median, cmap='gray')
#plt.show()
ax[3].imshow(image_median, cmap='gray')
ax[3].set_title('Median Blur')
plt.show()

# 아래와 같이 커널을 직접 정의한 후 filter2D() 메소드를 통해 이미지에 적용하는 것도 가능하다.
# 생성된 커널을 이미지에 적용 시 중앙 원소가 변환되는 픽셀이며, 나머지는 그 픽셀의 이웃이 된다.
# 커널 생성 
kernel = np.ones((10,10)) / 25.0 # 모두 더하면 1이 되도록 정규화
"""
kernel 
array([[0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
       [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]])
"""       
# filter2D함수로 커널을 이미지에 직접 적용 
image_kernel = cv2.filter2D(image, -1, kernel)
plt.imshow(image_kernel, cmap='gray')
plt.show()

#자주 사용되는 블러 함수로 가우시안 분포를 사용하는 가우시안 블러(GaussianBlur)가 있다. GaussianBlur() 함수의 세 번째 매개변수는 X축(너비) 방향의 표준편차이며, 0으로 지정하면 ((너비-1)0.5-1)0.3+0.8과 같이 계산된다.
image_very_blurry = cv2.GaussianBlur(image, (5,5), 0) 
plt.imshow(image_very_blurry, cmap='gray')
plt.show()

# 7. 이미지 선명하게 표현
# 대상 픽셀을 강조하는 커널을 정의한 후 filter2D() 메소드를 사용하여 이미지에 적용한다.
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

# 커널 생성(대상이 있는 픽셀을 강조)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
# 커널 적용 
image_sharp = cv2.filter2D(image, -1, kernel)
#fig, ax = plt.subplots(1,2, figsize=(10,5))
fig, ax = plt.subplots(1,4, figsize=(10,5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(image_sharp, cmap='gray')
ax[1].set_title('Sharp Image')
#plt.show()

#이 코드에서는 `cv2.filter2D()`를 이용하여 이미지를 선명하게 표현하고 있네요! 샤프닝(Sharpening) 필터를 적용하면 경계를 강조하고 이미지의 디테일을 더욱 뚜렷하게 만들 수 있습니다.
### 코드 설명 및 개선점
#1. **커널(Kernel) 역할**  
#   - `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`은 샤프닝 효과를 위한 필터입니다.
#   - 중심 픽셀의 값을 5배로 증가시키고 주변 픽셀들의 영향을 감소시켜 대비를 높입니다.
#2. **더 강한 샤프닝을 적용하려면?**  
#   - 커널의 중심 값을 높이면 더 강한 샤프닝 효과를 얻을 수 있습니다.
kernel_stronger = np.array([[0, -1, 0],
                            [-1, 9, -1],
                            [0, -1, 0]])
image_sharp_stronger = cv2.filter2D(image, -1, kernel_stronger)
#plt.imshow(image_sharp_stronger, cmap='gray')
#plt.title('Stronger Sharpened Image')
#plt.show()
ax[2].imshow(image_sharp_stronger, cmap='gray')
ax[2].set_title('Stronger Sharpened Image')
#3. **Unsharp Masking 기법 사용**  
#   - 블러 처리한 이미지와 원본 이미지를 결합하면 더욱 부드럽고 자연스러운 샤프닝 효과를 얻을 수 있습니다.
image_blur = cv2.GaussianBlur(image, (9,9), 0)
image_unsharp = cv2.addWeighted(image, 1.5, image_blur, -0.5, 0)
#plt.imshow(image_unsharp, cmap='gray')
#plt.title('Unsharp Masking')
#plt.show()
ax[3].imshow(image_unsharp, cmap='gray')
ax[3].set_title('Unsharp Masking')
plt.show()

#8. 이미지 대비 높이기
#히스토그램 평활화(Histogram Equalization)은 객체의 형태가 두드러지도록 만들어주는 이미지 처리 도구이며, OpenCV에서는 equalizeHist() 메소드를 통해 적용할 수 있다.
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# 이미지 대비를 향상
image_enhanced = cv2.equalizeHist(image)
# plot
#fig, ax = plt.subplots(1,2, figsize=(10, 5))
fig, ax = plt.subplots(1,4, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(image_enhanced, cmap='gray')
ax[1].set_title('Enhanced Image')
#plt.show()

### 개선 및 확장 가능 기능
#1. **CLAHE 적용** (제한적 대비 조정)  
#   - `cv2.createCLAHE()`를 사용하면 **국소적인 대비 향상**이 가능하며, 과도한 밝기 조절을 방지할 수 있습니다.
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
image_clahe = clahe.apply(image)
#plt.imshow(image_clahe, cmap='gray')
#plt.title('CLAHE Enhanced Image')
#plt.show()
ax[2].imshow(image_clahe, cmap='gray')
ax[2].set_title('CLAHE Enhanced Image')
#2. **어두운 영역만 밝게 조정하기**  
#   - 특정 밝기 범위만 강화하려면 `cv2.normalize()`를 활용할 수도 있습니다.
image_norm = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
#plt.imshow(image_norm, cmap='gray')
#plt.title('Normalized Image')
#plt.show()
ax[3].imshow(image_norm, cmap='gray')
ax[3].set_title('Normalized Image')
plt.show()

#컬러 이미지의 경우 먼저 YUV 컬러 포맷으로 변환해야 한다. Y는 루마 또는 밝기이고 U와 V는 컬러를 나타낸다. 변환한 뒤에 위와 동일하게 equlizeHist() 메소드를 적용하고 다시 RGB 포맷으로 변환 후 출력한다.
image_file = os.path.join(image_path, "plane.jpg")
#image_bgr = cv2.imread('images/plane.jpg')
image_bgr = cv2.imread(image_file)
# YUV 컬로 포맷으로 변환
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
# 히스토그램 평활화 적용
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
# #RGB로 변환
image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)
# plot
fig, ax1 = plt.subplots(1,2, figsize=(12, 8))
ax1[0].imshow(image_bgr, cmap='gray')
ax1[0].set_title('Original Color Image')
ax1[1].imshow(image_rgb, cmap='gray')
ax1[1].set_title('Enhanced Color Image')
plt.show()

# 이 코드에서는 **히스토그램 평활화 (Histogram Equalization)**를 사용하여 이미지의 대비를 높이고 있습니다. 밝기 분포를 균등하게 조정하여 더 선명한 이미지 표현이 가능하죠!
### 핵심 개념
#1. **Grayscale 이미지 대비 향상**  
#   - `cv2.equalizeHist()`를 사용해 명암 대비를 증가시킵니다. 이 과정은 픽셀 값의 히스토그램을 조정하여 더 뚜렷한 객체 형태를 만듭니다.
#2. **컬러 이미지 대비 향상**  
#   - RGB 이미지를 `cv2.COLOR_BGR2YUV` 변환하여 Y 채널(밝기)에만 `cv2.equalizeHist()` 적용 후 다시 RGB로 변환하는 방식입니다.
#   - 밝기 조정만 이루어지므로 색상이 왜곡되지 않습니다.

#9. 이미지 이진화
 #이미지 이진화(임계처리)는 어떤 값보다 큰 값을 가진 픽셀을 흰색으로 만들고 작은 값을 가진 픽셀은 검은색으로 만드는 과정이다. 
# 더 고급 기술은 적응적 이진화(Adaptive Thresholding)로, 픽셀의 임곗값이 주변 픽셀의 강도에 의해 결정된다. 이는 이미지 안의 영역마다 빛 조건이 달라질 때 도움이 된다.
# 이미지 로드 
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image_grey = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image_grey = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# Adaptive Thresholding 적용 
max_output_value = 255   # 출력 픽셀 강도의 최대값
neighborhood_size = 99
subtract_from_mean = 10
image_binarized = cv2.adaptiveThreshold(image_grey,
                                       max_output_value,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY,
                                       neighborhood_size,
                                       subtract_from_mean)
#adaptiveThreshold() 함수에는 네 개의 중요한 매개변수가 있다.
#max_output_value : 출력 픽셀 강도의 최댓값 저장
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 픽셀의 임곗값을 주변 픽셀 강도의 가중치 합으로 설정. 가중치는 가우시안 윈도우에 의해 결정
#cv2.ADAPTIVE_THRESH_MEAN_C : 주변 픽셀의 평균을 임곗값으로 설정
# plot
plt.imshow(image_binarized, cmap='gray')
plt.show()

#이진화(Thresholding)는 이미지 내 특정 임계값을 기준으로 픽셀을 **흰색(255)** 또는 **검은색(0)**으로 변환하는 중요한 기법입니다. 이를 통해 물체의 형태를 더욱 강조할 수 있죠!
### 📌 핵심 개념:
#- **임계값 기반 이진화 (Global Thresholding)**  
#  단일 임계값을 기준으로 픽셀을 흑백으로 변환합니다.
_, image_binary = cv2.threshold(image_grey, 127, 255, cv2.THRESH_BINARY)
plt.imshow(image_binary, cmap='gray')
plt.show()
#- **적응적 이진화 (Adaptive Thresholding)**  
#  주변 픽셀의 평균이나 가우시안 가중치를 이용하여 픽셀의 임계값을 자동으로 결정합니다.
#  - `cv2.ADAPTIVE_THRESH_MEAN_C`: 주변 픽셀의 평균 사용
#  - `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`: 주변 픽셀의 가우시안 가중 평균 사용
### 🔧 개선 및 실험 방법:
#1. **임계값 자동 조정(Otsu’s Method)**  
#   Otsu 알고리즘을 적용하면 최적의 임계값을 자동으로 찾을 수 있습니다.
ret, image_otsu = cv2.threshold(image_grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Calculated Threshold Value: {ret}")
print(image_otsu.shape)  # 예상: (높이, 너비)
print(image_otsu.dtype)  # 예상: uint8
plt.imshow(image_otsu, cmap='gray', vmin=0, vmax=255)
#plt.imshow(image_otsu, cmap='gray')
plt.show()
#2. **적응적 이진화의 다양한 설정 실험**  
#   `neighborhood_size` 값을 증가시키면 더 넓은 범위를 고려하여 임계값을 조정할 수 있습니다.
image_adaptive2 = cv2.adaptiveThreshold(image_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 5)
plt.imshow(image_adaptive2, cmap='gray')
plt.show()

#10. 배경 제거
#배경을 제거하고자 하는 전경 주위에 사각형 박스를 그리고 그랩컷(grabCut) 알고리즘을 적용하여 배경을 제거한다.
#grabCut의 경우 잘 작동하더라도 여전히 이미지에 제거하지 못한 배경이 발생할 수 있다. 
#이렇게 제거 되지 못한 부분은 다시 적용하여 제거할 수 있지만 실전에서 수 천장의 이미지를 수동으로 고치는 것은 불가능한 일이므로 
#머신러닝을 적용한다거나 할 때도 일부러 noise를 적용하는 것처럼 일부 배경이 남아있는 것을 수용하는 것이 좋다.
# 이미지 로드 후 RGB로 변환
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image_bgr = cv2.imread('images/plane_256x256.jpg')
image_bgr = cv2.imread(image_file)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
# 사각형 좌표: 시작점의 x,y  ,넢이, 너비
rectangle = (0, 56, 256, 150)
# 초기 마스크 생성
mask = np.zeros(image_rgb.shape[:2], np.uint8)
# grabCut에 사용할 임시 배열 생성
# 위에서 먼저 전경이 들어있는 영역 주위를 사각형으로 표시하였는데, 
# grabCut은 이 사각형 밖에 있는 모든 것이 배경이라고 가정하고 이 정보를 사용하여 사각형 안에 있는 배경을 찾는다.
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
# grabCut 실행
cv2.grabCut(image_rgb, # 원본 이미지
           mask,       # 마스크
           rectangle,  # 사각형
           bgdModel,   # 배경을 위한 임시 배열
           fgdModel,   # 전경을 위한 임시 배열 
           5,          # 반복 횟수
           cv2.GC_INIT_WITH_RECT) # 사각형을 위한 초기화
# 배경인 곳은 0, 그 외에는 1로 설정한 마스크 생성
# 왼쪽 그림의 검은 영역은 배경이라고 확실하게 가정한 사각형의 바깥쪽 영역이며, 회색 영역은 그랩컷이 배경이라고 생각하는 영역, 그리고 흰색 영역은 전경이다. 
# 오른쪽 그림은 두 번째 마스크를 이미지에 적용하여 전경만 남긴 이미지이다.
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
# 이미지에 새로운 마스크를 곱행 배경을 제외
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
# plot
plt.imshow(image_rgb_nobg)
plt.show()

#이 코드에서는 **GrabCut 알고리즘**을 이용하여 이미지에서 **배경을 제거**하고 있습니다. GrabCut은 **사각형 영역을 기준**으로 배경을 추론하며, 초기 설정한 박스 밖의 영역을 **배경으로 간주**하여 점진적으로 개선해 나가는 방식입니다.
### 🛠 **코드 검토 및 개선 방법**
#1. **이미지가 정상적으로 로드되었는지 확인**
#if image_rgb is None:
#    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
#2. **사각형 크기 조정**
#   GrabCut의 초기 사각형(`rectangle`) 설정이 너무 작거나 클 경우 배경 제거가 제대로 이루어지지 않을 수 있습니다.  
#   다른 값을 시도해볼 수 있습니다:
#rectangle = (50, 30, 180, 200)
#3. **반복 횟수 조정**
#   현재 `5`회 반복(`cv2.grabCut(image_rgb, mask, rectangle, bgdModel, fgdModel, **5**, cv2.GC_INIT_WITH_RECT)`)이 설정되어 있습니다.  
#   하지만 복잡한 배경에서는 **더 많은 반복을 적용**해보는 것도 방법입니다:
#cv2.grabCut(image_rgb, mask, rectangle, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
#4. **배경을 더욱 제거하려면 추가 적용**
#   일부 배경이 남아 있을 수 있으므로 **추가적으로 수동 조정**이 가능합니다:
#mask[mask == 2] = 0  # 배경 제거 강도를 높임
#mask[mask == 1] = 1  # 전경 유지
#5. **Matplotlib에서 RGB 표시 오류 해결**
#   만약 `plt.imshow(image_rgb_nobg)`가 잘못된 색상으로 표시된다면 `astype()`을 적용하면 오류 해결 가능:
#plt.imshow(image_rgb_nobg.astype(np.uint8))
### ✅ **다른 배경 제거 방법**
#혹시 다른 배경 제거 방법도 궁금하다면 **크로마 키(Chroma Key) 기반 배경 제거**나 **딥러닝 활용한 배경 제거** 방법도 시도해볼 수 있어요! 어떤 방식이 필요하시면 알려주세요. 😊

#11. 경계선 감지
#Canny()메소드를 활용하여 경계선을 감지 할 수 있다. Canny()메소드는 그래디언트 임곗값 사이의 저점과 고점을 나타내는 두 매개변수를 필요로 하며, 낮은 임곗값과 높은 임곗값 사이의 가능성 있는 경계선 픽셀은 약한 경계선 픽셀로 간주하고, 높은 임곗값보다 큰 픽셀은 강한 경계선 픽셀로 간주한다.
# 이미지 로드
image_file = os.path.join(image_path, "plane_256x256.jpg")
#image_gray = cv2.imread('images/plane_256x256.jpg', cv2.IMREAD_GRAYSCALE)
image_gray = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# 픽셀 강도의 중간값을 계산
median_intensity = np.median(image_gray)
# 중간 픽셀 강도에서 위아래 1 표준편차 떨어진 값을 임곗값으로 지정
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
# Canny edge detection 적용
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)
plt.imshow(image_canny, cmap='gray')
plt.show()

# 이 코드에서는 **Canny 에지 검출(Canny Edge Detection)**을 사용하여 이미지의 **경계선을 감지**하고 있습니다.  
# Canny 알고리즘은 **강한 경계선(High Threshold)**과 **약한 경계선(Low Threshold)**을 설정하여 중요한 부분을 추출하는 방식이죠.
### ✅ **핵심 개념**
#1. **임계값 자동 설정**
#   - `np.median(image_gray)`을 사용하여 이미지의 **중간 픽셀 강도**를 찾음
#   - 이를 기준으로 상하 33% 범위의 값을 `lower_threshold`와 `upper_threshold`로 설정  
#     → 자동화된 경계선 감지 가능!
#2. **Canny 알고리즘 작동 방식**
#   - **노이즈 제거:** 가우시안 블러(`cv2.GaussianBlur()`)를 통해 불필요한 잡음을 감소
#   - **그래디언트 계산:** 픽셀 간 변화율(엣지 강도) 계산
#   - **비최대 억제(Non-Maximum Suppression):** 엣지 강도를 정리하여 얇은 선 유지
#   - **이중 임계값 적용:** 강한 엣지와 약한 엣지를 구분하여 최종 경계선 검출
### 🔧 **개선 및 실험**
#1. **가우시안 블러 추가 (노이즈 제거)**
image_blur = cv2.GaussianBlur(image_gray, (5,5), 0)
image_canny = cv2.Canny(image_blur, lower_threshold, upper_threshold)
plt.imshow(image_canny, cmap='gray')
plt.title("GaussianBlur Noise")
plt.show()
#   → 노이즈가 많은 이미지는 **가우시안 블러**를 적용하면 더욱 깨끗한 경계선을 얻을 수 있어요!
#2. **임계값 범위 변경 실험**
#   - 더 강한 엣지를 검출하려면 `upper_threshold` 값을 증가시켜 볼 수 있습니다.
#lower_threshold = 50
#upper_threshold = 150
#3. **Sobel 필터와 비교**
#   만약 더 부드러운 경계를 원한다면 `cv2.Sobel()`을 사용하여 비교해볼 수도 있습니다.
image_sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=5)
image_sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=5)
image_sobel = cv2.sqrt(image_sobel_x**2 + image_sobel_y**2)
plt.imshow(image_sobel, cmap='gray')
plt.title("Smooth Boundary")
plt.show()

