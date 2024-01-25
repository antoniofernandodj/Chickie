from src.infra.database_postgres.handlers import QueryHandler
from src.domain.models import (
    Preco,
    Loja,
    Usuario,
    AvaliacaoDeLoja,
)
from src.domain.services import LojaService
from aiopg.connection import Connection
from typing import Optional
from .base import BaseService
from src.misc import Paginador
from typing import TypedDict, List, Any


class PaginateOptions(TypedDict):
    limit: int
    offset: int
    payload: List[Any]


class AvaliacaoDeLojaService(BaseService):

    model = AvaliacaoDeLoja

    def __init__(
        self,
        connection: Connection,
    ):
        conn = connection

        self.user_query_handler = QueryHandler(Usuario, conn)
        self.preco_query_handler = QueryHandler(Preco, conn)
        self.loja_query_handler = QueryHandler(Loja, conn)
        self.loja_service = LojaService(conn)

    async def avaliacao_de_loja(self, loja: Loja) -> Optional[dict]:
        sql = """
        SELECT AVG(nota) AS media_avaliacao
        FROM Avaliacoes
        WHERE empresa_uuid = %s;
        """
        result = await self.query_handler.execute_and_fetch_one(
            sql, (loja.uuid,)
        )
        return result

    async def buscar_lojas_por_avaliacao_acima_de(
        self,
        nota: int,
        pag_data: PaginateOptions
    ):
        avaliacoes = await self.buscar_avaliacoes_de_loja_acima_de(nota)

        lojas: List[Loja] = []
        for avaliacao in avaliacoes:
            loja = await self.loja_service.get(avaliacao.loja_uuid)
            if loja:
                lojas.append(loja)

        paginador = Paginador(
            data=lojas,
            offset=pag_data['offset'],
            limit=pag_data['limit']
        )
        return paginador.get_response()

    async def buscar_avaliacoes_de_loja_acima_de(
        self,
        nota: int,
    ):
        sql = """
        SELECT * FROM Avaliacoes
        GROUP BY empresa_uuid
        HAVING AVG(nota) > %s;
        """
        results = await self.query_handler.execute_and_fetch_all(
            sql, (nota,)
        )
        avaliacoes = [
            AvaliacaoDeLoja(**result) for result in results
        ]

        return avaliacoes
