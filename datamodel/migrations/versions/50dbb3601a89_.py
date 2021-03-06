"""empty message

Revision ID: 50dbb3601a89
Revises: 7ef1d9c70982
Create Date: 2020-06-18 21:18:21.067870

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '50dbb3601a89'
down_revision = '7ef1d9c70982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets2',
    sa.Column('id', sa.String(), autoincrement=False, nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('dttm', sa.DateTime(timezone=True), nullable=True),
    sa.Column('isRetweet', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tweets')
    op.drop_constraint('atuser_tweet_id_fkey', 'atuser', type_='foreignkey')
    op.create_foreign_key(None, 'atuser', 'tweets2', ['tweet_id'], ['id'])
    op.drop_constraint('hashtags_tweet_id_fkey', 'hashtags', type_='foreignkey')
    op.create_foreign_key(None, 'hashtags', 'tweets2', ['tweet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hashtags', type_='foreignkey')
    op.create_foreign_key('hashtags_tweet_id_fkey', 'hashtags', 'tweets', ['tweet_id'], ['id'])
    op.drop_constraint(None, 'atuser', type_='foreignkey')
    op.create_foreign_key('atuser_tweet_id_fkey', 'atuser', 'tweets', ['tweet_id'], ['id'])
    op.create_table('tweets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('dttm', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('isRetweet', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tweets_pkey')
    )
    op.drop_table('tweets2')
    # ### end Alembic commands ###
