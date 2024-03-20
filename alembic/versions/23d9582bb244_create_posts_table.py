"""create posts table

Revision ID: 23d9582bb244
Revises: 115f16399635
Create Date: 2024-03-07 11:38:51.061276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23d9582bb244'
down_revision: Union[str, None] = '115f16399635'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
