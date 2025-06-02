from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_mainWindow()

        self.ui_menuBar()
        self.ui_centralWidget()
        self.ui_statusBar()
        self.ui_dockWidget()
        self.ui_toolBar()

    def ui_mainWindow(self):
        self.resize(500,300)

    def ui_menuBar(self):
        menu = QMenuBar()
        menu.addMenu('menu1')
        menu.addMenu('menu2')
        self.setMenuBar(menu)

    def ui_centralWidget(self):
        widget_calendar=QCalendarWidget()
        self.setCentralWidget(widget_calendar)

    def ui_statusBar(self):
        widget_statusbar = QStatusBar()
        widget_statusbar.showMessage('statusbar')
        self.setStatusBar(widget_statusbar)

    def ui_dockWidget(self):
        widget_dockwidget = QDockWidget()
        widget_vbox = QWidget()
        widget_vboxlayout = QVBoxLayout(widget_vbox)
        for i in range(9):
            widget_button = QPushButton("button"+str(i))
            widget_vboxlayout.addWidget(widget_button)
        widget_dockwidget.setWidget(widget_vbox)
        self.addDockWidget(Qt.LeftDockWidgetArea,widget_dockwidget)

    def ui_toolBar(self):
        widget_toolbar = QToolBar()
        widget_toolbar.addAction("tool1")
        widget_toolbar.addAction("tool2")
        self.addToolBar(Qt.RightToolBarArea,widget_toolbar)
        self.addToolBarBreak(Qt.RightToolBarArea)



if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = mainWindow()
    myWindow.show()
    sys.exit(app.exec_())
