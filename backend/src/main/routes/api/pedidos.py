from typing import Annotated
from fastapi import (
    APIRouter, HTTPException, status,
    Path, Depends, Query
)
from src.schemas import Pedido
from src.infra.database.repositories import repo_handler
from src.infra.database.service import (
    DatabaseConnectionManager
)


repo_name = 'pedido'
Repository = repo_handler[repo_name]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Pedido não encontrado"
)

router = APIRouter(
    prefix='/pedidos',
    tags=["Pedidos"]
)


@router.get('/')
async def requisitar_pedidos():

    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        results = await repository.find_all()
    
    return results


@router.get('/{uuid}')
async def requisitar_pedido(
    uuid: Annotated[
        str, Path(title="O uuid do pedido a fazer get")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        result = await repository.find_one(uuid=uuid)
        
        if result is None:
            raise NotFoundException
    
    return result


@router.post('/', status_code=201)
async def cadastrar_pedidos(pedido: Pedido):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        uuid = repository.save(pedido)
        
    return {uuid: uuid}


@router.patch('/{uuid}')
async def atualizar_pedido_patch(
    uuid: Annotated[
        str, Path(title="O uuid do pedido a fazer patch")
    ]
):
    
    return {uuid: uuid}


@router.put('/{uuid}')
async def atualizar_pedido_put(
    itemData: Pedido,
    uuid: Annotated[
        str, Path(title="O uuid do pedido a fazer put")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        pedido = await repository.find_one(uuid=uuid)
        if pedido is None:
            raise NotFoundException
        
    num_rows_affected = await repository.update(
        pedido,
        itemData.model_dump()
    )

    return {'num_rows_affected': num_rows_affected}



@router.delete('/{uuid}')
async def remover_pedido(
    uuid: Annotated[
        str, Path(title="O uuid do pedido a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        itens_removed = await repository.delete_from_uuid(
            uuid=uuid
        )
        
    return {'itens_removed': itens_removed}
