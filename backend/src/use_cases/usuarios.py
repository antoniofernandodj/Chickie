from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Usuario, UsuarioSignIn
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

        user_repo = Repository(Usuario, connection=connection)

        user_data_dict = user_data.model_dump()

        hash_base64 = HashService.hash(password=user_data.password)
        user_data_dict["password_hash"] = hash_base64

        user = Usuario(**user_data_dict)

        del user.password
        del user_data
        uuid = await user_repo.save(model=user)

        return uuid
