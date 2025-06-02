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

# AutoCAD 실행 중인 인스턴스에 연결 : win32com
acad = win32com.client.Dispatch("AutoCAD.Application")
acad.Visible = True  # AutoCAD 창이 안 보일 경우 True로 설정

# AutoCAD 실행 중인 인스턴스에 연결 : pyautocad
#acad = Autocad(create_if_not_exists=True)
#acad.Visible = True  # AutoCAD 창이 안 보일 경우 True로 설정

# 현재 도면과 모델 공간 객체 접근 ActiveDocument : pyautocad
#doc = acad.doc
#ms = doc.model

# 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
doc = acad.ActiveDocument
#ms = doc.ModelSpace
acad_model = doc.ModelSpace
acad_app = acad.Application

#doc = acad.ActiveDocument
#acadModel = doc.ModelSpace

# [Prerequisites for creating a solid object in AutoCAD]
#Circle
#c1 = acad.AddCircle(ap(100, 100, 0), 50)
#c2 = acad.AddCircle(ap(100, 100, 0), 45)
#c1 = acad.model.AddCircle(ap(100, 100, 0), 50)
#c2 = acad.model.AddCircle(ap(100, 100, 0), 45)

# 중심 좌표
pt = ap(100.0, 100.0, 0.0)
win32com_center = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [pt.x, pt.y, pt.z])

# 원 2개 생성
#c1 = acad.model.AddCircle(pt, 50.0)
#c2 = acad.model.AddCircle(pt, 45.0)
c1 = acad_model.AddCircle(win32com_center, 50.0)
c2 = acad_model.AddCircle(win32com_center, 45.0)
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
#regions = acad.model.AddRegion(shapes)
regions = acad_model.AddRegion(shapes)

#Path
#a1 = acad.model.AddLine(ap(1000, 1000, 0), ap(1000, 1000, 1500))
p1 = ap(1000, 1000, 0)
p2 = ap(1000, 1000, 1500)
win32com_p1 = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [p1.x, p1.y, p1.z])
win32com_p2 = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [p2.x, p2.y, p2.z])
a1 = acad_model.AddLine(win32com_p1, win32com_p2)

# Creating solid objects using AutoCAD region and path : AutoCAD 영역 및 경로를 사용하여 솔리드 객체 만들기
for obj in acad_model:
    if obj.ObjectName=="AcDbRegion":
        acad_model.AddExtrudedSolidAlongPath(obj, a1)

# 화면 갱신
#acad.app.Update()
#acad.app.ZoomExtents()
acad_app.Update()
acad_app.ZoomExtents()

#print(f"Region 개수: {regions.Count}")

# COM 초기화 (필수)
pythoncom.CoUninitialize()