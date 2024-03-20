"""create users table

Revision ID: fd0588e2db89
Revises: 122872a36b5d
Create Date: 2024-03-11 12:34:41.792709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd0588e2db89'
down_revision: Union[str, None] = '122872a36b5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', 
     sa.Column('id',sa.Integer(), primary_key=True, nullable=False)
     , sa.Column('username', sa.String(), unique=True, nullable=False)
     , sa.Column('password', sa.String(), nullable=False)
     , sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
     , sa.Column('phone_number', sa.String()))
    pass


def downgrade():
    op.drop_table('users')
    pass