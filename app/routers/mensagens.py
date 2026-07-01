from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.mensagens import Mensagem
from app.models.mensagens import Model_Mensagem
from app.database import get_db

router = APIRouter(
    prefix="/mensagens",
    tags=["mensagens"]
)

@router.get("/", response_model=List[Mensagem], status_code=status.HTTP_200_OK)
async def buscar_valores (db: Session = Depends(get_db), skip: int=0, limit: int=100):
    mensagens=db.query(Model_Mensagem).offset(skip).limit(limit).all()
    return mensagens

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_mensagem(nova_mensagem: Mensagem, db_session: Session = Depends(get_db)):
    mensagem_criada = Model_Mensagem(**nova_mensagem.model_dump())
    db_session.add(mensagem_criada)
    db_session.commit()
    db_session.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}