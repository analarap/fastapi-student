# Projeto FastAPI - AT1

Este projeto foi desenvolvido como parte da atividade avaliativa AT1.
O objetivo é criar uma API simples utilizando FastAPI, com integração contínua configurada no GitHub Actions.

## Estrutura do Projeto

```
fastapi-student/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── requirements.txt
├── .flake8
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

## Funcionalidades

A API utiliza um banco de dados em memória contendo os campos:

* ID
* Nome do aluno
* E-mail

A lista inicial contém um registro de exemplo.

### Rotas disponíveis

* **GET /alunos** – Lista todos os alunos.
* **GET /alunos/{id}** – Retorna um aluno específico pelo ID.
* **POST /alunos** – Cria um novo aluno.

## Como executar o projeto

1. Crie e ative o ambiente virtual:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Execute o servidor:

   ```
   uvicorn app.main:app --reload
   ```

4. Acesse em:

   ```
   http://127.0.0.1:8000
   ```

## Testes

Para rodar os testes com o Pytest:

```
pytest
```

Os testes validam:

* Sucesso das rotas principais.
* Tratamento de erros e falhas esperadas.

## Integração Contínua

O repositório contém um workflow do GitHub Actions configurado para executar automaticamente:

* Black (formatação de código)
* Flake8 (análise de estilo)
* Pytest (testes automatizados)

## Autor

Ana Silva
