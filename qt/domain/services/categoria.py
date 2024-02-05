from config import settings
from domain.models import CategoriaProdutos
from .base import BaseService
import httpx


class CategoriaService(BaseService):

    base_url = f"{settings.HOST}/categorias/"

    def save(self, categoria: CategoriaProdutos):
        body = categoria.model_dump()
        response = httpx.post(self.base_url, json=body, headers=self.headers)
        return response
