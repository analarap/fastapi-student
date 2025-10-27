from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Aluno(BaseModel):
    id: int
    nome: str
    email: EmailStr


alunos = [
    {"id": 1, "nome": "Ana Silva", "email": "ana.silva@example.com"},
    {"id": 2, "nome": "Ãcaro Silva", "email": "icaro.silva@example.com"},
    {"id": 3, "nome": "Gustavo Silva", "email": "guga.silva@example.com"},
]


@app.get("/alunos")
def listar_alunos():
    return alunos


@app.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            return aluno
    raise HTTPException(status_code=404, detail="Aluno nÃ£o encontrado")


@app.post("/alunos")
def criar_aluno(aluno: Aluno):
    if any(a["id"] == aluno.id for a in alunos):
        raise HTTPException(status_code=400, detail="ID jÃ¡ existente")
    alunos.append(aluno.dict())
    return aluno.dict()
