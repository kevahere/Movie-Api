"""addded a column to the user

Revision ID: 320e19381c63
Revises: 003ca7c272fd
Create Date: 2018-09-04 11:52:11.272747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320e19381c63'
down_revision = '003ca7c272fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###