from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Loja, LojaSignIn, Endereco
from src.api.security import HashService
from src.exceptions import InvalidPasswordException
from typing import Optional


def validate_password(password: Optional[str]) -> bool:
    if password is None:
        return False
    if len(password) < 6:
        return False

    return True


async def registrar(loja_data: LojaSignIn) -> str:
    async with DatabaseConnectionManager() as connection:

        valid = validate_password(loja_data.password)
        if not valid:
            raise InvalidPasswordException

        loja_repo = Repository(Loja, connection=connection)
        endereco_repo = Repository(Endereco, connection=connection)

        endereco_uuid = await endereco_repo.save(
            Endereco(
                uf="RJ",
                cep="24422400",
                cidade="São Gonçalo",
                logradouro="Rua CDE",
                bairro="Galo Branco",
                numero="292",
                complemento="casa 72",
            )
        )

        loja_data_dict = loja_data.model_dump()
        hash_base64 = HashService.hash(password=loja_data.password)
        loja_data_dict["password_hash"] = hash_base64
        loja_data_dict["endereco_uuid"] = endereco_uuid
        loja = Loja(**loja_data_dict)

        del loja.password
        uuid = await loja_repo.save(model=loja)
        del loja_data

        return uuid
