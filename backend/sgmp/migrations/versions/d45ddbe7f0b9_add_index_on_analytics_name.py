"""Add index on analytics name.

Revision ID: d45ddbe7f0b9
Revises: 1e0b7b8ffdb3
Create Date: 2021-10-07 22:42:35.277432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd45ddbe7f0b9'
down_revision = '1e0b7b8ffdb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_analytics_name'), 'analytics', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_analytics_name'), table_name='analytics')
    # ### end Alembic commands ###
