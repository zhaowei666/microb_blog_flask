"""initial migration

Revision ID: a50640df99ec
Revises: 
Create Date: 2017-12-25 16:20:01.854614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a50640df99ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.BigInteger(), nullable=True),
    sa.Column('updated_timestamp', sa.BigInteger(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('_password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.BigInteger(), nullable=True),
    sa.Column('updated_timestamp', sa.BigInteger(), nullable=True),
    sa.Column('author_pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['author_pk'], ['users.pk'], ),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###
