from fastapi import FastAPI, HTTPException
from bd.models import Socio, Equipe, Plano, Contrato, Beneficio, Associacao, SocioUpdate, EquipeUpdate, PlanoUpdate, ContratoUpdate, RelatorioReceita, RelatorioGastosSocios, RelatorioSociosAtivos
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

@app.get("/socios/{cpf}")
async def get_socio_by_id(cpf: str) -> Socio:
    socio = db.get_socio_by_id(cpf=cpf)

    if socio is None:
        raise HTTPException(status_code=404, detail=f'Sócio com cpf: {cpf} não foi encontrado')
    
    return socio

@app.get("/socios/pesquisar/{nome}")
async def get_socio_by_name(nome: str) -> List[Socio]:
    return db.get_socio_by_name(nome=nome)

@app.get("/equipes")
async def get_equipes() -> List[Equipe]:
    return db.get_equipes()

@app.get("/equipes/{id}")
async def get_equipe_by_id(id: int) -> Equipe:
    equipe = db.get_equipe_by_id(id=id)

    if equipe is None:
        raise HTTPException(status_code=404, detail=f'Equipe com id: {id} não foi encontrada')
    
    return equipe

@app.get("/equipes/pesquisar/{nome}")
async def get_equipe_by_name(nome: str) -> List[Equipe]:
    return db.get_equipe_by_name(nome=nome)

@app.get("/planos")
async def get_plano() -> List[Plano]:
    return db.get_planos()

@app.get("/planos/{categoria}")
async def get_plano_by_categoria(categoria: str) -> Plano:
    plano = db.get_plano_by_id(categoria=categoria)

    if plano is None:
        raise HTTPException(status_code=404, detail=f'Plano com categoria: {categoria} não foi encontrado')
    
    return plano

@app.get("/contratos")
async def get_contratos() -> List[Contrato]:
    return db.get_contratos()

@app.get("/contratos/{id}")
async def get_contrato_by_id(id: int) -> Contrato:
    contrato = db.get_contrato_by_id(id=id)

    if contrato is None:
        raise HTTPException(status_code=404, detail=f'Contrato com id: {id} não foi encontrado')
    
    return contrato

@app.get("/beneficios")
async def get_beneficios() ->List[Beneficio]:
    return db.get_beneficios()

@app.get("/beneficios/pesquisar/{categoria}")
async def get_beneficios_by_categoria(categoria: str) -> List[Beneficio]:
    return db.get_beneficio_by_cat(categoria=categoria)

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

@app.put("/socios/{cpf}")
async def update_socios(cpf: str, socio: SocioUpdate) -> Socio:
    atual = db.get_socio_by_id(cpf=cpf)

    if atual is None:
        raise HTTPException(status_code=404, detail=f'Sócio com cpf: {cpf} não foi encontrado')

    new_values = socio.dict(exclude_none=True)

    for key, value in atual.dict().items():
        if key not in new_values.keys():
            new_values[key] = value
    
    updated = Socio(**new_values)

    db.update_socio(socio=updated)

    return updated

@app.put("/equipes/{id}")
async def update_equipes(id: int, equipe: EquipeUpdate) -> Equipe:
    atual = db.get_equipe_by_id(id=id)

    if atual is None:
        raise HTTPException(status_code=404, detail=f'Equipe com id: {id} não foi encontrada')

    new_values = equipe.dict(exclude_none=True)

    for key, value in atual.dict().items():
        if key not in new_values.keys():
            new_values[key] = value
    
    updated = Equipe(**new_values)

    db.update_equipe(equipe=updated)

    return updated

@app.put("/planos/{categoria}")
async def update_planos(categoria: str, plano: PlanoUpdate) -> Plano:
    atual = db.get_plano_by_id(categoria=categoria)

    if atual is None:
        raise HTTPException(status_code=404, detail=f'Plano com categoria: {categoria} não foi encontrado')

    new_values = plano.dict(exclude_none=True)

    for key, value in atual.dict().items():
        if key not in new_values.keys():
            new_values[key] = value
    
    updated = Plano(**new_values)

    db.update_plano(plano=updated)

    return updated

@app.put("/contratos/{id}")
async def update_contratos(id: int, contrato: ContratoUpdate) -> Contrato:
    atual = db.get_contrato_by_id(id=id)

    if atual is None:
        raise HTTPException(status_code=404, detail=f'Contrato com id: {id} não foi encontrado')

    new_values = contrato.dict(exclude_none=True)

    for key, value in atual.dict().items():
        if key not in new_values.keys():
            new_values[key] = value
    
    updated = Contrato(**new_values)

    db.update_contrato(contrato=updated)

    return updated

@app.delete("/socios/{cpf}")
async def delete_socio(cpf: str) -> Socio:
    row = db.get_socio_by_id(cpf=cpf)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Sócio com cpf: {cpf} não foi encontrado')
    
    db.delete_socio(socio=row)

    return row

@app.delete("/equipes/{id}")
async def delete_equipe(id: int) -> Equipe:
    row = db.get_equipe_by_id(id=id)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Equipe com id: {id} não foi encontrada')
    
    db.delete_equipe(equipe=row)

    return row

@app.delete("/planos/{categoria}")
async def delete_plano(categoria: str) -> Plano:
    row = db.get_plano_by_id(categoria=categoria)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Plano com categoria: {categoria} não foi encontrado')
    
    db.delete_plano(plano=row)

    return row

@app.delete("/contratos/{id}")
async def delete_contrato(id: int) -> Contrato:
    row = db.get_contrato_by_id(id=id)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Contrato com id: {id} não foi encontrado')
    
    db.delete_contrato(contrato=row)

    return row

@app.delete("/beneficios/{categoria}/{beneficio}")
async def delete_beneficio(categoria: str, beneficio: str) -> Beneficio:
    row = db.get_beneficio_by_cat_ben(categoria=categoria, beneficio=beneficio)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Benefício com categoria {categoria} e descrição {beneficio} não foi encontrado')
    
    db.delete_beneficio(beneficio=row)

    return row

@app.delete("/associacoes/{cpf_socio}/{id_equipe}/{id_contrato}")
async def delete_associacao(cpf_socio: str, id_equipe: int, id_contrato: int) -> Associacao:
    row = db.get_associacoes_by_id(cpf_socio=cpf_socio, id_equipe=id_equipe, id_contrato=id_contrato)

    if row is None:
        raise HTTPException(status_code=404, detail=f'Associação com cpf {cpf_socio}, equipe {id_equipe} e contrato {id_contrato} não foi encontrada')
    
    db.delete_associacao(associacao=row)

    return row

@app.get("/relatorio_receita")
async def relatorio_receita() -> List[RelatorioReceita]:
    return db.relatorio_receita()

@app.get("/relatorio_socios_ativos")
async def relatorio_socios_ativos() -> List[RelatorioSociosAtivos]:
    return db.relatorio_socios_ativos()

@app.get("/relatorio_gastos_socios")
async def relatorio_gastos_socios() -> List[RelatorioGastosSocios]:
    return db.relatorio_gastos_socios()
