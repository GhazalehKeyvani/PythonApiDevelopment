"""create users table

Revision ID: e795dd3e1709
Revises: 0b09f97138d2
Create Date: 2024-03-11 11:37:51.412657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e795dd3e1709'
down_revision: Union[str, None] = '0b09f97138d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
