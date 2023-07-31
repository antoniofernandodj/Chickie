from typing import Annotated
from fastapi import (
    APIRouter, HTTPException, status,
    Path, Depends, Query
)
from src.schemas import Preco
from src.infra.database.repositories import repo_handler
from src.infra.database.service import (
    DatabaseConnectionManager
)


repo_name = 'preco'
Repository = repo_handler[repo_name]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Preço não encontrado"
)

router = APIRouter(
    prefix='/precos',
    tags=["Preços"]
)


@router.get('/')
async def requisitar_precos():

    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        results = await repository.find_all()
    
    return results


@router.get('/{uuid}')
async def requisitar_preco(
    uuid: Annotated[
        str, Path(title="O uuid do preco a fazer get")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        result = await repository.find_one(uuid=uuid)
        
        if result is None:
            raise NotFoundException
    
    return result


@router.post('/', status_code=201)
async def cadastrar_precos(preco: Preco):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        uuid = repository.save(preco)
        
    return {uuid: uuid}


@router.patch('/{uuid}')
async def atualizar_preco_patch(
    uuid: Annotated[
        str, Path(title="O uuid do preco a fazer patch")
    ]
):
    
    return {}


@router.put('/{uuid}')
async def atualizar_preco_put(
    itemData: Preco,
    uuid: Annotated[
        str, Path(title="O uuid do preco a fazer put")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        preco = await repository.find_one(uuid=uuid)
        if preco is None:
            raise NotFoundException
        
    num_rows_affected = await repository.update(
        preco,
        itemData.model_dump()
    )

    return {'num_rows_affected': num_rows_affected}



@router.delete('/{uuid}')
async def remover_preco(
    uuid: Annotated[
        str, Path(title="O uuid do preco a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        itens_removed = await repository.delete_from_uuid(
            uuid=uuid
        )
        
    return {'itens_removed': itens_removed}
