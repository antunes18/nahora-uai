"""empty message

Revision ID: e98a92682f38
Revises: 887770f7fc9e
Create Date: 2025-07-18 11:01:34.434832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e98a92682f38'
down_revision: Union[str, None] = '887770f7fc9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
