import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
import time
from pyautocad import Autocad
import win32com.client


def draw_line(x1, y1, x2, y2):
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        print("✅ AutoCAD 실행 중입니다.")
        #return Autocad(create_if_not_exists=False)
    except Exception:
        print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad = win32com.client.Dispatch("AutoCAD.Application")
            acad.Visible = True
            time.sleep(3)  # 로딩 대기
            print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            #return Autocad(create_if_not_exists=False)
        except Exception as e:
            print("🚫 AutoCAD 연결 실패:", e)
            #return None
    #pythoncom.CoInitialize()
    #acad = win32com.client.Dispatch("AutoCAD.Application")
    #acad.Visible = True

    #doc = acad.ActiveDocument
    #ms = doc.ModelSpace
    #ms = acad.ModelSpace

    p1 = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x1, y1, 0))
    p2 = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x2, y2, 0))
    #ms.AddLine(p1, p2)
    line = acad.model.AddLine(p1, p2)

    return 1


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화
    #acad = connect_autocad()
    #draw_and_zoom(acad)
    draw_line(0.0, 10.0, 0.0, 10.0)
    pythoncom.CoUninitialize()