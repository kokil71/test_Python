import sys
import os
#sys.path.append("D:\\work\\testPythonToAutoCAD")  # 경로는 본인의 폴더에 맞게 수정
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) # 상대경로로
from drawing_intersection import *
from drawing_bulge_3P import *

import pythoncom
import win32com.client
from win32com.client import VARIANT
from pythoncom import VT_ARRAY, VT_R8
from array import array
from math import *
import time
import numpy as np

pythoncom.CoInitialize()
acad = win32com.client.Dispatch("AutoCAD.Application")
doc = acad.ActiveDocument
ms = doc.ModelSpacee 

"""
def calculate_bulge(start, end, center):
    # start, end, center: (x, y) 튜플 또는 np.array

    start = np.array(start)
    end = np.array(end)
    center = np.array(center)

    # 벡터
    v1 = start - center
    v2 = end - center

    # 중심각 (호의 각도)
    dot = np.dot(v1, v2)
    cross = np.cross(v1, v2)
    angle = np.arctan2(np.linalg.norm(cross), dot)  # 호의 중심각 (0 ~ pi)

    # 방향 판단 (z-값 부호로 시계/반시계 판단)
    direction = np.sign(cross)  # +1: CCW, -1: CW

    # bulge 계산
    bulge = direction * np.tan(angle / 4)

    return bulge, np.degrees(angle), "CCW" if direction > 0 else "CW"
"""

points_2d = [
    (0.00000000, 0.00000000),    
    (15.00000000, 0.00000000),    
    (16.16025404, 8.0),
    (-1.16025404, 8.0),
    (0.00000000, 0.00000000),    
]

"""
points_2d = [
    (0.0, 0.0),
    (10.0, 0.0),
    (10.0, 10.0),
    (0.0, 10.0),
    (0.0, 0.0),
]
"""

flat_points_2d = array('d', [coord for pt in points_2d for coord in pt])
safe_array_2d = VARIANT(VT_ARRAY | VT_R8, flat_points_2d)

pline = ms.AddLightWeightPolyline(safe_array_2d)
pline.Closed = True

num_vertices = len(flat_points_2d) // 2

time.sleep(0.5)  # 로딩 대기

# 화면 갱신
acad.Application.Update()
acad.Application.ZoomExtents()

# SetBulgeAt 메서드가 없거나 오류난다면 이 부분은 생략하거나,
# bulge 적용은 다른 방식으로 해야 함.
try:
    for i in range(num_vertices - 1):
        if i == 1:
            #pline.SetBulgeAt(i, 1.0)
            #pline.SetBulge(i, tan(19.12608458*pi/180.0)) 
            start_pt = (-12.13003152, 0.0)
            end_pt = (-10.96977748, 8.0)
            center_pt = (-16.62348522, 4.73583031)            
            bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
            pline.SetBulge(i, bulge_value)
        elif i == 2:
            #pline.SetBulge(i, tan(30.00000000*pi/180.0))
            start_pt = (-10.96977748, 8.0)
            end_pt = (-28.29028556, 8.0)
            center_pt = (-19.63003152, 3.0)            
            bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
            pline.SetBulge(i, bulge_value)
        elif i == 3:
            #pline.SetBulge(i, tan(19.12608458*pi/180.0))
            start_pt = (-28.29028556, 8.0)
            end_pt = (-27.13003152, 0.0)
            center_pt = (-22.63657782, 4.73583031)            
            bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
            pline.SetBulge(i, bulge_value)
        else:
            #pline.SetBulgeAt(i, 0.0)
            pline.SetBulge(i, 0.0)
except AttributeError:
    print("SetBulgeAt 메서드를 사용할 수 없습니다. bulge 설정이 생략됨.")

print("✅ 2D LightWeightPolyline 생성 완료")

print(pline.area)

time.sleep(0.5)  # 로딩 대기

# 화면 갱신
acad.Application.Update()
acad.Application.ZoomExtents()

pythoncom.CoUninitialize()