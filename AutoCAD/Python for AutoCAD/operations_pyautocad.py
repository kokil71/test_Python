# https://www.supplychaindataanalytics.com/operations-with-autocad-objects-using-pyautocad-python/
# AutoCAD object operations with pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
from math import pi

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
        
    # Adding AutoCAD objects to drawing template using pyautocad in Python
    # As we have already discussed from our previous blogs in this pyautocad series about creating objects, we will draw some objects to perform the operations on them as mentioned above.
    c1 = acad.model.AddCircle(APoint(100, 100, 0), 100)
    l1 = acad.model.AddLine(APoint(100,100), APoint(300, 350))
    el1 = acad.model.AddEllipse(APoint(250, 300), APoint(700, 450), 0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Using copy, move and delete methods for basic AutoCAD operations
    # As we have sketched the basic AutoCAD objects, we will start with three of the most used commands i.e. copy, move, and delete.
    # The way copy work while using pyautocad is, we can create a copy of an existing object, store that in a variable and use the “Move” method to paste it at the desired location.
    c2 = c1.Copy()   
    
    # obj.Move(previous location, new location)
    c2.Move(APoint(100, 100), APoint(300, 300))

    time.sleep(0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Rotate AutoCAD objects with pyautocad in Python
    # Now, we will discuss how to rotate objects. Here, we will copy line l1 and will rotate the same from its existing base point (100, 100, 0) to 90 degrees.
    l2 = l1.Copy()

    # obj.Rotate(Base point, Angle of rotation)
    l2.Rotate(APoint(100,100), pi*90/180)

    time.sleep(0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Offsets objects in AutoCAD using pyautocad
    # Now, lets discuss how to take offsets of any object. We will need the Offset method to use against the object we want that offset for.
    # Here, we will take offset for the existing ellipse i.e. “el1”.
    #el2 = el1.Offset(10)

    print(type(el1))
    print(dir(el1))

    time.sleep(0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Scaling AutoCAD objects in Python
    # To scale an object up or down we will need the “Offset” method to be used against the object we want to scale.
    # Let’s scale down the existing circle “c2”.
    # obj.ScaleEntity(Base point, Scaling factor)
    c3 = c2.ScaleEntity(APoint(300, 300), 0.5)

    time.sleep(0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
    """
    try:
        pythoncom.CoInitialize()  # COM 초기화
        acad = connect_autocad()    
        draw_and_zoom(acad)
        #pythoncom.CoUninitialize()
    except Exception as e:
        print("🚫 오류:", e)
    finally:
        pythoncom.CoUninitialize()
    """
