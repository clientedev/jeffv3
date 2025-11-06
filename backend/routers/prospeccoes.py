from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models import Prospeccao, Usuario, Empresa
from backend.schemas.prospeccoes import ProspeccaoCriar, ProspeccaoResposta
from backend.auth.security import obter_usuario_atual, obter_usuario_admin

router = APIRouter(prefix="/api/prospeccoes", tags=["Prospecções"])

@router.post("/", response_model=ProspeccaoResposta)
def criar_prospeccao(
    prospeccao: ProspeccaoCriar,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_atual)
):
    empresa = db.query(Empresa).filter(Empresa.id == prospeccao.empresa_id).first()
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não encontrada"
        )
    
    consultor = db.query(Usuario).filter(Usuario.id == prospeccao.consultor_id).first()
    if not consultor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consultor não encontrado"
        )
    
    if usuario.tipo != "admin" and usuario.id != prospeccao.consultor_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você só pode criar prospecções para si mesmo"
        )
    
    nova_prospeccao = Prospeccao(**prospeccao.model_dump())
    db.add(nova_prospeccao)
    db.commit()
    db.refresh(nova_prospeccao)
    return nova_prospeccao

@router.get("/", response_model=List[ProspeccaoResposta])
def listar_prospeccoes(
    skip: int = 0,
    limit: int = 100,
    empresa_id: int = None,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_atual)
):
    query = db.query(Prospeccao)
    
    if usuario.tipo != "admin":
        query = query.filter(Prospeccao.consultor_id == usuario.id)
    
    if empresa_id:
        query = query.filter(Prospeccao.empresa_id == empresa_id)
    
    prospeccoes = query.offset(skip).limit(limit).all()
    return prospeccoes

@router.get("/{prospeccao_id}", response_model=ProspeccaoResposta)
def obter_prospeccao(
    prospeccao_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_atual)
):
    prospeccao = db.query(Prospeccao).filter(Prospeccao.id == prospeccao_id).first()
    if not prospeccao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prospecção não encontrada"
        )
    
    if usuario.tipo != "admin" and prospeccao.consultor_id != usuario.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para acessar esta prospecção"
        )
    
    return prospeccao
