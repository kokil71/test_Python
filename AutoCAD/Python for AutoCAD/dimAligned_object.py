# https://www.supplychaindataanalytics.com/dimaligned-object-in-autocad-using-python/
# DimAligned object in AutoCAD using Python

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
import time
from pyautocad import Autocad, APoint
import win32gui
import win32com.client


def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #hwnd = win32gui.FindWindow(None, acad_app.Caption)
        #bring_autocad_to_front(hwnd)
        print("✅ AutoCAD 실행 중입니다.")
        return Autocad(create_if_not_exists=False)
    except Exception:
        print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            return Autocad(create_if_not_exists=False)
        except Exception as e:
            print("🚫 AutoCAD 연결 실패:", e)
            return None
    finally:
        hwnd = win32gui.FindWindow(None, acad_app.Caption)
        bring_autocad_to_front(hwnd)      

def bring_autocad_to_front(hwnd):
    try:
        #acad = win32com.client.GetActiveObject("AutoCAD.Application")
        #hwnd = win32gui.FindWindow(None, acad.Caption)
        if hwnd:
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
            print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)

def set_and_get_properties(ll):
    # general properties
    print(ll.ObjectName)
    print(ll.Rotation) # rotation angle of object in radians
    print(ll.LinearScaleFactor) 
    # specfies global scale factor for linear dimensioning  measurements
    print(ll.StyleName)
    ll.DecimalSeparator = "."
    print(ll.DecimalSeparator)
    # arrow head properties
    ll.ArrowheadSize = 15
    print(ll.ArrowheadSize)
    print(ll.Arrowhead1Type)
    print(ll.Arrowhead2Type)
    # color
    ll.DimensionLineColor = 200
    print("Dimension line color on the basis of 0-256 color index: " + str(ll.DimensionLineColor))
    print("The dimension line extends beyond the extension line when oblique strokes are drawn instead of arrowheads: " + str(ll.DimensionLineExtend))
    print("The dimension line type is: " + ll.DimensionLineType)
    # LineWeight
    ll.DimensionLineWeight = 100 
    print("Dimension lineweight: " + str(ll.DimensionLineWeight))
    print("Dimension text direction: ", end="" )
    print(ll.DimTxtDirection)
    # False: Left to right reading style
    # True: Right to Left reading style 
    #Text properties
    ll.TextHeight = 20
    print(ll.TextHeight)
    print(ll.TextInside)
    #Tolerance properties
    print(ll.ToleranceDisplay)
    print(ll.TolerancePrecision)

def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # 모델 공간에 객체 추가
    for l in acad.iter_objects_fast(object_name_or_list="AcDbLine"):
        ll = acad.model.AddDimAligned(APoint(l.StartPoint),  APoint(l.EndPoint),  APoint((l.StartPoint[0]+l.EndPoint[0]+100)/2, (l.StartPoint[1]+l.EndPoint[1]+100)/2, 0))
        set_and_get_properties(ll)  # Properties

    for i in acad.iter_objects_fast(object_name_or_list="AcDbPolyline"):
        nodes = len(i.Coordinates)/2        
        j=0        
        while j <= nodes+1:
            ii = acad.model.AddDimAligned(APoint(i.Coordinates[j], i.Coordinates[j+1], 0),    APoint(i.Coordinates[j+2], i.Coordinates[j+3], 0),    APoint((i.Coordinates[j]+i.Coordinates[j+2]+100)/2,     (i.Coordinates[j+1]+i.Coordinates[j+3]+100)/2, 0))
            set_and_get_properties(ii)  # Properties
            j+=2
        
    #print("▶ 선, 원 및 텍스트 추가 완료.")

    # 화면 갱신(Update) — 일부 버전에서는 자동 수행되지만 수동 호출도 가능
    acad.app.Update()
    print("▶ 화면 업데이트 완료.")

    # Zoom All (전체 보기)
    #acad.app.ZoomAll()
    #print("▶ Zoom All 완료.")

    # ZoomExtents
    acad.app.ZoomExtents()
    print("▶ Zoom Extents 완료.")


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
