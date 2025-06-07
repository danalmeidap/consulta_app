import os

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from consulta_app.app import app
from consulta_app.db.dependencies import get_session
from consulta_app.models.usuario import Usuario  # noqa: F401

DATABASE_TEST_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_TEST_URL, connect_args={"check_same_thread": False})  # noqa: E501


def override_get_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def preparar_banco():
    SQLModel.metadata.create_all(engine)
    yield
    # ❌ Apagar o banco de teste após os testes
    if os.path.exists("test.db"):
        os.remove("test.db")


@pytest.fixture
def usuario_criado():
    resposta = client.post("/usuarios/", json={
        "nome": "Dan",
        "email": "dan@email.com",
        "cpf": "12345678900",
        "telefone": "7999999999"
    })
    return resposta.json()


def test_criar_usuario():
    resposta = client.post("/usuarios/", json={
        "nome": "Dan",
        "email": "dan@email.com",
        "cpf": "98765432100",
        "telefone": "7998888888"
    })
    assert resposta.status_code == status.HTTP_201_CREATED
    dados = resposta.json()
    assert dados["nome"] == "Dan"
    assert dados["email"] == "dan@email.com"
