from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_mainWindow()
        self.ui_menubar()

    def ui_mainWindow(self):
        self.resize(300,100)

    def ui_menubar(self):
        menu = QMenuBar(self)   # menubar
        menu.addMenu('text')    # add menu (when Click, Popup Menu) QIon, str, QMenu object

        filemenu = QMenu(menu)  #  parent : menu -> QMenu 
        filemenu.setTitle('QMenu') # QMenu title
        filemenu.addAction('No.1') # add QMenu Action
        filemenu.addAction('No.2')
        filemenu.addSeparator() # add QMenu Separator
        action_exit = QAction(self) # QAction
        action_exit.triggered.connect(qApp.quit) # Close Action 
        action_exit.setText('&Exit') # QAction Title 
        filemenu.addAction(action_exit) # add QMenu QAction
        widget_line = QLineEdit(self) # QWidget object
        menu.setCornerWidget(widget_line,Qt.TopLeftCorner) # add widget on left Edge
        print(menu.cornerWidget(Qt.TopLeftCorner))
        menu.setDefaultUp(True) # upper to popup
        menu.addMenu(filemenu) # add QMenu QMenuBar

        menu.addAction('action') # add action (when click, execute) QAction object
        #menu.clear() # delete menubar

        self.setMenuBar(menu) # add QMenuBar in QMainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = mainWindow()
    myWindow.show()
    sys.exit(app.exec_())
