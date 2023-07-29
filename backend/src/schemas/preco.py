from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Preco(BaseModel):    
    produto_uuid: str
    valor: float
    dia_da_semana: str
    uuid: Optional[str] = None
    
