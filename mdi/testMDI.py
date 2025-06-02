import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QAction, QFileDialog
)

class MDIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 MDI Example")
        self.setGeometry(100, 100, 800, 600)

        # MDI Window Generation
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # Menu Generation
        self.create_menu()

    def create_menu(self):
        bar = self.menuBar()

        # File Menu
        file_menu = bar.addMenu("File")

        # New Open
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)

        # Open
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Close
        exit_action = QAction("Close", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def new_document(self):
        sub = QMdiSubWindow()
        text_edit = QTextEdit()
        sub.setWidget(text_edit)
        sub.setWindowTitle("New")
        self.mdi_area.addSubWindow(sub)
        sub.show()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "File Open")

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            sub = QMdiSubWindow()
            text_edit = QTextEdit()
            text_edit.setText(content)
            sub.setWidget(text_edit)
            sub.setWindowTitle(file_path)
            self.mdi_area.addSubWindow(sub)
            sub.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MDIWindow()
    window.show()
    sys.exit(app.exec_())
