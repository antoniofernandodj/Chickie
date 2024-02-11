from . import FileService
from typing import Optional


class CacheService:
    @classmethod
    def get_last_login_data(cls):
        try:
            return FileService.get_json('auth.json')
        except Exception:
            return None

    @classmethod
    def cache_login_data(cls, login, senha: Optional[str] = None):
        try:
            if senha is not None:
                data = {'login': login, 'senha': senha}
            else:
                data = {'login': login}

            return FileService.set_json('auth.json', data)
        except Exception:
            return None