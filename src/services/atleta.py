from databases.interfaces import Record
from sqlalchemy.exc import IntegrityError

from src.database import database
from src.models.atleta import athletes
from src.schemas.athlete import AtletaIn


class AtletaService:
    async def read_all(self, limit: int, skip: int = 0, nome: str | None = None, cpf: str | None = None) -> list[Record]:
        query = athletes.select()

        if nome:
            query = query.where(athletes.c.nome.ilike(f"%{nome}%"))

        if cpf:
            query = query.where(athletes.c.cpf == cpf)

        query = query.limit(limit).offset(skip)

        return await database.fetch_all(query)

    async def create(self, atleta: AtletaIn) -> Record:
        try:
            command = (
                athletes.insert().values(
                    nome=atleta.nome,
                    cpf=atleta.cpf,
                    centro_treinamento=atleta.centro_treinamento,
                    categoria=atleta.categoria,
                )
            )
            atleta_id = await database.execute(command)

            query = athletes.select().where(athletes.c.id == atleta_id)
            return await database.fetch_one(query)
        except IntegrityError:
            raise
