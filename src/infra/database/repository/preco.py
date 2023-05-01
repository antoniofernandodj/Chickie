from dataclasses import dataclass
from src.infra.database import entities as e
from src.infra.database.repository import BaseRepositoryClass


@dataclass
class PrecoRepository(BaseRepositoryClass):

    model_class = e.Preco
