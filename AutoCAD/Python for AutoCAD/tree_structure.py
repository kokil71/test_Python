# https://www.supplychaindataanalytics.com/tree-data-structure-for-autocad-objects-using-python-python/
# Tree structure for AutoCAD and pyautocad
import pythoncom
import win32gui
import win32com.client
import time
from pyautocad import Autocad, APoint, ADouble

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
    # Applying tree data structures when working with pyautocad in Python
    column = TreeNode("Column")

    c1 = TreeNode("Column1")
    c2 = TreeNode("Column2")
    c3 = TreeNode("Column3")
    c4 = TreeNode("Column4")

    column.add_child(c1)
    column.add_child(c2)
    column.add_child(c3)
    column.add_child(c4)   

    c1.add_child(TreeNode(acad.model.AddPolyline(ADouble(0, 0, 0, 100, 0, 0, 100, 100, 0, 0, 100, 0, 0, 0, 0))))
    c2.add_child(TreeNode(acad.model.AddPolyline(ADouble(500, 0, 0, 600, 0, 0, 600, 100, 0, 500, 100, 0, 500, 0, 0))))
    c3.add_child(TreeNode(acad.model.AddPolyline(ADouble(500, 500, 0, 600, 500, 0, 600, 600, 0, 500, 600, 0, 500, 500, 0))))
    c4.add_child(TreeNode(acad.model.AddPolyline(ADouble(0, 500, 0, 100, 500, 0, 100, 600, 0, 0, 600, 0, 0, 500, 0))))

    #column.print_tree()

    # 화면 갱신
    acad.app.Update()
    acad.app.ZoomExtents()

# TreeNode 클래스
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    # function for printing the structure and content of a data tree
    def print_tree(self):
        space = "   " * self.get_level()
        prefix = space + "|--" if self.parent else ""
        print(prefix, end="")
        try:
            print("Area = " +  str(round(self.data.Area,2)))
        except:
            print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()  

if __name__ == "__main__":    
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()