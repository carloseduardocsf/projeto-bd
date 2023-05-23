from pydantic import BaseModel, constr, EmailStr
from datetime import date


class Socio(BaseModel):
    cpf: constr(min_length=14, max_length=14)
    nome: constr(max_length=60)
    email: EmailStr
    telefone: constr(max_length=19)
    dt_nascimento: date
    dt_cadastro: date

class Equipe(BaseModel):
    id: int | None = None
    cnpj: constr(min_length=18, max_length=18)
    nome: constr(max_length=30)
    endereco: constr(max_length=100)
    email: EmailStr

class Plano(BaseModel):
    categoria: constr(min_length=1, max_length=1)
    valor: float

class Contrato(BaseModel):
    id: int | None = None
    dt_associacao: date | None = None
    dt_expiracao: date | None = None
    qtd_meses: int
    categoria_plano: constr(min_length=1, max_length=1)

class Beneficio(BaseModel):
    categoria_plano: constr(min_length=1, max_length=1)
    beneficio: constr(max_length=100)

class Assossiacao(BaseModel):
    cpf_socio: constr(min_length=14, max_length=14)
    id_equipe: int
    id_contrato: int
