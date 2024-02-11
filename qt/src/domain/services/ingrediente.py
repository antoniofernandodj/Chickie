from src.config import settings
from src.domain.data_models import Ingrediente
from .base import BaseService


class IngredienteService(BaseService):
    base_url = f"{settings.HOST}/ingredientes/"
    Model = Ingrediente
