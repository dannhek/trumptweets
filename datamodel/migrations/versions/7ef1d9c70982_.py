"""empty message

Revision ID: 7ef1d9c70982
Revises: f70c0680e162
Create Date: 2020-06-18 21:15:27.351282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ef1d9c70982'
down_revision = 'f70c0680e162'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('x')
    op.drop_index('ix_X_index', table_name='X')
    op.drop_table('X')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('X',
    sa.Column('index', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('0', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_X_index', 'X', ['index'], unique=False)
    op.create_table('x',
    sa.Column('1', sa.TEXT(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
