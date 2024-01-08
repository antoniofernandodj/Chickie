from src.infra.database_postgres.manager import DatabaseConnectionManager
from aiopg import Connection
from typing import Annotated
from fastapi import (  # noqa
    Depends
)

connection_dependency = Annotated[
    Connection, Depends(DatabaseConnectionManager.get_connection)
]
