# https://www.supplychaindataanalytics.com/drawing-arcs-in-autocad-using-pyautocad/
# Drawing arcs in AutoCAD using pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
from math import *

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

    # Parameters for the command
    # With the specified pyautocad method AddArc, we need to pass certain parameters to draw an arc object.
    # Therefore, we need have to pass coordinates for the center point of the arc object, its radius, start angle, and end angle.
    # Syntax:
    # acad.model.AddArc(<Center Point of Circle>, <Radius>, <Start Angle>, <End Angle>)
    # Center Point
    p1 = APoint(30,30)
    #arc1 = acad.model.AddArc(p1, 7.5, 0, 4)
    #arc1 = acad.model.AddArc(p1, 7.5, round(45.0 * (pi / 180.0),8), round(270.0 * (pi / 180.0),8))
    arc1 = acad.model.AddArc(p1, 7.5, (45.0 * (pi / 180.0)), (270.0 * (pi / 180.0)))

    # The pyautocad command accepts angle in radians and not in degrees.
    # The arc will be drawn counter-clockwise by autocad, starting from the x-axis of the 1st quadrant.
    # However, we can directly pass the center point coordinates to the command itself, with angles converting to radians from degrees, for instance.
    arc2 = acad.model.AddArc(APoint(45, 45), 10, 15*pi/180 , 105*pi/180)
    
    # Area of an arc object
    # In the case of open objects such as arcs, spline curves, and open polylines the area is computed as if a straight line connects the start point and endpoint of the arc.
    # To get the area of the arc object we will use the object.Area() method.
    a1a = print("Area of Arc1 = " + str(round(arc1.Area,2)))
    a2a = print("Area of Arc2 = " + str(round(arc2.Area,2)))

    # Other properties of an arc object
    # We can find more such properties related to an arc object. For example, center point, radius, start & endpoints, start and end angles, etc. as described below:
    #Center of Arc
    a1c = print("Center of Arc1 = " + str(arc1.Center))
    a2c = print("Center of Arc2 = " + str(arc2.Center))
    #Radius of Arc
    a1c = print("Radius of Arc1 = " + str(arc1.Radius))
    a2c = print("Radius of Arc2 = " + str(arc2.Radius))
    #Start & End points of Arc
    a1sp = print("Start point of Arc1 = " + str(arc1.StartPoint))
    a1ep = print("End point of Arc1 = " + str(arc1.EndPoint))
    a2sp = print("Start point of Arc2 = " + str(arc2.StartPoint))
    a2ep = print("End point of Arc2 = " + str(arc2.EndPoint))
    #Start & End angles of Arc
    a1sa = print("Start angle of Arc1 = " + str(arc1.StartAngle) + " rad / " + str(arc1.StartAngle * 180.0 / pi ) + " deg")
    a1ea = print("End angle of Arc1 = " + str(arc1.EndAngle) + " rad / " + str(arc1.EndAngle * 180.0 / pi ) +" deg")
    a2sa = print("Start angle of Arc2 = " + str(arc2.StartAngle) + " rad / " + str(arc2.StartAngle * 180.0 / pi ) + " deg")
    a2ea = print("End angle of Arc2 = " + str(arc2.EndAngle) + " rad / " + str(arc2.EndAngle * 180.0 / pi ) + " deg")


    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
    