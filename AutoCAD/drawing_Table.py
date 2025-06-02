import sys
import os
#sys.path.append("D:\\work\\testPythonToAutoCAD")  # 경로는 본인의 폴더에 맞게 수정
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) # 상대경로로
#from kko_makeTable import *
from kko_makeTableEA import *

import win32com.client
import pythoncom
import win32gui
import time
from array import array

def APoint(x, y, z = 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))    

def APoint(vObject):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (vObject))    

def aDouble(*xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (xyz))

def aVariant(vObject):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (vObject))

def connect_autocad():
    acad = None
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad = win32com.client.GetActiveObject("AutoCAD.Application")        
        #print("✅ AutoCAD 실행 중입니다.")
        #Autocad(create_if_not_exists=False)                # pyautocad 연결
        #return Autocad(create_if_not_exists=False)         # pyautocad 연결
        return acad                                         # pywin32 연결
    except Exception:
        #print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad = win32com.client.Dispatch("AutoCAD.Application")
            acad.Visible = True
            time.sleep(3)  # 로딩 대기
            #print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            #Autocad(create_if_not_exists=False)            # pyautocad 연결
            #return Autocad(create_if_not_exists=False)     # pyautocad 연결
            return acad                                     # pywin32 연결
        except Exception as e:
            print("🚫 AutoCAD 연결 실패:", e)
            return None
    finally:
        if acad is not None:
            hwnd = win32gui.FindWindow(None, acad.Caption)
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
    try:
        if acad is None:
            print("AutoCAD 연결이 안 되어 종료합니다.")
            return
        else:
            # 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
            doc = acad.ActiveDocument
            acad_model = doc.ModelSpace
            acad_app = acad.Application

        """
        # 엑셀에서 Data 읽어와서 캐드 표 만드는 코드
        excel_file = r"D:\work\makeTable.xlsx"  # 수정 필요
        data = read_excel_data(excel_file)        
        draw_table(acad, data)
        """

        excel_file = r"D:\work\makeTable.xlsx"
        export_file = r"D:\work\exportedTable.xlsx"

        # 1. 엑셀 → AutoCAD 표 생성
        if os.path.exists(excel_file):
            data = read_excel_data(excel_file)
            draw_table(acad, data)
        else:
            print("📂 엑셀 파일이 없어서 AutoCAD 표 생성 생략")

        # 2. AutoCAD 표 선택 → 엑셀 저장
        table = select_table(acad)
        if table:
            export_table_to_excel(table, export_file) 

        # 화면 갱신
        acad_app.Update()
        acad_app.ZoomExtents()

    except Exception as e:
        print("🚫 오류:", e)


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()

