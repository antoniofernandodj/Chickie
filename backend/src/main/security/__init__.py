from datetime import datetime, timedelta
from typing import Annotated, Optional
from src.infra.database.repositories import LojaRepository, UsuarioRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from config import settings as s
from src.infra.database.service import DatabaseConnectionManager
from src.schemas import TokenData, Loja, Usuario


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)


async def authenticate_user(
        username: str,
        password: str
    ) -> Optional[Usuario]:

    async with DatabaseConnectionManager() as connection:
        user_repo = UsuarioRepository(connection=connection)
        user = await user_repo.find_one(username=username)

        if user is None or not isinstance(user, Usuario):
            return None
        
        if not user_repo.authenticate(user, password):
            return None
        
        return user
    

async def authenticate_company(
        username: str,
        password: str
    ) -> Optional[Loja]:
    
    async with DatabaseConnectionManager() as connection:
        loja_repo = LojaRepository(connection=connection)
        loja = await loja_repo.find_one(username=username)

        if loja is None or not isinstance(loja, Loja):
            return None
        
        if not loja_repo.authenticate(loja, password):
            return None
        
        return loja


def create_access_token(
        data: dict,
        expires_delta: timedelta | None = None
    ):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, s.SECRET_KEY,
        algorithm=s.AUTH_ALGORITHM
    )
    return encoded_jwt


async def current_user(
        token: Annotated[str, Depends(oauth2_scheme)]
    ) -> Usuario:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, s.SECRET_KEY,
            algorithms=[s.AUTH_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    async with DatabaseConnectionManager() as connection:
        user_repo = UsuarioRepository(connection=connection)
        user = await user_repo.find_one(
            username=token_data.username
        )
    
    if user is None or not isinstance(user, Usuario):
        raise credentials_exception
    
    return user


async def current_company(
        token: Annotated[str, Depends(oauth2_scheme)]
    ) -> Loja:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, s.SECRET_KEY,
            algorithms=[s.AUTH_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    async with DatabaseConnectionManager() as connection:
        loja_repo = LojaRepository(connection=connection)
        loja = await loja_repo.find_one(
            username=token_data.username
        )
    
    if loja is None or not isinstance(loja, Loja):
        raise credentials_exception
    
    return loja
