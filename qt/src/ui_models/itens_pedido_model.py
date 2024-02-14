from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtWidgets import QTableView, QHeaderView
from src.domain.services import PedidoService
from src.domain.data_models import (  # noqa
    PedidoGET,
    EnderecoEntrega,
    Ingrediente
)
from pandas import DataFrame  # type: ignore
from typing import Any, List, NoReturn, Optional  # noqa
from typing_extensions import Never
from src.helpers.adapters import AdapterTableItemPedidos  # noqa


class ItensPedidoTableModel(QAbstractTableModel):

    def __init__(
        self,
        table_view: QTableView,
        pedido_uuid: Optional[str] = None
    ) -> None:

        super().__init__()

        self.columns = [
            'Produto',
            'Descrição',
            'Quantidade',
            'Observações',
            'Ingredientes',
            'Valor',
            'Subtotal'
        ]

        self.adapter = AdapterTableItemPedidos()
        self.pedido = None
        self.pedido_service = PedidoService()
        if pedido_uuid is None:
            self._data = DataFrame([])
            self.sizes: list[int] = []
            return

        self.refresh(pedido_uuid, table_view)

    def get_pedido(self) -> PedidoGET:
        pedido = self.pedido
        if not isinstance(pedido, PedidoGET):
            raise ValueError('Nenhum pedido alocado')

        return pedido

    def refresh(self, pedido_uuid: str, table_view: QTableView):
        self.pedido = self.pedido_service.get(pedido_uuid)
        if not isinstance(self.pedido, PedidoGET):
            raise ValueError('Pedido não encotrado!')

        sizes, rows = self.adapter.adapt(self.pedido.itens)

        index = [str(i) for i in range(len(rows))]
        data = DataFrame(rows, columns=self.columns, index=index)
        self.layoutChanged.emit()

        self._data = data
        self.sizes = sizes

        self.set_size(table_view, sizes)

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
        item_uuid = self._data.iloc[index.row(), index.column()]
        return str(item_uuid)

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
