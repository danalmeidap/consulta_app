from typing import List, Optional

from sqlmodel import Session, select

from consulta_app.db.engine import engine
from consulta_app.models.usuario import Usuario
from consulta_app.schemas.usuario import UsuarioCreate


def criar_usuario(usuario: UsuarioCreate) -> Usuario:
    novo_usuario = Usuario(**usuario.model.dump())
    with Session(engine) as session:
        session.add(novo_usuario)
        session.commit()
        session.refresh(novo_usuario)
        return novo_usuario


def listar_usuarios() -> List[Usuario]:
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios


def buscar_usuario_por_id(usuario_id: int) -> Optional[Usuario]:
    with Session(engine) as session:
        return session.get(Usuario, usuario_id)


def atualizar_usuario(usuario_id: int, dados: UsuarioCreate) -> Optional[Usuario]:  # noqa: E501
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            return None
        for key, value in dados.obj.model.dump().items():
            setattr(usuario, key, value)
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario


def deletar_usuario(usuario_id: int) -> bool:
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            return False
        session.delete(usuario)
        session.commit()
        return True
