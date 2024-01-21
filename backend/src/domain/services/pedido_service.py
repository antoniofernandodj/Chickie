from src.infra.database_postgres.repository import QueryHandler, CommandHandler
import datetime
from src.domain.models import (
    Produto,
    Preco,
    Loja,
    PedidoGET,
    PedidoPOST,
    ItemPedido,
    ItemPedidoPOST,
    EnderecoEntrega,
    Pedido,
    Usuario,
    Status
)
from aiopg.connection import Connection
from typing import List, Optional, Dict, Union
from .base import BaseService


class PedidoService(BaseService):
    def __init__(
        self, connection: Connection
    ):
        self.model = Pedido
        self.connection = connection
        self.repo = QueryHandler(
            model=self.model, connection=self.connection
        )
        self.user_repo = QueryHandler(
            model=Usuario, connection=self.connection
        )
        self.preco_repo = QueryHandler(
            model=Preco, connection=self.connection
        )
        self.produto_repo = QueryHandler(
            model=Produto, connection=self.connection
        )
        self.loja_repo = QueryHandler(
            model=Loja, connection=self.connection
        )
        self.endereco_repo = QueryHandler(
            model=EnderecoEntrega, connection=connection
        )
        self.itens_pedido_repo = QueryHandler(
            model=ItemPedido, connection=connection
        )
        self.status_repo = QueryHandler(
            model=Status, connection=connection
        )
        self.pedido_cmd_handler = CommandHandler(
            model=Pedido, connection=self.connection
        )
        self.itens_pedido_cmd_handler = CommandHandler(
            model=ItemPedido, connection=self.connection
        )
        self.endereco_cmd_handler = CommandHandler(
            model=EnderecoEntrega, connection=connection
        )

    async def get_all_pedidos(self, **kwargs) -> List[PedidoGET]:
        pedidos: List[Pedido] = await self.repo.find_all(
            **kwargs
        )

        response: List[PedidoGET] = []
        for pedido in pedidos:
            items: List[ItemPedido] = await self.itens_pedido_repo.find_all(
                pedido_uuid=pedido.uuid
            )

            status: Optional[Status] = await self.status_repo.find_one(
                uuid=pedido.status_uuid
            )

            endereco: Optional[EnderecoEntrega] = (
                await self.endereco_repo.find_one(pedido_uuid=pedido.uuid)
            )
            if endereco is None:
                raise ValueError('Endereço não encontrado!')

            total = 0.0
            itens: List[ItemPedido] = await self.itens_pedido_repo.find_all(
                pedido_uuid=pedido.uuid
            )

            for item in itens:
                if item.valor is None:
                    raise AttributeError('Item sem valor definido')

                total += (item.quantidade * item.valor)

            response.append(
                PedidoGET(
                    status_uuid=pedido.status_uuid,
                    status=status,
                    celular=pedido.celular,
                    frete=pedido.frete,
                    loja_uuid=pedido.loja_uuid,
                    endereco=endereco,
                    uuid=pedido.uuid,
                    itens=items,
                    total=total,
                    data_hora=pedido.data_hora,
                    concluido=pedido.concluido,
                    comentarios=pedido.comentarios,
                    usuario_uuid=pedido.usuario_uuid
                )
            )

        return response

    async def get_produto(self, produto_uuid: str):
        produto: Optional[Produto] = await self.produto_repo.find_one(
            uuid=produto_uuid
        )
        if produto is None or produto.uuid is None:
            raise ValueError('Produto não encontrado')

        return produto

    async def get_loja_from_uuid(self, loja_uuid: str):
        loja: Optional[Loja] = await self.loja_repo.find_one(
            uuid=loja_uuid
        )
        if loja is None:
            raise ValueError('Loja não encontrada')

        return loja

    async def get_produto_preco(
        self,
        produto: Produto
    ) -> float:
        data_atual = datetime.datetime.now()
        dias_handler = {
            'Monday': 'seg',
            'Tuesday': 'ter',
            'Wednesday': 'qua',
            'Thursday': 'qui',
            'Friday': 'sex',
            'Saturday': 'sab',
            'Sunday': 'dom'
        }
        dia_da_semana_hoje = dias_handler[data_atual.strftime("%A")]
        preco_selecionado = produto.preco
        precos: List[Preco] = await self.preco_repo.find_all(
            produto_uuid=produto.uuid
        )
        for preco in precos:
            if preco.dia_da_semana == dia_da_semana_hoje:
                preco_selecionado = preco.valor

        return preco_selecionado

    async def get_pedido(self, uuid: str) -> Optional[PedidoGET]:
        pedido: Optional[Pedido] = await self.repo.find_one(
            uuid=uuid
        )
        if pedido is None or pedido.uuid is None:
            return None

        items: List[ItemPedido] = await self.itens_pedido_repo.find_all(
            pedido_uuid=uuid
        )
        endereco = await self.endereco_repo.find_one(
            pedido_uuid=pedido.uuid
        )
        if endereco is None:
            raise ValueError('Endereço não encontrado!')

        status: Optional[Status] = await self.status_repo.find_one(
            uuid=pedido.status_uuid
        )

        total = 0.0
        itens: List[ItemPedido] = await self.itens_pedido_repo.find_all(
            pedido_uuid=pedido.uuid
        )
        for item in itens:
            if item.valor is None:
                raise AttributeError('Item sem valor definido')
            total += (item.quantidade * item.valor)

        return PedidoGET(
            status_uuid=pedido.status_uuid,
            status=status,
            frete=pedido.frete,
            celular=pedido.celular,
            loja_uuid=pedido.loja_uuid,
            endereco=endereco,
            uuid=pedido.uuid,
            total=total,
            itens=items,
            data_hora=pedido.data_hora,
            concluido=pedido.concluido,
            comentarios=pedido.comentarios
        )

    async def save_pedido(
        self,
        pedido_data: PedidoPOST
    ) -> Dict[str, Union[str, list[str]]]:

        pedido = Pedido(
            data_hora=pedido_data.data_hora,
            loja_uuid=pedido_data.loja_uuid,
            frete=pedido_data.frete,
            celular=pedido_data.celular,
            concluido=False,
            comentarios=pedido_data.comentarios,
            usuario_uuid=pedido_data.usuario_uuid
        )

        self.pedido_cmd_handler.save(pedido)
        results = await self.pedido_cmd_handler.commit()

        pedido.uuid = results[0]['uuid']

        itens_uuid = await self.save_itens_for_pedido(
            itens=pedido_data.itens, pedido=pedido
        )

        pedido_data.endereco.pedido_uuid = pedido.uuid
        endereco_uuid = await self.save_endereco_for_pedido(
            pedido_data=pedido_data
        )

        return {
            'pedido_uuid': pedido.uuid,
            'endereco_uuid': endereco_uuid,
            'itens': itens_uuid
        }

    async def save_itens_for_pedido(
        self,
        itens: list[ItemPedidoPOST],
        pedido: Pedido,
    ) -> list[str]:
        itens_uuid: list[str] = []

        if pedido.uuid is None:
            raise AttributeError('Produto sem uuid')

        for item in itens:
            produto = await self.get_produto(item.produto_uuid)
            valor = await self.get_produto_preco(produto)

            item_pedido = ItemPedido(
                quantidade=item.quantidade,
                observacoes=item.observacoes,
                pedido_uuid=pedido.uuid,
                valor=valor,
                produto_nome=produto.nome,
                produto_descricao=produto.descricao,
                loja_uuid=pedido.loja_uuid
            )

            self.itens_pedido_cmd_handler.save(item_pedido)
            results = await self.itens_pedido_cmd_handler.commit()

            item_uuid = results[0]['uuid']

            itens_uuid.append(item_uuid)

        return itens_uuid

    async def save_endereco_for_pedido(
        self, pedido_data: PedidoPOST
    ):
        self.endereco_cmd_handler.save(pedido_data.endereco)
        results = await self.endereco_cmd_handler.commit()
        uuid = results[0]['uuid']
        return uuid

    async def listar_pedidos_de_usuario(self) -> None:
        return None

    async def listar_pedidos_de_loja(self):
        return None

    async def montar_historico(self):
        return None

    async def get_loja(self, produto: Produto) -> Optional[Loja]:
        loja = await self.loja_repo.find_one(
            uuid=produto.loja_uuid
        )

        if loja is None:
            raise ValueError('Loja não encontrada')

        return loja

    async def alterar_status(
        self, pedido:
        Pedido, status: str
    ) -> None:

        return None

    async def remover_pedido(self, uuid: str) -> Dict[str, int]:
        itens_removed = 0
        pedidos_removed = 0

        itens_pedido: List[ItemPedido] = (
            await self.itens_pedido_repo.find_all(
                pedido_uuid=uuid
            )
        )

        for item in itens_pedido:
            if item.uuid is None:
                continue
            i = await self.itens_pedido_repo.delete_from_uuid(
                uuid=item.uuid
            )
            itens_removed += i
        pedidos_removed = await self.repo.delete_from_uuid(
            uuid=uuid
        )

        return {
            "pedidos_removed": pedidos_removed,
            'itens_removed': itens_removed
        }

    async def alterar_status_de_pedido(
        self, pedido_uuid: str, status_uuid: str
    ) -> None:
        pedido = await self.repo.find_one(uuid=pedido_uuid)
        if pedido is None:
            raise ValueError("Pedido não encontrado")

        print({'status_uuid': status_uuid})
        novo_status = await self.status_repo.find_one(uuid=status_uuid)
        if novo_status is None:
            raise ValueError("Novo status não encontrado")

        await self.repo.update(pedido, {'status_uuid': novo_status.uuid})

    async def concluir_pedido(
        self,
        pedido_uuid: str
    ) -> None:
        pedido = await self.repo.find_one(uuid=pedido_uuid)

        if pedido is None:
            raise ValueError("Pedido não encontrado")

        await self.repo.update(pedido, {'concluido': True})
