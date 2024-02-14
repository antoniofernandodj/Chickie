from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtWidgets import QTableView, QHeaderView
from src.domain.services import PedidoService
from src.domain.data_models import PedidoGET, EnderecoEntrega  # noqa
from pandas import DataFrame  # type: ignore
from typing import Any, List, NoReturn, Optional  # noqa
from typing_extensions import Never
from src.helpers.adapters import AdapterTablePedidos


class BasePedidosTableModel(QAbstractTableModel):

    reverse: bool
    mode: bool

    def __init__(self, table_view: QTableView) -> None:

        super().__init__()

        self.adapter = AdapterTablePedidos()
        self.pedidos_service = PedidoService()
        self.columns = [
            'ID',
            'Data/Hora',
            'Celular',
            'Comentários',
            'Endereço'
        ]
        self.refresh(table_view)

    def refresh(self, table_view: QTableView, reverse=False) -> list[int]:

        pedidos: List[PedidoGET] = self.pedidos_service.get_all()

        sizes, rows = self.adapter.adapt(
            pedidos, mode=self.mode, reverse=self.reverse

        )

        index = [str(i) for i in range(len(rows))]

        self._data = DataFrame(rows, columns=self.columns, index=index)
        self.set_size(table_view, sizes)

        self.layoutChanged.emit()

        return sizes

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole
    ):
        match role:
            case Qt.ItemDataRole.DisplayRole:
                value = self._data.iloc[index.row(), index.column()]
                return str(value)

    def get(self, index: QModelIndex | QPersistentModelIndex):
        pedido_uuid = self._data.iloc[index.row(), index.column()]
        return str(pedido_uuid)

    def rowCount(
        self,
        parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:

        return int(self._data.shape[0])

    def columnCount(
        self,
        parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:

        return int(self._data.shape[1])

    def set_size(self, table_view: QTableView, sizes: List[int]):
        for index, value in enumerate(sizes):
            table_view.setColumnWidth(index, int(value * 9))

        mode = QHeaderView.ResizeMode.Fixed
        table_view.horizontalHeader().setSectionResizeMode(mode)

    def assert_never(self, arg: Never) -> NoReturn:
        raise NotImplementedError('Caso não tratado')

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole
    ) -> Optional[Any]:
        match role:
            case Qt.ItemDataRole.DisplayRole:
                match orientation:
                    case Qt.Orientation.Horizontal:
                        return str(self._data.columns[section])
                    case Qt.Orientation.Vertical:
                        return str(self._data.index[section])
                    case arg:
                        return self.assert_never(arg)

        return None

    def clear(self):
        self._data = DataFrame([])
