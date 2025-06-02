Declare PtrSafe Function DrawAutoCAD Lib "C:\Path\To\acadwrapper.dll" () As Long

Sub TestDraw()
    Dim result As Long
    result = DrawAutoCAD()
    MsgBox "AutoCAD 실행 결과: " & result
End Sub