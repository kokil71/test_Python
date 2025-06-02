import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
import time
import win32gui
import win32com.client

from pickle import TRUE
from pyautocad import Autocad, APoint, aDouble

def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #hwnd = win32gui.FindWindow(None, acad_app.Caption)
        #bring_autocad_to_front(hwnd)
        print("✅ AutoCAD 실행 중입니다.")
        return Autocad(create_if_not_exists=False)
    except Exception:
        print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            return Autocad(create_if_not_exists=False)
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
            print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)

def set_and_get_properties(br):
    # properties
   print("Does the Block contain any Attributes: ", end="")
   print(br.HasAttributes)


def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # 모델 공간에 객체 추가
    ip = APoint(0, 0, 0)
    b1 = acad.doc.Blocks.Add(ip, "Attributed_Block_1")

    pl = b1.AddPolyline(aDouble(0, 0, 0, 10000, 0, 0, 10000, 5000, 0, 0, 5000, 0, 0, 0, 0))
    l = b1.AddLine(APoint(0, 250, 0), APoint(10000, 250, 0))
    l = b1.AddLine(APoint(5000, 250, 0), APoint(5000, 0, 0))

    a1 = b1.AddAttribute(50, 0, "DATE", aDouble(200, 100, 0), "DATE", "Date: 17/07/2022")
    a2 = b1.AddAttribute(50, 0, "DWG", aDouble(5200, 100, 0), "DWG", "Drawing Name: Drawing 1")

    br = acad.model.InsertBlock(APoint(50, 50, 0), "Attributed_Block_1", 1, 1, 1, 0)

    # Properties
    set_and_get_properties(br)
        
    #print("▶ 선, 원 및 텍스트 추가 완료.")

    # 화면 갱신(Update) — 일부 버전에서는 자동 수행되지만 수동 호출도 가능
    acad.app.Update()
    #print("▶ 화면 업데이트 완료.")

    # Zoom All (전체 보기)
    #acad.app.ZoomAll()
    #print("▶ Zoom All 완료.")

    # ZoomExtents
    acad.app.ZoomExtents()
    #print("▶ Zoom Extents 완료.")


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
