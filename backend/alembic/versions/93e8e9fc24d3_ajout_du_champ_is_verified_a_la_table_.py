"""ajout du champ is_verified a la table users

Revision ID: 93e8e9fc24d3
Revises: 16aa7df35a39
Create Date: 2026-01-18 10:09:35.860148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93e8e9fc24d3'
down_revision: Union[str, Sequence[str], None] = '16aa7df35a39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
