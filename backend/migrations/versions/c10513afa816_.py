"""empty message

Revision ID: c10513afa816
Revises: 3612c9a2b4e1
Create Date: 2020-06-25 03:47:20.935749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c10513afa816'
down_revision = '3612c9a2b4e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'age',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('actors', 'name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('movies', 'release_date',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('movies', 'release_date',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('actors', 'name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('actors', 'age',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###