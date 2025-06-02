# 호의 양 끝점과 중심점을 주고 Bulge 구하기

import numpy as np

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

# ✅ 테스트
#start_pt = (-12.13003152, 0.0)
#end_pt = (-10.96977748, 8.0)
#center_pt = (-16.62348522, 4.73583031)

##start_pt = (0, 0)
##end_pt = (10, 0)
##center_pt = (5, 5)

#bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)

#print(f"✅ Bulge 값: {bulge_value:.4f}")
#print(f"🎯 중심각: {arc_angle_deg:.2f}도")
#print(f"↻ 방향: {direction}")
