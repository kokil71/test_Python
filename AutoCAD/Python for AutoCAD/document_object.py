# https://www.supplychaindataanalytics.com/autocad-document-object-in-pyautocad/
# AutoCAD Document object in pyautocad

# pyautocad 모듈을 사용하고 있습니다. 
# 또한, 문서 자체에 접근하기 위해 acad.doc 파일을 사용하고 있습니다. 아래 코드에서 이 내용을 확인할 수 있습니다.
from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)
print(acad.doc.Name)

# pyautocad 모듈에서만 사용

# Properties of the AutoCAD Document object class
# determine if the document is the active document
print(acad.doc.Active)
print(acad.doc.ActiveDimStyle.Name)
print(acad.doc.ActiveLayer.Name)
print(acad.doc.ActiveLayout.Name)
# Accessing the AutoCAD Document object Blocks property
print(acad.doc.Blocks)
for i in (acad.doc.Blocks):
    print(i.Name)
print(acad.doc.Database)
# Sub-objects contained by AutoCAD Document object
print(acad.doc.DimStyles)
for i in (acad.doc.DimStyles):
    print(i.Name)
# height of document window
print(acad.doc.Height)
# width of document window
print(acad.doc.Width)
# lower Left to Upper Right Limits
print(acad.doc.Limits)
# return a boolean value for ObjectSnapMode to check if it is on/off
print(acad.doc.ObjectSnapMode)
# path of Document
print(acad.doc.Path)
# return if Document is ReadOnly/Read-Write using boolean value
print(acad.doc.ReadOnly)
# check if document contains any unsaved changes using boolean value
print(acad.doc.Saved)
# returns SummaryInfo objects which contains document metadata (Title, subject, author, keywords)
print(acad.doc.SummaryInfo)
# returns if window is Minimized, Maximized or in a Normal state
print(acad.doc.WindowState)
# returns the document title
print(acad.doc.WindowTitle)

# Methods of the Document object class in AutoCAD
# To activate any document I can use this method.
acad.doc.Activate
# to evaluate the integrity of any drawing I can use the AuditInfo() method. Here, I can pass true or false as parameters for whether or not I want AutoCAD to fix the problems it encounters.
acad.doc.AuditInfo(True)
# regenerate drawing
acad.doc.Regen
# save drawing
acad.doc.Save
# while closing pass boolean to save changes or not followed by drawing name
acad.doc.Close(False, "Drawing2.dwg")
# to remove unused named references like blocks or layers from the Document I can use the PurgeAll command.
acad.doc.PurgeAll

# communication(통신) 모듈도 사용할 수 있습니다
# 즉, pyautocad 이외의 다른 모듈입니다. 아래 예에서는 통신 모듈이라고도 하는 pythoncom과 win32com을 사용하여 AutoCAD 문서 객체 클래스에 접근합니다.
#from win32com.client import *
#import pythoncom
#import win32com

#acad1 = win32com.client.Dispatch("AutoCAD.Application")
#print(acad1.ActiveDocument.Name)

# communication(통신) 모듈에서만 사용

# Properties of the AutoCAD Document object class
# determine if the document is the active document
#print(acad1.ActiveDocument.Active)
#print(acad1.ActiveDocument.ActiveDimStyle.Name)
#print(acad1.ActiveDocument.ActiveLayer.Name)
#print(acad1.ActiveDocument.ActiveLayout.Name)
# Accessing the AutoCAD Document object Blocks property
#print(acad1.ActiveDocument.Blocks)
#for i in (acad1.ActiveDocument.Blocks):
#    print(i.Name)
#print(acad1.ActiveDocument.Database)
# Sub-objects contained by AutoCAD Document object
#print(acad.ActiveDocument.DimStyles)
#for i in (acad.ActiveDocument.DimStyles):
#    print(i.Name)
# height of document window
#print(acad.ActiveDocument.Height)
# width of document window
#print(acad.ActiveDocument.Width)
# lower Left to Upper Right Limits
#print(acad.ActiveDocument.Limits)
# return a boolean value for ObjectSnapMode to check if it is on/off
#print(acad.ActiveDocument.ObjectSnapMode)
# path of Document
#print(acad.ActiveDocument.Path)
# return if Document is ReadOnly/Read-Write using boolean value
#print(acad.ActiveDocument.ReadOnly)
# check if document contains any unsaved changes using boolean value
#print(acad.ActiveDocument.Saved)
# returns SummaryInfo objects which contains document metadata (Title, subject, author, keywords)
#print(acad.ActiveDocument.SummaryInfo)
# returns if window is Minimized, Maximized or in a Normal state
#print(acad.ActiveDocument.WindowState)
# returns the document title
#print(acad.ActiveDocument.WindowTitle)

# Methods of the Document object class in AutoCAD
# To activate any document I can use this method.
#acad1.ActiveDocument.Activate
# to evaluate the integrity of any drawing I can use the AuditInfo() method. Here, I can pass true or false as parameters for whether or not I want AutoCAD to fix the problems it encounters.
#acad1.ActiveDocument.AuditInfo(True)
# regenerate drawing
#acad1.dActiveDocumentoc.Regen
# save drawing
#acad1.ActiveDocument.Save
# while closing pass boolean to save changes or not followed by drawing name
#acad1.ActiveDocument.Close(False, "Drawing2.dwg")
# to remove unused named references like blocks or layers from the Document I can use the PurgeAll command.
#acad1.ActiveDocument.PurgeAll
