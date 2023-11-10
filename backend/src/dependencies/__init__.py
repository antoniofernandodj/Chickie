from src.infra.database_postgres.manager import DatabaseConnectionManager
from aiopg import Connection
from src.schemas import Loja, Usuario
from typing import Annotated
from src.api import security
from fastapi import (  # noqa
    Depends
)

connection_dependency = Annotated[
    Connection, Depends(DatabaseConnectionManager.get_connection)
]

current_user = Annotated[Usuario, Depends(security.current_user)]
current_company = Annotated[Loja, Depends(security.current_company)]
