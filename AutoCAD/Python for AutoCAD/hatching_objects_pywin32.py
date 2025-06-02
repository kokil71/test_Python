# https://www.supplychaindataanalytics.com/hatching-objects-on-autocad-template-using-pywin32-python/
# Hatching objects in AutoCAD with pywin32

# Setting up environment using pywin32 module

import pythoncom
import win32gui
import win32com.client
import time
from math import pi
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

def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return
    else:
        # 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
        doc = acad.ActiveDocument
        acad_model = doc.ModelSpace
        acad_app = acad.Application

    # Creating loop of objects in AutoCAD
    #out_loop = []
    #sq = acad_model.AddPolyline(aDouble(0,0,0,1000,0,0,1000,1000,0,0,1000,0))            
    #sq = acad_model.AddPolyline(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [0,0,0,1000,0,0,1000,1000,0,0,1000,0]))    
    sq_Plist = aDouble(0,0,0,1000,0,0,1000,1000,0,0,1000,0)
    sq = acad_model.AddPolyline(sq_Plist)    
    #arc = acad_model.AddArc(APoint(0, 500, 0), 500, 90*pi/180, 270*pi/180)
    #arc = acad_model.AddArc(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [0, 500, 0]), 500, 90*pi/180, 270*pi/180)
    arc_plist = aDouble(0, 500, 0)
    arc = acad_model.AddArc(arc_plist, 500, 90*pi/180, 270*pi/180)

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()

    #out_loop.append(sq)
    #out_loop.append(arc)

    #outer = variants(out_loop)
    #outer = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [out_loop])
    #outer = variants(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, out_loop)
    outer = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [sq, arc])

    # Creating hatch object and appending the hatch
    # object.AddHatch(PatternType, PatternName, Associativity)
    hatch = acad_model.AddHatch(0, "ANSI37", True)    

    #Now to add this hatch to the loop we have created, we will use the AppendOuterLoop method.
    hatch.AppendOuterLoop(outer)

    print(hatch.HatchStyle)
    print(hatch.PatternName)
    print(hatch.AssociativeHatch)

    print(round(hatch.Area,2))
    print(hatch.PatternAngle)
    print(hatch.PatternDouble)
    print(hatch.PatternScale)
    print(hatch.PatternSpace)
    print(hatch.PatternType)
    print(hatch.NumberOfLoops)

    # Now, let’s change the pattern scale to 10.
    hatch.PatternScale = 10

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()

    # Adding inner loop to hatched AutoCAD object loop
    #in_loop = []
    #in_loop.append(acad_model.AddCircle(APoint(250, 250, 0), 100))    
    #inner = variants(in_loop)
    
    #circle = acad_model.AddCircle(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [250, 250, 0]), 100)
    circle_Plist = aDouble(250, 250, 0)
    circle = acad_model.AddCircle(circle_Plist, 100)
    inner = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [circle])

    hatch.AppendInnerLoop(inner)

    print(round(hatch.Area,2))

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()

# Creating necessary constructors using pywin32 & pythoncom
def aDouble(*argv):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (argv))

def variants(object):
#def variants(typeVar, object):    
    #return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (object))    
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, [object])
    #return win32com.client.VARIANT(typeVar, [object])


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad() 
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
