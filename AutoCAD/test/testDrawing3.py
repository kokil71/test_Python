import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from pyautocad import Autocad, APoint, ACAD

import math

acad = Autocad()
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

p1 = APoint(0, 0)
p2 = APoint(50, 25)
for i in range(5):
    text = acad.model.AddText(u'Hi %s!' % i, p1, 2.5)
    text.Color=i
    text.Alignment = ACAD.acAlignmentMiddle
    text.TextAlignmentPoint = p1
    text.Rotation = math.pi * 0.25
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1, 10)
    p1.y += 10

    # Update
    acad.app.Update()

    # Zoom All
    #acad.app.ZoomAll()

    # ZoomExtents
    acad.app.ZoomExtents()

    # acad.iter_objects(조건) : 전체 도면에서 선택하기
    for obj in acad.iter_objects(['Circle', 'Line']):
        #print(obj.ObjectName)
        if obj.ObjectName=='AcDbLine':
            print(obj.Length, obj.StartPoint, obj.EndPoint)
        if obj.ObjectName=='AcDbCircle':
            print(obj.Area)


    #for obj in acad.get_selection('select object: '):
        #print(obj.ObjectName)