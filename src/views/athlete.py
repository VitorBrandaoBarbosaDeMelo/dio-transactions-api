from pydantic import AwareDatetime, BaseModel, NaiveDatetime


class AtletaOut(BaseModel):
    id: int
    nome: str
    centro_treinamento: str | None = None
    categoria: str | None = None
    created_at: AwareDatetime | NaiveDatetime
