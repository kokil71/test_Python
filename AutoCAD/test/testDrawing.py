import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from pyautocad import Autocad, APoint
acad = Autocad(create_if_not_exists=True)
p1 = APoint(0,0)
p2 = APoint(50,25)
for i in range(5):
    text = acad.model.AddText(u'Hi %s!'% i, p1,2.5)
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1,10)
    p1.y +=10


    