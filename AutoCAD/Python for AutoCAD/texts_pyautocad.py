# https://www.supplychaindataanalytics.com/working-with-texts-in-autocad-using-pyautocad-python/
# Working with AutoCAD texts in pyautocad

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

    # Working with normal texts with pyautocad
    # To insert a text string in an AutoCAD template, we need a very simple command. Let’s check out the syntax and use it.
    # Syntax: acad.model.AddText(Text String, Insertion Point, Text Height)
    t1 = acad.model.AddText("Hello", APoint(75, 50), 25)
    
    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    print("Text content: " + t1.TextString)
    print("Text style: " + t1.StyleName)
    print("Text insertion point: ", end=" " )
    print(t1.InsertionPoint)
    print("Text alignment: " + str(t1.Alignment))
    print("Text alignment point: " + str(t1.TextAlignmentPoint))
    print("Text height: " + str(t1.Height))
    print("Text rotation: " + str(t1.Rotation))
    print("Text scale factor: " + str(t1.ScaleFactor))
    print("Is the text upside down: " + str(t1.UpsideDown))
    
    #We can change the text and its properties using these functions. Let’s try the same.
    t1.TextString = "Hi"
    t1.Height = 50
    t1.Rotation = 2
    t1.ScaleFactor = 1
    t1.UpsideDown = True
    
    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Working with multi-line AutoCAD text objects in pyautocad
    # Sometimes, we need to be more descriptive in the drawing to explain certain attributes, in that case, we need long sentences and hence the need for multiline texts arises. With this, we can set horizontal limits for the text we want to enter.
    # The command for multiline text is as simple as that of normal text.
    # Syntax: acad.model.AddMText(Insertion Point, Width, Text String)
    mt1 = acad.model.AddMText(APoint(275, 150), 100, "This is auotocad text")
    mt1.Height = 25

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()