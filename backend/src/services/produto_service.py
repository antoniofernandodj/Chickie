from src.services import ImageUploadProdutoService
from src.infra.database_postgres.repository import Repository
from src.schemas import Produto, Preco, Loja
from aiopg.connection import Connection
from typing import List, Optional


class ProdutoService:
    def __init__(self, connection: Connection, loja: Optional[Loja]):
        self.repo_builder = Repository
        self.model = Produto
        self.connection = connection
        self.loja = loja

    async def get(self, uuid: str):
        repo = self.repo_builder(
            model=self.model, connection=self.connection
        )
        return await repo.find_one(uuid=uuid)

    async def get_precos(self, produto: Produto) -> List[Preco]:
        preco_repo = self.repo_builder(
            model=Preco, connection=self.connection
        )
        return await preco_repo.find_all(uuid=produto.uuid)

    async def get_public_url_image(self, produto: Produto) -> str | None:
        if self.loja is None:
            loja_repo = self.repo_builder(
                model=Loja, connection=self.connection
            )
            self.loja = await loja_repo.find_one(
                uuid=produto.loja_uuid
            )

            if self.loja is None:
                raise Exception('Loja de produto não encontrada!')

        image_service = ImageUploadProdutoService(loja=self.loja)
        image_url = image_service.get_public_url_image_produto(
            produto=produto
        )

        return image_url
