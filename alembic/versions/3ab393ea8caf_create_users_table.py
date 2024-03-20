"""create users table

Revision ID: 3ab393ea8caf
Revises: 2b5e86a6fd0d
Create Date: 2024-03-11 11:41:30.570399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ab393ea8caf'
down_revision: Union[str, None] = '2b5e86a6fd0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
