from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    Response,
    status,
    Path
)
from src.misc import Paginador  # noqa
from src.domain.models import ZonaDeEntrega
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/zonas-de-entrega", tags=["Zonas de entrega"])


@router.get("/")
async def requisitar_zonas_de_entrega(connection: ConnectionDependency):

    zonas_query_handler = QueryHandler(ZonaDeEntrega, connection)
    results = await zonas_query_handler.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_zona_de_entrega(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da zona de entrega a fazer get")]
):

    zonas_query_handler = QueryHandler(ZonaDeEntrega, connection)
    result = await zonas_query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Zona de entrega não encontrada")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_zonas_de_entrega(
    connection: ConnectionDependency,
    zona_de_entrega: ZonaDeEntrega
):

    zonas_query_handler = QueryHandler(ZonaDeEntrega, connection)

    query = await zonas_query_handler.find_one(
        cidade=zona_de_entrega.cidade,
        uf=zona_de_entrega.uf,
        bairro=zona_de_entrega.bairro
    )
    if query:
        raise Exception

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.save(zona_de_entrega)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_zona_de_entrega_put(
    connection: ConnectionDependency,
    zona_de_entrega_Data: ZonaDeEntrega,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
):

    zonas_query_handler = QueryHandler(ZonaDeEntrega, connection)
    cmd_handler = CommandHandler(connection)

    zona_de_entrega = await zonas_query_handler.find_one(uuid=uuid)
    if zona_de_entrega is None:
        raise NotFoundException("Zona de entrega não encontrada")

    cmd_handler.update(
        zona_de_entrega, zona_de_entrega_Data.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_zona_de_entrega_patch(
    connection: ConnectionDependency,
    zona_de_entregaData: ZonaDeEntrega,
    uuid: Annotated[
        str, Path(title="O uuid da zona de entrega a fazer patch")
    ],
):

    zonas_query_handler = QueryHandler(ZonaDeEntrega, connection)
    cmd_handler = CommandHandler(connection)

    zona_de_entrega = await zonas_query_handler.find_one(uuid=uuid)
    if zona_de_entrega is None:
        raise NotFoundException("Zona de entrega não encontrada")

    cmd_handler.update(
        zona_de_entrega, zona_de_entregaData.model_dump()  # type: ignore
    )

    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_zona_de_entrega(
    connection: ConnectionDependency,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ]
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(ZonaDeEntrega, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
