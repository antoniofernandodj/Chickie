from src.event import store
import logging
from src.infra.database.manager import DatabaseConnectionManager
from src.infra.database.interfaces import CommandInterface
from src.infra.database.commands import (
    CreateCommand,
    UpdateCommand,
    DeleteCommand
)


console = logging.getLogger(__file__)


async def database_handler(message: CommandInterface):

    if isinstance(message, CreateCommand):
        console.log(logging.INFO, f"Creating item: {message.attributes}")

    elif isinstance(message, UpdateCommand):
        console.log(logging.INFO, f"Updating item: {message.attributes}")

    elif isinstance(message, DeleteCommand):
        console.log(logging.INFO, f"Deleting item: {message}")
    else:
        raise ValueError("Invalid message type.")

    async with DatabaseConnectionManager() as connection:
        cursor = await connection.cursor()
        result = await cursor.execute(message.sql())

    return result


async def event_handler(message: CommandInterface):

    if isinstance(message, CreateCommand):
        event = message.event()
        store.register(event)

    elif isinstance(message, UpdateCommand):
        pass

    elif isinstance(message, DeleteCommand):
        pass

    else:
        raise ValueError("Invalid message type.")

    return True
