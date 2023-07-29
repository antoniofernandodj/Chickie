from __future__ import annotations

from pydantic import BaseModel
from typing import List

class AgendaDePrecos(BaseModel):
    valor: str
    dia_da_semana: str

class PrecoDados(BaseModel):
    produto_uuid: str
    precos: List[AgendaDePrecos]