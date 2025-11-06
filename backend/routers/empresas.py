from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.database import get_db
from backend.models import Empresa, Usuario
from backend.schemas.empresas import EmpresaCriar, EmpresaResposta, EmpresaAtualizar
from backend.auth.security import obter_usuario_atual, obter_usuario_admin

router = APIRouter(prefix="/api/empresas", tags=["Empresas"])

@router.post("/", response_model=EmpresaResposta)
def criar_empresa(
    empresa: EmpresaCriar,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_admin)
):
    if empresa.cnpj:
        db_empresa = db.query(Empresa).filter(Empresa.cnpj == empresa.cnpj).first()
        if db_empresa:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Empresa com este CNPJ já cadastrada"
            )
    
    nova_empresa = Empresa(**empresa.model_dump())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

@router.get("/", response_model=List[EmpresaResposta])
def listar_empresas(
    skip: int = 0,
    limit: int = 100,
    nome: Optional[str] = None,
    cnpj: Optional[str] = None,
    municipio: Optional[str] = None,
    er: Optional[str] = None,
    carteira: Optional[str] = None,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_atual)
):
    query = db.query(Empresa)
    
    if nome:
        query = query.filter(Empresa.empresa.ilike(f"%{nome}%"))
    if cnpj:
        query = query.filter(Empresa.cnpj.ilike(f"%{cnpj}%"))
    if municipio:
        query = query.filter(Empresa.municipio.ilike(f"%{municipio}%"))
    if er:
        query = query.filter(Empresa.er == er)
    if carteira:
        query = query.filter(Empresa.carteira == carteira)
    
    empresas = query.offset(skip).limit(limit).all()
    return empresas

@router.get("/{empresa_id}", response_model=EmpresaResposta)
def obter_empresa(
    empresa_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_atual)
):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não encontrada"
        )
    return empresa

@router.put("/{empresa_id}", response_model=EmpresaResposta)
def atualizar_empresa(
    empresa_id: int,
    empresa_atualizada: EmpresaAtualizar,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_admin)
):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não encontrada"
        )
    
    for key, value in empresa_atualizada.model_dump(exclude_unset=True).items():
        setattr(empresa, key, value)
    
    db.commit()
    db.refresh(empresa)
    return empresa

@router.delete("/{empresa_id}")
def deletar_empresa(
    empresa_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_admin)
):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não encontrada"
        )
    
    db.delete(empresa)
    db.commit()
    return {"detail": "Empresa deletada com sucesso"}
