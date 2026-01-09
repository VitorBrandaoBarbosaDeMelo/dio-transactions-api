"""Add athletes table

Revision ID: add_athletes_table
Revises: 09f7da264602
Create Date: 2026-01-09 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_athletes_table'
down_revision: Union[str, None] = '09f7da264602'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'athletes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=255), nullable=False),
        sa.Column('cpf', sa.String(length=14), nullable=False),
        sa.Column('centro_treinamento', sa.String(length=255), nullable=True),
        sa.Column('categoria', sa.String(length=100), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_athletes_cpf'), 'athletes', ['cpf'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_athletes_cpf'), table_name='athletes')
    op.drop_table('athletes')
