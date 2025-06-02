import pythoncom
import win32com.client
import win32gui
import time
from math import pi

def APoint(x, y, z=0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [x, y, z])

def bring_autocad_to_front(acad):
    hwnd = win32gui.FindWindow(None, acad.Caption)
    if hwnd:
        win32gui.ShowWindow(hwnd, 5)
        win32gui.SetForegroundWindow(hwnd)

def connect_autocad():
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
    except:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        acad.Visible = True
        time.sleep(3)
    bring_autocad_to_front(acad)
    return acad

def draw_and_operate(acad):
    doc = acad.ActiveDocument
    model = doc.ModelSpace

    # 좌표는 반드시 VARIANT 배열로 전달해야 함
    c1 = model.AddCircle(APoint(100, 100), 100)
    l1 = model.AddLine(APoint(100, 100), APoint(300, 350))
    el1 = model.AddEllipse(APoint(250, 300), APoint(100, 50), 0.5)

    time.sleep(0.5)
    acad.Update()
    doc.SendCommand("ZOOM E ")

    # 복사 및 이동
    c2 = c1.Copy()
    c2.Move(APoint(100, 100), APoint(300, 300))

    time.sleep(0.5)
    acad.Update()
    doc.SendCommand("ZOOM E ")

    # 회전
    l2 = l1.Copy()
    l2.Rotate(APoint(100, 100), pi / 2)

    time.sleep(0.5)
    acad.Update()
    doc.SendCommand("ZOOM E ")

    # 오프셋
    offsets = el1.Offset(10)
    for offset in offsets:
        pass

    time.sleep(0.5)
    acad.Update()
    doc.SendCommand("ZOOM E ")

    # 스케일링
    c2.ScaleEntity(APoint(300, 300), 0.5)

    time.sleep(0.5)
    acad.Update()
    doc.SendCommand("ZOOM E ")

if __name__ == "__main__":
    pythoncom.CoInitialize()
    try:
        acad = connect_autocad()
        draw_and_operate(acad)
    finally:
        pythoncom.CoUninitialize()
