from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from config import settings as s
from src.infra.database_postgres.repository import Repository
from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.schemas import TokenData, Loja
from src.api.security.scheme import oauth2_scheme


async def authenticate_company(
    username: str, password: str
) -> Optional[Loja]:
    """
    Autentica uma loja com base no nome de usuário e senha fornecidos.

    Args:
        username (str): O nome de usuário da loja.
        password (str): A senha da loja.

    Returns:
        Optional[Loja]: O objeto da loja autenticada ou None se a autenticação falhar.
    """
    async with DatabaseConnectionManager() as connection:
        loja_repo = Repository(Loja, connection=connection)
        loja = await loja_repo.find_one(username=username)

        if loja is None or not isinstance(loja, Loja):
            return None

        if not loja.authenticate(password):
            return None

        return loja


async def current_company(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Loja:
    """
    Obtém o objeto da loja atualmente autenticada.

    Args:
        token (Annotated[str, Depends(oauth2_scheme)]): O token de acesso JWT.

    Returns:
        Loja: O objeto da loja autenticada.

    Raises:
        HTTPException: Se a autenticação falhar.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, s.SECRET_KEY, algorithms=[s.AUTH_ALGORITHM]
        )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    async with DatabaseConnectionManager() as connection:
        loja_repo = Repository(Loja, connection=connection)
        loja = await loja_repo.find_one(username=token_data.username)

    if loja is None or not isinstance(loja, Loja):
        raise credentials_exception

    return loja
