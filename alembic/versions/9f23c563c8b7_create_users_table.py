"""create users table

Revision ID: 9f23c563c8b7
Revises: fd0588e2db89
Create Date: 2024-03-11 12:36:38.682044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f23c563c8b7'
down_revision: Union[str, None] = 'fd0588e2db89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
