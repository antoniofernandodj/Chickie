from src.config import settings
from src.domain.data_models import Ingrediente
from .base import BaseService
import httpx


class IngredienteService(BaseService):

    base_url = f"{settings.HOST}/ingredientes/"

    def get(self, uuid: str):
        url = f"{self.base_url}{uuid}"
        response = httpx.get(url, headers=self.headers)
        return Ingrediente(**response.json())
