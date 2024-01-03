from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.schemas import Loja, LojaSignUp, EnderecoLoja as Endereco
from src.api.security import HashService
from src.exceptions import LojaJaCadastradaException, InvalidPasswordException
from typing import Optional


def validate_password(password: Optional[str]) -> bool:
    if password is None:
        return False
    if len(password) < 6:
        return False

    return True


async def registrar(loja_data: LojaSignUp) -> Loja:
    async with DatabaseConnectionManager() as connection:

        valid = validate_password(loja_data.password)
        if not valid:
            raise InvalidPasswordException

        loja_repo = Repository(Loja, connection=connection)
        endereco_repo = Repository(Endereco, connection=connection)

        q1 = await loja_repo.find_one(username=loja_data.username)
        q2 = await loja_repo.find_one(email=loja_data.email)
        if q1 or q2:
            raise LojaJaCadastradaException

        def only_numbers(string: str) -> str:
            return ''.join([n for n in string if n.isdecimal()])

        loja = Loja(
            nome=loja_data.nome,
            username=loja_data.username,
            email=loja_data.email,
            celular=only_numbers(loja_data.celular),
            password_hash=HashService.hash(loja_data.password),
            telefone=only_numbers(loja_data.telefone),
            ativo=True,
            passou_pelo_primeiro_acesso=False,
            horarios_de_funcionamento=loja_data.horarios_de_funcionamento
        )

        del loja.password
        loja.uuid = await loja_repo.save(model=loja)
        await endereco_repo.save(
            Endereco(
                uf=loja_data.uf,
                cep=loja_data.cep,
                cidade=loja_data.cidade,
                logradouro=loja_data.logradouro,
                bairro=loja_data.bairro,
                numero=loja_data.numero,
                complemento=loja_data.complemento,
                loja_uuid=loja.uuid
            )
        )

        return loja
