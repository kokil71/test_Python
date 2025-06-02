# https://www.supplychaindataanalytics.com/mirror-object-on-a-2d-plane-with-pyautocad-python/
# Mirror object in 2D plane with pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint

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

    # Setting up the environment for mirror objects in Python
    l1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
    
    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Creating mirror images with pyautocad
    # Creating a mirror image from an existing object needs a very simple command. Please check the syntax given below.
    # Syntax: object.Mirror(point1, point2)

    # Here, point1 and point2 are the start point and endpoint of the line with reference to which the object is being mirrored.
    # For instance, we will create a mirror image of the existing line with reference to an invisible line starting from point (100, 100, 0) to point (0, 100, 0).
    l1.Mirror(APoint(100, 100, 0), APoint(100, 0, 0))

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Now, let us move this imaginary line of reference 50 units away from the point (150, 0, 0) and check.
    l1.Mirror(APoint(150, 100, 0), APoint(150, 0, 0))

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()