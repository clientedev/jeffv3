from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from backend.database import Base
from datetime import datetime

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    empresa = Column(String, nullable=False, index=True)
    cnpj = Column(String(18), unique=True, index=True)
    sigla = Column(String(20))
    porte = Column(String(50))
    er = Column(String(50))
    carteira = Column(String(20))
    endereco = Column(String(255))
    bairro = Column(String(100))
    zona = Column(String(50))
    municipio = Column(String(100), index=True)
    estado = Column(String(2))
    pais = Column(String(100))
    area = Column(String(100))
    cnae_principal = Column(String(20))
    descricao_cnae = Column(Text)
    tipo_empresa = Column(String(100))
    data_cadastro = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    numero_funcionarios = Column(Integer)
    observacao = Column(Text)

    prospeccoes = relationship("Prospeccao", back_populates="empresa")
