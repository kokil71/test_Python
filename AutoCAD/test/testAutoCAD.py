#-- coding: utf-8 --

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from pyautocad import Autocad, APoint

# AutoCAD 인스턴스 시작
acad = Autocad(create_if_not_exists=True)
print(f"Connected to AutoCAD: {acad.doc.Name}")

# 점 좌표 지정
p1 = APoint(0, 0)
p2 = APoint(100, 100)

# 선(Line) 그리기
line = acad.model.AddLine(p1, p2)
print("Line drawn from", p1, "to", p2)

# 텍스트 추가
text = acad.model.AddText("Hello AutoCAD", APoint(50, 50), 10)
print("Text added at", APoint(50, 50))
