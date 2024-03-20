"""create posts table

Revision ID: 08eefade22d8
Revises: b6d8741e67bc
Create Date: 2024-03-06 20:21:26.024263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08eefade22d8'
down_revision: Union[str, None] = 'b6d8741e67bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
