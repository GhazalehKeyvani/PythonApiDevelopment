"""create users table

Revision ID: 0b09f97138d2
Revises: 77a83bc97234
Create Date: 2024-03-11 11:36:57.258620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b09f97138d2'
down_revision: Union[str, None] = '77a83bc97234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
