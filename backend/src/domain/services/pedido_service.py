from src.infra.database_postgres.handlers import QueryHandler
from src.domain.models import (
    Produto,
    Preco,
    Loja,
    PedidoGET,
    PedidoPOST,
    ItemPedido,
    ItemPedidoPOST,
    ItemPedidoGET,
    EnderecoEntrega,
    Pedido,
    Usuario,
    Status,
    Ingrediente,
    IngredienteDeItemDePedido
)
from aiopg.connection import Connection
from typing import List, Optional
from .base import BaseService
import uuid


class PedidoService(BaseService):

    model = Pedido

    def __init__(self, connection: Connection):
        from src.domain.services import ProdutoService

        super().__init__(connection)
        conn = connection

        self.produto_service = ProdutoService(conn)

        self.get_produto_preco = self.produto_service.get_produto_preco
        self.get_produto = self.produto_service.get
        self.user_query_handler = QueryHandler(Usuario, conn)
        self.preco_query_handler = QueryHandler(Preco, conn)
        self.produto_query_handler = QueryHandler(Produto, conn)
        self.loja_query_handler = QueryHandler(Loja, conn)
        self.status_query_handler = QueryHandler(Status, conn)
        self.endereco_query_handler = QueryHandler(EnderecoEntrega, conn)
        self.itens_pedido_query_handler = QueryHandler(ItemPedido, conn)
        self.ingrediente_query_handler = QueryHandler(Ingrediente, conn)
        self.ingrediente_item_pedido_query_handler = (
            QueryHandler(IngredienteDeItemDePedido, conn)
        )

    async def get_all_pedidos(self, **kwargs) -> List[PedidoGET]:
        pedidos: List[Pedido] = await self.query_handler.find_all(
            **kwargs
        )

        response: List[PedidoGET] = []
        for pedido in pedidos:
            itens: List[ItemPedido] = (
                await self.itens_pedido_query_handler.find_all(
                    pedido_uuid=pedido.uuid
                )
            )

            status: Optional[Status] = (
                await self.status_query_handler.find_one(
                    uuid=pedido.status_uuid
                )
            )

            endereco: Optional[EnderecoEntrega] = (
                await self.endereco_query_handler.find_one(
                    pedido_uuid=pedido.uuid
                )
            )
            if endereco is None:
                raise ValueError('Endereço não encontrado!')

            total = 0.0

            itens_do_pedido = []
            for item in itens:
                if item.valor is None:
                    raise AttributeError('Item sem valor definido')

                ingredientes: List[IngredienteDeItemDePedido] = await (
                    self.ingrediente_item_pedido_query_handler.find_all(
                        item_uuid=item.uuid
                    )
                )

                itens_do_pedido.append(
                    ItemPedidoGET(
                        quantidade=item.quantidade,
                        observacoes=item.observacoes,
                        pedido_uuid=item.pedido_uuid,
                        loja_uuid=item.loja_uuid,
                        produto_descricao=item.produto_descricao,
                        produto_nome=item.produto_nome,
                        ingredientes=ingredientes,
                        valor=item.valor
                    )
                )

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
                    itens=itens_do_pedido,
                    total=total,
                    data_hora=pedido.data_hora,
                    concluido=pedido.concluido,
                    comentarios=pedido.comentarios,
                    usuario_uuid=pedido.usuario_uuid
                )
            )

        return response

    # async def get_produto(self, produto_uuid: str):
    #     produto: Optional[Produto] = await self.produto_query_handler.find_one(  # noqa
    #         uuid=produto_uuid
    #     )
    #     if produto is None or produto.uuid is None:
    #         raise ValueError('Produto não encontrado')

    #     return produto

    async def get_loja_from_uuid(self, loja_uuid: str):
        loja: Optional[Loja] = await self.loja_query_handler.find_one(
            uuid=loja_uuid
        )
        if loja is None:
            raise ValueError('Loja não encontrada')

        return loja

    # async def get_produto_preco(
    #     self,
    #     produto: Produto
    # ) -> float:
    #     data_atual = datetime.datetime.now()
    #     dias_handler = {
    #         'Monday': 'seg',
    #         'Tuesday': 'ter',
    #         'Wednesday': 'qua',
    #         'Thursday': 'qui',
    #         'Friday': 'sex',
    #         'Saturday': 'sab',
    #         'Sunday': 'dom'
    #     }
    #     dia_da_semana_hoje = dias_handler[data_atual.strftime("%A")]
    #     preco_selecionado = produto.preco
    #     precos: List[Preco] = await self.preco_query_handler.find_all(
    #         produto_uuid=produto.uuid
    #     )
    #     for preco in precos:
    #         if preco.dia_da_semana == dia_da_semana_hoje:
    #             preco_selecionado = preco.valor

    #     return preco_selecionado

    async def get_loja_from_produto(self, produto: Produto) -> Loja:

        loja = await self.loja_query_handler.find_one(
            uuid=produto.loja_uuid
        )
        if loja is None:
            raise

        return loja

    async def get_pedido(self, uuid: str) -> Optional[PedidoGET]:
        pedido: Optional[Pedido] = await self.query_handler.find_one(
            uuid=uuid
        )
        if pedido is None or pedido.uuid is None:
            return None

        itens: List[ItemPedido] = (
            await self.itens_pedido_query_handler.find_all(
                pedido_uuid=pedido.uuid
            )
        )
        endereco = await self.endereco_query_handler.find_one(
            pedido_uuid=pedido.uuid
        )
        if endereco is None:
            raise ValueError('Endereço não encontrado!')

        status: Optional[Status] = await self.status_query_handler.find_one(
            uuid=pedido.status_uuid
        )

        total = 0.0

        itens_do_pedido: List[ItemPedidoGET] = []
        for item in itens:
            if item.valor is None:
                raise AttributeError('Item sem valor definido')

            ingredientes: List[IngredienteDeItemDePedido] = await (
                self.ingrediente_item_pedido_query_handler.find_all(
                    item_uuid=item.uuid
                )
            )

            itens_do_pedido.append(
                ItemPedidoGET(
                    quantidade=item.quantidade,
                    observacoes=item.observacoes,
                    pedido_uuid=item.pedido_uuid,
                    loja_uuid=item.loja_uuid,
                    produto_descricao=item.produto_descricao,
                    produto_nome=item.produto_nome,
                    ingredientes=ingredientes,
                    valor=item.valor
                )
            )
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
            itens=itens_do_pedido,
            data_hora=pedido.data_hora,
            concluido=pedido.concluido,
            comentarios=pedido.comentarios
        )

    async def save_pedido(self, pedido_data: PedidoPOST) -> None:

        pedido_uuid = str(uuid.uuid1())

        pedido = Pedido(
            uuid=pedido_uuid,
            data_hora=pedido_data.data_hora,
            loja_uuid=pedido_data.loja_uuid,
            frete=pedido_data.frete,
            celular=pedido_data.celular,
            concluido=False,
            comentarios=pedido_data.comentarios,
            usuario_uuid=pedido_data.usuario_uuid
        )

        self.cmd_handler.save(pedido, pedido_uuid)    # COMMAND!

        await self.save_itens_for_pedido(    # COMMAND!
            itens=pedido_data.itens,
            pedido=pedido
        )

        pedido_data.endereco.pedido_uuid = pedido.uuid
        await self.save_endereco_for_pedido(    # COMMAND!
            pedido_data=pedido_data
        )

        await self.cmd_handler.commit()

        return None

    async def save_itens_for_pedido(
        self,
        itens: list[ItemPedidoPOST],
        pedido: Pedido
    ) -> list[str]:
        itens_uuid: list[str] = []

        if pedido.uuid is None:
            raise AttributeError('Produto sem uuid')

        for item in itens:
            produto: Optional[Produto] = (
                await self.get_produto(item.produto_uuid)
            )
            if produto is None:
                raise

            valor = await self.get_produto_preco(produto)

            item_uuid = str(uuid.uuid1())
            item_pedido = ItemPedido(
                uuid=item_uuid,
                quantidade=item.quantidade,
                observacoes=item.observacoes,
                pedido_uuid=pedido.uuid,
                valor=valor,
                produto_nome=produto.nome,
                produto_descricao=produto.descricao,
                loja_uuid=pedido.loja_uuid
            )

            self.cmd_handler.save(item_pedido, item_uuid)  # COMMAND!

            await self.save_ingredientes_for_item(item, item_uuid)

            itens_uuid.append(item_uuid)

        return itens_uuid

    async def save_ingredientes_for_item(
        self, item_pedido: ItemPedidoPOST, uuid: str
    ):

        for ingrediente in item_pedido.ingredientes:
            query: Optional[Ingrediente] = (
                await self.ingrediente_query_handler.find_one(
                    uuid=ingrediente.uuid
                )
            )
            if query is None:
                raise ValueError('Ingrediente não encontrado')

            ingrediente_de_item_de_pedido = IngredienteDeItemDePedido(
                item_uuid=uuid,
                nome=query.nome,
                descricao=query.descricao,
                incluso=ingrediente.value,
                loja_uuid=query.loja_uuid
            )

            self.cmd_handler.save(ingrediente_de_item_de_pedido)  # COMMAND!

    async def save_endereco_for_pedido(
        self, pedido_data: PedidoPOST
    ):
        endereco_uuid = str(uuid.uuid1())
        self.cmd_handler.save(pedido_data.endereco, endereco_uuid)   # COMMAND!

        return endereco_uuid

    async def listar_pedidos_de_usuario(self) -> None:
        return None

    async def listar_pedidos_de_loja(self):
        return None

    async def montar_historico(self):
        return None

    async def get_loja(self, produto: Produto) -> Optional[Loja]:
        loja = await self.loja_query_handler.find_one(
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

    async def remover_pedido(self, uuid: str) -> None:
        itens_pedido: List[ItemPedido] = (
            await self.itens_pedido_query_handler.find_all(
                pedido_uuid=uuid
            )
        )

        for item in itens_pedido:
            if item.uuid is None:
                continue

            self.cmd_handler.delete_from_uuid(  # COMMAND!
                ItemPedido,
                uuid=item.uuid
            )

        self.cmd_handler.delete_from_uuid(Pedido, uuid=uuid)  # COMMAND!
        await self.cmd_handler.commit()

        return None

    async def alterar_status_de_pedido(
        self, pedido_uuid: str, status_uuid: str
    ) -> None:
        pedido = await self.query_handler.find_one(uuid=pedido_uuid)
        if pedido is None:
            raise ValueError("Pedido não encontrado")

        novo_status = (
            await self.status_query_handler.find_one(uuid=status_uuid)
        )
        if novo_status is None:
            raise ValueError("Novo status não encontrado")

        self.cmd_handler.update(pedido, {'status_uuid': novo_status.uuid})  # COMMAND!  # noqa
        await self.cmd_handler.commit()

    async def concluir_pedido(
        self,
        pedido_uuid: str
    ) -> None:
        pedido = await self.query_handler.find_one(uuid=pedido_uuid)

        if pedido is None:
            raise ValueError("Pedido não encontrado")

        self.cmd_handler.update(pedido, {'concluido': True})  # COMMAND!
        await self.cmd_handler.commit()
