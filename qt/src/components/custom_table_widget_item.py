from typing import Any
from PySide6.QtWidgets import (
    QTableWidgetItem
)


class CustomTableWidgetItem(QTableWidgetItem):
    def store_data(self, value: Any) -> None:
        self.stored_data = value

    def get_stored_data(self) -> Any:
        try:
            return self.stored_data
        except Exception:
            return None
