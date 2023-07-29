import logging
from typing import Any, Union

from config import settings as s
from dropbox import Dropbox
from dropbox.files import WriteMode
from src.infra.database.repository import (
    AnexoCotacao, AnexoHomologacao, AnexoProposta, Empresa
)
from src.libs import seguranca


Anexo = Union[AnexoCotacao, AnexoHomologacao, AnexoProposta]


class DropboxService:
    def __init__(self, empresa: Empresa):
        self.empresa = empresa
        self.dbx = Dropbox(
            app_key = self.empresa.dropbox_config.app_key,
            app_secret = seguranca.decrypt(
                self.empresa.dropbox_config.app_secret,
                s.CRYPT_SECRET_KEY
            ),  
            oauth2_refresh_token = seguranca.decrypt(
                self.empresa.dropbox_config.oauth2_refresh_token,
                s.CRYPT_SECRET_KEY
            )
        )

    def download(self, anexo: Anexo) -> bytes:
        _, response = self.dbx.files_download(path=anexo.path)
        logging.info('Download de item realizado com sucesso')
        return response.content
    

    def upload(self, anexo: Anexo, file_bytes: bytes):
        response = self.dbx.files_upload(
            f=file_bytes, path=anexo.path, mode=WriteMode("overwrite")
        )
        logging.info('Item upload realizado com sucesso')
        return response

    def delete(self, anexo: Any):
        response = self.dbx.files_delete_v2(path=anexo.path)
        logging.debug('Item removido com sucesso do Dropbox')
        return response
