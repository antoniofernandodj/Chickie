from fastapi.security import OAuth2PasswordRequestForm
from src.domain.models import Loja, Usuario
from typing import Annotated
from src.api import security
from fastapi import (  # noqa
    Depends
)

from src.dependencies.repository_dependecies import (  # noqa
    loja_repository_dependency,
    status_repository_dependency
)

from src.dependencies.service_dependencies import (  # noqa
    produto_service_dependency,
    pedido_service_dependency,
    loja_service_dependency
)


current_user = Annotated[Usuario, Depends(security.current_user)]
current_company = Annotated[Loja, Depends(security.current_company)]
oauth2_password_request_form_dependency = Annotated[
    OAuth2PasswordRequestForm, Depends()
]
