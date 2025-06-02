import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit,
    QFileDialog, QAction
)
import chardet  # pip install chardet


class MDIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MDI Example")
        self.setGeometry(100, 100, 800, 600)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        self.create_menu()

    def create_menu(self):
        bar = self.menuBar()
        file_menu = bar.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "File Open")

        if file_path:
            try:
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    detected = chardet.detect(raw_data)
                    encoding = detected['encoding']
                    if encoding is None:
                        raise ValueError("Encoding Error")

                    content = raw_data.decode(encoding)

                sub = QMdiSubWindow()
                text_edit = QTextEdit()
                text_edit.setText(content)
                sub.setWidget(text_edit)
                sub.setWindowTitle(file_path)
                self.mdi_area.addSubWindow(sub)
                sub.show()

            except Exception as e:
                print(f"File Open Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MDIApp()
    window.show()
    sys.exit(app.exec_())
