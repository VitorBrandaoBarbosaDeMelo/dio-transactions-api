import sqlalchemy as sa

from src.database import metadata


athletes = sa.Table(
    "athletes",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("nome", sa.String(255), nullable=False),
    sa.Column("cpf", sa.String(14), nullable=False, unique=True, index=True),
    sa.Column("centro_treinamento", sa.String(255), nullable=True),
    sa.Column("categoria", sa.String(100), nullable=True),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
