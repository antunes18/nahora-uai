"""empty message

Revision ID: 887770f7fc9e
Revises: 7ea08dccea38
Create Date: 2025-07-16 11:21:50.559794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '887770f7fc9e'
down_revision: Union[str, None] = '7ea08dccea38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
