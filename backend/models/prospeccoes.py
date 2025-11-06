from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Time, Text
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

    empresa = relationship("Empresa", back_populates="prospeccoes")
    consultor = relationship("Usuario")
    agendamentos = relationship("Agendamento", back_populates="prospeccao")
