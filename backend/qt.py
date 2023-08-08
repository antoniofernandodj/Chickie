import sys
from PySide6.QtWidgets import QApplication
from src.qt import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app=app)
    window.show()
    sys.exit(app.exec())
