"""ItensPedido.valor

Revision ID: 49666cd4c8c1
Revises: 09a9e0a1222f
Create Date: 2024-01-07 05:16:38.905360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49666cd4c8c1'
down_revision: Union[str, None] = '09a9e0a1222f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'avaliacoes_de_loja', ['uuid'])
    op.create_unique_constraint(None, 'avaliacoes_de_produtos', ['uuid'])
    op.create_unique_constraint(None, 'categorias_de_produtos', ['uuid'])
    op.create_unique_constraint(None, 'enderecos', ['uuid'])
    op.create_unique_constraint(None, 'enderecos_entregas', ['uuid'])
    op.create_unique_constraint(None, 'enderecos_lojas', ['uuid'])
    op.create_unique_constraint(None, 'enderecos_usuarios', ['uuid'])
    op.create_unique_constraint(None, 'entregadores', ['uuid'])
    op.create_unique_constraint(None, 'funcionarios', ['uuid'])
    op.add_column('itens_pedido', sa.Column('valor', sa.Float(), nullable=True))
    op.create_unique_constraint(None, 'itens_pedido', ['uuid'])
    op.create_unique_constraint(None, 'lojas', ['uuid'])
    op.create_unique_constraint(None, 'pagamentos', ['uuid'])
    op.create_unique_constraint(None, 'pedidos', ['uuid'])
    op.create_unique_constraint(None, 'precos', ['uuid'])
    op.create_unique_constraint(None, 'produtos', ['uuid'])
    op.create_unique_constraint(None, 'status', ['uuid'])
    op.create_unique_constraint(None, 'zonas_de_entrega', ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'zonas_de_entrega', type_='unique')
    op.drop_constraint(None, 'status', type_='unique')
    op.drop_constraint(None, 'produtos', type_='unique')
    op.drop_constraint(None, 'precos', type_='unique')
    op.drop_constraint(None, 'pedidos', type_='unique')
    op.drop_constraint(None, 'pagamentos', type_='unique')
    op.drop_constraint(None, 'lojas', type_='unique')
    op.drop_constraint(None, 'itens_pedido', type_='unique')
    op.drop_column('itens_pedido', 'valor')
    op.drop_constraint(None, 'funcionarios', type_='unique')
    op.drop_constraint(None, 'entregadores', type_='unique')
    op.drop_constraint(None, 'enderecos_usuarios', type_='unique')
    op.drop_constraint(None, 'enderecos_lojas', type_='unique')
    op.drop_constraint(None, 'enderecos_entregas', type_='unique')
    op.drop_constraint(None, 'enderecos', type_='unique')
    op.drop_constraint(None, 'categorias_de_produtos', type_='unique')
    op.drop_constraint(None, 'avaliacoes_de_produtos', type_='unique')
    op.drop_constraint(None, 'avaliacoes_de_loja', type_='unique')
    # ### end Alembic commands ###