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
    
    porte: Optional[str] = None
    lr: Optional[str] = None
    id_externo: Optional[str] = None
    cfr: Optional[str] = None
    tipo_producao: Optional[str] = None
    data_prospeccao: Optional[date] = None
    follow_up: Optional[date] = None
    
    nome_contato: Optional[str] = None
    cargo: Optional[str] = None
    celular: Optional[str] = None
    telefone: Optional[str] = None
    telefone_contato: Optional[str] = None
    email_contato: Optional[str] = None
    cargo_contato: Optional[str] = None
    cnpj: Optional[str] = None
    
    status_prospeccao: Optional[str] = None
    responsavel: Optional[str] = None
    opcoes: Optional[str] = None
    retorno: Optional[str] = None
    observacoes_prospeccao: Optional[str] = None
    
    interesse_treinamento: bool = False
    interesse_consultoria: bool = False
    interesse_certificacao: bool = False
    interesse_eventos: bool = False
    interesse_produtos: bool = False
    interesse_seguranca: bool = False
    interesse_meio_ambiente: bool = False
    outros_interesses: Optional[str] = None
    
    potencial_negocio: Optional[str] = None
    status_follow_up: Optional[str] = None
    proxima_prospeccao_data: Optional[date] = None

class ProspeccaoCriar(ProspeccaoBase):
    pass

class ProspeccaoResposta(ProspeccaoBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True
