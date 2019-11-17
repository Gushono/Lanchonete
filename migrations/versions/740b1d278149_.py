"""empty message

Revision ID: 740b1d278149
Revises: 6ea18186d29d
Create Date: 2019-11-17 13:04:18.734870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '740b1d278149'
down_revision = '6ea18186d29d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_perfil', sa.Integer(), nullable=True),
    sa.Column('id_pessoa', sa.Integer(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['id_perfil'], ['tb_perfil.id'], ),
    sa.ForeignKeyConstraint(['id_pessoa'], ['tb_pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_usuario')
    # ### end Alembic commands ###
