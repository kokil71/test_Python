# https://www.supplychaindataanalytics.com/rectangular-arrays-in-autocad-using-pyautocad-python/
# Rectangular AutoCAD arrays in pyautocad

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble

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
    
    # Creating an object
    #To create an array I will draw a rectangle using the AddPolyline method to use it as a base object.
    sqp = aDouble(50, 150, 0, 50, 550, 0, 850, 550, 0, 850, 150, 0, 50, 150, 0)
    sq1 = acad.model.AddPolyline(sqp)

    # Working with the ArrayRectangular method
    # Now I will create a rectangular array. But before creating the same I explain how pyautocad creates the rectangular array based on the parameters that we pass on to the respective method.
    # Let us check out the syntax of the ArrayRectangular method:
    # Syntax: object.ArrayRectangular(NumberOfRows, NumberOfColumns, NumberOfLevels, DistBetweenRows, DistBetweenColumns, DistBetweenLevels)

    # Levels are 3D parameters. We use that to create layers of array along z axis. We set NumberOfLevels parameter to 1 always as we need to create the array on x, y plane.
    # The object in the selection set is assumed to be in the lower left-hand corner, and the array is generated up and to the right when the object is created.
    # For instance, let’s create an array from the rectangle we have already created.
    arr1 = sq1.ArrayRectangular(5, 5, 1, 100, 100, 0)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    # Creating array using boundaries as base
    # Now, we will write a simple code to use the boundaries of objects as a base for creating array offsets for the rectangle.
    # 이제 사각형의 배열 오프셋을 생성하기 위한 기준으로 객체의 경계를 사용하는 간단한 코드를 작성해보겠습니다.
    def array_rectangle(x, y, z, r, c, lr, dr, dc, dl):
        l=int(input("Enter length of rectangle:"))
        w=int(input("Enter width of rectangle:"))
        rect = (x, y, z, x, y+w, z, x+l, y+w, z, x+l, y, z, x, y, z)
        rec = acad.model.AddPolyline(aDouble(rect))
        arr = rec.ArrayRectangular(r, c, lr, dr+w, dc+l, dl)

    # In this code, we have to pass x, y, z coordinates as the base point for creating the rectangle. After that we will add the same set of parameters as mentioned in the command syntax.
    # Now, let us see how the array gets created after passing parameters in this code.
    # 이 코드에서는 사각형을 생성하기 위한 기준점으로 x, y, z 좌표를 전달해야 합니다. 그 후 명령 구문에 언급된 것과 동일한 매개변수 집합을 추가합니다.
    # 이제 이 코드에서 매개변수를 전달한 후 배열이 어떻게 생성되는지 살펴보겠습니다.
    array_rectangle(50, 150, 0, 3, 3, 1, 150, 250, 0)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
