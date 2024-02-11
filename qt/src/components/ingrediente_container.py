from src.domain.data_models import Ingrediente
from PySide6.QtWidgets import QWidget, QScrollArea
from typing import List


class IngredientesContainer(QWidget):

    _data: List[Ingrediente]
    select: dict[str, bool | None]

    def setup(self, scroll_area: QScrollArea) -> None:
        self._data = []
        self.select = {}
        self.clear_scroll_area(scroll_area)

    def add_data(self, ingrediente: Ingrediente):
        self._data.append(ingrediente)

    def get_data(self):
        return self._data

    def clear_scroll_area(self, scroll_area: QScrollArea):
        scroll_layout = scroll_area.widget().layout()
        if scroll_layout:
            while scroll_layout.count():
                item = scroll_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
