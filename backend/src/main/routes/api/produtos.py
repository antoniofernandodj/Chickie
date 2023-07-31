from typing import Annotated
from fastapi import (
    APIRouter, HTTPException, status,
    Path, Depends, Query
)
from src.schemas import Produto
from src.infra.database.repositories import repo_handler
from src.infra.database.service import (
    DatabaseConnectionManager
)
# cliente endereco item_pedido status pedido

repo_name = 'produto'
Repository = repo_handler[repo_name]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Produto não encontrado"
)

router = APIRouter(
    prefix='/produtos',
    tags=["Produto"]
)


@router.get('/')
async def requisitar_produtos():

    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        results = await repository.find_all()
    
    return results


@router.get('/{uuid}')
async def requisitar_produto(
    uuid: Annotated[
        str, Path(title="O uuid do produto a fazer get")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        result = await repository.find_one(uuid=uuid)
        
        if result is None:
            raise NotFoundException
    
    return result


@router.post('/', status_code=201)
async def cadastrar_produtos(produto: Produto):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        uuid = repository.save(produto)
        
    return {uuid: uuid}


@router.put('/{uuid}')
async def atualizar_produto_put(
    produtoData: Produto,
    uuid: Annotated[
        str, Path(title="O uuid do produto a fazer put")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        produto = await repository.find_one(uuid=uuid)
        if produto is None:
            raise NotFoundException
        
    num_rows_affected = await repository.update(
        produto,
        produtoData.model_dump()
    )

    return {'num_rows_affected': num_rows_affected}


@router.patch('/{uuid}')
async def atualizar_produto_patch(
    uuid: Annotated[
        str, Path(title="O uuid do produto a fazer patch")
    ]
):

    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        produto = await repository.find_one(uuid=uuid)
        if produto is None:
            raise NotFoundException
        
    # num_rows_affected = await repository.update(
    #     produto,
    #     produtoData.model_dump()
    # )

    return {}



@router.delete('/{uuid}')
async def remover_produto(
    uuid: Annotated[
        str, Path(title="O uuid do produto a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        itens_removed = await repository.delete_from_uuid(
            uuid=uuid
        )
        
    return {'itens_removed': itens_removed}
