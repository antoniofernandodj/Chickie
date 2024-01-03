from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Loja, LojaSignUp
from src import use_cases
from config import settings as s


async def init_app(args: list):
    async with DatabaseConnectionManager(args) as connection:
        loja_repository = Repository(Loja, connection=connection)
        loja = await loja_repository.find_one(nome=s.LOJA_NOME)
        if loja is not None:
            return

        loja = LojaSignUp(
            nome=s.LOJA_NOME,
            username=s.LOJA_USERNAME,
            email=s.LOJA_EMAIL,
            telefone=s.LOJA_TELEFONE,
            celular=s.LOJA_CELULAR,
            password=s.LOJA_SENHA,
        )
        await use_cases.lojas.registrar(loja)
