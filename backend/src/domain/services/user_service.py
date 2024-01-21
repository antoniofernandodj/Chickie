from src.infra.database_postgres.repository import CommandHandler
from src.domain.models import (
    Usuario,
    UsuarioSignUp,
    EnderecoUsuario as Endereco
)
from aiopg import Connection
from src.api.security import HashService
from src.exceptions import InvalidPasswordException
from typing import Optional


class UserService:
    def __init__(
        self,
        connection: Connection
    ):
        self.user_cmd_handler = CommandHandler(Usuario, connection)
        self.endereco_cmd_handler = CommandHandler(Endereco, connection)

    async def registrar(
        self,
        user_data: UsuarioSignUp,

    ) -> Usuario:

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

        self.user_cmd_handler.save(user)
        results = await self.user_cmd_handler.commit()
        user.uuid = results[0]['uuid']

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
        self.endereco_cmd_handler.save(endereco)
        await self.endereco_cmd_handler.commit()

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
