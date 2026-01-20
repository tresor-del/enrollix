"""rename password to hashed_password

Revision ID: 820ac6683106
Revises: 93e8e9fc24d3
Create Date: 2026-01-20 19:35:02.567808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '820ac6683106'
down_revision: Union[str, Sequence[str], None] = '93e8e9fc24d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        'users',
        'password',
        new_column_name='hashed_password'
    )


def downgrade():
    op.alter_column(
        'users',
        'hashed_password',
        new_column_name='password'
    )
