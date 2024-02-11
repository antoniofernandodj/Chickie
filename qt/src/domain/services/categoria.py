from src.config import settings
from src.domain.data_models import CategoriaProdutos
from .base import BaseService


class CategoriaService(BaseService):
    base_url = f"{settings.HOST}/categorias/"
    Model = CategoriaProdutos
