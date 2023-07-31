from typing import Annotated
from fastapi import (
    APIRouter, HTTPException, status,
    Path, Depends, Query
)
from src.schemas import CategoriaProdutos
from src.infra.database.repositories import repo_handler
from src.infra.database.service import (
    DatabaseConnectionManager
)


repo_name = 'categoria'
Repository = repo_handler[repo_name]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Categoria não encontrada"
)

router = APIRouter(
    prefix='/categorias',
    tags=["Categorias"],
    # dependencies=[Depends(get_token_header)],
    # responses={
    #     404: {"description": "Categoria não encontrada"}
    # }
)


@router.get('/')
async def requisitar_categorias():

    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        results = await repository.find_all()
    
    return results


@router.get('/{uuid}')
async def requisitar_categoria(
    uuid: Annotated[
        str, Path(title="O uuid da categoria a fazer get")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        result = await repository.find_one(uuid=uuid)
        
        if result is None:
            raise NotFoundException
    
    return result


@router.post('/', status_code=201)
async def cadastrar_categorias(categoria: CategoriaProdutos):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        uuid = repository.save(categoria)
        
    return {uuid: uuid}


@router.patch('/{uuid}')
async def atualizar_categoria_patch(
    uuid: Annotated[
        str, Path(title="O uuid da categoria a fazer patch")
    ]
):
    
    return {}


@router.put('/{uuid}')
async def atualizar_categoria_put(
    itemData: CategoriaProdutos,
    uuid: Annotated[
        str, Path(title="O uuid da categoria a fazer put")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        categoria = await repository.find_one(uuid=uuid)
        if categoria is None:
            raise NotFoundException
        
    num_rows_affected = await repository.update(
        categoria,
        itemData.model_dump()
    )

    return {'num_rows_affected': num_rows_affected}



@router.delete('/{uuid}')
async def remover_categoria(
    uuid: Annotated[
        str, Path(title="O uuid da categoria a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(connection=connection)
        itens_removed = await repository.delete_from_uuid(
            uuid=uuid
        )
        
    return {'itens_removed': itens_removed}
