"""Change: product name unique

Revision ID: 07ac7679d80e
Revises: 
Create Date: 2021-12-07 11:31:46.549979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ac7679d80e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_joined_at', table_name='users')
    op.drop_index('ix_users_role', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_products_name', table_name='products')
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.create_index('ix_products_name', 'products', ['name'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('role', sa.INTEGER(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.Column('confirmed_email', sa.BOOLEAN(), nullable=True),
    sa.Column('pw_hash', sa.VARCHAR(length=102), nullable=True),
    sa.Column('joined_at', sa.VARCHAR(length=14), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_role', 'users', ['role'], unique=False)
    op.create_index('ix_users_joined_at', 'users', ['joined_at'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    # ### end Alembic commands ###
