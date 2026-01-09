from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.controllers import account, auth, transaction, atleta
from src.database import database
from src.exceptions import AccountNotFoundError, BusinessError


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Operações de autenticação.",
    },
    {
        "name": "account",
        "description": "Operações para manter contas.",
    },
    {
        "name": "transaction",
        "description": "Operações para manter transações.",
    },
    {
        "name": "atleta",
        "description": "Operações para manter atletas.",
    },
]


app = FastAPI(
    title="API de Gestão de Atletas e Transações",
    version="1.0.0",
    summary="Microsserviço para gerenciar atletas, centros de treinamento e transações de contas correntes.",
    description="""
A API de Gestão de Atletas e Transações é um microsserviço completo para registrar e manter dados de atletas e suas atividades em centros de treinamento. 🏋️💪

## Atleta

* **Criar atletas**.
* **Listar atletas com filtros (nome, CPF)**.
* **Paginação com limit e offset**.

## Conta

* **Criar contas correntes**.
* **Listar contas**.
* **Listar transações da conta por ID**.

## Transação

* **Registrar depósitos e saques**.
* **Consultar histórico de transações**.

## Autenticação

* **Fazer login** para obter token JWT (para operações protegidas).
""",
    openapi_tags=tags_metadata,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])
app.include_router(atleta.router, tags=["atleta"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."})


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})
