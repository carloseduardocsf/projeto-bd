from models import Socio, Equipe, Plano, Contrato, Beneficio, Associacao
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
        sql = '''INSERT INTO Socios (cpf, nome, email, telefone, dt_nascimento, dt_cadastro)
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

        params = (socio.cpf,)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def create_equipe(self, equipe: Equipe):
        sql = '''INSERT INTO Equipes (cnpj, nome, endereco, email)
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

        params = (equipe.id,)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def create_plano(self, plano: Plano):
        sql = '''INSERT INTO Planos (categoria, valor)
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

        params = (plano.categoria,)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
    
    def create_contrato(self, contrato: Contrato):
        sql = '''INSERT INTO Contratos (dt_associacao, dt_expiracao, qtd_meses, categoria_plano)
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

        params = (contrato.id,)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()
    
    def create_beneficio(self, beneficio: Beneficio):
        sql = '''INSERT INTO Beneficios (categoria_plano, beneficio)
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

    def create_associacao(self, associacao: Associacao):
        sql = '''INSERT INTO Associacoes (id_equipe, cpf_socio, id_contrato)
                VALUES(?,?,?) '''
        
        params = (associacao.id_equipe, associacao.cpf_socio, associacao.id_contrato)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def delete_associacao(self, associacao: Associacao):
        sql = 'DELETE FROM Associacoes WHERE cpf_socio=? AND id_equipe=? AND id_contrato=?'

        params = (associacao.cpf_socio, associacao.id_equipe, associacao.id_contrato)

        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def get_socios(self):
        sql = '''SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM
                Socios'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        socios = list()
        for r in res:
            socios.append(Socio(cpf=r[0], nome=r[1], email=r[2], telefone=r[3], dt_nascimento=r[4], dt_cadastro=r[5]))
        
        return socios

    def get_socio_by_id(self, cpf):
        sql = ''' SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM Socios WHERE cpf=? '''

        params = (cpf,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Socio(cpf=res[0], nome=res[1], email=res[2], telefone=res[3], dt_nascimento=res[4], dt_cadastro=res[5]) if res else None
    
    def get_socio_by_name(self, nome):
        sql = '''SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM
                Socios WHERE nome LIKE ?'''
        
        params = ('%' + nome + '%',)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchall()
        conn.close()

        socios = list()
        for r in res:
            socios.append(Socio(cpf=r[0], nome=r[1], email=r[2], telefone=r[3], dt_nascimento=r[4], dt_cadastro=r[5]))
        
        return socios

    def get_equipes(self):
        sql = '''SELECT id, cnpj, nome, endereco, email FROM
                Equipes'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        equipes = list()
        for r in res:
            equipes.append(Equipe(id=r[0], cnpj=r[1], nome=r[2], endereco=r[3], email=r[4]))
        
        return equipes

    def get_equipe_by_id(self, id):
        sql = ''' SELECT id, cnpj, nome, endereco, email FROM Equipes WHERE id=? '''

        params = (id,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Equipe(id=res[0], cnpj=res[1], nome=res[2], endereco=res[3], email=res[4]) if res else None
    
    def get_equipe_by_name(self, nome):
        sql = '''SELECT id, cnpj, nome, endereco, email FROM
                Equipes WHERE nome LIKE ?'''
        
        params = ('%' + nome + '%',)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchall()
        conn.close()

        equipes = list()
        for r in res:
            equipes.append(Equipe(id=r[0], cnpj=r[1], nome=r[2], endereco=r[3], email=r[4]))
        
        return equipes

    def get_planos(self):
        sql = '''SELECT categoria, valor FROM
                Planos'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        planos = list()
        for r in res:
            planos.append(Plano(categoria=r[0], valor=r[1]))
        
        return planos

    def get_plano_by_id(self, categoria):
        sql = ''' SELECT categoria, valor FROM Planos WHERE categoria=? '''

        params = (categoria,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Plano(categoria=res[0], valor=res[1]) if res else None

    def get_contratos(self):
        sql = '''SELECT id, dt_associacao, dt_expiracao, qtd_meses, categoria_plano FROM
                Contratos'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        contratos = list()
        for r in res:
            contratos.append(Contrato(id=r[0], dt_associacao=r[1], dt_expiracao=r[2], qtd_meses=r[3], categoria_plano=r[4]))
        
        return contratos

    def get_contrato_by_id(self, id):
        sql = ''' SELECT id, dt_associacao, dt_expiracao, qtd_meses, categoria_plano FROM Contratos WHERE id=? '''

        params = (id,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Contrato(id=res[0], dt_associacao=res[1], dt_expiracao=res[2], qtd_meses=res[3], categoria_plano=res[4]) if res else None

    def get_beneficio_by_cat(self, categoria):
        sql = '''SELECT categoria_plano, beneficio FROM
                Beneficios WHERE categoria_plano = ?'''
        
        params = (categoria,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchall()
        conn.close()

        beneficios = list()
        for r in res:
            beneficios.append(Beneficio(categoria_plano=r[0], beneficio=r[1]))
        
        return beneficios

    def get_beneficios(self):
        sql = '''SELECT categoria_plano, beneficio FROM
                Beneficios'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        beneficios = list()
        for r in res:
            beneficios.append(Beneficio(categoria_plano=r[0], beneficio=r[1]))
        
        return beneficios

    def get_associacoes(self):
        sql = '''SELECT cpf_socio, id_equipe, id_contrato FROM
                Associacoes'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        associacoes = list()
        for r in res:
            associacoes.append(Associacao(cpf_socio=r[0], id_equipe=r[1], id_contrato=r[2]))
        
        return associacoes
