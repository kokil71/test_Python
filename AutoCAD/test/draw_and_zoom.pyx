#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#import pythoncom
#from pyautocad import Autocad, APoint
#import win32com.client

# mymath.pyx
# c에서 접근 가능한 함수로 선언

cdef public int draw_and_zoom(Application  &acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return 0

    # 모델 공간에 객체 추가
    p1 = APoint(0, 0)
    p2 = APoint(200, 150)
    line = acad.model.AddLine(p1, p2)
    circle = acad.model.AddCircle(p1+p2,100)
    text = acad.model.AddText("Zoomed Line", APoint(100, 100), 10)    

    # 화면 갱신(Update) 일부 버전에서는 자동 수행되지만 수동 호출도 가능
    acad.app.Update()
    print("▶ 화면 업데이트 완료.")

    # ZoomExtents (전체 보기)
    acad.app.ZoomExtents()
    print("▶ Zoom Extents 완료.")

	return 1
