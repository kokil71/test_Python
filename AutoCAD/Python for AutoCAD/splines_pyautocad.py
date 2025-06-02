# https://www.supplychaindataanalytics.com/drawing-splines-in-autocad-with-pyautocad-python/
# Drawing AutoCAD splines with pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
#from math import pi

def connect_autocad():
    acad_app = None
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
        if acad_app is not None:
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

    # To create a AutoCAD spline object with pyautocad we need to pass the points which we want to connect using the spline.
    # Hence, we need to use a method called “aDouble”, which we have used previously while creating polylines in one of our previous blogs.
    p1 = aDouble(0, 0, 0, 42, 25, 0, 100, -15, 0, 155, 45, 0)

    # As you can see, I have passed 4 points in the form of (x, y, z) format.
    # Now, to attach these points with spline, we need to pass these points along with tangent points to the AddSpline command.
    # Syntax:
    # object.AddSpline(PointsArray, StartTangent, EndTangent)
    # PointsArray: An array of 3D coordinates defining the spline curve. At least two points (six elements) are required for constructing a Spline object. The array size must be in multiples of three.
    # 포인트 배열: 스플라인 곡선을 정의하는 3D 좌표 배열입니다. Spline 객체를 생성하려면 최소 두 개의 점(요소 6개)이 필요합니다. 배열 크기는 3의 배수여야 합니다.
    # StartTangent: A 3D vector specifying the tangency of the spline curve at the first point.
    # 시작 탄젠트: 첫 번째 지점에서 스플라인 곡선의 접선을 지정하는 3D 벡터입니다.
    # EndTangent: A 3D vector specifying the tangency of the spline curve at the last point.
    # 끝 탄젠트: 마지막 지점에서 스플라인 곡선의 접선을 지정하는 3D 벡터입니다.
    # Let’s draw a spline now.
    sp1 = acad.model.AddSpline(p1, APoint(2, 2, 0), APoint(50, 75, 0))

    # Python properties of a AutoCAD spline object in pyautocad
    # To utilize the objects for various purposes, we need to know the properties of the objects in depth.
    # Hence, we will start going through some of the properties of the spline.
    # We can use, closed & closed2 methods to check whether the line is closed in 2D space or 3D space respectively.
    print(sp1.Closed)
    print(sp1.Closed2)

    # We can also find control points, with the help of which the spline curve is sketched.
    # Technically, the control point is a member of a set of points used to determine the shape of a spline curve.
    # Let’s check the output for the same first.
    print(sp1.ControlPoints)
    print("Number of control points: " + str(sp1.NumberOfControlPoints))

    # To make this more understandable, we will connect these control points and see the results.
    # To get the degree of the spline’s polynomial representation we can use Degree or Degree2 which works for 2D & 3D respectively.
    print(sp1.Degree)
    print(sp1.Degree2)

    # We can also find the start and end tangents of the spline:
    print(sp1.StartTangent)
    print(sp1.EndTangent)

    # To print the fit points attaching which the spline has been drawn using the FitPoints property:
    print(sp1.FitPoints)
    print("Number of fit points: " + str(sp1.NumberOfFitPoints))

    time.sleep(0.5)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # So fit points are basically the points which we have passed to draw the spline attaching those specific points.
    # We can also set tolerance for the fit points using the FitTolerance property:
    sp1.FitTolerance = 15

    # If we set the fit point tolerance as mentioned above, we will get a curve within that tolerance limit.
    # Let’s draw the curve and check its properties:
    # Figure 2.2: Spline with fit point tolerance set to 15
    print(sp1.Closed)
    print(sp1.Closed2)
    print("Control Points:")
    print(sp1.ControlPoints)
    print(sp1.Degree)
    print(sp1.Degree2)
    print(sp1.StartTangent)
    print(sp1.EndTangent)
    print(sp1.FitPoints)
    print(sp1.FitTolerance)

    # Other properties of AutoCAD spline object
    # Along with the above-mentioned properties, we can also find some other properties with the attribute names listed below:
    print(sp1.IsPeriodic)
    print(sp1.IsPlanar)
    print(sp1.IsRational)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()