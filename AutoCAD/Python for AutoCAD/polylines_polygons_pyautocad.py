# https://www.supplychaindataanalytics.com/polylines-in-pyautocad-for-drawing-autocad-polygons/
# pyautocad polylines for AutoCAD polygons

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
from os import *                            # os.X_OK: Checks if path can be executed:
from math import *                          # Importing math library to compute coordinates for a polygon:


def connect_autocad():
    acad_app = None
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
        if acad_app is not None:
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

    # Request and embed user input into workflow and code
    # With this code we can create an inscribed polygon.
    # To draw this polygon we need some user inputs to generate the drawing. This includes input concerning center point coordinate for circle, radius of circle.
    # We can code this as per our preferred coding language. In this case Python, using pyautocad:
    # 1. Number of vertices for polygon
    na = int(input("Enter the number of vertices for the polygone: "))
    # 2. Center & Radius of Circle
    # Center
    cc = input("Enter x, y coordinates for center of circle with comma separators e.g. x, y: ")
    ccc = (map(float, cc.split(", ")))
    # Converting list to tuple as pyautocad accepts tuple as input
    ccct = tuple(ccc)
    print('The coordinates for the center of circle : ',ccct)
    # Radius
    rc = float(input("Enter the radius of Circle: "))

    # Calculate coordinates for vertices of AutoCAD polygon
    # We can calculate coordinates for vertices of the polygon using the formula below:
    # x  +  r * cos( 2 * pi * i / n ),  y + r * sin(2 * pi * i / n)
    # The components of this formula are list below:
    # x, y = Coordinates for the center of the circle
    # r = Radius of circle
    # i = Iteration
    # n = Number of vertices
    # I have encoded this as mentioned below:
    # 3. Calculate coordinates
    i=0
    # Creating an empty list for coordinates
    pgonc=[]
    for i in range(na):
        x=round(ccct[0]+rc*cos(2*pi*i/na),2)
        y=round(ccct[1]+rc*sin(2*pi*i/na),2)
        z=0
        crd = [x, y, z]
        pgonc.extend(crd)
        i += 1
    # Addind first point again to complete the loop of polygon
    fp = [pgonc[0], pgonc[1], pgonc[2]]
    pgonc.extend(fp)
    # Converting list to tuple as pyautocad accepts tuple as input
    pgont=tuple(pgonc)
    print("Coordinates of polygon: ")
    print(pgont)

    # Draw the AutoCAD polygon using polylines in pyautocad
    # To draw the polygon, we need to pass the coordinates to aDouble method in a tuple format:
    polygon = aDouble(pgont)
    # Now with the AddPolyline method we can draw the polygon according to the coordinates we passed to aDouble:
    polygond = acad.model.AddPolyline(polygon)

    """
    if polygond is None:
        print("polygond : " + "❌ AddPolyline() 실패: 유효하지 않은 좌표 또는 AutoCAD 모델 공간 문제일 수 있습니다.")
        return
    """

    # Rotate the AutoCAD polygon with pyautocad
    # We can rotate the polygon using rotate method on the variable assigned to polyline:
    # Here we will try rotating the polygon around its center i.e. (100, 25, 0), at 185 degrees.
    # Syntax for rotation:
    # object.Rotate(Coordinates for Axis, Angle)
    # Rotate the polygon : 
    #polygond1 = polygond.Rotate(APoint(100, 25, 0), pi * 185.0 / 180.0)  # Rotate return 값이 없는데
    polygond.Rotate(APoint(100, 25, 0), pi * 185.0 / 180.0)  # Rotate return 값이 없는데
    #Note: We shall convert the angle in radians if we want to enter the same in degrees.

    time.sleep(0.5)
    
    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    """
    if polygond1 is None:
        print("polygond1 : " + "❌ AddPolyline() 실패: 유효하지 않은 좌표 또는 AutoCAD 모델 공간 문제일 수 있습니다.")
        return
    """

    # Other properties of polylines in pyautocad
    # We can find other properties of the created objects, i.e. here polygon too; using some of the methods mentioned below:    
    #Area = Specifies the area of closed entities:    
    pa = polygond.Area
    print("Area of polygon: " + str(pa))
    #Length = Specifies the length of any object:
    pl = polygond.Length
    print("Perimeter of polygon: " + str(pl))    
    #Closed = Specified whether the created object is open or closed:
    is_closed = polygond.Closed
    print("Is the Polyline Object a Closed space: " + str(is_closed))
    #Coordinate: Specify coordinates of a single vertex by passing vertex index no as a parameter:
    print("Elevation of Vertex: ")
    print(polygond.Coordinate(1))
    #Coordinates: We can get coordinates of all the vertices of polygon:
    print(polygond.Coordinates)
    #Layer = Specifies the layer used to draw the object:
    print("Perimeter of polygon: " + polygond.Layer)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()