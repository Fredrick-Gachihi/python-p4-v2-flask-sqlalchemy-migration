"""add Department

Revision ID: bc8770c40376
Revises: 5e0cbdf1f23e
Create Date: 2024-06-28 14:31:18.569993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc8770c40376'
down_revision = '5e0cbdf1f23e'
branch_labels = None
depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.create_table('department',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(), nullable=False),
#     sa.Column('address', sa.String(), nullable=True),
#     sa.PrimaryKeyConstraint('id')
#     )
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_table('department')
#     # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
