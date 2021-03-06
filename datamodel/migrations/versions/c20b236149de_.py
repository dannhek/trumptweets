"""empty message

Revision ID: c20b236149de
Revises: 
Create Date: 2020-06-16 13:01:18.159894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c20b236149de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('dttm', sa.DateTime(timezone=True), nullable=True),
    sa.Column('isRetweet', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
