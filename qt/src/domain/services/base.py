from src.domain.data_models import LojaAuthData
from src.domain.services import AuthService
from typing import Optional


class BaseService:

    def __init__(self) -> None:
        self.auth_data: Optional[LojaAuthData] = None
        self.auth_service = AuthService()

        self.auth_data = self.auth_service.get_auth_data()
        self.loja_data = self.auth_service.get_loja_data()

        self.headers = {
            "Authorization": f"Bearer {self.auth_data.access_token}"
        }
