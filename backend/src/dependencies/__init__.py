from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import (  # noqa
    Depends
)

from .connection_dependency import ConnectionDependency  # noqa
oauth2_password_request_form_dependency = Annotated[
    OAuth2PasswordRequestForm, Depends()
]
