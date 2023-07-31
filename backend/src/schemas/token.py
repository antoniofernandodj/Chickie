from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str
    uuid: str


class TokenData(BaseModel):
    username: str | None = None


