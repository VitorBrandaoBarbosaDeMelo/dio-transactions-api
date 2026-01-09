import asyncio
import sqlalchemy as sa
from src.database import database, engine
from src.models.athlete import athletes


async def seed_athletes():
    """Seed the athletes table with sample data."""
    athletes_data = [
        {
            "nome": "João Silva",
            "cpf": "12345678901",
            "centro_treinamento": "Centro de Treinamento São Paulo",
            "categoria": "Elite"
        },
        {
            "nome": "Maria Santos",
            "cpf": "98765432101",
            "centro_treinamento": "Centro de Treinamento Rio de Janeiro",
            "categoria": "Senior"
        },
        {
            "nome": "Carlos Oliveira",
            "cpf": "11122233344",
            "centro_treinamento": "Centro de Treinamento Belo Horizonte",
            "categoria": "Junior"
        },
        {
            "nome": "Ana Costa",
            "cpf": "55566677788",
            "centro_treinamento": "Centro de Treinamento Salvador",
            "categoria": "Elite"
        },
        {
            "nome": "Pedro Ferreira",
            "cpf": "99988877766",
            "centro_treinamento": "Centro de Treinamento Brasília",
            "categoria": "Senior"
        },
        {
            "nome": "Fernanda Lima",
            "cpf": "44455566677",
            "centro_treinamento": "Centro de Treinamento Curitiba",
            "categoria": "Junior"
        },
        {
            "nome": "Lucas Alves",
            "cpf": "22233344455",
            "centro_treinamento": "Centro de Treinamento Fortaleza",
            "categoria": "Elite"
        },
        {
            "nome": "Juliana Rocha",
            "cpf": "77788899900",
            "centro_treinamento": "Centro de Treinamento Recife",
            "categoria": "Senior"
        },
    ]

    await database.connect()
    try:
        for athlete in athletes_data:
            query = athletes.insert().values(**athlete)
            await database.execute(query)
        print(f"✅ {len(athletes_data)} atletas adicionados com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao adicionar atletas: {e}")
    finally:
        await database.disconnect()


if __name__ == "__main__":
    asyncio.run(seed_athletes())
