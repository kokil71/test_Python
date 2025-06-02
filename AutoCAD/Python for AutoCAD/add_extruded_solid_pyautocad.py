# https://www.supplychaindataanalytics.com/autocad-application-object-class-in-python/

# pyautocad 모듈을 사용하고 있습니다. 
#from pyautocad import Autocad, APoint, aDouble

#acad = Autocad(create_if_not_exists=True)

# communication(통신) 모듈도 사용할 수 있습니다
from win32com.client import *
import pythoncom
import win32com
from pyautocad import Autocad, APoint as ap


# COM 초기화 (필수)
pythoncom.CoInitialize()

# AutoCAD 실행 중인 인스턴스에 연결
#acad = win32com.client.Dispatch("AutoCAD.Application")
#acad.Visible = True  # AutoCAD 창이 안 보일 경우 True로 설정

acad = Autocad(create_if_not_exists=True)
acad.Visible = True  # AutoCAD 창이 안 보일 경우 True로 설정

# 현재 도면과 모델 공간 객체 접근
#doc = acad.doc
#ms = doc.ModelSpace

# [Prerequisites for creating a solid object in AutoCAD]
#Circle
#c1 = acad.AddCircle(ap(100, 100, 0), 50)
#c2 = acad.AddCircle(ap(100, 100, 0), 45)
#c1 = acad.model.AddCircle(ap(100, 100, 0), 50)
#c2 = acad.model.AddCircle(ap(100, 100, 0), 45)

# 중심 좌표
pt = ap(100.0, 100.0, 0.0)
#center = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [pt.x, pt.y, pt.z])

# 원 2개 생성
c1 = acad.model.AddCircle(pt, 50.0)
c2 = acad.model.AddCircle(pt, 45.0)
#c1 = acad.model.AddCircle(center, 50.0)
#c2 = acad.model.AddCircle(center, 45.0)
########################################
#Region
#r1 = acad.AddRegion(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (c1, c2)))
#r1 = acad.model.AddRegion(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [c1, c2]))
#r1 = acad.doc.AddRegion(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [c1, c2]))

# Region 생성을 위한 원 리스트를 Variant로 포장
shapes = win32com.client.VARIANT(
    pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH,
    [c1, c2]
)
# Region 생성 (주의: acad.doc 사용)
regions = acad.model.AddRegion(shapes)
#regions = acad.doc.AddRegion(shapes)

#Path
#a1 = acad.AddLine(ap(1000, 1000, 0), ap(1000, 1000, 1500))
a1 = acad.model.AddLine(ap(1000, 1000, 0), ap(1000, 1000, 1500))

# Creating solid objects using AutoCAD region and path : AutoCAD 영역 및 경로를 사용하여 솔리드 객체 만들기
for obj in acad:
    if obj.ObjectName=="AcDbRegion":
        acad.AddExtrudedSolidAlongPath(obj, a1)

# 화면 갱신
acad.app.Update()
acad.app.ZoomExtents()

#print(f"Region 개수: {regions.Count}")

# COM 초기화 (필수)
pythoncom.CoUninitialize()