from typing import List, Any, Optional
from src.domain.data_models import ItemPedidoGET, PedidoGET  # type: ignore
import datetime


class Adapter:
    def formatar_para_string_monetaria(self, valor: float):
        return f'R${valor:.2f}'.replace('.', ',')

    def formatar_data_hora(self, data_hora: str | datetime.datetime) -> str:
        if isinstance(data_hora, datetime.datetime):
            return data_hora.strftime('%d/%m/%Y %H:%M:%S')
        else:
            try:
                truncated_data_hora = data_hora.split('.', 1)[0]
                return (
                    datetime.datetime.fromisoformat(truncated_data_hora)
                    .strftime('%d/%m/%Y %H:%M:%S')
                )
            except ValueError as error:
                print({'error': error})
                return data_hora

    def get_size_str(self, max_size: int, item: Optional[Any]):
        len_string = len(str(item or ''))
        if len_string > max_size:
            max_size = len_string

        return max_size


class AdapterTablePedidos(Adapter):
    def adapt(
        self,
        list_models: List[PedidoGET],
        mode: bool,
        min_column_size: int = 12,
        reverse: bool = False,
    ):

        rows: List[List[Any]] = []

        max_size_1 = min_column_size
        max_size_2 = min_column_size
        max_size_3 = min_column_size
        max_size_4 = min_column_size
        max_size_5 = min_column_size

        for item in list_models:
            if item.concluido is mode:

                endereco = item.endereco.to_string() if item.endereco else ''
                max_size_1 = self.get_size_str(max_size_1, item.uuid)
                max_size_2 = self.get_size_str(max_size_2, item.data_hora)
                max_size_3 = self.get_size_str(max_size_3, item.celular)
                max_size_4 = self.get_size_str(max_size_4, item.comentarios)
                max_size_5 = self.get_size_str(max_size_5, endereco)

                rows.append([
                    item.uuid,
                    self.formatar_data_hora(item.data_hora),
                    item.celular,
                    item.comentarios,
                    endereco
                ])

        sizes = [
            max_size_1,
            max_size_2,
            max_size_3,
            max_size_4,
            max_size_5
        ]

        rows.sort(key=lambda row: row[1], reverse=reverse)

        return sizes, rows


class AdapterTableItemPedidos(Adapter):
    def adapt(
        self,
        list_models: List[ItemPedidoGET],
        min_column_size: int = 12
    ):
        rows: List[List[str]] = []

        max_size_1 = min_column_size
        max_size_2 = min_column_size
        max_size_3 = min_column_size
        max_size_4 = min_column_size
        max_size_5 = min_column_size
        max_size_6 = min_column_size
        max_size_7 = min_column_size

        def ingrediente_nome(ingrediente): return ingrediente.nome

        for item in list_models:

            nomes_ingredientes = ', '.join(
                list(map(ingrediente_nome, item.ingredientes))
            )

            subtotal = item.quantidade * item.valor
            max_size_1 = self.get_size_str(max_size_1, item.produto_nome)
            max_size_2 = self.get_size_str(max_size_2, item.produto_descricao)
            max_size_3 = self.get_size_str(max_size_3, item.quantidade)
            max_size_4 = self.get_size_str(max_size_4, item.observacoes)
            max_size_5 = self.get_size_str(max_size_5, nomes_ingredientes)
            max_size_6 = self.get_size_str(max_size_6, item.valor)
            max_size_7 = self.get_size_str(max_size_7, subtotal)

            rows.append([
                item.produto_nome,
                item.produto_descricao,
                str(item.quantidade),
                str(item.observacoes),
                nomes_ingredientes,
                self.formatar_para_string_monetaria(item.valor),
                self.formatar_para_string_monetaria(subtotal)
            ])

        sizes = [
            max_size_1,
            max_size_2,
            max_size_3,
            max_size_4,
            max_size_5,
            max_size_6,
            max_size_7
        ]

        rows.sort(key=lambda row: row[0], reverse=False) 

        return sizes, rows
