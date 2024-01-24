"""empty message

Revision ID: 13fee054ad82
Revises: 55209c9a70ce
Create Date: 2024-01-21 23:39:01.838265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13fee054ad82'
down_revision = '55209c9a70ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_activated', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_activated')

    # ### end Alembic commands ###
