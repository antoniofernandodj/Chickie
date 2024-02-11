from src.config import settings
from src.domain.data_models import Status
from .base import BaseService


class StatusService(BaseService):
    base_url = f"{settings.HOST}/status/"
    Model = Status
