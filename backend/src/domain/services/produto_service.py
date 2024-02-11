from src.infra.database_postgres.handlers import QueryHandler
from src.domain.models import (
    Produto,
    Preco,
    Loja,
    ProdutoPOST,
    ProdutoPUT,
    ProdutoGET,
    Ingrediente,
    AvaliacaoDeProduto as Avaliacao
)
from contextlib import suppress
from aiopg.connection import Connection
from typing import List, Dict, Any, Optional
from .base import BaseService
import asyncio
import datetime


class ProdutoService(BaseService):

    model = Produto

    def __init__(self, connection: Connection):
        super().__init__(connection)
        conn = connection

        self.preco_query_handler = QueryHandler(Preco, conn)
        self.ingrediente_query_handler = QueryHandler(Ingrediente, conn)
        self.loja_query_handler = QueryHandler(Loja, conn)
        self.avaliacao_query_handler = QueryHandler(Avaliacao, conn)

    async def save_produto(self, produto_data: ProdutoPOST) -> Dict[str, str]:
        from src.services import ImageUploadProdutoService

        produto = Produto(
            nome=produto_data.nome,
            descricao=produto_data.descricao,
            preco=produto_data.preco,
            categoria_uuid=produto_data.categoria_uuid,
            loja_uuid=produto_data.loja_uuid
        )

        self.cmd_handler.save(produto)  # COMMAND!
        results = await self.cmd_handler.commit()  # COMMIT!
        produto.uuid = results[0].uuid

        loja = await self.get_loja_from_produto(produto=produto)
        if loja is None:
            raise Exception('Loja não encontrada!')

        try:
            image_service = ImageUploadProdutoService(loja=loja)
            image_service.upload_image_produto(
                base64_string=produto_data.image_bytes,
                filename=produto_data.filename,
                produto=produto
            )
            try:
                image_url = image_service.get_public_url_image_produto(produto)
            except ValueError:
                image_url = None

        except Exception:
            self.cmd_handler.delete_from_uuid(Produto, produto.uuid)  # COMMAND!  # noqa
            await self.cmd_handler.commit()

            raise

        return {"uuid": produto.uuid, 'image_url': image_url or ''}

    async def get_loja_from_produto(self, produto: Produto) -> Loja:

        loja = await self.loja_query_handler.find_one(
            uuid=produto.loja_uuid
        )
        if loja is None:
            raise

        return loja

    async def get_precos(self, produto: Produto) -> List[Preco]:
        return await self.preco_query_handler.find_all(
            produto_uuid=produto.uuid
        )

    async def get_precos_disponiveis(
        self,
        produto: Produto
    ) -> dict[str, str]:

        dias_da_semana_disponiveis = {
            'seg': 'Segunda',
            'ter': 'Terça',
            'qua': 'Quarta',
            'qui': 'Quinta',
            'sex': 'Sexta',
            'sab': 'Sábado',
            'dom': 'Domingo'
        }

        precos = await self.preco_query_handler.find_all(
            produto_uuid=produto.uuid
        )
        for preco in precos:
            dias_da_semana_disponiveis.pop(preco.dia_da_semana, None)

        return dias_da_semana_disponiveis

    async def get_public_url_image(self, produto: Produto) -> str | None:

        from src.services import ImageUploadProdutoService

        try:
            loja = await self.get_loja_from_produto(produto)

            image_service = ImageUploadProdutoService(loja=loja)
            image_url = image_service.get_public_url_image_produto(
                produto=produto
            )
        except Exception:
            image_url = None

        return image_url

    async def atualizar_imagem_de_produto(
        self,
        base_64_string: str,
        produto: Produto
    ):
        from src.services import ImageUploadProdutoService

        loja = await self.get_loja_from_produto(produto)
        image_service = ImageUploadProdutoService(loja=loja)
        image_service.upload_image_produto(
            produto=produto,
            base64_string=base_64_string
        )

    async def avaliar_produto(
        self,
        produto: Produto,
        avaliacao_data: Any
    ) -> str:
        avaliacao = await self.avaliacao_query_handler.find_one(
            uuid=avaliacao_data.id
        )

        if produto.uuid is None:
            raise

        if avaliacao is None:
            avaliacao = Avaliacao(
                usuario_uuid=avaliacao_data.usuario.uuid,
                loja_uuid=avaliacao_data.loja_uuid,
                nota=avaliacao_data.nota,
                descricao=avaliacao_data.descricao,
                produto_uuid=produto.uuid
            )
            self.cmd_handler.save(avaliacao)  # COMMAND!
            results = await self.cmd_handler.commit()
            uuid = results[0].uuid

            return uuid

        else:
            self.cmd_handler.update(  # COMMAND!
                avaliacao, avaliacao_data.model_dump()
            )
            await self.cmd_handler.commit()  # COMMIT

            return avaliacao.uuid

    async def get_all_produtos(self, **kwargs) -> List[ProdutoGET]:
        response: List[ProdutoGET] = []
        produtos: List[Produto] = await self.get_all(**kwargs)

        for produto in produtos:
            results = await asyncio.gather(
                self.get_precos(produto),
                self.get_public_url_image(produto)
            )

            precos_disponiveis = await self.get_precos_disponiveis(produto)

            precos = results[0]
            image_url = results[1]

            preco_hoje = await self.get_produto_preco(produto)

            response.append(
                ProdutoGET(
                    uuid=produto.uuid,
                    nome=produto.nome,
                    descricao=produto.nome,
                    preco=produto.preco,
                    categoria_uuid=produto.categoria_uuid,
                    loja_uuid=produto.loja_uuid,
                    precos=precos,
                    precos_disponiveis=precos_disponiveis,
                    preco_hoje=preco_hoje,
                    image_url=image_url
                )
            )

        return response

    async def get_produto_preco(self, produto: Produto) -> float:
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
        precos: List[Preco] = await self.preco_query_handler.find_all(
            produto_uuid=produto.uuid
        )
        for preco in precos:
            if preco.dia_da_semana == dia_da_semana_hoje:
                preco_selecionado = preco.valor

        return preco_selecionado

    async def get_produto(self, uuid: str):
        produto: Optional[Produto] = await self.get(uuid)
        if produto is None:
            return None

        preco_hoje = await self.get_produto_preco(produto)
        precos_disponiveis = await self.get_precos_disponiveis(produto)

        results = await asyncio.gather(
            self.get_precos(produto),
            self.get_public_url_image(produto)
        )
        precos = results[0]
        image_url = results[1]

        return ProdutoGET(
            uuid=produto.uuid,
            nome=produto.nome,
            descricao=produto.nome,
            preco=produto.preco,
            categoria_uuid=produto.categoria_uuid,
            loja_uuid=produto.loja_uuid,
            precos=precos,
            precos_disponiveis=precos_disponiveis,
            preco_hoje=preco_hoje,
            image_url=image_url
        )

    async def atualizar_produto(self, uuid: str, produto_data: ProdutoPUT):
        produto = await self.query_handler.find_one(uuid=uuid)
        if produto is None:
            raise ValueError("Produto não encontrado")

        self.cmd_handler.update(  # COMMAND!
            produto, produto_data.model_dump()
        )
        await self.cmd_handler.commit()  # COMMIT

        return None

    async def remove_produto(self, uuid: str) -> None:
        from src.services import ImageUploadProdutoService
        # Remover avaliações, Preços e Imagem de cadastro

        precos: List[Preco] = (
            await self.preco_query_handler.find_all(produto_uuid=uuid)
        )

        for preco in precos:
            self.cmd_handler.delete(preco)

        ingredientes: List[Ingrediente] = (
            await self.ingrediente_query_handler.find_all(produto_uuid=uuid)
        )

        for ingrediente in ingredientes:
            self.cmd_handler.delete(ingrediente)

        produto: Optional[Produto] = await (
            self.query_handler.find_one(uuid=uuid)
        )

        if produto is None:
            raise ValueError('Produto não encontrado')

        self.cmd_handler.delete(produto)
        loja = await self.get_loja_from_produto(produto)
        image_service = ImageUploadProdutoService(loja)
        with suppress(ValueError):
            image_service.delete_image_produto(produto)

        await self.cmd_handler.commit()
