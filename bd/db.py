from bd.models import Socio, Equipe, Plano, Associacao, Ingresso, Venda, Estoque, RelatorioReceita, RelatorioSociosAtivos, RelatorioGastosSocios
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
        sql = '''INSERT INTO Socio (cpf, nome, email, telefone, dt_nascimento, dt_cadastro)
                VALUES(?,?,?,?,?,?) '''
        
        params = (socio.cpf, socio.nome, socio.email, socio.telefone, socio.dt_nascimento, socio.dt_cadastro)


        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def update_socio(self, socio: Socio):
        sql = ''' UPDATE Socio SET nome=?, email=?, telefone=?, dt_nascimento=?, dt_cadastro=? WHERE cpf=? '''

        params = (socio.nome, socio.email, socio.telefone, socio.dt_nascimento, socio.dt_cadastro, socio.cpf)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_socio(self, socio: Socio):
        sql = 'DELETE FROM Socio WHERE cpf=?'

        params = (socio.cpf,)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def create_equipe(self, equipe: Equipe):
        sql = '''INSERT INTO Equipe (cnpj, nome, endereco, email)
                VALUES(?,?,?,?) '''
        
        params = (equipe.cnpj, equipe.nome, equipe.endereco, equipe.email)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def update_equipe(self, equipe: Equipe):
        sql = ''' UPDATE Equipe SET cnpj=?, nome=?, endereco=?, email=? WHERE id=? '''

        params = (equipe.cnpj, equipe.nome, equipe.endereco, equipe.email, equipe.id)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_equipe(self, equipe: Equipe):
        sql = 'DELETE FROM Equipe WHERE id=?'

        params = (equipe.id,)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def create_plano(self, plano: Plano):
        sql = '''INSERT INTO Plano (categoria, valor, desconto_ingresso)
                VALUES(?,?,?) '''
        
        params = (plano.categoria, plano.valor, plano.desconto_ingresso)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def update_plano(self, plano: Plano):
        sql = ''' UPDATE Plano SET valor=?, desconto_ingresso=? WHERE categoria=? '''

        params = (plano.valor, plano.desconto_ingresso, plano.categoria)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_plano(self, plano: Plano):
        sql = 'DELETE FROM Plano WHERE categoria=?'

        params = (plano.categoria,)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
    
    def create_associacao(self, associacao: Associacao):
        sql = '''INSERT INTO Associacao (cpf_socio, id_equipe, categoria_plano, dt_associacao, dt_expiracao)
                VALUES(?,?,?,?,?) '''
        
        params = (associacao.cpf_socio, associacao.id_equipe, associacao.categoria_plano, associacao.dt_associacao, associacao.dt_expiracao)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_associacao(self, associacao: Associacao):
        sql = 'DELETE FROM Associacao WHERE cpf_socio=? AND id_equipe=? AND categoria_plano=?'

        params = (associacao.cpf_socio, associacao.id_equipe, associacao.categoria_plano)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def get_socios(self):
        sql = '''SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM Socio'''

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
        sql = ''' SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM Socio WHERE cpf=? '''

        params = (cpf,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Socio(cpf=res[0], nome=res[1], email=res[2], telefone=res[3], dt_nascimento=res[4], dt_cadastro=res[5]) if res else None
    
    def get_socio_by_name(self, nome):
        sql = '''SELECT cpf, nome, email, telefone, dt_nascimento, dt_cadastro FROM Socio WHERE nome LIKE ?'''
        
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
                Equipe'''

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
        sql = ''' SELECT id, cnpj, nome, endereco, email FROM Equipe WHERE id=? '''

        params = (id,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Equipe(id=res[0], cnpj=res[1], nome=res[2], endereco=res[3], email=res[4]) if res else None
    
    def get_equipe_by_name(self, nome):
        sql = '''SELECT id, cnpj, nome, endereco, email FROM
                Equipe WHERE nome LIKE ?'''
        
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
        sql = '''SELECT categoria, valor, desconto_ingresso FROM
                Plano'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        planos = list()
        for r in res:
            planos.append(Plano(categoria=r[0], valor=r[1], desconto_ingresso=r[2]))
        
        return planos

    def get_plano_by_id(self, categoria):
        sql = ''' SELECT categoria, valor, desconto_ingresso FROM Plano WHERE categoria=? '''

        params = (categoria,)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close

        return Plano(categoria=res[0], valor=res[1], desconto_ingresso=res[2]) if res else None

    def get_associacoes(self):
        sql = '''SELECT cpf_socio, id_equipe, categoria_plano, dt_associacao, dt_expiracao FROM Associacao'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        associacoes = list()
        for r in res:
            associacoes.append(Associacao(cpf_socio=r[0], id_equipe=r[1], categoria_plano=r[2], dt_associacao=r[3], dt_expiracao=r[4]))
        
        return associacoes
    
    def get_associacoes_by_id(self, cpf_socio, id_equipe, categoria_plano):
        sql = '''SELECT cpf_socio, id_equipe, categoria_plano, dt_associacao, dt_expiracao FROM Associacao where cpf_socio = ? AND id_equipe = ? AND categoria_plano = ?'''

        params = (cpf_socio, id_equipe, categoria_plano)

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()
        conn.close()
        
        return Associacao(cpf_socio=res[0], id_equipe=res[1], categoria_plano=res[2], dt_associacao=res[3], dt_expiracao=res[4]) if res else None

    def create_ingresso(self, ingresso: Ingresso):
        sql = '''INSERT INTO Ingresso (visitante, dt_evento, preco_inteiro, id_mandante)
                VALUES(?,?,?,?) '''
        
        params = (ingresso.visitante, ingresso.dt_evento, ingresso.preco_inteiro, ingresso.id_mandante)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_ingresso(self, ingresso: Ingresso):
        sql = 'DELETE FROM Ingresso WHERE id=?'

        params = (ingresso.id,)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def update_ingresso(self, ingresso: Ingresso):
        sql = ''' UPDATE Ingresso SET visitante=?, dt_evento=?, preco_inteiro=?, id_mandante=? WHERE id=? '''

        params = (ingresso.visitante, ingresso.dt_evento, ingresso.preco_inteiro, ingresso.id_mandante, ingresso.id)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def get_ingresso(self):
        sql = '''SELECT id, visitante, dt_evento, preco_inteiro, id_mandante FROM Ingresso'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        ingressos = list()
        for r in res:
            ingressos.append(Ingresso(id=r[0], visitante=r[1], dt_evento=r[2], preco_inteiro=r[3], id_mandante=r[4]))
        
        return ingressos

    def create_estoque(self, estoque: Estoque):
        sql = '''INSERT INTO Estoque (quantidade, id_ingresso)
                VALUES(?,?) '''
        
        params = (estoque.quantidade, estoque.id_ingresso)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def delete_estoque(self, estoque: Estoque):
        sql = 'DELETE FROM Estoque WHERE id=?'

        params = (estoque.id,)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def update_estoque(self, estoque: Estoque):
        sql = ''' UPDATE Estoque SET quantidade=? WHERE id=? '''

        params = (estoque.quantidade, estoque.id)

        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()

    def get_estoque(self):
        sql = '''SELECT id, quantidade, id_ingresso FROM
                Estoque'''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        estoques = list()
        for r in res:
            estoques.append(Ingresso(id=r[0], quantidade=r[1], id_ingresso=r[2]))
        
        return estoques

    def relatorio_receita(self):
        sql = '''
            SELECT e.nome AS time,
                IFNULL(SUM(p.valor * c.qtd_meses), 0) AS receita, 
                IFNULL(SUM(p.valor * c.qtd_meses) / SUM(c.qtd_meses), 0) AS receita_media_mensal 
            FROM Equipes AS e
            LEFT JOIN Associacoes AS a
            ON a.id_equipe = e.id
            LEFT JOIN Socio AS s
            ON a.cpf_socio = s.cpf
            LEFT JOIN Contratos AS c
            ON a.id_contrato = c.id
            LEFT JOIN Planos AS p
            ON p.categoria = c.categoria_plano
            GROUP BY e.nome
            ORDER BY -receita
        '''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        relatorio_time = list()
        for r in res:
            relatorio_time.append(RelatorioReceita(time=r[0], receita=r[1], receita_media_mensal=[2]))
        
        return relatorio_time

    def relatorio_socios_ativos(self):
        sql = '''
            SELECT e.nome as time, IFNULL(COUNT(DISTINCT s.nome), 0) AS socios_ativos
            FROM Equipes AS e
            LEFT JOIN Associacoes AS a
            ON a.id_equipe = e.id
            LEFT JOIN Socio AS s
            ON a.cpf_socio = s.cpf
            LEFT JOIN Contratos AS c
            ON a.id_contrato = c.id
            LEFT JOIN Planos AS p
            ON p.categoria = c.categoria_plano
            WHERE c.dt_expiracao >= CURRENT_DATE
            GROUP BY e.nome
        '''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        relatorio_time = list()
        for r in res:
            relatorio_time.append(RelatorioSociosAtivos(time=r[0], socios_ativos=r[1]))
        
        return relatorio_time

    def relatorio_receita(self):
        sql = '''
            SELECT e.nome AS time,
                    IFNULL(SUM(p.valor * c.qtd_meses), 0) AS receita, 
                    IFNULL(SUM(p.valor * c.qtd_meses) / SUM(c.qtd_meses), 0) AS receita_media_mensal 
            FROM Equipes AS e
            LEFT JOIN Associacoes AS a
            ON a.id_equipe = e.id
            LEFT JOIN Socios AS s
            ON a.cpf_socio = s.cpf
            LEFT JOIN Contratos AS c
            ON a.id_contrato = c.id
            LEFT JOIN Planos AS p
            ON p.categoria = c.categoria_plano
            GROUP BY e.nome
            ORDER BY -receita
        '''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        relatorio_time = list()
        for r in res:
            relatorio_time.append(RelatorioReceita(time=r[0], receita=r[1], receita_media_mensal=r[2]))
        
        return relatorio_time
    
    def relatorio_gastos_socios(self):
        sql = '''
            SELECT s.nome,
                   IFNULL(SUM(p.valor * c.qtd_meses), 0) AS gasto
            FROM Socios AS s
            LEFT JOIN Associacoes AS a
            ON a.cpf_socio = s.cpf
            LEFT JOIN Equipes AS e
            ON e.id = a.id_equipe
            LEFT JOIN Contratos AS c
            ON a.id_contrato = c.id
            LEFT JOIN Planos AS p
            ON p.categoria = c.categoria_plano
            GROUP BY s.nome
            ORDER BY -gasto
        '''

        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        conn.close()

        relatorio = list()
        for r in res:
            relatorio.append(RelatorioGastosSocios(nome=r[0], gasto=r[1]))
        
        return relatorio
    
