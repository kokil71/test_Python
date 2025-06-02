import win32com.client
import time
import os

def connect_autocad():
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
    except:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        acad.Visible = True
        time.sleep(2)
    return acad

def select_entity():
    acad = connect_autocad()
    doc = acad.ActiveDocument
    
    try:
        ss = doc.SelectionSets.Item("SS1")
        ss.Clear()
    except:
        ss = doc.SelectionSets.Add("SS1")
    
    print("📌 객체를 선택하세요 (하나 선택 후 Enter):")
    ss.SelectOnScreen()
    
    if ss.Count == 0:
        print("선택된 객체가 없습니다.")
        return None
    
    entity = ss.Item(0)
    print(f"선택된 객체 유형: {entity.ObjectName}")
    return entity

if __name__ == "__main__":
    #select_entity()

    font_path = os.path.join(os.environ["WINDIR"], "Fonts")
    print(f"Windows 폰트 폴더 경로: {font_path}")
