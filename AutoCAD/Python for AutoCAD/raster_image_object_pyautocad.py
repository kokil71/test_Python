# https://www.supplychaindataanalytics.com/raster-image-object-in-autocad-with-pyautocad-python/
# AutoCAD raster image object with pyautocad

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
    # Setting up environment using pyautocad (Python)
    # Adding image to AutoCAD template using AddRaster method
    # object.AddRaster(ImageFileName, InsertionPoint, ScaleFactor, RotationAngle)
    #ri = acad.model.AddRaster("C:\\Users\\91998\\OneDrive\\Desktop\\physics-science-school-blueprint-G35FEF.jpg", APoint(100, 100, 0), 1, 0)
    ri = acad.model.AddRaster("C:\\Users\\TESO\\Pictures\\Screenshots\\스크린샷 2025-05-22 125418.png", APoint(100, 100, 0), 1, 0)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Properties of the raster image object
    print(ri.Contrast)
    print(ri.Fade)
    print(ri.ImageFile)
    print(round(ri.ImageHeight,2))
    print(round(ri.ImageWidth,2))
    print(ri.ImageVisibility)
    print(ri.Rotation)
    print(round(ri.ScaleFactor,2))

if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
