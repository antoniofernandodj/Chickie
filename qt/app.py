import sys
from PySide6.QtWidgets import QApplication
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from src.windows import LoginWindow  # noqa


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow(app=app)
    window.show()
    sys.exit(app.exec())
