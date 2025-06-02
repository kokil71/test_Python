from pyautocad import Autocad, APoint
import pythoncom
import win32com.client

def run_draw_and_zoom():
    pythoncom.CoInitialize()
    try:
        acad = Autocad(create_if_not_exists=True)
        p1 = APoint(0, 0)
        p2 = APoint(200, 100)
        line = acad.model.AddLine(p1, p2)
        circle = acad.model.AddCircle(p1 + p2, 100)
        text = acad.model.AddText("Hello AutoCAD", APoint(100, 50), 10)
        acad.app.ZoomExtents()
        return 1
    except Exception as e:
        print("Error:", e)
        #return "Error:" + e
        return -33333
    finally:
        pythoncom.CoUninitialize()