import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


import pythoncom
from pyautocad import Autocad, APoint
import win32com.client
import time

def connect_autocad():
    try:
        # 이미 실행 중인 AutoCAD에 연결 시도
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        print("✅ AutoCAD가 실행 중입니다. 연결 성공.")
        return Autocad(create_if_not_exists=False)
    except Exception as e:
        print("❌ AutoCAD가 실행 중이지 않습니다.")
        print("▶ 새로운 AutoCAD 인스턴스를 실행합니다...")
        try:
            acad = win32com.client.Dispatch("AutoCAD.Application")
            acad.Visible = True  # AutoCAD를 화면에 표시
            # AutoCAD가 완전히 로딩될 때까지 대기
            time.sleep(3)
            print("✅ AutoCAD 인스턴스 생성 및 연결 완료.")
            return Autocad(create_if_not_exists=False)
        except Exception as e:
            print("🚫 AutoCAD 실행 또는 연결에 실패했습니다.")
            print("오류:", e)
            return None

def draw_sample(acad):
    if acad is None:
        print("AutoCAD와 연결되어 있지 않습니다. 종료합니다.")
        return

    # 좌표 설정
    p1 = APoint(0, 0)
    p2 = APoint(300, 300)

    # 선 그리기
    line = acad.model.AddLine(p1, p2)
    print("▶ 선을 그렸습니다:", p1, "->", p2)

    # 텍스트 삽입
    acad.model.AddText("Hello AutoCAD!", APoint(150, 150), 10)
    print("▶ 텍스트 삽입 완료.")    

if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화 (필수)
    acad = connect_autocad()
    draw_sample(acad)
    pythoncom.CoUninitialize()
