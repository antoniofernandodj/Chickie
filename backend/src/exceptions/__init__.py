from fastapi import HTTPException, status
from typing import Any


class InvalidPasswordException(Exception):
    ...


class LojaJaCadastradaException(Exception):
    ...


class NotFoundException(HTTPException):
    def __init__(
        self,
        detail: Any = None,
    ) -> None:

        super().__init__(status.HTTP_404_NOT_FOUND, detail)


class ConflictException(HTTPException):
    def __init__(
        self,
        detail: Any = None,
    ) -> None:

        super().__init__(status.HTTP_409_CONFLICT, detail)


class UnauthorizedException(HTTPException):
    def __init__(
        self,
        detail: Any = None,
    ) -> None:

        super().__init__(
            status.HTTP_401_UNAUTHORIZED,
            detail,
            {"WWW-Authenticate": "Bearer"}
        )
