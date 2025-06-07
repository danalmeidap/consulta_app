from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from consulta_app.db.dependencies import get_session
from consulta_app.repositories import usuario_repository as repo
from consulta_app.schemas.usuario import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRead)
def criar(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return repo.criar_usuario(usuario, session)


@router.get("/", response_model=list[UsuarioRead])
def listar(session: Session = Depends(get_session)):
    return repo.listar_usuarios(session)


@router.get("/{usuario_id}", response_model=UsuarioRead)
def buscar(usuario_id: int, session: Session = Depends(get_session)):
    usuario = repo.buscar_usuario_por_id(usuario_id, session)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioRead)
def atualizar(usuario_id: int, dados: UsuarioCreate, session: Session = Depends(get_session)):  # noqa: E501
    usuario = repo.atualizar_usuario(usuario_id, dados, session)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.delete("/{usuario_id}")
def deletar(usuario_id: int, session: Session = Depends(get_session)):
    sucesso = repo.deletar_usuario(usuario_id, session)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário removido com sucesso"}
