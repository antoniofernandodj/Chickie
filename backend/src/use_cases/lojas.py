from src.infra.database.manager import DatabaseConnectionManager
from src.infra.database.repository import Repository
from src.schemas import Loja, LojaSignIn
import base64
import bcrypt


async def registrar(loja_data: LojaSignIn) -> str:
    async with DatabaseConnectionManager() as connection:
        loja_service = Repository(Loja, connection=connection)

        salt = bcrypt.gensalt()
        password: str = loja_data.password
        loja_data_dict = loja_data.model_dump()  # type: ignore
        hashpw = bcrypt.hashpw(password.encode("utf-8"), salt)
        hash_base64 = base64.b64encode(hashpw).decode("utf-8")
        loja_data_dict["password_hash"] = hash_base64
        loja = Loja(**loja_data_dict)

        del loja.password
        uuid = await loja_service.save(model=loja)
        del loja_data

        return uuid
