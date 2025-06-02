# https://www.supplychaindataanalytics.com/drawing-ellipse-ellipse-arcs-in-autocad-using-pyautocad-python/
# Ellipse & ellipse arcs with pyautocad

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
    
    # Command parameters for ellipse
    # While working with the AddEllipse method, we need to pass certain parameters to the command itself, and sometimes separately in case of drawing an elliptical arc.
    # Syntax:
    # acad.model.AddEllipse(<Centre of ellipse>, <Greater radius end point>, <Ratio of greater to smaller radius>)
    # acad.model.AddEllipse(<Centre of ellipse>, 장축 벡타 : 벡터 끝점(벡터시점 : 원점(0,0,0)), <Ratio of greater to smaller radius>)
    # We will pass the points for the center of the ellipse object and the position of the endpoint of the greater radius.
    # Ellipse 1
    p1 = APoint(35, 35)
    p2 = APoint(40, 35)
    #p2 = APoint(-40, 35)
    #p2 = APoint(35, 40)
    #p2 = APoint(35, -40)

    el1 = acad.model.AddEllipse(p1, p2, 0.5)

    time.sleep(0.5)   

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Elliptical arcs in pyautocad
    # Now that we have seen how to draw an ellipse, we need to learn how we can create elliptical arcs.
    # We need 2 extra arguments having the below-mentioned syntax:
    # object.StartAngle = Angle in radians
    # object.EndAngle = Angle in radians
    # Ellipse 2
    el2 = acad.model.AddEllipse(APoint(100, 50), APoint(150, 50), 0.5)    
    # Creating arc out of ellipse 2 : 타원 중심에서 장축을 기준으로의 반시계방향각
    el2.StartAngle = round(45.0 * (pi / 180.0),8)
    el2.EndAngle = round(270.0 * (pi / 180.0),8)

    # Properties of an AutoCAD ellipse object in pyautocad
    # We can generate the properties of the ellipse using the below-mentioned commands for detailed information
    print("Ellipse 1 properties: " + "\n" +
    "Area of Ellipse 1 = " + str(round(el1.Area,2)) + "\n" +
    "Center of Ellipse 1 = " + str(el1.Center) + "\n" +
    "Start point of Ellipse 1 = " + str(el1.StartPoint) + "\n" +
    "End point of Ellipse 1 = " + str(el1.EndPoint) + "\n" +
    "Start angle of Ellipse 1 = " + str(round(el1.StartAngle,2)) + "\n" +
    "End angle of Ellipse 1 = " + str(round(el1.EndAngle,2)) + "\n" +
    "Start parameter of Ellipse 1 = " + str(el1.StartParameter) + "\n" +
    "End parameter of Ellipse 1 = " + str(el1.EndParameter) + "\n" +
    "Major axis of Ellipse 1 = " + str(el1.MajorAxis) + "\n" +
    "Minor axis of Ellipse 1 = " + str(el1.MinorAxis) + "\n" +
    "Major radius of Ellipse 1 = " + str(round(el1.MajorRadius,2)) + "\n" +
    "Minor radius of Ellipse 1 = " + str(round(el1.MinorRadius,2)) + "\n" + 
    "Radius ratio of Ellipse 1 = " + str(el1.RadiusRatio)
    )

    # Properties of elliptical arcs in AutoCAD
    # The reason behind creating a separate point for properties of elliptical arcs is the area of arc.
    # As we have already discussed in one of our previous blogs regarding arcs; in the case of open objects such as arcs, spline curves, and open polylines:
    # The area is computed as though a straight line connects the start point and endpoint.
    # For example:
    # Let’s generate the properties of the elliptical arc that we created from ellipse 2.
    print("Ellipse 2 properties: " + "\n" +
    "Area of Ellipse 2 = " + str(round(el2.Area,2)) + "\n" +
    "Center of Ellipse 2 = " + str(el2.Center) + "\n" +
    "Start point of Ellipse 2 = " + str(el2.StartPoint) + "\n" +
    "End point of Ellipse 2 = " + str(el2.EndPoint) + "\n" +
    "Start angle of Ellipse 2 = " + str(round(el2.StartAngle,2)) + "\n" +
    "End angle of Ellipse 2 = " + str(round(el2.EndAngle,2)) + "\n" +
    "Start parameter of Ellipse 2 = " + str(el2.StartParameter) + "\n" +
    "End parameter of Ellipse 2 = " + str(el2.EndParameter) + "\n" +
    "Major axis of Ellipse 2 = " + str(el2.MajorAxis) + "\n" +
    "Minor axis of Ellipse 2 = " + str(el2.MinorAxis) + "\n" +
    "Major radius of Ellipse 2 = " + str(round(el2.MajorRadius,2)) + "\n" +
    "Minor radius of Ellipse 2 = " + str(round(el2.MinorRadius,2)) + "\n" + 
    "Radius ratio of Ellipse 2 = " + str(el2.RadiusRatio)
    )

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()

