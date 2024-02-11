import sys
from PySide6.QtWidgets import QApplication
from src.windows import LoginWindow
import os

# Set environment variable to disable force dark mode
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-force-dark"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow(app=app)
    window.show()
    sys.exit(app.exec())
