"""create posts table

Revision ID: 1cf5bd398098
Revises: 08eefade22d8
Create Date: 2024-03-06 20:22:21.305226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cf5bd398098'
down_revision: Union[str, None] = '08eefade22d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
