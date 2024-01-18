from pydantic import BaseModel


class Cliente(BaseModel):
    __tablename__ = "clientes"

    usuario_uuid: str
    loja_uuid: str
    uuid: str


class ClientePOST(BaseModel):
    __tablename__ = "clientes"

    usuario_uuid: str
    loja_uuid: str
