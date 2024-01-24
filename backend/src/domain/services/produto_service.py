from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.domain.models import (
    Produto,
    Preco,
    Loja,
    ProdutoPOST,
    ProdutoPUT,
    ProdutoGET,
    AvaliacaoDeProduto
)
from aiopg.connection import Connection
from typing import List, Dict, Any
from .base import BaseService


class ProdutoService(BaseService):
    def __init__(self, connection: Connection):
        from src.domain.services import PedidoService

        self.model = Produto
        self.connection = connection
        self.query_handler = QueryHandler(
            model=self.model, connection=self.connection
        )
        self.cmd_handler = CommandHandler(
            model=self.model, connection=self.connection
        )
        self.preco_query_handler = QueryHandler(
            model=Preco, connection=self.connection
        )
        self.loja_query_handler = QueryHandler(
            model=Loja, connection=self.connection
        )
        self.avaliacao_query_handler = QueryHandler(
            model=AvaliacaoDeProduto, connection=connection
        )
        self.avaliacao_cmd_handler = CommandHandler(
            model=AvaliacaoDeProduto, connection=connection
        )
        self.produto_cmd_handler = CommandHandler(
            model=Produto, connection=self.connection
        )

        self.pedido_service = PedidoService(connection=connection)

    async def save_produto(
        self,
        produto_data: ProdutoPOST
    ) -> Dict[str, str]:
        from src.services import ImageUploadProdutoService

        produto = Produto(
            nome=produto_data.nome,
            descricao=produto_data.descricao,
            preco=produto_data.preco,
            categoria_uuid=produto_data.categoria_uuid,
            loja_uuid=produto_data.loja_uuid
        )

        self.produto_cmd_handler.save(produto)
        results = await self.produto_cmd_handler.commit()
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
            self.cmd_handler.delete_from_uuid(produto.uuid)
            await self.cmd_handler.commit()

            raise

        return {
            "uuid": produto.uuid,
            'image_url': image_url or ''
        }

    async def get_loja_from_produto(
        self,
        produto: Produto
    ) -> Loja:

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

    async def get_public_url_image(self, produto: Produto) -> str | None:

        from src.services import ImageUploadProdutoService

        loja = await self.get_loja_from_produto(produto)

        image_service = ImageUploadProdutoService(loja=loja)
        image_url = image_service.get_public_url_image_produto(
            produto=produto
        )

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
            avaliacao = AvaliacaoDeProduto(
                usuario_uuid=avaliacao_data.usuario.uuid,
                loja_uuid=avaliacao_data.loja_uuid,
                nota=avaliacao_data.nota,
                descricao=avaliacao_data.descricao,
                produto_uuid=produto.uuid
            )
            self.avaliacao_cmd_handler.save(avaliacao)
            results = await self.avaliacao_cmd_handler.commit()
            uuid = results[0].uuid

            return uuid

        else:
            self.avaliacao_cmd_handler.update(
                avaliacao, avaliacao_data.model_dump()
            )
            await self.avaliacao_cmd_handler.commit()

            return avaliacao.uuid

    async def get_all_produtos(self, **kwargs) -> List[ProdutoGET]:
        response: List[ProdutoGET] = []
        produtos = await self.get_all(**kwargs)
        for produto in produtos:
            try:
                image_url = await self.get_public_url_image(produto)
            except ValueError:
                image_url = None

            precos = await self.get_precos(produto)
            preco_hoje = await self.pedido_service.get_produto_preco(produto)

            response.append(
                ProdutoGET(
                    uuid=produto.uuid,
                    nome=produto.nome,
                    descricao=produto.nome,
                    preco=produto.preco,
                    categoria_uuid=produto.categoria_uuid,
                    loja_uuid=produto.loja_uuid,
                    precos=precos,
                    preco_hoje=preco_hoje,
                    image_url=image_url
                )
            )

        return response

    async def get_produto(self, uuid: str):
        produto = await self.get(uuid)
        if produto is None:
            return None

        preco_hoje = await self.pedido_service.get_produto_preco(produto)

        precos = await self.get_precos(produto)
        try:
            image_url = await self.get_public_url_image(produto)
        except ValueError:
            image_url = None

        return ProdutoGET(
            nome=produto.nome,
            descricao=produto.nome,
            preco=produto.preco,
            categoria_uuid=produto.categoria_uuid,
            loja_uuid=produto.loja_uuid,
            precos=precos,
            preco_hoje=preco_hoje,
            image_url=image_url
        )

    async def atualizar_produto(self, uuid: str, produto_data: ProdutoPUT):
        produto = await self.repo.find_one(uuid=uuid)
        if produto is None:
            raise ValueError("Produto não encontrado")

        self.cmd_handler.update(
            produto, produto_data.model_dump()
        )
        await self.cmd_handler.commit()

        return None

    async def remove_produto(self, uuid: str) -> Dict[str, str]:

        # Remover avaliações, Preços e Imagem de cadastro

        return {"uuid": 'removido'}
