from fastapi import FastAPI
from models import Socio, Equipe, Plano, Contrato, Beneficio, Associacao
from typing import List
from bd.db import DataBase

app = FastAPI()
db = DataBase('./bd/data.db')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/socios")
async def get_socios() -> List[Socio]:
    return db.get_socios()

@app.get("/equipes")
async def get_equipes() -> List[Equipe]:
    return db.get_equipes()

@app.get("/planos")
async def get_plano() -> List[Plano]:
    return db.get_planos()

@app.get("/contratos")
async def get_contratos() -> List[Contrato]:
    return db.get_contratos()

@app.get("/beneficios")
async def get_beneficios() ->List[Beneficio]:
    return db.get_beneficios()

@app.get("/associacoes")
async def get_associacoes() -> List[Associacao]:
    return db.get_associacoes()

@app.post("/socios")
async def create_socio(socio: Socio) -> Socio:
    db.create_socio(socio=socio)
    
    return db.get_socio_by_id(socio.cpf)

@app.post("/equipes")
async def create_equipe(equipe: Equipe) -> Equipe:
    db.create_equipe(equipe=equipe)
    
    return db.get_equipe_by_name(equipe.nome)[0]

@app.post("/planos")
async def create_plano(plano: Plano) -> Plano:
    db.create_plano(plano=plano)
    
    return db.get_plano_by_id(plano.categoria)

@app.post("/contratos")
async def create_contrato(contrato: Contrato) -> Contrato:
    db.create_contrato(contrato=contrato)
    
    return contrato

@app.post("/beneficios")
async def create_beneficio(beneficio: Beneficio) -> Beneficio:
    db.create_beneficio(beneficio=beneficio)
    
    return beneficio

@app.post("/associacoes")
async def create_associacao(associacao: Associacao) -> Associacao:
    db.create_associacao(associacao=associacao)
    
    return associacao