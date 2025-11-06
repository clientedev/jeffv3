from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AtribuicaoEmpresaBase(BaseModel):
    consultor_id: int
    empresa_id: int
    ativa: bool = True

class AtribuicaoEmpresaCreate(AtribuicaoEmpresaBase):
    pass

class AtribuicaoEmpresaUpdate(BaseModel):
    ativa: Optional[bool] = None

class AtribuicaoEmpresaResponse(AtribuicaoEmpresaBase):
    id: int
    data_atribuicao: datetime
    data_desativacao: Optional[datetime] = None
    
    class Config:
        from_attributes = True
