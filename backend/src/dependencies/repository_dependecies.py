from src.infra.database_postgres.repository import Repository
from .connection_dependency import connection_dependency
from src.domain.models import (
    Loja,
    Status
)
from typing import Annotated
from fastapi import (  # noqa
    Depends
)


def get_loja_repository(connection: connection_dependency):
    repository = Repository(Loja, connection=connection)
    return repository


def get_status_repository(connection: connection_dependency):
    repository = Repository(Status, connection=connection)
    return repository


loja_repository_dependency = Annotated[
    Repository, Depends(get_loja_repository)
]


status_repository_dependency = Annotated[
    Repository, Depends(get_status_repository)
]
