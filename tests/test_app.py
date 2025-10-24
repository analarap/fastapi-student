from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_alunos_sucesso():
    response = client.get("/alunos")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_buscar_aluno_sucesso():
    response = client.get("/alunos/1")
    assert response.status_code == 200
    assert response.json()["nome"] == "Ana Silva"


def test_buscar_aluno_falha():
    response = client.get("/alunos/999")
    assert response.status_code == 404


def test_criar_aluno_sucesso():
    novo_aluno = {"id": 2, "nome": "Carlos Souza", "email": "carlos@example.com"}
    response = client.post("/alunos", json=novo_aluno)
    assert response.status_code == 200
    assert response.json()["id"] == 2


def test_criar_aluno_falha():
    aluno_invalido = {"id": 3, "nome": "Erro"}
    response = client.post("/alunos", json=aluno_invalido)
    assert response.status_code == 400
