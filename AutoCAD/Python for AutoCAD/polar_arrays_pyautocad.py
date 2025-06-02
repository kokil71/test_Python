# https://www.supplychaindataanalytics.com/polar-arrays-in-autocad-using-pyautocad-python/
# Polar AutoCAD arrays using pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
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
    
    # Creating some AutoCAD object as base for the polar array
    # To create an array, we will use the circle as an object. We will draw the circle using the AddCircle method. Also, we will store this circle in a variable “c1” to apply the array command against the created circle.
    c1 = acad.model.AddCircle(APoint(100, 100), 100)

    # Concept of a polar array in AutoCAD
    # AutoCAD determines the distance from the array’s center point to a reference point on the last object selected. The reference point used depends on the type of object previously selected. AutoCAD uses the center point of a circle or arc, the insertion point of a block or shape, the start point of the text, and one endpoint of a line or trace.
    # Creating a polar array in AutoCAD with pyautocad in Python
    # Before creating the polar array, let’s check the syntax for creating the polar array.
    # Syntax: object.ArrayPolar(NumberOfObjects, AngleToFill, CenterPointofArray)
    # Angle shall be specified in radians
    # Center point of array shall be specified in the form of three-element array of doubles
    # Using the above-mentioned syntax, we will create the array.    
    #arr1 = c1.ArrayPolar(10, round(pi*180/180), aDouble(550, 600, 0))
    #arr1 = c1.ArrayPolar(10, pi, aDouble(550, 600, 0))
    center_point = aDouble(550, 600, 0)
    arr1 = c1.ArrayPolar(10, pi, center_point)

    # radians(360)은 2 * pi와 동일하고, 360도 전체 회전을 의미합니다.

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()