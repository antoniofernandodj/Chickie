from src.domain.data_models import LojaAuthData
from src.domain.services import AuthService
from typing import Optional
from pydantic import BaseModel
import httpx


class BaseService:
    base_url: str
    Model: type

    def __init__(self) -> None:
        self.auth_data: Optional[LojaAuthData] = None
        self.auth_service = AuthService()

        self.auth_data = self.auth_service.get_auth_data()
        self.loja_data = self.auth_service.get_loja_data()
        token = self.auth_data.access_token
        self.headers = {"Authorization": f"Bearer {token}"}

    def get(self, uuid: Optional[str]):
        if uuid is None:
            return None
        url_request = self.base_url + uuid
        response = httpx.get(url_request, headers=self.headers)
        return self.Model(**response.json())

    def delete_by_uuid(self, uuid: str):
        url_request = self.base_url + uuid
        response = httpx.delete(url_request, headers=self.headers)
        return response.status_code

    def get_all(self, params={}):
        h = self.headers
        params.update({'loja_uuid': self.loja_data.uuid})
        response = httpx.get(self.base_url, params=params, headers=h)
        try:
            return [self.Model(**item) for item in response.json()]
        except TypeError:
            payload = response.json()['payload']
            return [self.Model(**item) for item in payload]

    def save(self, item: BaseModel):
        body = item.model_dump()
        return httpx.post(self.base_url, json=body, headers=self.headers)
