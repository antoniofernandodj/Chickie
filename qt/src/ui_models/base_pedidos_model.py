from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtWidgets import QTableView
import datetime
from src.domain.services import PedidoService
from src.domain.data_models import PedidoGET, EnderecoEntrega  # noqa
from pandas import DataFrame  # type: ignore
from typing import Any, List, NoReturn, Optional  # noqa
from typing_extensions import Never


class BasePedidosTableModel(QAbstractTableModel):

    def __init__(self) -> None:

        super().__init__()

        self.pedidos_service = PedidoService()
        self.columns = [
            'ID',
            'Data/Hora',
            'Celular',
            'Comentários',
            'Endereço'
        ]
        sizes = self.refresh()
        self.sizes = sizes

    def mode(self):
        raise NotImplementedError(
            "Escolher um modo de concluído para o pedido, "
            "Concluído == False ou Concluído == True."
        )

    def refresh(self) -> list[int]:
        pedidos: List[PedidoGET] = self.pedidos_service.get_all()
        rows: List[List[Any]] = []

        max_size_1 = 0
        max_size_2 = 0
        max_size_3 = 0
        max_size_4 = 0
        max_size_5 = 0

        for pedido in pedidos:
            if pedido.concluido is self.mode():

                len_string = len(pedido.uuid or '')
                if len_string > max_size_1:
                    max_size_1 = len_string

                len_string = len(self.formatar_data_hora(pedido.data_hora))
                if len_string > max_size_2:
                    max_size_2 = len_string

                len_string = len(pedido.celular)
                if len_string > max_size_3:
                    max_size_3 = len_string

                len_string = len(pedido.comentarios)
                if len_string > max_size_4:
                    max_size_4 = len_string

                len_string = len(
                    pedido.endereco.to_string() if pedido.endereco else ''
                )
                if len_string > max_size_5:
                    max_size_5 = len_string

                row = [
                    pedido.uuid,
                    self.formatar_data_hora(pedido.data_hora),
                    pedido.celular,
                    pedido.comentarios,
                    pedido.endereco.to_string() if pedido.endereco else ''
                ]

                rows.append(row)

        rows.sort(key=lambda row: row[1], reverse=False)

        index = [str(i) for i in range(len(rows))]
        self._data = DataFrame(rows, columns=self.columns, index=index)
        self.layoutChanged.emit()

        sizes = [
            max_size_1,
            max_size_2,
            max_size_3,
            max_size_4,
            max_size_5
        ]

        return sizes

    def formatar_data_hora(self, data_hora: str | datetime.datetime) -> str:
        if isinstance(data_hora, datetime.datetime):
            return data_hora.strftime('%d/%m/%Y %H:%M:%S')
        else:
            try:
                return (
                    datetime.datetime.fromisoformat(data_hora)
                    .strftime('%d/%m/%Y %H:%M:%S')
                )
            except ValueError:
                return data_hora

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
