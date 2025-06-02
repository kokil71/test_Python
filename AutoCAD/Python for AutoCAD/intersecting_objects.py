# https://www.supplychaindataanalytics.com/operations-with-intersecting-objects-in-autocad-using-pyautocad-python/

# Intersecting objects in AutoCAD with pyautocad
# IntersectWith method in pyautocad
# object.IntersectWith(IntersectObject, ExtendOption)
# acExtendNone: Does not extend either object. This can fetch a 3D array of coordinate points if both the passed objects are already intersecting each other at a particular point. To use this parameter we have to pass 0 as parameter input value.
# acExtendNone : 두 객체 모두 확장하지 않습니다. 전달된 두 객체가 이미 특정 지점에서 교차하는 경우, 좌표점의 3D 배열을 가져올 수 있습니다. 이 매개변수를 사용하려면 매개변수 입력 값으로 0을 전달해야 합니다.
# acExtendThisEntity : Extends the base object. If extending the object against which we are using the IntersectWith method is able to intersect the object we are passing as a parameter then this parameter gives us the point at which both the entities intersect after extending the first object. To use this parameter we need to pass 1 as parameter input value.
# acExtendThisEntity : 기본 객체를 확장합니다. IntersectWith 메서드를 사용하는 객체를 확장할 때 매개변수로 전달하는 객체와 교차할 수 있는 경우, 이 매개변수는 첫 번째 객체를 확장한 후 두 엔티티가 교차하는 지점을 반환합니다. 이 매개변수를 사용하려면 매개변수 입력 값으로 1을 전달해야 합니다.
# acExtendOtherEntity : Extends the object passed as an argument. Pass 2 as parameter input value if we want to fetch the point at which the two objects intersect on extending the object passed as a parameter.
# acExtendOtherEntity : 인수로 전달된 객체를 확장합니다. 매개변수로 전달된 객체를 확장할 때 두 객체가 교차하는 지점을 가져오려면 매개변수 입력 값으로 2를 전달합니다.
# acExtendBoth : Extends both objects. We need to pass 3 as parameter input value if we want to get the intersection point of two objects after extending both of them.
# acExtendBoth : 두 객체를 모두 확장합니다. 두 객체를 확장한 후 교차점을 구하려면 매개변수 입력 값으로 3을 전달해야 합니다.

import pythoncom
import win32gui
import win32com.client
import time
from math import pi
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
    # IntersectWith method using acExtendNone parameter as ExtendOption
    c1 = acad.model.AddCircle(APoint(100, 100, 0), 75)
    c2 = acad.model.AddCircle(APoint(100, 200, 0), 75)

    # Let us apply the IntersectWith method against circle c1, and pass c2 as IntersectObject parameter. 
    # We can use it either way. Also, pass 0 for “acExtendNone” to check the intersection points.
    print(c1.IntersectWith(c2, 0)) # acExtendNone : 두 객체 모두 확장하지 않습니다
    
    #IntersectWith method using acExtendThisEntity and acExtendOtherEntity parameters with pyautocad
    a1 = acad.model.AddArc(APoint(150, 105, 0), 75, 0, round(105*pi/180,2))
    l1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))

    print(l1.IntersectWith(a1, 1))  # acExtendThisEntity : 기본 객체를 확장합니다
    print(l1.IntersectWith(a1, 2))  # acExtendOtherEntity : 인수로 전달된 객체를 확장

    # IntersectWith method using acExtendBoth parameter with pyautocad
    l1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
    l2 = acad.model.AddLine(APoint(300, 0, 0), APoint(200, 100, 0))

    print(l1.IntersectWith(l2, 3))  # acExtendBoth : 두 객체를 모두 확장
    print(l1.IntersectWith(l2, 1))  # acExtendThisEntity : 기본 객체를 확장합니다

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()


