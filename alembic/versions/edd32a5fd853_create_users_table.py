"""create users table

Revision ID: edd32a5fd853
Revises: e795dd3e1709
Create Date: 2024-03-11 11:38:42.647911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edd32a5fd853'
down_revision: Union[str, None] = 'e795dd3e1709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
