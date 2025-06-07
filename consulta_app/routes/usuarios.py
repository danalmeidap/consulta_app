from fastapi import APIRouter, HTTPException

from consulta_app.repositories import usuario_repository as repo
from consulta_app.schemas.usuario import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRead)
def criar(usuario: UsuarioCreate):
    return repo.criar_usuario(usuario)


@router.get("/", response_model=list[UsuarioRead])
def listar():
    return repo.listar_usuarios()


@router.get("/{usuario_id}", response_model=UsuarioRead)
def buscar(usuario_id: int):
    usuario = repo.buscar_usuario_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioRead)
def atualizar(usuario_id: int, dados: UsuarioCreate):
    usuario = repo.atualizar_usuario(usuario_id, dados)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.delete("/{usuario_id}")
def deletar(usuario_id: int):
    sucesso = repo.deletar_usuario(usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário removido com sucesso"}
