from fastapi import FastAPI

from consulta_app.db.engine import criar_banco
from consulta_app.routes import usuarios

app = FastAPI(title="Consulta App API")

criar_banco()  # cria as tabelas no primeiro run

app.include_router(usuarios.router)


@app.get("/", tags=["Root"])
def read_root():
    return {'message': 'Welcome to Consulta App!'}
