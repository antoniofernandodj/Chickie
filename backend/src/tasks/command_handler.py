from typing import Any
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


async def post(item):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(type(item), connection=connection)
        try:
            uuid = await repository.save(item)
            print({"uuid": uuid})
        except Exception as error:
            print({'error': str(error)})


async def patch(itemData):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(type(itemData), connection=connection)
        item = await repository.find_one(uuid=itemData.uuid)
        if item is None:
            raise Exception('Not found')

    num_rows_affected = await repository.update(
        item, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


async def put(itemData):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(type(itemData), connection=connection)
        item = await repository.find_one(uuid=itemData.uuid)
        if item is None:
            raise Exception('Not found')

    num_rows_affected = await repository.update(
        item, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


async def delete(item):
    print('delete item')
    print(item)


handler: dict[str, Any] = {
    'post': post,
    'put': put,
    'delete': delete
}
