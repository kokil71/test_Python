# https://www.supplychaindataanalytics.com/autocad-application-object-class-in-python/

# communication(통신) 모듈도 사용할 수 있습니다
#from win32com.client import *
#import pythoncom
#import win32com

#acad1 = win32com.client.Dispatch("AutoCAD.Application")

# pyautocad 모듈을 사용하고 있습니다. 
from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

# [Properties of the Application AutoCAD object]
# application details
print(acad.app.Application.Name)
print(acad.app.Caption)
print(acad.app.ActiveDocument.Name)
print(acad.app.Path)
print(acad.app.FullName)
# get currently opened docuements
print(acad.app.Documents)
for i in acad.app.Documents:
    print(i.Name)

# [MenuGroups and MenuBar attributes]
# get menu bar object from the session
print(acad.app.MenuBar)
# a collection of PopupMenu objects representing the current AutoCAD menu bar.
print(acad.app.MenuGroups)
for i in acad.app.MenuGroups:
    print(i.Name)

# [AutoCAD Application object WindowState property]
# specify if window is minimized, maximized or normal
# acMin(1): The window is minimized.
# acMax(2): The window is maximized.
# acNorm(3): The window is normal (not minimized nor maximized).
print(acad.app.WindowState)

# [AutoCAD Application object methods]
# get current state of application : 코드를 작성할 때마다 애플리케이션이 Quiescent(Inactive) 상태인지 확인
print(acad.app.GetAcadState().IsQuiescent)
# close drawing file and exist application
#acad.app.Quit()
# update the application
acad.app.Update()