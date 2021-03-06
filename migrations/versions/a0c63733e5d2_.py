"""empty message

Revision ID: a0c63733e5d2
Revises: e4311ef3ddf5
Create Date: 2018-08-02 17:57:10.483859

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a0c63733e5d2'
down_revision = 'e4311ef3ddf5'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket_holders', sa.Column('device_name_checkin', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket_holders', 'device_name_checkin')
    # ### end Alembic commands ###
