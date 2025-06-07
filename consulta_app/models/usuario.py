from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):  # noqa: F821
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100, nullable=False)
    email: str = Field(max_length=100, nullable=False, unique=True)
    cpf: str = Field(max_length=11, nullable=False, unique=True)
    data_nascimento: Optional[datetime] = None
    telefone: Optional[str] = None
    criado_em: datetime = Field(default_factory=datetime.utcnow)
