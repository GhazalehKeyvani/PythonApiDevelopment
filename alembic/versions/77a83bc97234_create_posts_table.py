"""create posts table

Revision ID: 77a83bc97234
Revises: 9ace478a000e
Create Date: 2024-03-11 11:02:33.766200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77a83bc97234'
down_revision: Union[str, None] = '9ace478a000e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
