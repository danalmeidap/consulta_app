from typing import List, Optional

from sqlmodel import Session, select

from consulta_app.models.usuario import Usuario
from consulta_app.schemas.usuario import UsuarioCreate


def criar_usuario(usuario: UsuarioCreate, session: Session) -> Usuario:
    novo_usuario = Usuario(**usuario.model_dump())
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario


def listar_usuarios(session: Session) -> List[Usuario]:
    return session.exec(select(Usuario)).all()


def buscar_usuario_por_id(usuario_id: int, session: Session) -> Optional[Usuario]:  # noqa: E501
    return session.get(Usuario, usuario_id)


def atualizar_usuario(usuario_id: int, dados: UsuarioCreate, session: Session) -> Optional[Usuario]:  # noqa: E501
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return None
    for key, value in dados.model.dump().items():
        setattr(usuario, key, value)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def deletar_usuario(usuario_id: int, session: Session) -> bool:
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return False
    session.delete(usuario)
    session.commit()
    return True
