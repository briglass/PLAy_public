"""empty message

Revision ID: 4db460b0f07e
Revises: 4e6e81664f8b
Create Date: 2015-05-17 17:43:40.618000

"""

# revision identifiers, used by Alembic.
revision = '4db460b0f07e'
down_revision = '4e6e81664f8b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasktable_ANT', sa.Column('rawdata', sa.Text(), nullable=True))
    op.add_column('tasktable_LRN', sa.Column('rawdata', sa.Text(), nullable=True))
    op.add_column('tasktable_PRC', sa.Column('rawdata', sa.Text(), nullable=True))
    op.add_column('tasktable_SYM', sa.Column('rawdata', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasktable_SYM', 'rawdata')
    op.drop_column('tasktable_PRC', 'rawdata')
    op.drop_column('tasktable_LRN', 'rawdata')
    op.drop_column('tasktable_ANT', 'rawdata')
    ### end Alembic commands ###