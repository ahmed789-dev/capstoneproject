"""empty message

Revision ID: 3612c9a2b4e1
Revises: 
Create Date: 2020-06-25 03:27:04.692759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3612c9a2b4e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('age', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('release_date', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('actors')
    # ### end Alembic commands ###
