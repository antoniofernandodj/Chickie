from src.infra.database_postgres.repository import Repository
from src.models import Loja, LojaSignUp, EnderecoLoja, LojaGET, LojaPUT
from src.exceptions import (
    LojaJaCadastradaException,
    InvalidPasswordException
)
from typing import Optional
from src.services.domain.base import BaseService

from aiopg.connection import Connection


class LojaService(BaseService):
    def __init__(
        self, connection: Connection
    ):
        self.model = Loja
        self.connection = connection
        self.repo = Repository(
            model=self.model, connection=self.connection
        )

        self.endereco_repo = Repository(
            model=EnderecoLoja, connection=connection
        )

    async def update_loja_data(self, uuid: str, data: LojaPUT):
        loja: Optional[Loja] = await self.repo.find_one(uuid=uuid)
        if loja is None:
            raise ValueError('Loja não encontrada')

        def only_numbers(string: str | None) -> str | None:
            if string is None:
                return None

            return ''.join([n for n in string if n.isdecimal()])

        loja_data = dict(
            nome=data.nome,
            username=data.username,
            email=data.email,
            celular=only_numbers(data.celular),
            telefone=only_numbers(data.telefone),
            horarios_de_funcionamento=data.horarios_de_funcionamento
        )

        await self.repo.update(
            loja, loja_data
        )

        endereco = await self.endereco_repo.find_one(
            loja_uuid=loja.uuid
        )

        endereco_data = dict(
            uf=data.uf,
            cidade=data.cidade,
            logradouro=data.logradouro,
            numero=data.numero,
            bairro=data.bairro,
            cep=only_numbers(data.cep),
            complemento=data.complemento
        )

        await self.endereco_repo.update(
            endereco, endereco_data
        )

    async def get_data(self, loja: Loja):

        from src.services import ImageUploadService

        endereco: Optional[EnderecoLoja] = await self.endereco_repo.find_one(
            loja_uuid=loja.uuid
        )

        if endereco is None:
            raise ValueError("Endereço da loja não encontrado")

        if loja.uuid is None:
            raise AttributeError('Loja sem uuid definido!')

        loja_data = LojaGET(
            nome=loja.nome,
            username=loja.username,
            email=loja.email,
            celular=loja.celular,
            uuid=loja.uuid,
            endereco=endereco,
            telefone=loja.telefone,
            horarios_de_funcionamento=loja.horarios_de_funcionamento
        )
        image_service = ImageUploadService(loja=loja)
        try:
            public_url = image_service.get_public_url_image_cadastro()
        except ValueError:
            public_url = None

        loja_data.imagem_cadastro = public_url
        return loja_data

    async def registrar(self, loja_data: LojaSignUp) -> Loja:
        from src.api.security import HashService
        from src.services import ImageUploadService

        valid = self.validate_password(loja_data.password)
        if not valid:
            raise InvalidPasswordException

        q1 = await self.repo.find_one(username=loja_data.username)
        q2 = await self.repo.find_one(email=loja_data.email)

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
        loja.uuid = await self.repo.save(model=loja)
        endereco = EnderecoLoja(
            uf=loja_data.uf,
            cep=loja_data.cep,
            cidade=loja_data.cidade,
            logradouro=loja_data.logradouro,
            bairro=loja_data.bairro,
            numero=loja_data.numero,
            complemento=loja_data.complemento,
            loja_uuid=loja.uuid
        )
        await self.endereco_repo.save(endereco)

        try:
            if loja_data.image_bytes and loja_data.image_filename:
                image_service = ImageUploadService(loja=loja)
                try:
                    image_bytes_base64 = loja_data.image_bytes.split(',')[1]
                except IndexError:
                    image_bytes_base64 = loja_data.image_bytes
                image_service.upload_image_cadastro(
                    base64_string=image_bytes_base64,
                    filename=loja_data.image_filename
                )
        except Exception:
            pass

        return loja

    def validate_password(self, password: Optional[str]) -> bool:
        if password is None:
            return False
        if len(password) < 6:
            return False

        return True
