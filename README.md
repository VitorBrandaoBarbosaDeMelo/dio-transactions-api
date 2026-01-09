# API de Gestão de Atletas 🏋️💪

Uma API RESTful moderna e assíncrona construída com **FastAPI** para gerenciar atletas e seus centros de treinamento.

## 📋 O que é essa API?

<img width="2752" height="1536" alt="image" src="https://github.com/user-attachments/assets/bd501a75-a0b9-48ba-ad6c-bbd21b2e918c" />
<img width="524" height="272" alt="image" src="https://github.com/user-attachments/assets/12423b96-028d-43b0-9bcd-6516252b010e" /> <img width="250" height="136" alt="image" src="https://github.com/user-attachments/assets/74b72614-49e1-4423-b787-fe57d8fefd07" />




Esta API permite:
- **Criar atletas** com nome, CPF, centro de treinamento e categoria
- **Listar atletas** com filtros por nome e CPF
- **Paginação** com parâmetros limit e offset
- **Tratamento de erros** com mensagens customizadas para integridade de dados

## 🚀 Implementações e Modificações

### 1. **Modelo de Atleta** (`src/models/athlete.py`)
- Tabela `athletes` com campos:
  - `id` (chave primária)
  - `nome` (String, obrigatório)
  - `cpf` (String, único e obrigatório)
  - `centro_treinamento` (String, opcional)
  - `categoria` (String, opcional - Elite, Senior, Junior)
  - `created_at` (Timestamp com timezone)

### 2. **Query Parameters** (`src/controllers/atleta.py`)
Implementados filtros nos endpoints:
- `nome`: Filtra atletas por nome (busca parcial/case-insensitive)
- `cpf`: Filtra atleta por CPF (busca exata)
- `limit`: Quantidade de registros a retornar (padrão: 10)
- `offset`: Deslocamento para paginação (padrão: 0)

### 3. **Response Customizado** (`src/views/athlete.py`)
Endpoint GET /atletas retorna:
```json
{
  "id": 1,
  "nome": "João Silva",
  "centro_treinamento": "Centro de Treinamento São Paulo",
  "categoria": "Elite",
  "created_at": "2026-01-09T10:30:00Z"
}
```

### 4. **Tratamento de Integridade de Dados** (`src/services/atleta.py`)
- Captura exceção `sqlalchemy.exc.IntegrityError`
- Retorna status **303** com mensagem:
  ```json
  {
    "detail": "Já existe um atleta cadastrado com o cpf: 12345678901"
  }
  ```

### 5. **Paginação** 
- Implementada com query parameters `limit` e `offset`
- Permite consultas eficientes com grandes volumes de dados

### 6. **Endpoints Públicos**
Removida autenticação de `/atletas` para facilitar testes (endpoints de `/auth` e `/accounts` mantêm autenticação JWT)

### 7. **Documentação em Português**
- API renomeada para "API de Gestão de Atletas"
- Descrições dos endpoints em português
- Documentação clara no Swagger

### 8. **Migration Alembic** (`migrations/versions/add_athletes_table.py`)
- Cria tabela `athletes` com índice único no `cpf`
- Suporta downgrade para reverter alterações

### 9. **Script de Seed** (`seed.py`)
Insere 8 atletas de exemplo para facilitar testes:
- João Silva (CPF: 12345678901) - Elite - São Paulo
- Maria Santos (CPF: 98765432101) - Senior - Rio de Janeiro
- Carlos Oliveira (CPF: 11122233344) - Junior - Belo Horizonte
- Ana Costa (CPF: 55566677788) - Elite - Salvador
- Pedro Ferreira (CPF: 99988877766) - Senior - Brasília
- Fernanda Lima (CPF: 44455566677) - Junior - Curitiba
- Lucas Alves (CPF: 22233344455) - Elite - Fortaleza
- Juliana Rocha (CPF: 77788899900) - Senior - Recife

## 🛠️ Tecnologias

- **FastAPI**: Framework web assíncrono
- **SQLAlchemy**: ORM para banco de dados
- **Alembic**: Versionamento de schema do banco
- **Pydantic**: Validação de dados
- **SQLite**: Banco de dados local
- **Uvicorn**: Servidor ASGI

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/dio-transactions-api.git
cd dio-transactions-api
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
cp .env.example .env
alembic upgrade head
```

### 5. Popule com dados de teste
```bash
python seed.py
```

## ▶️ Como Rodar

### Iniciar o servidor
```bash
uvicorn src.main:app --reload
```

O servidor estará disponível em: `http://localhost:8000`

### Acessar a documentação interativa
```
http://localhost:8000/docs
```

## 📊 Exemplos de Uso

### Listar todos os atletas
```bash
curl -X GET "http://localhost:8000/atletas?limit=10&offset=0"
```

### Filtrar por nome
```bash
curl -X GET "http://localhost:8000/atletas?nome=João&limit=10"
```

### Filtrar por CPF
```bash
curl -X GET "http://localhost:8000/atletas?cpf=12345678901"
```

### Criar um novo atleta
```bash
curl -X POST "http://localhost:8000/atletas" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Roberto Costa",
    "cpf": "12345678902",
    "centro_treinamento": "Centro de Treinamento Manaus",
    "categoria": "Elite"
  }'
```

### Erro ao tentar CPF duplicado
```json
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678901"
}
```

## 📸 Screenshots

### Documentação Swagger (OpenAPI)
Visualize a documentação interativa da API:

![Swagger Documentation](images/swagger_docs.png)

### Tabela de Atletas
Lista completa dos 8 atletas cadastrados:

![Athletes Table](images/athletes_table.png)

## 📁 Estrutura do Projeto

```
desafio/
├── src/
│   ├── controllers/       # Rotas e endpoints
│   │   └── atleta.py      # GET /atletas, POST /atletas
│   ├── services/          # Lógica de negócio
│   │   └── atleta.py      # Serviço de atletas
│   ├── models/            # Modelos de dados
│   │   └── athlete.py     # Tabela de atletas
│   ├── schemas/           # Validação Pydantic
│   │   └── athlete.py     # AtletaIn (input)
│   ├── views/             # Response models
│   │   └── athlete.py     # AtletaOut (output)
│   ├── main.py            # Aplicação FastAPI
│   ├── config.py          # Configurações
│   └── database.py        # Conexão com BD
├── migrations/            # Scripts Alembic
│   └── versions/
│       └── add_athletes_table.py
├── seed.py                # Script para popular BD
├── requirements.txt       # Dependências
├── .env.example           # Variáveis de exemplo
└── README.md              # Este arquivo
```

## 🔧 Configuração

### Variáveis de Ambiente (.env)
```
ENVIRONMENT=local
DATABASE_URL=sqlite:///./bank.db
```

## 📝 API Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/atletas` | Lista atletas com filtros e paginação |
| POST | `/atletas` | Cria um novo atleta |
| GET | `/docs` | Documentação Swagger (OpenAPI) |

## ✅ Status do Projeto

- ✅ Modelo de Atleta implementado
- ✅ Endpoints GET e POST funcionando
- ✅ Filtros por nome e CPF
- ✅ Paginação com limit/offset
- ✅ Tratamento de integridade (CPF único)
- ✅ Respostas customizadas
- ✅ Documentação em português
- ✅ Script seed com 8 atletas
- ✅ Migration Alembic
- ✅ Repositório GitHub

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

**Vitor Brandão Barbosa**

Desenvolvido como desafio da **Trilha Python DIO - Guilherme Carvalho**

---

**Última atualização:** 9 de Janeiro de 2026
