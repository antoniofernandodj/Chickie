from src.schemas import Loja, Usuario
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from src.api import security
from fastapi import (  # noqa
    Depends
)
from src.dependencies.repository_dependecies import (  # noqa
    connection_dependency,
    produto_repository_dependency,
    loja_repository_dependency,
    usuario_repository_dependency,
    preco_repository_dependency,
    endereco_repository_dependency,
    pedido_repository_dependency,
    status_repository_dependency,
    zona_de_entrega_repository_dependency,
    categoria_repository_dependency,
    metodo_de_pagamento_repository_dependency,
    item_pedido_repository_dependency
)


current_user = Annotated[Usuario, Depends(security.current_user)]
current_company = Annotated[Loja, Depends(security.current_company)]
oauth2_password_request_form_dependency = Annotated[
    OAuth2PasswordRequestForm, Depends()
]
