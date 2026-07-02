from fastapi import FastAPI, status, Depends
from fastapi.params import Body
from app.schemas.mensagens import Mensagem
import app.models.mensagens as mensagens
from app.database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from app.routers import mensagens as msg_router
from fastapi.middleware.cors import CORSMiddleware
from app.models import mensagens as mensagens_model

mensagens_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000",
    "http://127.0.0.1:3000","http://localhost:5173","http://127.0.0.1:52563"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(msg_router.router)

@app.get("/")
def root():
    return {"status":"funcionando"}