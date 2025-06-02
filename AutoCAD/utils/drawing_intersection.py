import pythoncom
import win32com.client
import numpy as np

# AutoCAD 초기화
pythoncom.CoInitialize()
acad = win32com.client.Dispatch("AutoCAD.Application")
doc = acad.ActiveDocument
ms = doc.ModelSpace

# ✅ 1. 두 점 정의
P1 = np.array([-10.96977748, 8.0])
P2 = np.array([-12.13003152, 0.0])

# ✅ 2. 중간점
M = (P1 + P2) / 2

# ✅ 3. 벡터 및 법선 벡터 계산
direction = P2 - P1
normal = np.array([direction[1], -direction[0]])  # 2D 법선
normal = normal / np.linalg.norm(normal)          # 단위 벡터

# ✅ 4. 법선 방향 선 (중간점 기준으로 충분히 연장)
start_point = M - normal * 100
end_point = M + normal * 100

# CAD에 법선 벡터 선 그리기
ms.AddLine(
    win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (start_point[0], start_point[1], 0.0)),
    win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (end_point[0], end_point[1], 0.0))
)

# ✅ 5. 비교할 기준 직선 정의
L1 = np.array([-19.63003152, 3.0])
L2 = np.array([-10.96977748, 8.0])
line_dir = L2 - L1
line_dir = line_dir / np.linalg.norm(line_dir)

# ✅ 6. 교점 계산 함수
def get_intersection(p1, dir1, p2, dir2):
    A = np.array([dir1, -dir2]).T
    b = np.array(p2) - np.array(p1)
    try:
        t = np.linalg.solve(A, b)
        return p1 + t[0] * dir1
    except np.linalg.LinAlgError:
        return None

intersection = get_intersection(M, normal, L1, line_dir)

# ✅ 7. 교점 AutoCAD에 출력
if intersection is not None:
    x, y = intersection
    print(f"✅ 교차점 좌표: ({x:.3f}, {y:.3f})")

    ms.AddPoint(
        win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, 0.0))
    )
else:
    print("❌ 교차점 없음 또는 직선이 평행합니다.")
