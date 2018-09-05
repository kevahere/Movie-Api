"""added email column

Revision ID: 6664ea777711
Revises: 85338c431b6d
Create Date: 2018-09-04 18:54:43.466714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6664ea777711'
down_revision = '85338c431b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_constraint('users_roles_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'roles_id')
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('roles_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_roles_id_fkey', 'users', 'roles', ['roles_id'], ['id'])
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###