import sys
from PySide6.QtWidgets import QApplication
from src.windows import LoginWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow(app=app)
    window.show()
    sys.exit(app.exec())
