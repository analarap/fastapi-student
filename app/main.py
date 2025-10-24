from fastapi import FastAPI, HTTPException

app = FastAPI()

alunos = [
    {"id": 1, "nome": "Ana Silva", "email": "ana.silva@example.com"}
]


@app.get("/alunos")
def listar_alunos():
    return alunos


@app.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado")


@app.post("/alunos")
def criar_aluno(aluno: dict):
    if "id" not in aluno or "nome" not in aluno or "email" not in aluno:
        raise HTTPException(status_code=400, detail="Campos inválidos")
    alunos.append(aluno)
    return aluno
