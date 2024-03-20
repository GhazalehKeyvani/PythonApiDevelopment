"""create users table

Revision ID: a16430b39c81
Revises: 9f23c563c8b7
Create Date: 2024-03-11 12:37:28.753991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a16430b39c81'
down_revision: Union[str, None] = '9f23c563c8b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
