"""create posts table

Revision ID: 115f16399635
Revises: 9602c75f6262
Create Date: 2024-03-07 11:31:56.074395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '115f16399635'
down_revision: Union[str, None] = '9602c75f6262'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
