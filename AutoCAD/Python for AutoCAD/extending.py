# https://www.supplychaindataanalytics.com/extending-the-objects-in-autocad-using-pyautocad-python/
# Extending AutoCAD objects with pyautocad

import pythoncom
import win32gui
import win32com.client
import time
import math
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

def split_tuple(t):
    return [t[i:i+3] for i in range(0, len(t), 3)]
# Extending objects based on the acExtendThisEntity parameter in IntersectWith pyautocad-method
# condition 1: acExtendThisEntity
def extend(obj1, obj2):
    if obj1.IntersectWith(obj2, 1) > (0, 0, 0):
        intersection_points = split_tuple(obj1.IntersectWith(obj2, 1))
        if len(intersection_points) == 0:   
            print("Condition 1 satisfies ", end="")
            print(split_tuple(obj1.IntersectWith(obj2, 1)))
            if math.dist(obj1.EndPoint, split_tuple(obj1.IntersectWith(obj2, 1))) < math.dist(obj1.StartPoint, split_tuple(obj1.IntersectWith(obj2, 1))):
                obj1.EndPoint = APoint(intersection_points[0])
            else:
                obj1.StartPoint = APoint(intersection_points[0])
        else:   
            print("Condition 1 satisfies ", end="")
            print(split_tuple(obj1.IntersectWith(obj2, 1)))
            end_point_index = int(input("There are more than one intersection points, please select the index value of specific intersection point: "))
            if math.dist(obj1.EndPoint, APoint(intersection_points[end_point_index])) < math.dist(obj1.StartPoint, APoint(intersection_points[end_point_index])):
                obj1.EndPoint = APoint(intersection_points[end_point_index])
            else:
                obj1.StartPoint = APoint(intersection_points[end_point_index])                
# Extending objects based on acExtendOtherEntity parameter in IntersectWith method (pyautocad)
# condition 2: acExtendOtherEntity
    elif obj1.IntersectWith(obj2, 2) > (0, 0, 0):
        intersection_points = split_tuple(obj1.IntersectWith(obj2, 2))
        if len(intersection_points) == 0:   
            print("Condition 2 satisfies ", end="")
            print(split_tuple(obj1.IntersectWith(obj2, 2)))
            if math.dist(obj2.EndPoint, split_tuple(obj1.IntersectWith(obj2, 2))) < math.dist(obj1.StartPoint, split_tuple(obj1.IntersectWith(obj2, 2))):
                obj2.EndPoint = APoint(intersection_points[0])
            else:
                obj2.StartPoint = APoint(intersection_points[0])            
        else:   
            print("Condition 2 satisfies ", end="")
            print(split_tuple(obj1.IntersectWith(obj2, 2)))
            end_point_index = int(input("There are more than one intersection points, please select the index value of specific intersection point: "))
            if math.dist(obj2.EndPoint, APoint(intersection_points[end_point_index])) < math.dist(obj2.StartPoint, APoint(intersection_points[end_point_index])):
                obj2.EndPoint = APoint(intersection_points[end_point_index])
            else:
                obj2.StartPoint = APoint(intersection_points[end_point_index])
# Extending object based on acExtendBoth parameter in IntersectWith method (pyautocad)
# condition 3: acExtendBoth 
    elif obj1.IntersectWith(obj2, 3) > (0, 0, 0):
        intersection_points = obj1.IntersectWith(obj2, 3)
        print("Condition 3 satisfies ", end="")
        print(obj1.IntersectWith(obj2, 3))
        obj1.EndPoint = APoint(intersection_points)
        obj2.EndPoint = APoint(intersection_points)

# if objects are not intersecting each other.
    else:
        print("The objects does not intersect each other.")
import math
from pyautocad import APoint

def split_tuple(t):
    return [t[i:i+3] for i in range(0, len(t), 3)]

def extend_ChatGPT(obj1, obj2):
    for mode in [1, 2, 3]:  # 1: None, 2: ExtendOtherEntity, 3: ExtendBoth
        points_raw = obj1.IntersectWith(obj2, mode)
        points = split_tuple(points_raw)

        if len(points) == 0:
            continue  # No intersection found in this mode

        print(f"Condition {mode} satisfies", points)

        # 선택 지점 결정
        if len(points) == 1:
            selected_point = points[0]
        else:
            for idx, pt in enumerate(points):
                print(f"[{idx}]: {pt}")
            end_point_index = int(input("Select index of intersection point: "))
            selected_point = points[end_point_index]

        # 확장 대상 결정
        if mode == 1:
            target = obj1
        elif mode == 2:
            target = obj2
        else:  # mode == 3
            obj1.EndPoint = APoint(selected_point)
            obj2.EndPoint = APoint(selected_point)
            return

        # 거리 비교 후 시작점 또는 끝점 확장
        dist_start = math.dist(target.StartPoint, selected_point)
        dist_end = math.dist(target.EndPoint, selected_point)

        if dist_end < dist_start:
            target.EndPoint = APoint(selected_point)
        else:
            target.StartPoint = APoint(selected_point)
        
        return  # 교차 지점이 하나라도 처리되면 함수 종료

    print("No intersection found in any mode.")

def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # Implementing the extend method created using pyautocad
    c1 = acad.model.AddCircle(APoint(1000, 750), 200)
    l1 = acad.model.AddLine(APoint(1255, 1000, 0), APoint(1555, 1550, 0))

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

    #extend(c1, l1) 
    extend_ChatGPT(c1, l1)

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()