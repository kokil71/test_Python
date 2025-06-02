import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
import time
from pyautocad import Autocad, APoint
import win32com.client


def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")
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


def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # 모델 공간에 객체 추가
    p1 = APoint(0, 0)
    p2 = APoint(200, 150)
    line = acad.model.AddLine(p1, p2)
    circle = acad.model.AddCircle(p1+p2,100)
    text = acad.model.AddText("Zoomed Line", APoint(100, 100), 10)

    print("▶ 선, 원 및 텍스트 추가 완료.")

    # 화면 갱신(Update) — 일부 버전에서는 자동 수행되지만 수동 호출도 가능
    acad.app.Update()
    print("▶ 화면 업데이트 완료.")

    # Zoom All (전체 보기)
    #acad.app.ZoomAll()
    #print("▶ Zoom All 완료.")

    # ZoomExtents
    acad.app.ZoomExtents()
    print("▶ Zoom Extents 완료.")


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
