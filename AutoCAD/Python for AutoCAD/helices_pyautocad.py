# https://www.supplychaindataanalytics.com/working-with-helices-in-autocad-using-pyautocad-python/
# Helices in AutoCAD with pyautocad (Python)

import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, aDouble
#from math import pi

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

    # Creating a AutoCAD helix object with pyautocad in Python
    # Unlike other AutoCAD objects such as AutoCAD lines, AutoCAD polylines, AutoCAD arcs, AutoCAD ellipses, etc. we do not have any method provided by pyautocad to draw a helix.
    # So, we can only fetch properties of the pre-created helix.
    # Let’s draw a helix first.
    # As you can see from Figures 1.1 & 1.2, I have created a helix with the below-mentioned properties:
    # Top Radius: 250 units / Bottom Radius: 200 units / Center: (2000, 1500) / Height: 100 units

    # Storing a AutoCAD helix object in a variable
    # As we cannot create a helix using pyautocad, we do not have a variable assigned to the helix which has been created on the AutoCAD template.
    # In this case, we can utilize a wonderful method provided by pyautocad, i.e. iter_objects.
    # With this, we can iterate through all the previously created objects from the AutoCAD template.
    # As per pyautocad, the type of a helix object is “AcDbHelix”, which can be found out using the “ObjectName” property against the created drawing.
    # So, through a combination of this iter_objects method and filtering out the helix with its “ObjectName” (which is “AcDbHelix”) we can store it in a variable while implementing “for loop”, eventually using # it to fetch the properties of the helix.
    # Let us implement the loop now, to filter out helix from the template:
    
    # ith its “ObjectName” (which is “AcDbHelix”) we can store it in a variable while implementing “for loop”, eventually using it to fetch the properties of the helix.
    # Let us implement the loop now, to filter out helix from the template:
    # def helix():
    #    obj = acad.iter_objects(limit=None, block=acad.doc.Layouts.item(2).Block)
    #    for obj in obj:
    #        print("Type of object: " + obj.ObjectName)
    #        if obj.ObjectName == "AcDbHelix":
    # ...
    # Syntax for “iter_objects”:
    # iter_objects(object_name_or_list=None, block=None, limit=None, dont_cast=False)
    # Parameters:
    # object_name_or_list – part of object type name, or list of it
    # object_name_or_list – 객체 유형 이름의 일부 또는 해당 목록
    # block – Autocad template, default – ActiveDocument.ActiveLayout.Block
    # block – Autocad 템플릿, 기본값 – ActiveDocument.ActiveLayout.Block
    # limit – max number of objects to return, default infinite
    # limit – 반환할 최대 객체 수, 기본값은 무한대
    # To make things work a little faster by iterating only through the “AcDbHelix” object, we can pass the parameter “object_name_or_list” as:
    # def helix():
    #     obj = acad.iter_objects(object_name_or_list= "AcDbHelix", limit=None, block=acad.doc.Layouts.item(2).Block)
    #    for obj in obj:
    # ...
    # This will store the helix object in the variable obj and we can fetch properties of the helix by applying different methods against that variable.
    # AutoCAD helix properties
    # Let’s fetch properties of our helix now:
    print("Top radius of helix: " + str(round(obj.TopRadius,2)))
    print("Base radius of helix: " + str(round(obj.BaseRadius,2)))
    print("Helix constrain: " + str(round(obj.constrain,2)))
    print("Height of helix: " + str(round(obj.Height,2)))
    print("Center point of helix: ")
    print(obj.Position)
    print("Total length of helix: " + str(round(obj.TotalLength,2)))
    print("Number fo turns helix took to complete: " + str(round(obj.Turns,2)))
    print("Slope of turns: " + str(round(obj.TurnSlope,2)))
    print("Height of single turn: " + str(round(obj.TurnHeight,2)))
    print("Twist of the helix: " +  str(round(obj.Twist,2)))

    # Editing the newly created AutoCAD helix object using pyautocad
    # Although we cannot create a helix using pyautocad, we can definitely edit the previously created helix.
    # Let’s change the center point of the helix.
    # We can use the Move method to move objects from one point to another.
    # Syntax:
    # object.Move(<current location>, <new location>)
    # obj.Move(APoint(obj.Position), APoint(1500, 1000))
    # Now, we will change some other properties too and, let’s see what happens.
    obj.TopRadius = 450
    obj.BaseRadius = 700
    obj.Height = 500
    obj.Twist = 1
    #Let’s run the code now and print the properties again.

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()


if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
