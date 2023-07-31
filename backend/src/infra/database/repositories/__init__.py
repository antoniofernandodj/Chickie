from typing import Union, Type
from .base.base_repository_class import (
    BaseRepositoryClass, UserMixin
)
from .usuario import UsuarioRepository
from .pedido import PedidoRepository
from .preco import PrecoRepository
from .produto import ProdutoRepository
from .categoria import CategoriaProdutosRepository
from .loja import LojaRepository
from .endereco import EnderecoRepository

Repository = Union[
    Type[UsuarioRepository],
    Type[PedidoRepository],
    Type[PrecoRepository],
    Type[ProdutoRepository],
    Type[CategoriaProdutosRepository],
    Type[LojaRepository]
]

repo_handler: dict[str, Repository] = {
    'usuario': UsuarioRepository,
    'pedido': PedidoRepository,
    'preco': PrecoRepository,
    'produto': ProdutoRepository,
    'endereco': EnderecoRepository,
    'categoria': CategoriaProdutosRepository,
    'loja': LojaRepository
}