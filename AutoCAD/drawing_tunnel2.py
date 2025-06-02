import math
import pythoncom
import win32com.client

from win32com.client import VARIANT
from pythoncom import VT_R8  # double
from array import array

# AutoCAD 연결
pythoncom.CoInitialize()
acad = win32com.client.Dispatch("AutoCAD.Application")
doc = acad.ActiveDocument
ms = doc.ModelSpace

# 단면 파라미터
radius = 3.0
width = 6.0
center_x = 0
center_y = 0

half_width = width / 2
bottom_y = center_y - radius

# 점 좌표 생성
points = []

# 좌측 하단
points.append((center_x - half_width, bottom_y))

# 반원 상단 호 (좌 → 우)
num_arc_points = 30
for i in range(num_arc_points + 1):
    angle = math.pi * (i / num_arc_points)
    #x = center_x + radius * math.cos(angle)
    x = center_x - radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    points.append((x, y))

# 우측 하단
points.append((center_x + half_width, bottom_y))

# 시작점으로 닫기
points.append((center_x - half_width, bottom_y))

# 우측 하단
#points.append((center_x + half_width, bottom_y))

"""
"""

# 배열 평탄화 및 double형으로 변환
flat_coords = []
for x, y in points:
    flat_coords.append(float(x))
    flat_coords.append(float(y))

# AutoCAD가 요구하는 SAFEARRAY 형태로 변환
safe_array = VARIANT(pythoncom.VT_ARRAY | VT_R8, array('d', flat_coords))

# 도면에 2D 경량 폴리라인 삽입
pline = ms.AddLightWeightPolyline(safe_array)
pline.Closed = True

print("✅ 터널 단면이 AutoCAD에 성공적으로 그려졌습니다.")
