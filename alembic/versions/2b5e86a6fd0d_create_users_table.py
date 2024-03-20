"""create users table

Revision ID: 2b5e86a6fd0d
Revises: edd32a5fd853
Create Date: 2024-03-11 11:40:33.612726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b5e86a6fd0d'
down_revision: Union[str, None] = 'edd32a5fd853'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
