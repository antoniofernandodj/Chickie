from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QObject
)
from typing import Optional
from src.domain.services import ProdutoService
from .mock import Mock


class ProdutosListModel(QAbstractListModel):
    def __init__(
        self,
        categoria_uuid: Optional[str] = None,
        parent: Optional[QObject] = None
    ):
        super().__init__(parent)
        params = {}
        if categoria_uuid:
            params = {'categoria_uuid': categoria_uuid}

        self.produto_service = ProdutoService()
        self._data = self.produto_service.get_all(params)
        self._data = [Mock(nome='Escolha um item...')] + self._data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        try:
            if len(self._data) == 0:
                return None
            elif role == Qt.ItemDataRole.DisplayRole:
                return self._data[index.row()].nome
            elif role == Qt.ItemDataRole.UserRole:
                return self._data[index.row()].uuid
        except Exception:
            return 'Escolha um item...'

    def refresh(self, categoria_uuid: str):
        params = {'categoria_uuid': categoria_uuid}
        self._data = self.produto_service.get_all(params)
        self._data = [Mock(nome='Escolha um item...')] + self._data
        self.layoutChanged.emit()

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return (Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

    def clear(self):
        self._data = []
        self.layoutChanged.emit()
