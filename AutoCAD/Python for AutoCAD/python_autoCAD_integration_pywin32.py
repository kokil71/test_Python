# https://www.supplychaindataanalytics.com/python-integration-with-autocad-using-pywin32-win32com/
# Python AutoCAD integration in pywin32

# Initiating a drawing template using pywin32
"""
# Now, to open a new drawing sheet using VBA, we use the following line of code in VBA:
# pyautocad
import pyautocad
NewDrawing1 = ThisDrawing.Application.Documents.Add("")
# pywin32
import win32com.client
acad = win32com.client.Dispatch("AutoCAD.Application") 
acad.Visible = True
acadModel = acad.ActiveDocument.ModelSpace

# To initiate AutoCAD application
# pyautocad
ThisDrawing.Application
# pywin32
acad = win32com.client.Dispatch("AutoCAD.Application")
acad.Visible = True

# To create a new template
# pyautocad
.Documents.Add("") 
# pywin32
acad.ActiveDocument.ModelSpace 
"""