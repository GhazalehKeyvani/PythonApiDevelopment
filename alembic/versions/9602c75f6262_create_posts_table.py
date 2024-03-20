"""create posts table

Revision ID: 9602c75f6262
Revises: a90b1adfe910
Create Date: 2024-03-07 10:28:03.043377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9602c75f6262'
down_revision: Union[str, None] = 'a90b1adfe910'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
