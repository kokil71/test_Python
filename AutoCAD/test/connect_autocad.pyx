import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
from pyautocad import Autocad, APoint
import win32com.client


cdef connect_autocad():
    try:
        # ���� ���� AutoCAD �ν��Ͻ��� ����
        acad_app = win32com.client.GetActiveObject("AutoCAD.Application")
        print("AutoCAD ���� ���Դϴ�.")
        return Autocad(create_if_not_exists=False)
    except Exception:
        print("���� ���� AutoCAD ����. �� �ν��Ͻ��� �����մϴ�.")
        try:
            acad_app = win32com.client.Dispatch("AutoCAD.Application")
            acad_app.Visible = True
            time.sleep(3)  # �ε� ���
            print("�� AutoCAD �ν��Ͻ� ���� �Ϸ�.")
            return Autocad(create_if_not_exists=False)
        except Exception as e:
            print("AutoCAD ���� ����:", e)
            return None


def draw_and_zoom(acad):
    if acad is None:
        print("AutoCAD ������ �� �Ǿ� �����մϴ�.")
        return

    # �� ������ ��ü �߰�
    

    # ȭ�� ����(Update) ? �Ϻ� ���������� �ڵ� ��������� ���� ȣ�⵵ ����
    acad.app.Update()
    print("�� ȭ�� ������Ʈ �Ϸ�.")

    # ZoomExtents (��ü ����)
    acad.app.ZoomExtents()
    print("�� Zoom Extents �Ϸ�.")


if __name__ == "__main__":
    pythoncom.CoInitialize()  # COM �ʱ�ȭ
    acad = connect_autocad()
    draw_and_zoom(acad)
    pythoncom.CoUninitialize()