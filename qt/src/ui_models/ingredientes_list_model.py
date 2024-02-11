from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QObject
)
from typing import Optional


class IngredientesListModel(QAbstractListModel):
    def __init__(
        self,
        parent: Optional[QObject] = None
    ):
        super().__init__(parent)

        self._data: list[dict[str, str]] = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        try:
            if len(self._data) == 0:
                return None
            elif role == Qt.ItemDataRole.DisplayRole:
                return self._data[index.row()]['nome']
            elif role == Qt.ItemDataRole.UserRole:
                return self._data[index.row()]
        except Exception:
            return ''

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return (Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

    def add_ingrediente(self, ingrediente: dict[str, str]):
        self._data.append(ingrediente)
        self.layoutChanged.emit()

    def clear(self):
        self._data = []
        self.layoutChanged.emit()

    def remove_ingrediente(self, index):
        self._data.pop(index)

    def get(self, item: QModelIndex):
        return self._data[item.row()]

    def ingredientes(self):
        return self._data

    def remove(self, item: QModelIndex):
        ingrediente = self.get(item)
        try:
            self._data.remove(ingrediente)
        except Exception:
            pass

        self.layoutChanged.emit()
