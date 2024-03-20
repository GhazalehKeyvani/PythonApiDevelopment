"""create votes table

Revision ID: 6e86dcc4ac4d
Revises: 5e310e92fccf
Create Date: 2024-03-20 11:06:47.616899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '6e86dcc4ac4d'
down_revision = '5e310e92fccf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'votes',  # Table name should be 'votes' (lowercase)
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),  # Added auto-incrementing id column
        sa.Column('user_id', sa.Integer(),  nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'],['posts.id'], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(['user_id'],['users.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('users.id', 'posts.id'),
        
    )


def downgrade():
    op.drop_table('votes')  # Correct table name for downgrade
    pass
