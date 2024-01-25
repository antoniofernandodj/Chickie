from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response,
    Depends
)
from src.api.security import oauth2_scheme
from typing import Optional
from src.domain.models import Funcionario
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.api.security import AuthService
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])


@router.get("/")
async def requisitar_funcionarios(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
):

    query_handler = QueryHandler(Funcionario, connection=connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results = await query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_funcionario(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do funcionário a fazer get")]
):

    query_handler = QueryHandler(Funcionario, connection=connection)
    result = await query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Funcionario não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_funcionarios(
    connection: ConnectionDependency,
    funcionario: Funcionario,
    token: Annotated[str, Depends(oauth2_scheme)],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(Funcionario, connection=connection)

    q1 = await query_handler.find_one(nome=funcionario.nome)
    q2 = await query_handler.find_one(username=funcionario.username)
    q3 = await query_handler.find_one(email=funcionario.email)
    q4 = await query_handler.find_one(celular=funcionario.celular)

    if q1 or q2 or q3 or q4:
        raise Exception

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.save(funcionario)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_funcionario_put(
    connection: ConnectionDependency,
    funcionarioData: Funcionario,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer put")]
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(Funcionario, connection=connection)
    cmd_handler = CommandHandler(connection)

    funcionario = await query_handler.find_one(uuid=uuid)
    if funcionario is None:
        raise NotFoundException("Funcionario não encontrado")

    cmd_handler.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_funcionario_patch(
    connection: ConnectionDependency,
    funcionarioData: Funcionario,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer patch")],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(Funcionario, connection=connection)
    cmd_handler = CommandHandler(connection)

    funcionario = await query_handler.find_one(uuid=uuid)
    if funcionario is None:
        raise NotFoundException("Funcionario não encontrado")

    cmd_handler.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_funcionario(
    connection: ConnectionDependency,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer delete")],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(Funcionario, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
