from src.domain.models import (
    Usuario,
    UsuarioSignUp,
    EnderecoUsuario as Endereco
)
from src.api.security.hash_service import HashService
from src.exceptions import InvalidPasswordException
from typing import Optional
from .base import BaseService
import uuid


class UserService(BaseService):

    model = Usuario

    async def registrar(
        self,
        user_data: UsuarioSignUp,
    ) -> Usuario:

        usuario_uuid = str(uuid.uuid1())
        endereco_uuid = str(uuid.uuid1())

        valid = self.validate_password(user_data.password)
        if not valid:
            raise InvalidPasswordException

        user = Usuario(
            nome=user_data.nome,
            username=user_data.username,
            email=user_data.email,
            celular=self.only_numbers(user_data.celular),
            telefone=self.only_numbers(user_data.telefone),
            modo_de_cadastro=user_data.modo_de_cadastro,
            password_hash=HashService.hash(password=user_data.password),
        )
        del user.password

        self.cmd_handler.save(user, usuario_uuid)  # COMMAND!
        user.uuid = usuario_uuid

        endereco = Endereco(
            uf=user_data.uf,
            cidade=user_data.cidade,
            logradouro=user_data.logradouro,
            numero=user_data.numero,
            bairro=user_data.bairro,
            cep=user_data.cep,
            complemento=user_data.complemento,
            usuario_uuid=user.uuid
        )
        self.cmd_handler.save(endereco, endereco_uuid)  # COMMAND!

        await self.cmd_handler.commit()

        del user_data
        return user

    def validate_password(self, password: Optional[str]) -> bool:
        if password is None:
            return False
        if len(password) < 6:
            return False

        return True

    def only_numbers(self, string: str | None) -> str:
        if string is None:
            return ''
        return ''.join([n for n in string if n.isdecimal()])
