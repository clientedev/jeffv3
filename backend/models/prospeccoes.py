from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Time, Text, Boolean
from sqlalchemy.orm import relationship
from backend.database import Base
from datetime import datetime

class Prospeccao(Base):
    __tablename__ = "prospeccoes"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    consultor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data_ligacao = Column(Date)
    hora_ligacao = Column(Time)
    resultado = Column(String(100))
    observacoes = Column(Text)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    porte = Column(String(50))
    lr = Column(String(50))
    id_externo = Column(String(100))
    cfr = Column(String(50))
    tipo_producao = Column(String(200))
    data_prospeccao = Column(Date)
    follow_up = Column(Date)
    
    nome_contato = Column(String(200))
    cargo = Column(String(200))
    celular = Column(String(50))
    telefone = Column(String(50))
    telefone_contato = Column(String(50))
    email_contato = Column(String(200))
    cargo_contato = Column(String(200))
    cnpj = Column(String(50))
    
    status_prospeccao = Column(String(100))
    responsavel = Column(String(200))
    opcoes = Column(Text)
    retorno = Column(Text)
    observacoes_prospeccao = Column(Text)
    
    interesse_treinamento = Column(Boolean, default=False)
    interesse_consultoria = Column(Boolean, default=False)
    interesse_certificacao = Column(Boolean, default=False)
    interesse_eventos = Column(Boolean, default=False)
    interesse_produtos = Column(Boolean, default=False)
    interesse_seguranca = Column(Boolean, default=False)
    interesse_meio_ambiente = Column(Boolean, default=False)
    outros_interesses = Column(Text)
    
    potencial_negocio = Column(String(50))
    status_follow_up = Column(String(100))
    proxima_prospeccao_data = Column(Date)

    empresa = relationship("Empresa", back_populates="prospeccoes")
    consultor = relationship("Usuario", foreign_keys=[consultor_id], overlaps="prospeccoes")
    agendamentos = relationship("Agendamento", back_populates="prospeccao")
