# https://www.supplychaindataanalytics.com/working-with-3d-mesh-object-in-autocad-using-pyautocad-python/
# 3D mesh object in AutoCAD with win32com

import pythoncom
import win32gui
import win32com.client
import time
#from pyautocad import Autocad, APoint, aDouble

def connect_autocad():
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


def aDouble(*argv):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (argv))


def draw_and_zoom(acad):    
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return
    else:
        # 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
        doc = acad.ActiveDocument
        acad_model = doc.ModelSpace
        acad_app = acad.Application

    # Significance of 3D mesh representation
    # Adding 3D mesh to AutoCAD templates using pyautocad or pywin32
    # To draw a 3D mesh onto the AutoCAD template it takes a very small command with a few parameters.
    # The syntax of the command is as stated below:
    # object.Add3DMesh(M, N, PointsMatrix)
    # Here, M & N takes an integer input ranging from 2-256 representing the size of the array in (or the number of vertices along) both M & N directions.
    pmatrx = aDouble(10, 1, 3, 10, 5, 5, 10, 10, 3, 15, 1, 0, 15, 5, 0, 15, 10, 0, 20, 1, 0, 20, 5, -1, 20, 10, 0, 25, 1, 0, 25, 5,  0, 25, 10, 0)
    mesh1 = acad_model.Add3DMesh(4, 3, pmatrx)

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()

    # Analysis of the newly created 3D mesh
    pl = acad_model.AddPolyline(pmatrx)

    # Properties of a 3D mesh using win32com
    print("Coordinates of the mesh:", end='')
    print(mesh1.Coordinates)
    print("Is mesh one is closed in M direction: " + str(mesh1.MClose))
    print("Density of mesh in M direction: " + str(mesh1.MDensity))
    print("Number of vertices in M direction: " + str(mesh1.MVertexCount))
    print("Is mesh one is closed in N direction: " + str(mesh1.NClose))
    print("Density of mesh in N direction: " + str(mesh1.NDensity))
    print("Number of vertices in N direction: " + str(mesh1.NVertexCount))

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
