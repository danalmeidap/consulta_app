from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class UsuarioCreate(SQLModel):
    nome: str
    email: str
    cpf: str
    data_nascimento: Optional[datetime] = None
    telefone: Optional[str] = None


class UsuarioRead(SQLModel):
    id: int
    nome: str
    email: str
    data_nascimento: Optional[datetime] = None
    telefone: Optional[str] = None
    criado_em: datetime
