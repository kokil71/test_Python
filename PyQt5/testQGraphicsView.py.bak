import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep


#============================  class define  ================================================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting  ============================================================
        scene = QGraphicsScene()
        scene.addLine(QLineF(0,-400,0,400))
        scene.addLine(QLineF(-400,0,400,0))
        #scene.addLine(QLineF(290, 290, 310, 310))
        #scene.addLine(QLineF(310, 290, 290, 310))

        line_obj1 = QGraphicsLineItem(-10,-10,10,10)
        line_obj2 = QGraphicsLineItem(10,-10,-10,10)
        circle_obj= QGraphicsEllipseItem(-5,-5,10,10)
        mark = [line_obj1,line_obj2,circle_obj]
        scene.createItemGroup(mark).setPos(300,300)

        scene.addText("(300,300)").setPos(300,300)

        self.graphics.setScene(scene)



        self.btn_centerOn.clicked.connect(self.fnc_btn_centerOn)
#===============================  Slot   ==================================================================
    def fnc_btn_centerOn(self) : self.graphics.centerOn(350,350)
#==============================  app execution =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )
