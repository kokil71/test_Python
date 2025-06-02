# https://www.supplychaindataanalytics.com/using-python-lists-and-dictionaries-to-work-with-autocad-objects-with-pyautocad/
# Python lists and dictionaries for pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble

def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #print("✅ AutoCAD 실행 중입니다.")
        return Autocad(create_if_not_exists=False)          # pyautocad 연결
    except Exception:
        #print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            #acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            #print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            return Autocad(create_if_not_exists=False)      # pyautocad 연결
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
            #print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)

def draw_and_zoom(acad):
    # Use of Python lists and dictionaries for pyautocad objects
    # Use cases
    line1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
    line2 = acad.model.AddLine(APoint(200, 0, 0), APoint(100, 100, 0))

    circle1 = acad.model.AddCircle(APoint(100, 250, 0), 50)
    pl1 = acad.model.AddPolyline(aDouble(0, 0, 0, 100, 0, 0, 100, 100, 0, 0, 100, 0, 0, 0, 0))

    #Creating list for line objects
    ls_line = []
    ls_line.append(line1)
    ls_line.append(line2)

    # Creating dictionary for objects by specifying random properties as their keys
    dict_mixed = {"round": circle1, "square": pl1}

    # Now, we’ll iterate through the objects in the list and will change their properties.
    for l in ls_line:
        l.ScaleEntity(APoint(l.StartPoint), 2)
    
    # Also, we can iterate through dictionary objects using keys as given below.
    for j in dict_mixed:
        if j == "round":
            dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Center), 2)
        elif j == "square":
            dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Coordinate(4)), 2)

    # We can also filter objects based on the AutoCAD assigned property of value from a dictionary. For instance as in the demonstrated in the following lines of code:
    for j in dict_mixed:
        if dict_mixed[j].ObjectName == "AcDbCircle":
            dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Center), 2)
        elif dict_mixed[j].ObjectName == "AcDb2dPolyline":
            dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Coordinate(4)), 2)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()

