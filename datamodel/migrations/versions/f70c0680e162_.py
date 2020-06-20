"""empty message

Revision ID: f70c0680e162
Revises: 6e332df593f6
Create Date: 2020-06-16 20:50:57.543956

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f70c0680e162'
down_revision = '6e332df593f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Tweets_index', table_name='Tweets')
    op.drop_table('Tweets')
    op.drop_column('tweets', 'twitter_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('twitter_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_table('Tweets',
    sa.Column('index', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('Tweets', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('len', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('source', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('likes', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('retweets', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('is_retweet', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Tweets_index', 'Tweets', ['index'], unique=False)
    # ### end Alembic commands ###