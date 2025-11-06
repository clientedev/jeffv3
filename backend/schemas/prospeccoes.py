from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date, time

class ProspeccaoBase(BaseModel):
    empresa_id: int
    consultor_id: int
    data_ligacao: Optional[date] = None
    hora_ligacao: Optional[time] = None
    resultado: Optional[str] = None
    observacoes: Optional[str] = None

class ProspeccaoCriar(ProspeccaoBase):
    pass

class ProspeccaoResposta(ProspeccaoBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True
