"""empty message

Revision ID: 1f356ad4737f
Revises: 4e9cb54e4bc8
Create Date: 2015-05-05 16:19:45.929000

"""

# revision identifiers, used by Alembic.
revision = '1f356ad4737f'
down_revision = '4e9cb54e4bc8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('favfood', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'favfood')
    ### end Alembic commands ###
