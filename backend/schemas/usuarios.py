from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    email: EmailStr
    nome: str
    tipo: str

class UsuarioCriar(UsuarioBase):
    senha: str

class UsuarioResposta(UsuarioBase):
    id: int

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioResposta
