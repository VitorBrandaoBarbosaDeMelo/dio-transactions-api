from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from src.schemas.athlete import AtletaIn
from src.views.athlete import AtletaOut
from src.services.atleta import AtletaService
from src.security import login_required

router = APIRouter(prefix="/atletas", dependencies=[Depends(login_required)])

service = AtletaService()


@router.get("/", response_model=list[AtletaOut])
async def read_atletas(nome: str | None = None, cpf: str | None = None, limit: int = 10, offset: int = 0):
    return await service.read_all(limit=limit, skip=offset, nome=nome, cpf=cpf)


@router.post("/", response_model=AtletaOut)
async def create_atleta(atleta: AtletaIn):
    try:
        return await service.create(atleta)
    except IntegrityError:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
