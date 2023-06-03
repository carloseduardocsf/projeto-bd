from pydantic import BaseModel, constr
from datetime import date


class Socio(BaseModel):
    cpf: constr(min_length=14, max_length=14)
    nome: constr(max_length=60)
    email: constr(max_length=40)
    telefone: constr(max_length=19) | None = None
    dt_nascimento: date
    dt_cadastro: date

class SocioUpdate(BaseModel):
    nome: constr(max_length=60) | None = None
    email: constr(max_length=40) | None = None
    telefone: constr(max_length=19) | None = None
    dt_nascimento: date | None = None
    dt_cadastro: date | None = None

class Equipe(BaseModel):
    id: int | None = None
    cnpj: constr(min_length=18, max_length=18)
    nome: constr(max_length=30)
    endereco: constr(max_length=100)
    email: constr(max_length=40)

class EquipeUpdate(BaseModel):
    cnpj: constr(min_length=18, max_length=18) | None = None
    nome: constr(max_length=30) | None = None
    endereco: constr(max_length=100) | None = None
    email: constr(max_length=40) | None = None

class Plano(BaseModel):
    categoria: constr(min_length=1, max_length=1)
    valor: float

class PlanoUpdate(BaseModel):
    valor: float | None = None

class Contrato(BaseModel):
    id: int | None = None
    dt_associacao: date | None = None
    dt_expiracao: date | None = None
    qtd_meses: int
    categoria_plano: constr(min_length=1, max_length=1)

class ContratoUpdate(BaseModel):
    dt_associacao: date | None = None
    dt_expiracao: date | None = None
    qtd_meses: int | None = None
    categoria_plano: constr(min_length=1, max_length=1) | None = None

class Beneficio(BaseModel):
    categoria_plano: constr(min_length=1, max_length=1)
    beneficio: constr(max_length=100)

class Associacao(BaseModel):
    cpf_socio: constr(min_length=14, max_length=14)
    id_equipe: int
    id_contrato: int

class RelatorioReceita(BaseModel):
    time: str
    receita: float
    receita_media_mensal: float

class RelatorioSociosAtivos(BaseModel):
    time: str
    socios_ativos: int

class RelatorioGastosSocios(BaseModel):
    nome: str
    gasto: float
