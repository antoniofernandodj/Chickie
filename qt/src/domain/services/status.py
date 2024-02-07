from src.config import settings
from src.domain.data_models import Status
from .base import BaseService
import httpx


class StatusService(BaseService):

    base_url = f"{settings.HOST}/status/"

    def save(self, status: Status):
        body = status.model_dump()
        response = httpx.post(self.base_url, json=body, headers=self.headers)
        return response
