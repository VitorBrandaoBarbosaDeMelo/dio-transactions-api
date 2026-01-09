from pydantic import BaseModel


class AtletaIn(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str | None = None
    categoria: str | None = None
