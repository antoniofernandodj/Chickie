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


def get_size_str(max_size: int, item: Any):
    len_string = len(str(item))
    if len_string > max_size:
        max_size = len_string

    return max_size


class ItensPedidoTableModel(QAbstractTableModel):

    def __init__(self, pedido_uuid: Optional[str] = None) -> None:

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

        self.pedido = None
        self.pedido_service = PedidoService()
        if pedido_uuid is None:
            self._data = DataFrame([])
            self.sizes = []
            return

        sizes, data = self.refresh(pedido_uuid)
        self.sizes = sizes
        self._data = data

    def get_pedido(self) -> PedidoGET:
        pedido = self.pedido
        if not isinstance(pedido, PedidoGET):
            raise ValueError('Nenhum pedido alocado')

        return pedido

    def refresh(self, pedido_uuid: str):
        self.pedido = self.pedido_service.get(pedido_uuid)
        if not isinstance(self.pedido, PedidoGET):
            raise ValueError('Pedido não encotrado!')

        rows: List[List[str]] = []

        max_size_1 = 12
        max_size_2 = 12
        max_size_3 = 12
        max_size_4 = 12
        max_size_5 = 12
        max_size_6 = 12
        max_size_7 = 12

        def ingrediente_nome(ingrediente): return ingrediente.nome

        for item in self.pedido.itens:

            nomes_ingredientes = ', '.join(
                list(map(ingrediente_nome, item.ingredientes))
            )

            max_size_1 = get_size_str(max_size_1, item.produto_nome)
            max_size_2 = get_size_str(max_size_2, item.produto_descricao)
            max_size_3 = get_size_str(max_size_3, item.quantidade)
            max_size_4 = get_size_str(max_size_4, item.observacoes)
            max_size_5 = get_size_str(max_size_5, nomes_ingredientes)
            max_size_6 = get_size_str(max_size_6, item.valor)
            max_size_7 = get_size_str(max_size_7, item.quantidade * item.valor)

            row = [
                item.produto_nome,
                item.produto_descricao,
                str(item.quantidade),
                str(item.observacoes),
                nomes_ingredientes,
                f'R${item.valor:.2f}'.replace('.', ','),
                f'R${(item.quantidade * item.valor):.2f}'.replace('.', ',')
            ]
            rows.append(row)

            rows.sort(key=lambda row: row[1], reverse=False)

        index = [str(i) for i in range(len(rows))]
        data = DataFrame(rows, columns=self.columns, index=index)
        self.layoutChanged.emit()

        sizes = [
            max_size_1,
            max_size_2,
            max_size_3,
            max_size_4,
            max_size_5,
            max_size_6,
            max_size_7
        ]

        self.layoutChanged.emit()

        self._data = data
        self.sizes = sizes

        return sizes, data

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
