"""empty message

Revision ID: 7321bd8bfdc
Revises: 5d52042b0c9
Create Date: 2015-07-17 13:30:40.317000

"""

# revision identifiers, used by Alembic.
revision = '7321bd8bfdc'
down_revision = '5d52042b0c9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userinfo_expert', sa.Column('specific_starcraft2_battlenetdivision', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userinfo_expert', 'specific_starcraft2_battlenetdivision')
    ### end Alembic commands ###