from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Usuario, UsuarioSignIn
import base64
import bcrypt


async def registrar(user_data: UsuarioSignIn) -> str:
    async with DatabaseConnectionManager() as connection:
        user_service = Repository(Usuario, connection=connection)

        salt = bcrypt.gensalt()
        password: str = user_data.password
        user_data_dict = user_data.model_dump()  # type: ignore
        hashpw = bcrypt.hashpw(password.encode("utf-8"), salt)
        hash_base64 = base64.b64encode(hashpw).decode("utf-8")
        user_data_dict["password_hash"] = hash_base64
        user = Usuario(**user_data_dict)

        del user.password
        del user_data
        uuid = await user_service.save(model=user)

        return uuid
