# 호의 양 끝점과 호상의 임의점을 주고 Bulge 구하기

import math
from typing import Tuple, Optional

Point = Tuple[float, float]

def calculate_bulge_from_3points(start: Point, on_arc: Point, end: Point) -> Tuple[float, float, str]:
    """
    세 점(시작, 중간(아크 위), 끝)을 이용하여 AutoCAD bulge 값을 계산합니다.

    Args:
        start (Point): 아크 시작점 (x, y)
        on_arc (Point): 아크 위의 중간점 (x, y)
        end (Point): 아크 끝점 (x, y)

    Returns:
        Tuple[float, float, str]: bulge 값, 중심각(degree), 방향("CW"/"CCW")
    """
    center = find_circle_center(start, on_arc, end)
    if center is None:
        raise ValueError("세 점이 일직선상에 있어 원의 중심을 찾을 수 없습니다.")

    angle_rad = calculate_sweep_angle(start, center, end)
    direction = 'CCW' if angle_rad > 0 else 'CW'
    arc_angle = abs(angle_rad)

    bulge = math.tan(arc_angle / 4)
    if direction == 'CW':
        bulge = -bulge

    return bulge, math.degrees(arc_angle), direction


def find_circle_center(a: Point, b: Point, c: Point) -> Optional[Point]:
    """
    세 점을 지나는 원의 중심을 계산합니다.

    Returns:
        중심 좌표 (x, y) 또는 일직선이면 None
    """
    def midpoint(p1: Point, p2: Point) -> Point:
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def slope(p1: Point, p2: Point) -> Optional[float]:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return None
        return dy / dx

    mid1, mid2 = midpoint(a, b), midpoint(b, c)
    m1, m2 = slope(a, b), slope(b, c)

    # 수직이등분선 기울기
    def perp_slope(m: Optional[float]) -> Optional[float]:
        if m is None:
            return 0
        elif m == 0:
            return None
        return -1 / m

    p1_slope = perp_slope(m1)
    p2_slope = perp_slope(m2)

    try:
        if p1_slope is None:  # 수직선
            cx = mid1[0]
            cy = p2_slope * (cx - mid2[0]) + mid2[1]
        elif p2_slope is None:
            cx = mid2[0]
            cy = p1_slope * (cx - mid1[0]) + mid1[1]
        else:
            cx = ((p1_slope * mid1[0] - mid1[1]) - (p2_slope * mid2[0] - mid2[1])) / (p1_slope - p2_slope)
            cy = p1_slope * (cx - mid1[0]) + mid1[1]
        return (cx, cy)
    except ZeroDivisionError:
        return None  # 세 점이 일직선


def calculate_sweep_angle(start: Point, center: Point, end: Point) -> float:
    """
    중심으로부터 시작점과 끝점까지의 벡터를 기준으로 중심각을 계산합니다.

    Returns:
        중심각 (라디안, CCW 양수)
    """
    def vector(p: Point, c: Point) -> Tuple[float, float]:
        return (p[0] - c[0], p[1] - c[1])

    v1 = vector(start, center)
    v2 = vector(end, center)

    dot = v1[0]*v2[0] + v1[1]*v2[1]
    det = v1[0]*v2[1] - v1[1]*v2[0]

    angle = math.atan2(det, dot)
    return angle

"""
if __name__ == "__main__":
    #start = (0.0, 0.0)
    #on_arc = (5.0, 5.0)
    #end = (10.0, 0.0)

    start = (15.00000000, 0.0)
    end = (16.16025404, 8.0)
    on_arc = (16.88132429, 3.32820094)

    try:
        bulge, angle_deg, direction = calculate_bulge_from_3points(start, on_arc, end)
        print(f"✅ Bulge: {bulge:.6f}")
        print(f"🎯 중심각: {angle_deg:.2f}°")
        print(f"🔁 방향: {direction}")
    except ValueError as e:
        print("🚫 오류:", e)
"""