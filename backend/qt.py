from PySide6.QtWidgets import QApplication, QMainWindow
from src.qt.views.main import Ui_Chickie
import sys


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.view = Ui_Chickie()
        self.view.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app=app)
    window.show()
    sys.exit(app.exec())
