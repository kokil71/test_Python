# https://www.supplychaindataanalytics.com/autocad-block-object-in-python/
# AutoCAD Block object in Python

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
import time
import win32gui
import win32com.client

from pickle import TRUE
from pyautocad import Autocad, APoint, aDouble

def connect_autocad():
    try:
        # 실행 중인 AutoCAD 인스턴스에 연결
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")        
        #hwnd = win32gui.FindWindow(None, acad_app.Caption)
        #bring_autocad_to_front(hwnd)
        print("✅ AutoCAD 실행 중입니다.")
        return Autocad(create_if_not_exists=False)
    except Exception:
        print("❌ 실행 중인 AutoCAD 없음. 새 인스턴스를 시작합니다.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            acad_app.Visible = True
            time.sleep(3)  # 로딩 대기
            print("✅ 새 AutoCAD 인스턴스 시작 완료.")
            return Autocad(create_if_not_exists=False)
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
            print("✅ AutoCAD 창을 전면으로 전환 완료.")
        else:
            print("❌ AutoCAD 창을 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류:", e)

def set_and_get_properties(b1, block_ref1):
    # properties
    print("Object Name: " + b1.ObjectName)
    print("Name of Block: " + b1.Name)
    print("Native units of measures for the Block: ", end="")
    print(b1.Units)
    print("Is scaling allowed for the Block ? ", end="")
    print(b1.BlockScaling)
    print("Is the Block explodable ? ", end="")
    print(b1.Explodable)
    print("Is the Block dynamic ? ", end="")
    print(b1.IsDynamicBlock)
    
    # properties of BlockReference
    print("Object Name: " + block_ref1.ObjectName)
    print("Block Name: " + block_ref1.Name)
    print("Original Block Name: " + block_ref1.EffectiveName)
    print("Entity Transparency: ", end="")
    print(block_ref1.EntityTransparency)
    print("Does the Block contain any Attributes: ", end="")
    print(block_ref1.HasAttributes)
    print("Insertion Point: ", end="")
    print(block_ref1.InsertionPoint)
    print("Insert units saved with Blocks: ", end="")
    print(block_ref1.InsUnits)
    print("Conversion factor between Block units and drawing units: ", end="")
    print(block_ref1.InsUnitsFactor)
    print("Is the Block dynamic ? ", end="")
    print(block_ref1.IsDynamicBlock)
    print("Layer: " + block_ref1.Layer)
    print("Line type: " + block_ref1.Linetype)
    print("Line type scale: ")
    print(block_ref1.LinetypeScale)
    print("Line weight: ")
    print(block_ref1.Lineweight)
    print("Rotation angle for the block: ")
    print(block_ref1.Lineweight)
    #Scale factors
    print("X Scale factor of block: ", end="")
    print(block_ref1.XEffectiveScaleFactor)
    print("X Scale factor for block or external reference (xref): ", end="")
    print(block_ref1.XScaleFactor)
    print("Y Scale factor of block: ", end="")
    print(block_ref1.YEffectiveScaleFactor)
    print("Y Scale factor for block or external reference (xref): ", end="")
    print(block_ref1.YScaleFactor)
    print("Z Scale factor of block: ", end="")
    print(block_ref1.ZEffectiveScaleFactor)
    print("Z Scale factor for block or external reference (xref): ", end="")
    print(block_ref1.ZScaleFactor)


def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD 연결이 안 되어 종료합니다.")
        return

    # 모델 공간에 객체 추가
    # flow
    # Document > BlocksCollection > Block > BlockReference

    # insertion point for block
    ip = APoint(0, 0, 0)

    # adding block to documents block collection
    b1 = acad.doc.Blocks.Add(ip, "Test_block_1")

    # adding geometries to block
    pl = b1.AddPolyline(aDouble(0, 0, 0, 10000, 0, 0, 10000, 5000, 0, 0, 5000, 0, 0, 0, 0))
    l = b1.AddLine(APoint(0, 250, 0), APoint(10000, 250, 0))

    # adding block instance to drawing (creating a reference to the block)
    block_ref1 = acad.model.InsertBlock(APoint(50, 50, 0), "Test_block_1", 1, 1, 1, 0)

    # Properties
    set_and_get_properties(b1, block_ref1)
        
    #print("▶ 선, 원 및 텍스트 추가 완료.")

    # 화면 갱신(Update) — 일부 버전에서는 자동 수행되지만 수동 호출도 가능
    acad.app.Update()
    #print("▶ 화면 업데이트 완료.")

    # Zoom All (전체 보기)
    #acad.app.ZoomAll()
    #print("▶ Zoom All 완료.")

    # ZoomExtents
    acad.app.ZoomExtents()
    #print("▶ Zoom Extents 완료.")


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM 초기화
    acad = connect_autocad()    
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()
