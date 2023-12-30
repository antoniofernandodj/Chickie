from src.infra.database_postgres.manager import DatabaseConnectionManager
from aiopg import Connection
from src.infra.database_postgres.repository import Repository
from src.schemas import (
    Loja,
    Usuario,
    AvaliacaoDeProduto,
    Produto,
    Preco,
    Endereco,
    PedidoItens,
    Status,
    ZonaDeEntrega,
    CategoriaProdutos,
    MetodoDePagamento
)
from typing import Annotated
from fastapi import (  # noqa
    Depends
)

connection_dependency = Annotated[
    Connection, Depends(DatabaseConnectionManager.get_connection)
]


def get_produto_repository(connection: connection_dependency):
    repository = Repository(Produto, connection=connection)
    return repository


def get_loja_repository(connection: connection_dependency):
    repository = Repository(Loja, connection=connection)
    return repository


def get_usuario_repository(connection: connection_dependency):
    repository = Repository(Usuario, connection=connection)
    return repository


def get_avaliacao_repository(connection: connection_dependency):
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    return repository


def get_preco_repository(connection: connection_dependency):
    repository = Repository(Preco, connection=connection)
    return repository


def get_endereco_repository(connection: connection_dependency):
    repository = Repository(Endereco, connection=connection)
    return repository


def get_pedido_repository(connection: connection_dependency):
    repository = Repository(PedidoItens, connection=connection)
    return repository


def get_status_repository(connection: connection_dependency):
    repository = Repository(Status, connection=connection)
    return repository


def get_zona_de_entrega_repository(connection: connection_dependency):
    repository = Repository(ZonaDeEntrega, connection=connection)
    return repository


def get_categoria_repository(connection: connection_dependency):
    repository = Repository(CategoriaProdutos, connection=connection)
    return repository


def get_metodo_de_pagamento_repository(connection: connection_dependency):
    repository = Repository(MetodoDePagamento, connection=connection)
    return repository


produto_repository_dependency = Annotated[
    Repository, Depends(get_produto_repository)
]

loja_repository_dependency = Annotated[
    Repository, Depends(get_loja_repository)
]


usuario_repository_dependency = Annotated[
    Repository, Depends(get_usuario_repository)
]


preco_repository_dependency = Annotated[
    Repository, Depends(get_preco_repository)
]


endereco_repository_dependency = Annotated[
    Repository, Depends(get_endereco_repository)
]


pedido_repository_dependency = Annotated[
    Repository, Depends(get_pedido_repository)
]


status_repository_dependency = Annotated[
    Repository, Depends(get_status_repository)
]


zona_de_entrega_repository_dependency = Annotated[
    Repository, Depends(get_zona_de_entrega_repository)
]


categoria_repository_dependency = Annotated[
    Repository, Depends(get_categoria_repository)
]


metodo_de_pagamento_repository_dependency = Annotated[
    Repository, Depends(get_metodo_de_pagamento_repository)
]
