from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
from fastapi_pagination.params import LimitOffsetParams
from sqlalchemy.exc import IntegrityError

from src.schemas.athlete import AtletaIn
from src.views.athlete import AtletaOut
from src.services.atleta import AtletaService
from src.security import login_required

router = APIRouter(prefix="/atletas", dependencies=[Depends(login_required)])

service = AtletaService()


@router.get("/", response_model=LimitOffsetPage[AtletaOut])
async def read_atletas(nome: str | None = None, cpf: str | None = None, params: LimitOffsetParams = Depends()):
    records = await service.read_all(limit=params.limit, skip=params.offset, nome=nome, cpf=cpf)
    return paginate(records, params)


@router.post("/", response_model=AtletaOut)
async def create_atleta(atleta: AtletaIn):
    try:
        return await service.create(atleta)
    except IntegrityError:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
