# https://www.supplychaindataanalytics.com/python-for-autocad-pyautocad-module/
# Python for AutoCAD (pyautocad module)

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
from os import *                            # os.X_OK: Checks if path can be executed:
from math import *                          # Importing math library to compute coordinates for a polygon:


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
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return
    
    # print name of document currently recognized as being active in AutoCAD
    print(acad.doc.Name)
    # specify x and y coordinates of circle center point
    point1 = APoint(100.0,100.0) # x and y coordinates of points
    # add circle to drawing
    circle1 = acad.model.AddCircle(point1,100)
    # change color of circle to red
    circle1.Color = 10 # 10 is a red color
    # check layer assignment
    print("current layer: "  + str(circle1.Layer))
    # check current linetype
    print("current linetype: " + str(circle1.Linetype))
    # check linetype scale
    print("current linetype scale: " + str(circle1.LinetypeScale))
    # check current line weight
    print("current line weight: " + str(circle1.Lineweight))
    # check current thickness
    print("current thickness: " + str(circle1.Thickness))
    # check current material
    print("current material:" + str(circle1.Material))

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # I can use the property attributes of e.g. the circle object to make adjustments. 
    # For example I have the layer “circles” which I want to assign the circle to. I can do this using pyautocad:
    layerObj = acad.doc.Layers.Add("circles")
    circle1.Layer = "circles"
    # I could now also adjust the color setting for the circle object, such that the color is specified by the layer – the index for this is the color index number 256:
    circle1.Color = 256

    # adding two circles to drawing
    circle2 = acad.model.AddCircle(APoint(200.0,200.0),100)
    circle3 = acad.model.AddCircle(APoint(300.0,300.0),100)
    # looping through all objects
    for obj in acad.iter_objects():
        print(obj)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()