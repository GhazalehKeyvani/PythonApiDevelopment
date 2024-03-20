"""create posts table

Revision ID: 9ace478a000e
Revises: 23d9582bb244
Create Date: 2024-03-07 11:44:24.380577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ace478a000e'
down_revision: Union[str, None] = '23d9582bb244'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
