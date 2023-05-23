from fastapi import FastAPI
from models import Socio, Equipe, Plano, Contrato, Beneficio, Assossiacao
import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file

    def _create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)
        
        return conn
    
    def create_socio(self, socio: Socio):
        sql = '''INSERT INTO INSERT INTO Socios (cpf, nome, email, telefone, dt_nascimento, dt_cadastro)
                VALUES(?,?,?,?,?,?) '''
        
        params = (socio.cpf, socio.nome, socio.email, socio.telefone, socio.dt_nascimento, socio.dt_cadastro)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def update_socio(self, socio: Socio):
        sql = ''' UPDATE Socios SET nome=?, email=?, telefone=?, dt_nascimento=?, dt_cadastro=? WHERE cpf=? '''

        params = (socio.nome, socio.email, socio.telefone, socio.dt_nascimento, socio.dt_cadastro, socio.cpf)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_socio(self, socio: Socio):
        pass

    def create_equipe(self, equipe: Equipe):
        sql = '''INSERT INTO INSERT INTO Equipes (cnpj, nome, endereco, email)
                VALUES(?,?,?,?) '''
        
        params = (equipe.cnpj, equipe.nome, equipe.endereco, equipe.email)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def update_equipe(self, equipe: Equipe):
        sql = ''' UPDATE Equipes SET cnpj=?, nome=?, endereco=?, email=? WHERE id=? '''

        params = (equipe.cnpj, equipe.nome, equipe.endereco, equipe.email, equipe.id)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_equipe(self, equipe: Equipe):
        pass

    def create_plano(self, plano: Plano):
        sql = '''INSERT INTO INSERT INTO Planos (categoria, valor)
                VALUES(?,?) '''
        
        params = (plano.categoria, plano.valor)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def update_plano(self, plano: Plano):
        sql = ''' UPDATE Planos SET valor=? WHERE categoria=? '''

        params = (plano.valor, plano.categoria)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_plano(self, plano: Plano):
        pass
    
    def create_contrato(self, contrato: Contrato):
        sql = '''INSERT INTO INSERT INTO Contratos (dt_associacao, dt_expiracao, qtd_meses, categoria_plano)
                VALUES(?,?,?,?) '''
        
        params = (contrato.dt_associacao, contrato.dt_expiracao, contrato.qtd_meses, contrato.categoria_plano)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def update_contrato(self, contrato: Contrato):
        sql = ''' UPDATE Contratos SET dt_associacao=?, dt_expiracao=?, qtd_meses=?, categoria_plano=? WHERE id=? '''

        params = (contrato.dt_associacao, contrato.dt_expiracao, contrato.qtd_meses, contrato.categoria_plano, contrato.id)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_contrato(self, contrato: Contrato):
        pass
    
    def create_beneficio(self, beneficio: Beneficio):
        sql = '''INSERT INTO INSERT INTO Beneficio (categoria_plano, beneficio)
                VALUES(?,?) '''
        
        params = (beneficio.categoria_plano, beneficio.beneficio)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_beneficio(self, beneficio: Beneficio):
        pass

    def create_associacao(self, associacao: Assossiacao):
        pass

    def delete_associacao(self, associacao: Assossiacao):
        pass


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
