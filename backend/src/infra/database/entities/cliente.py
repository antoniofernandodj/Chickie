from __future__ import annotations
from .base import Base
from sqlalchemy import Column, String, Table, ForeignKey


Cliente = Table(
    "clientes",
    Base.metadata,
    Column("uuid", String(36), primary_key=True),
    Column("loja_uuid", ForeignKey("lojas.uuid")),
    Column("usuario_uuid", ForeignKey("usuarios.uuid")),
)
