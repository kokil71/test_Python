from pyautocad import Autocad, APoint
import pythoncom
import win32gui
import win32com.client

def run_draw_and_zoom():
    pythoncom.CoInitialize()
    try:
        #acad = win32com.client.GetActiveObject("AutoCAD.Application")
        acad = Autocad(create_if_not_exists=True)
        p1 = APoint(0, 0)
        p2 = APoint(200, 100)
        line = acad.model.AddLine(p1, p2)
        circle = acad.model.AddCircle(p1 + p2, 100)
        text = acad.model.AddText("Hello AutoCAD", APoint(100, 50), 10)
        acad.app.ZoomExtents()
        #print("Normal running")
        intRtn = 1
        #return 1
    except Exception as e:
        print("Error:", e)
        intRtn = -2222
        #return -2222
        #return "Error:" + e
    finally:        
        pythoncom.CoUninitialize()
        return intRtn


def bring_autocad_to_front():
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        hwnd = win32gui.FindWindow(None, acad.Caption)
        if hwnd:
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
            print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)


if __name__ == "__main__":
    bring_autocad_to_front()
    run_draw_and_zoom()
    