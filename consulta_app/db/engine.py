from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./banco.db"

engine = create_engine(DATABASE_URL, echo=True)


def criar_banco():
    from consulta_app.models.usuario import Usuario  # noqa: F401, PLC0415
    SQLModel.metadata.create_all(engine)
