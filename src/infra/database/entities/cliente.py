from __future__ import annotations

from .base.declarative_base import Base
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey


Cliente = Table(
    "clientes", Base.metadata,
    Column("loja_uuid", ForeignKey("lojas.uuid")),
    Column("usuario_uuid", ForeignKey("usuarios.uuid")),
)
