"""create posts table

Revision ID: 2969db154a8e
Revises: c49ff72de6bf
Create Date: 2024-03-07 09:58:07.845747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2969db154a8e'
down_revision: Union[str, None] = 'c49ff72de6bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
