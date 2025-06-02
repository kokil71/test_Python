# acad_control.pyx
# cython: language_level=3

from libc.stdlib cimport malloc, free
import pythoncom
import time
from pyautocad import Autocad, APoint

cpdef int run_draw_and_zoom():
    try:
        acad = Autocad(create_if_not_exists=True)
        p1 = APoint(0, 0)
        p2 = APoint(200, 100)
        line = acad.model.AddLine(p1, p2)
        circle = acad.model.AddCircle(p1 + p2, 100)
        text = acad.model.AddText("Hello AutoCAD", APoint(100, 50), 10)
        acad.app.ZoomExtents()
        #print("Normal running")
        #return 1        
        intRtn = 1
    except Exception as e:
        with open("D:/work/test_Python/AutoCAD/AutoCAD_DLL_GCC_Python313/cython_log.txt", "w", encoding="utf-8") as f:
            import traceback
            traceback.print_exc(file=f)
        pythoncom.CoUninitialize()
        #return -333333
        intRtn = -333333
    finally:
        pythoncom.CoUninitialize()
        return intRtn