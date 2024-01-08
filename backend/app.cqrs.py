import asyncio
import logging
import random
import secrets

from faker import Faker
from src.infra.database_postgres.bus import get_message_bus
from src.infra.database_postgres.commands import (
    CreateCommand,
    DeleteCommand,
    UpdateCommand
)
from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from src.models import Usuario

f = Faker()


logging.basicConfig(
    level=logging.INFO,
    format='\n%(asctime)s - %(levelname)s \n %(message)s'
)


async def main():

    bus = get_message_bus()
    
    name = f.name()
    user = Usuario(
        nome=name,
        username=name.replace(' ', '_').lower(),
        email=f.email(),
        telefone=str(random.randint(10000000, 99999999)),
        celular=str(random.randint(10000000, 99999999)),
        password_hash=secrets.token_urlsafe(30),
    )

    message = CreateCommand(user)
    await bus.send_message(message)

    # Atualizando o usuario!
    message = UpdateCommand(user)
    await bus.send_message(message)

    # Removendo o usuario!
    await bus.send_message(DeleteCommand(user))

    # Fazendo Query
    async with DatabaseConnectionManager() as connection:
        user_repo = Repository(Usuario, connection=connection)
        user = await user_repo.find_all()

    print(user)

asyncio.run(main())
