"""add foreign-key to posts table

Revision ID: 5e310e92fccf
Revises: a16430b39c81
Create Date: 2024-03-11 13:08:18.851452

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e310e92fccf'
down_revision: Union[str, None] = 'a16430b39c81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
