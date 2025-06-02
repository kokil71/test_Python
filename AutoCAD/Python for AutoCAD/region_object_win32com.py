# https://www.supplychaindataanalytics.com/region-object-in-autocad-with-python/
# Region object in AutoCAD with Python
# Region object in AutoCAD
# Creating a region object in AutoCAD (win32com etc.)

# pyautocad 모듈을 사용하고 있습니다. 
#from pyautocad import Autocad, APoint as ap, aDouble as ad
#acad = Autocad(create_if_not_exists=True)

# AutoCAD 실행 중인 인스턴스에 연결 : win32com
# communication(통신) 모듈도 사용할 수 있습니다
from win32com.client import *
import pythoncom
import win32com
from pyautocad import Autocad, APoint as ap, ADouble as ad

# COM 초기화 (필수)
pythoncom.CoInitialize()

acad = win32com.client.Dispatch("AutoCAD.Application")
acad.Visible = True  # AutoCAD 창이 안 보일 경우 True로 설정

# 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
doc = acad.ActiveDocument
#ms = doc.ModelSpace
acad_model = doc.ModelSpace
acad_app = acad.Application

#Enclosed polyline
#pl1 = acad_model.AddPolyline(ad(0,0,0,1000,0,0,1000,500,0,750,500,0,750,1000,0,250,1000,0,250,500,0,0,500,0,0,0,0))
pl1 = acad_model.AddPolyline(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [0,0,0,1000,0,0,1000,500,0,750,500,0,750,1000,0,250,1000,0,250,500,0,0,500,0,0,0,0]))

#Circle
#c1 = acad_model.AddCircle(ap(500, 1000, 0), 250)
c1 = acad_model.AddCircle(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [500.0, 1000.0, 0.0]), 250)

"""
#Syntax:
#object.AddRegion(array_of_enclosed_objects)
#Here object can be Block, ModelSpace or PaperSpace
region = acad_model.AddRegion(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [pl1, c1]))
#region["reg0"] = acad_model.AddRegion(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [pl1, c1]))

# Performing boolean operations on region objects : pyautocad
#Union (0) / #Intersection (1) / #Subtraction (2)
#Syntax:
#object1.Boolean(operation_id, object2)
#Here objects could be 3DSolids or Regions
#regions["reg1"].Boolean(2, regions["reg0"])


# Region 불리언 연산
region0 = region[0]
region1 = region[1]
region1.Boolean(2, region0)  # Subtraction

#region1.Move(ap(0, 0, 0), ap(1500, 0, 0))

acad1 = Autocad()
for l in acad1.iter_objects_fast(object_name_or_list="Region"):
#for l in acad1.iter_objects_fast(object_name_or_list = acDbRegion):
    print(str(l.ObjectID) + ": " + l.ObjectName)
    l.Move(ap(0, 0, 0), ap(1500, 0, 0))
"""
# 딕셔너리
# Region 생성
region_tuple = acad_model.AddRegion(
    VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [pl1, c1])
)

# 딕셔너리로 래핑
region = {
    f"reg{i}": region_tuple[i]
    for i in range(len(region_tuple))
}

# 불리언 연산: reg1 - reg0
region["reg1"].Boolean(2, region["reg0"])  # Subtract

# 이동
#regions["reg1"].Move(ap(0, 0, 0), ap(1500, 0, 0))
acad1 = Autocad()
for l in acad1.iter_objects_fast(object_name_or_list="Region"):
#for l in acad1.iter_objects_fast(object_name_or_list = acDbRegion):
    print(str(l.ObjectID) + ": " + l.ObjectName)
    l.Move(ap(0, 0, 0), ap(1500, 0, 0))

# 화면 갱신
#acad.app.Update()
#acad.app.ZoomExtents()
acad_app.Update()
acad_app.ZoomExtents()

# COM 초기화 (필수)
pythoncom.CoUninitialize()