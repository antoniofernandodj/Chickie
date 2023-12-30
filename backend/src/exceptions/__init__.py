from fastapi import HTTPException, status
from typing import Any


class UnvalidPasswordException(Exception):
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
