from pyautocad import Autocad, APoint
import math

# 초기화
acad = Autocad(create_if_not_exists=True)
print(f"연결된 도면: {acad.doc.Name}")

# 파라미터 정의
radius = 3.0         # 상부 반원 반지름 (m)
width = 6.0          # 전체 하부 직선부 너비 (m)
center_x = 0         # 중심 x좌표
center_y = 0         # 중심 y좌표

# 계산
half_width = width / 2
bottom_y = center_y - radius
top_y = center_y + radius

# 좌측 반원 시작점 → 반시계 방향으로 그리기
points = []

# 하부 직선부
left = APoint(center_x - half_width, bottom_y,0)
right = APoint(center_x + half_width, bottom_y,0)
points.append(left)

# 우측 반원 중심
right_center = APoint(center_x + half_width - radius, center_y,0)

# 반원 (우측 상단부터 좌측 상단까지)
num_arc_points = 30
for i in range(num_arc_points + 1):
    angle = math.pi * (i / num_arc_points)  # 0 ~ pi
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    z =0
    points.append(APoint(x, y,z))

points.append(right)
points.append(left)  # 폐곡선 만들기 위해 처음 점으로 다시 닫음

# Polyline 생성
pl = acad.model.AddPolyline(points)
pl.Closed = True

print("✅ 말굽형 터널 단면이 그려졌습니다.")
