from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Usuario, UsuarioSignIn, Endereco
from src.api.security import HashService
from src.exceptions import InvalidPasswordException
from typing import Optional


def validate_password(password: Optional[str]) -> bool:
    if password is None:
        return False
    if len(password) < 6:
        return False

    return True


async def registrar(user_data: UsuarioSignIn) -> str:
    async with DatabaseConnectionManager() as connection:

        valid = validate_password(user_data.password)
        if not valid:
            raise InvalidPasswordException

        endereco = Endereco(
            uf=user_data.uf,
            cidade=user_data.cidade,
            logradouro=user_data.logradouro,
            numero=user_data.numero,
            bairro=user_data.bairro,
            cep=user_data.cep,
            complemento=user_data.complemento
        )

        user_repo = Repository(Usuario, connection=connection)
        endereco_repo = Repository(Endereco, connection=connection)

        endereco_uuid = await endereco_repo.save(endereco)

        user = Usuario(
            nome=user_data.nome,
            username=user_data.username,
            email=user_data.email,
            celular=user_data.celular,
            endereco_uuid=endereco_uuid,
            telefone=user_data.telefone,
            password_hash=HashService.hash(password=user_data.password)
        )

        del user_data
        del user.password

        uuid = await user_repo.save(model=user)

        return uuid
