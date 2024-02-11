from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex
)
from src.domain.data_models import ProdutoGET, Preco  # noqa
from src.domain.services import PrecoService, ProdutoService
from typing import Optional, List


class PrecosListModel(QAbstractListModel):

    _data: list

    def __init__(self, produto_uuid: Optional[str] = None, parent=None):
        super().__init__(parent)

        self.preco_service = PrecoService()
        self.produto_service = ProdutoService()
        self._data = self.get_data(produto_uuid)

    def get_label(self, dia_da_semana: str, preco: str):
        raise NotImplementedError('Método get_label não definido!')

    def get_data(self, produto_uuid: Optional[str]):
        raise NotImplementedError('Método get_data não definido!')

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        dias_da_semana = {
            "seg": "Segunda-feira",
            "ter": "Terça-feira",
            "qua": "Quarta-feira",
            "qui": "Quinta-feira",
            "sex": "Sexta-feira",
            "sab": "Sábado",
            "dom": "Domingo"
        }
        try:
            if len(self._data) == 0:
                return None
            elif role == Qt.ItemDataRole.DisplayRole:

                abbr = self._data[index.row()].dia_da_semana
                dia_da_semana = dias_da_semana[abbr]
                preco = (
                    f"R${self._data[index.row()].valor:.2f}"
                    .replace('.', ',')
                )

                return self.get_label(dia_da_semana, preco)
            elif role == Qt.ItemDataRole.UserRole:
                return self._data[index.row()].uuid
        except Exception:
            return 'Escolha um item...'

    def refresh(self, produto_uuid: str) -> None:
        self._data = self.get_data(produto_uuid)
        self.layoutChanged.emit()

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return (Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

    def get(self, item: QModelIndex):
        return self._data[item.row()]

    def clear(self):
        self._data = []
        self.layoutChanged.emit()


class PrecosDeProdutoListModel(PrecosListModel):

    def get_data(self, produto_uuid: Optional[str]):
        if produto_uuid is None:
            return []

        produto = self.produto_service.get(produto_uuid)
        if not isinstance(produto, ProdutoGET):
            raise ValueError('Produto não encontrado')

        return produto.precos

    def get_label(self, dia_da_semana: str, preco: str):
        return '{dia}: {preco}'.format(dia=dia_da_semana, preco=preco)

    def remove(self, item: QModelIndex) -> Preco:
        preco = self.get(item)
        if not isinstance(preco, Preco) or preco.uuid is None:
            raise ValueError('Erro: item sem id!')

        status_code = self.preco_service.delete_by_uuid(preco.uuid)

        if not (300 > status_code >= 200):
            raise Exception('Erro na remoção do item')

        try:
            self._data.remove(preco)
        except Exception:
            pass

        self.layoutChanged.emit()
        return preco


class DiasDisponiveisListModel(PrecosListModel):

    def get_data(self, produto_uuid: Optional[str]):
        """
        dias_da_semana_disponiveis = {
            'seg': 'Segunda',
            'ter': 'Terça',
            'qua': 'Quarta',
            'qui': 'Quinta',
            'sex': 'Sexta',
            'sab': 'Sábado',
            'dom': 'Domingo'
        }
        """
        if produto_uuid is None:
            return []

        produto = self.produto_service.get(produto_uuid)
        if not isinstance(produto, ProdutoGET) or produto.uuid is None:
            raise ValueError('Produto não encontrado')

        data: List[Preco] = []  # type: ignore
        for abbr, _ in produto.precos_disponiveis.items():
            data.append(
                Preco(
                    produto_uuid=produto.uuid,
                    valor=0,
                    dia_da_semana=abbr
                )
            )

        return data

    def get_label(self, dia_da_semana: str, _: str):
        return dia_da_semana
