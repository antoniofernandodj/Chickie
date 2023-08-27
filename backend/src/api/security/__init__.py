from datetime import datetime, timedelta
from typing import Annotated, Optional
from src.infra.database.repository import Repository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from config import settings as s
from src.infra.database.manager import DatabaseConnectionManager
from src.schemas import TokenData, Loja, Usuario


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def authenticate_user(
    username: str, password: str
) -> Optional[Usuario]:
    """
    Autentica um usuário com base no nome de usuário e senha fornecidos.
    
    Args:
        username (str): O nome de usuário do usuário.
        password (str): A senha do usuário.
    
    Returns:
        Optional[Usuario]: O objeto do usuário autenticado ou None se a autenticação falhar.
    """
    async with DatabaseConnectionManager() as connection:
        user_repo = Repository(Usuario, connection=connection)
        user = await user_repo.find_one(username=username)

        if user is None or not isinstance(user, Usuario):
            return None

        if not user.authenticate(password):
            return None

        return user


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


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Cria um token de acesso JWT com os dados fornecidos.
    
    Args:
        data (dict): Os dados a serem codificados no token.
        expires_delta (timedelta | None, optional): A duração de validade do token. Se None, será usado o tempo padrão.
    
    Returns:
        str: O token de acesso JWT.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            seconds=int(str(s.JWT_EXPIRE_TIME))
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, s.SECRET_KEY, algorithm=s.AUTH_ALGORITHM
    )
    return encoded_jwt


async def current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Usuario:
    """
    Obtém o objeto do usuário atualmente autenticado.
    
    Args:
        token (Annotated[str, Depends(oauth2_scheme)]): O token de acesso JWT.
    
    Returns:
        Usuario: O objeto do usuário autenticado.
    
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
        user_repo = Repository(Usuario, connection=connection)
        user = await user_repo.find_one(username=token_data.username)

    if user is None or not isinstance(user, Usuario):
        raise credentials_exception

    return user


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
