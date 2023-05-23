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
        sql = 'DELETE FROM Socios WHERE cpf=?'

        params = (socio.cpf)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

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
        sql = 'DELETE FROM Equipes WHERE id=?'

        params = (equipe.id)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

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
        sql = 'DELETE FROM Planos WHERE categoria=?'

        params = (plano.categoria)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
    
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
        sql = 'DELETE FROM Contratos WHERE id=?'

        params = (contrato.id)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
    
    def create_beneficio(self, beneficio: Beneficio):
        sql = '''INSERT INTO INSERT INTO Beneficios (categoria_plano, beneficio)
                VALUES(?,?) '''
        
        params = (beneficio.categoria_plano, beneficio.beneficio)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_beneficio(self, beneficio: Beneficio):
        sql = 'DELETE FROM Beneficios WHERE categoria_plano=? AND beneficio=?'

        params = (beneficio.categoria_plano, beneficio.beneficio)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def create_associacao(self, associacao: Assossiacao):
        sql = '''INSERT INTO INSERT INTO Assossiacoes (id_equipe, cpf_socio, id_contrato)
                VALUES(?,?,?) '''
        
        params = (associacao.id_equipe, associacao.cpf_socio, associacao.id_contrato)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_associacao(self, associacao: Assossiacao):
        sql = 'DELETE FROM Assossiacoes WHERE cpf_socio=? AND id_equipe=? AND id_contrato=?'

        params = (associacao.cpf_socio, associacao.id_equipe, associacao.id_contrato)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def get_socio(self):
        pass

    def get_socio_by_id(self, cpf):
        pass
    
    def get_socio_by_name(self, nome):
        pass

    def get_equipe(self):
        pass

    def get_equipe_by_id(self, id):
        pass
    
    def get_equipe_by_name(self, nome):
        pass

    def get_plano(self):
        pass

    def get_plano_by_id(self, categoria):
        pass

    def get_contrato(self):
        pass

    def get_contrato_by_id(self, id):
        pass

    def get_beneficio_by_cat(self, categoria):
        pass

    def get_associacoes(self):
        pass


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
