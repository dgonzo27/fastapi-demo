"""add description

Revision ID: 3069212988b8
Revises: 54d2edcd1794
Create Date: 2021-12-29 21:26:31.989309

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '3069212988b8'
down_revision = '54d2edcd1794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'description')
    # ### end Alembic commands ###
