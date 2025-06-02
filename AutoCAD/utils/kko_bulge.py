# arc 양 끝점, arc상 임의점 주고 bulge 구하기
# 호의 양끝점과 중심점 을 주고 bulge 구하기
# 호의 반지름 구하기
# 호의 중심점 구하기

import math
from typing import Tuple, Optional

# 타입 정의
Point = Tuple[float, float]


# -----------------------------
# 기본 벡터 및 기하 유틸
# -----------------------------
def distance(p1: Point, p2: Point) -> float:
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def vector(p: Point, c: Point) -> Tuple[float, float]:
    return (p[0] - c[0], p[1] - c[1])


def angle_between_vectors(v1: Tuple[float, float], v2: Tuple[float, float]) -> float:
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    det = v1[0]*v2[1] - v1[1]*v2[0]
    return math.atan2(det, dot)


# -----------------------------
# 주요 계산 함수
# -----------------------------
def find_circle_center_from_3points(a: Point, b: Point, c: Point) -> Optional[Point]:
    def midpoint(p1: Point, p2: Point) -> Point:
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def slope(p1: Point, p2: Point) -> Optional[float]:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:
            return None
        return dy / dx

    def perp_slope(m: Optional[float]) -> Optional[float]:
        if m is None: return 0
        if m == 0: return None
        return -1 / m

    mid1, mid2 = midpoint(a, b), midpoint(b, c)
    m1, m2 = slope(a, b), slope(b, c)
    pm1, pm2 = perp_slope(m1), perp_slope(m2)

    try:
        if pm1 is None:
            cx = mid1[0]
            cy = pm2 * (cx - mid2[0]) + mid2[1]
        elif pm2 is None:
            cx = mid2[0]
            cy = pm1 * (cx - mid1[0]) + mid1[1]
        else:
            cx = ((pm1 * mid1[0] - mid1[1]) - (pm2 * mid2[0] - mid2[1])) / (pm1 - pm2)
            cy = pm1 * (cx - mid1[0]) + mid1[1]
        return (cx, cy)
    except ZeroDivisionError:
        return None


def calculate_radius(center: Point, any_point: Point) -> float:
    return distance(center, any_point)


def calculate_sweep_angle(start: Point, center: Point, end: Point) -> Tuple[float, float, str]:
    v1 = vector(start, center)
    v2 = vector(end, center)
    angle_rad = angle_between_vectors(v1, v2)
    direction = "CCW" if angle_rad > 0 else "CW"
    return abs(angle_rad), math.degrees(abs(angle_rad)), direction


def calculate_bulge_from_center(start: Point, end: Point, center: Point) -> float:
    angle_rad, _, direction = calculate_sweep_angle(start, center, end)
    bulge = math.tan(angle_rad / 4)
    return bulge if direction == "CCW" else -bulge


def calculate_bulge_from_3points(start: Point, on_arc: Point, end: Point) -> Tuple[float, float, str, float, Point]:
    center = find_circle_center_from_3points(start, on_arc, end)
    if center is None:
        raise ValueError("세 점이 일직선상에 있습니다. 중심을 계산할 수 없습니다.")
    
    radius = calculate_radius(center, start)
    angle_rad, angle_deg, direction = calculate_sweep_angle(start, center, end)
    bulge = math.tan(angle_rad / 4)
    if direction == "CW":
        bulge = -bulge

    return bulge, angle_deg, direction, radius, center

"""
if __name__ == "__main__":
    # 예제 1: 시작점, 끝점, 중심점 → bulge 계산
    #start = (0.0, 0.0)
    #end = (10.0, 0.0)
    #center = (5.0, 5.0)
    
    start = (15.00000000, 0.0)
    end = (16.16025404, 8.0)
    center = (10.50654630, 4.73583031)

    bulge = calculate_bulge_from_center(start, end, center)
    print(f"[중심점 기반] Bulge: {bulge:.8f}")

    # 예제 2: 시작점, 중간(호 위), 끝점 → bulge + 중심 + 반지름
    #start = (0.0, 0.0)
    #on_arc = (5.0, 5.0)
    #end = (10.0, 0.0)

    start = (15.00000000, 0.0)
    end = (16.16025404, 8.0)
    on_arc = (16.88132429, 3.32820094)

    bulge, angle_deg, direction, radius, center = calculate_bulge_from_3points(start, on_arc, end)

    print("\n[3점 기반 계산]")
    print(f"✅ Bulge: {bulge:.8f}")
    print(f"🎯 중심각: {angle_deg:.8f}°")
    print(f"🔁 방향: {direction}")
    print(f"📍 중심점: ({center[0]:.8f}, {center[1]:.8f})")
    print(f"📏 반지름: {radius:.8f}")
"""