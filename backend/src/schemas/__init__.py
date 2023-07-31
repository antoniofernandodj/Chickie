from typing import Union,Type

from .categoria import CategoriaProdutos
from .item_pedido import ItemPedido
from .login import Login
from .loja import Loja
from .pedido import Pedido
from .preco import Preco
from .produto import Produto
from .signin import UsuarioSignIn, LojaSignIn
from .token import Token, TokenData
from .usuario import Usuario
from .endereco import Endereco

Model = Union[
    Type[CategoriaProdutos],
    Type[ItemPedido],
    Type[Loja],
    Type[Pedido],
    Type[Produto],
    Type[Usuario],
    Type[Endereco]
]

ModelInstance = Union[
    CategoriaProdutos,
    ItemPedido,
    Loja,
    Pedido,
    Produto,
    Usuario,
    Endereco
]