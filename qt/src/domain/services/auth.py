from src.config import settings
from src.domain.data_models import LojaAuthData
from typing import Optional
import httpx


class InvalidCredentials(Exception):
    ...


class AuthService:

    __instance = None
    login_url = f"{settings.HOST}/loja/login"

    auth_data: Optional[LojaAuthData] = None

    def __new__(cls, *args, **kwargs):
        if AuthService.__instance is not None:
            return AuthService.__instance

        instance = super(AuthService, cls).__new__(cls)
        AuthService.__instance = instance
        return instance

    def get_auth_data(self):
        if AuthService.auth_data is None:
            raise RuntimeError

        return AuthService.auth_data

    def get_loja_data(self):
        auth_data = self.get_auth_data()
        loja_data = auth_data.loja
        if loja_data is None:
            raise RuntimeError
        return loja_data

    def login(self, login: str, senha: str):
        data = {"username": login, "password": senha}
        response = httpx.post(self.login_url, data=data)

        if response.status_code == 200:
            response_data = response.json()
            auth_data = LojaAuthData(**response_data)
            AuthService.auth_data = auth_data

        else:
            msg = f'Erro na autenticação. Detalhes: {response.text}'
            raise InvalidCredentials(msg)
