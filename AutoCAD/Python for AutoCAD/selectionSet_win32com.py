# https://www.supplychaindataanalytics.com/selectionset-object-in-autocad-with-python/
# SelectionSet object in AutoCAD with Python

#Preparing the code for this AutoCAD example
#For this coding example I am using the pythoncom and win32com modules. These modules initiate my application and perform various different tasks.

import win32com.client
import pythoncom
import win32gui
import time
#from pyautocad import Autocad, APoint, aDouble

def APoint(x, y, z = 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

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
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return
    else:
        # 현재 도면과 모델 공간 객체 접근 ActiveDocument : win32com
        doc = acad.ActiveDocument
        acad_model = doc.ModelSpace
        acad_app = acad.Application

    # The SelectionSet AutoCAD object
    # First, let me explain the SelectionSet object in AutoCAD. A SelectionSet object simply refers to the set of items that I select in AutoCAD. While using AutoCAD I usually select items by creating a window around objects that I want to select from the drawing. In that case I usually do so by using the mouse. Different objects require SelectionSet as a reference object to perform different activities. Lets understand how to create SelectionSet object in Python.
    # Creating a SelectionSet AutoCAD object in Python
    # In this coding example, I will try to create two lines using the AddLine method. I add these two lines to a SelectionSet object.
    l1 = acad_model.AddLine(APoint(0, 0, 0),APoint(1000, 1000, 0))
    l2 = acad_model.AddLine(APoint(1000, 1000, 0),APoint(2000, 0, 0))
    # Now, I can create a SelectionSet object with the name “SS1” using the Add method. I use that method on the SelectionSets object. This SelectionSets object is a collection of all SelectionSet objects present inside the Document object.
    # To know more about the Document object and other AutoCAD objects, do check out my other Blog posts.    
    try:
        ss1 = doc.SelectionSets.Item("SS1")     # 기존에 있으면 가져오기
        ss1.Delete()                            # 삭제
    except Exception:
        pass                                    # 없으면 무시
    ss1 = doc.SelectionSets.Add("SS1")          # 새로 생성

    # The SelectionSet object takes an array of objects as input parameter. Those are the objects that are to be added to the SelectionSet. To do so, I use the AddItems method on the SelectionSet object to pass the created lines as input values. See below code.
    ss1.AddItems(aVariant([l1, l2]))
    # To confirm whether the SelectionSet is created and whether the two objects are present in the SelectionSet or not I can use two methods: Name and Count.
    print(ss1.Name)
    print(ss1.Count)

    # Methods of the SelectionSet AutoCAD object
    # There are also a few other methods that can be used to perform various different tasks on a SelectionSet object. For instance, Clear, Delete, Erase, Highlight, Item, RemoveItems, SelectOnScreen.
    # From the method mentioned above, the Item method can be used to fetch the Item present at a given index in a Collection, Group or SelectionSet.
    print(ss1.Item(0).ObjectName)

    # SelectionSet 또는 SelectionSet의 항목을 삭제하려면 Clear, Delete, Erase 또는 Remove Items 메서드를 사용할 수 있습니다. 이러한 메서드의 기능은 다음과 같습니다.
    # Clear:  이 메서드는 SelectionSet을 비웁니다. SelectionSet 객체는 여전히 존재하지만 항목을 포함하지 않습니다. 이전에 선택 영역에 있던 항목은 여전히 ​​존재하지만 더 이상 SelectionSet에 존재하지 않습니다.
    # RemoveItems:  이 메서드는 SelectionSet에서 하나 이상의 항목을 제거하는 데 사용됩니다. 제거된 항목은 여전히 ​​존재하지만, 더 이상 SelectionSet에 존재하지 않습니다.
    # Erase:  이 메서드는 SelectionSet의 모든 항목을 삭제합니다. SelectionSet 객체는 여전히 존재하지만 항목을 포함하지 않습니다. 이전에 SelectionSet에 있던 항목은 더 이상 존재하지 않습니다.
    # Delete:  SelectionSet 객체를 삭제하지만, SelectionSet에 포함된 객체는 삭제하지 않습니다. Delete 메서드 호출 후 SelectionSet 자체는 더 이상 존재하지 않지만, 이전에 SelectionSet에 포함된 항목은 여전히 ​​존재합니다.

    # From the methods listed above only RemoveItems method requires parameters to be passed. 
    # For example, from the lines that I have added to SelectionSet I want to remove Line2 (l2). I must pass l2 as an element of the array of the Items list that I want to remove from the SelectionSet.
    ss1.RemoveItems(aVariant([l2]))
    print(ss1.Count)

    # Sometimes I want to select objects using the conventional method only. I.e. dragging/drawing a window around the objects that I want to select using my mouse. Python also allows me to do so using the SelectOnScreen method.
    ss1.SelectOnScreen()
    
    # Once I apply the method as shown above, the code waits for AutoCAD user to select objects. Upon selecting the objects the AutoCAD user needs to press Enter on the keyboard. This will finalize the selection. The code then eventually moves ahead.

    # Group object in AutoCAD using Python
    # The Group object is a named SelectionSet object. Since is does not contain any special methods I have added this small introductory section for the purpose of discussing the Group object.
    # I can add the Group object similarly to how I added the SelectionSet object. I.e. by using the Add method. Obviously, here I need to use the Groups collection object to Add a Group.
    # Also, to add items to the created Group object I can use the AppendItems method. I can perform the task similarly to how I did with the AddItems method for the SelectionSet object.
    # In addition to that here follows a list of various different methods and properties that can be used to perform activities on AutoCAD Group objects:
    # Delete / GetExtensionDictionary / Highlight / Item / RemoveItems / Update / Count / Document / Handle / HasExtensionDictionary / Layer / Linetype / LinetypeScale
    # Lineweight / Material / Name / ObjectID / ObjectName / OwnerID / PlotStyleName / TrueColor / Visible

    # 화면 갱신
    acad_app.Update()
    acad_app.ZoomExtents()



if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()