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
    interesse_treinamento: bool = False
    interesse_consultoria: bool = False
    interesse_certificacao: bool = False
    interesse_eventos: bool = False
    interesse_produtos: bool = False
    outros_interesses: Optional[str] = None

class ProspeccaoCriar(ProspeccaoBase):
    pass

class ProspeccaoResposta(ProspeccaoBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True
