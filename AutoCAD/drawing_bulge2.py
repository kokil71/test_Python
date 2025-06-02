import sys
import os
#sys.path.append("D:\\work\\testPythonToAutoCAD")  # 경로는 본인의 폴더에 맞게 수정
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) # 상대경로로
#from drawing_intersection import *
#from bulge_3P_SEC import *
#from bulge_3P_SME import *
from kko_bulge import *

import win32com.client
import pythoncom
import win32gui
import time
#from pyautocad import Autocad, APoint, aDouble
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
    acad_app = None
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #print("✅ AutoCAD 실행 중입니다.")
        #Autocad(create_if_not_exists=False)                  # pyautocad 연결
        #return Autocad(create_if_not_exists=False)          # pyautocad 연결
        return acad_app                                      # pywin32 연결
    except Exception:
        #print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            #acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            #print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            #Autocad(create_if_not_exists=False)              # pyautocad 연결
            #return Autocad(create_if_not_exists=False)      # pyautocad 연결
            return acad_app                                  # pywin32 연결
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
    try:
        if acad is None:
            print("AutoCAD 연결이 안 되어 종료합니다.")
            return
        else:
            # 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
            doc = acad.ActiveDocument
            acad_model = doc.ModelSpace
            acad_app = acad.Application

        points_2d = [
        (0.00000000, 0.00000000),    
        (15.00000000, 0.00000000),    
        (16.16025404, 8.0),
        (-1.16025404, 8.0),
        (0.00000000, 0.00000000),    
        ]

        flat_points_2d = array('d', [coord for pt in points_2d for coord in pt])
        #safe_array_2d = VARIANT(VT_ARRAY | VT_R8, flat_points_2d)
        safe_array_2d = APoint(flat_points_2d)    

        #pline = ms.AddLightWeightPolyline(safe_array_2d)
        pline = acad_model.AddLightWeightPolyline(safe_array_2d)
        pline.Closed = True

        num_vertices = len(flat_points_2d) // 2
        #num_vertices = len(flat_points_2d) // 3

        print ("len(flat_points_2d)", len(flat_points_2d))
        print ("num_vertices = ", num_vertices)

        #return

        time.sleep(0.5)  # 로딩 대기

        # 화면 갱신
        acad_app.Update()
        acad_app.ZoomExtents()

        #return

        # SetBulgeAt 메서드가 없거나 오류난다면 이 부분은 생략하거나,
        # bulge 적용은 다른 방식으로 해야 함.
        try:
            for i in range(num_vertices - 1):
                if i == 1:
                    #pline.SetBulgeAt(i, 1.0)
                    #pline.SetBulge(i, tan(19.12608458*pi/180.0)) 
                    #start_pt = (-12.13003152, 0.0)
                    #end_pt = (-10.96977748, 8.0)
                    start_pt = (15.00000000, 0.0)
                    end_pt = (16.16025404, 8.0)
                    #center_pt = (10.50654630, 4.73583031)
                    #bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
                    on_arc = (16.88132429, 3.32820094)
                    #bulge_value, arc_angle_deg, direction = calculate_bulge_from_3points(start_pt, on_arc, end_pt)
                    bulge, angle_deg, direction, radius, center = calculate_bulge_from_3points(start_pt, on_arc, end_pt)
                    pline.SetBulge(i, bulge)
                elif i == 2:
                    #pline.SetBulge(i, tan(30.00000000*pi/180.0))
                    #start_pt = (-10.96977748, 8.0)
                    #end_pt = (-28.29028556, 8.0)
                    start_pt = (16.16025404, 8.0)
                    end_pt = (-1.16025404, 8.0)
                    center_pt = (7.5, 3.0)            
                    #bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
                    bulge = calculate_bulge_from_center(start_pt, end_pt, center_pt)
                    pline.SetBulge(i, bulge)
                elif i == 3:
                    #pline.SetBulge(i, tan(19.12608458*pi/180.0))
                    start_pt = (-1.16025404, 8.0)
                    end_pt = (0.0, 0.0)
                    center_pt = (4.49345370, 4.73583031)            
                    #bulge_value, arc_angle_deg, direction = calculate_bulge(start_pt, end_pt, center_pt)   
                    bulge = calculate_bulge_from_center(start_pt, end_pt, center_pt)
                    pline.SetBulge(i, bulge)
                else:
                    #pline.SetBulgeAt(i, 0.0)
                    pline.SetBulge(i, 0.0)
        except AttributeError:
            print("SetBulgeAt 메서드를 사용할 수 없습니다. bulge 설정이 생략됨.")

        print("✅ 2D LightWeightPolyline 생성 완료")

        print(pline.area)

        time.sleep(0.5)  # 로딩 대기

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