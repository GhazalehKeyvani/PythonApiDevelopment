"""create posts table

Revision ID: a90b1adfe910
Revises: 2969db154a8e
Create Date: 2024-03-07 10:21:07.119048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a90b1adfe910'
down_revision: Union[str, None] = '2969db154a8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
