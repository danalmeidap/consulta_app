from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from consulta_app.db.dependencies import get_session
from consulta_app.repositories import usuario_repository as repo
from consulta_app.schemas.usuario import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)  # noqa: E501
def criar(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return repo.criar_usuario(usuario, session)


@router.get("/", response_model=list[UsuarioRead], status_code=status.HTTP_200_OK)  # noqa: E501
def listar(session: Session = Depends(get_session)):
    return repo.listar_usuarios(session)


@router.get("/{usuario_id}", response_model=UsuarioRead, status_code=status.HTTP_200_OK)  # noqa: E501
def buscar(usuario_id: int, session: Session = Depends(get_session)):
    usuario = repo.buscar_usuario_por_id(usuario_id, session)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")  # noqa: E501
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioRead, status_code=status.HTTP_200_OK)  # noqa: E501
def atualizar(usuario_id: int, dados: UsuarioCreate, session: Session = Depends(get_session)):  # noqa: E501
    usuario = repo.atualizar_usuario(usuario_id, dados, session)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")  # noqa: E501
    return usuario


@router.delete("/{usuario_id}", status_code=status.HTTP_200_OK)
def deletar(usuario_id: int, session: Session = Depends(get_session)):
    sucesso = repo.deletar_usuario(usuario_id, session)
    if not sucesso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")  # noqa: E501
    return {"mensagem": "Usuário removido com sucesso"}
