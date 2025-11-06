from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class TipoUsuario(str, enum.Enum):
    admin = "admin"
    consultor = "consultor"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    tipo = Column(Enum(TipoUsuario), nullable=False, default=TipoUsuario.consultor)
    
    empresas_atribuidas = relationship("AtribuicaoEmpresa", back_populates="consultor")
