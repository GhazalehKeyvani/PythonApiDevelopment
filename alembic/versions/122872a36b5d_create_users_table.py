"""create users table

Revision ID: 122872a36b5d
Revises: 3ab393ea8caf
Create Date: 2024-03-11 11:43:49.621612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '122872a36b5d'
down_revision: Union[str, None] = '3ab393ea8caf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
