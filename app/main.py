from fastapi import FastAPI, status, Depends
from fastapi.params import Body
from app.schemas.mensagens import Mensagem
import app.models.mensagens as mensagens
from app.database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from app.routers import mensagens as msg_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
'http://localhost:3000'
]
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']
)

mensagens.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(msg_router.router)

@app.get("/")
def root():
    return {"status":"funcionando"}