from bd.models import Socio, Equipe, Plano, Ingresso, PedidosRealizados
from typing import Optional, Tuple, Union
from tkinter import messagebox
import customtkinter as ctk
from bd.db import DataBase
from tkinter import ttk
import tkinter as tk
import datetime

db = DataBase('./bd/data.db')

# Tela de cadastro
#     Inserir cpf
#         Se não existir, tela de cadastro
#         Se existir Tela com o(s) time(s) associado(s) e ingressos comprados

# Se associar
#     Checa se o CPF existe, se não existir na base, retorna erro
#     Checa se ja existe uma associação ativa daquele CPF com aquele time, se tiver retorna erro explicando
#     Lista da times para escolher
#     Lista dos planos

# Comprar ingresso
#     Inserir seu cpf
#         Checar no banco se tem associação, se tiver aplica desconto
#         O desconto só se aplica em 1 ingresso
#     Selecionar ingresso, mostrar qntd restante de cada
#     Selecionar forma de pagamento a partir de um dropdown

#     Abrir popup avisando se deu certo a compra ou n

# Entrar como funcionário
#     Tela de times
#         Primeiramente lista completa, area de pesquisa, mediante seleção editar ou remover
#         Adicionar
#     Tela de socios
#         Padrão
#     Tela de ingressos
#         Padrao
#     Tela de planos
#         Padrao
#     Tela de estoque
#         Padrao
#     Tela de relatórios
#         Vendas por time 
    

class TelaInicial(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1280x720")
        self.title("Sócios")

        # Configuração para o frame da direita ser 4x mais largo do que o da direita
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        # Frame da esqueda, que ocupa toda a primeira coluna que tem peso 1
        self.side_frame = ctk.CTkFrame(self)
        self.side_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.side_frame.grid_columnconfigure(1, weight=1)
        self.side_frame.grid_rowconfigure(0, weight=1)
        self.side_frame.grid_rowconfigure((1, 2, 3, 4), weight=1)

        self.telas = [TelaCadastro(self), TelaAssociacao(self), TelaIngresso(self), TelaFuncionario(self)]
        for i in range(1, 4):
            self.telas[i].grid_forget()

        # Frame da direita (principal), que ocupa toda a primeira coluna que tem peso 4, começa no cadastro
        # self.main_frame = ctk.CTkFrame(self)
        # self.main_frame = TelaFuncionario(self)
        # self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

        # Dentro do side bar
        self.menu_label = ctk.CTkLabel(self.side_frame, text='Menu', font=("Roboto", 40))
        self.menu_label.grid(column=1, row=0 ,padx=10, pady=10, sticky='nswe')

        self.botao_cadastro = ctk.CTkButton(self.side_frame, text='Cadastro', command=self.clique_cadastro, font=("Roboto", 20), height=50)
        self.botao_cadastro.grid(column=1, row=1 ,padx=(10, 25), pady=10, sticky='we')
        self.indicador_cadastro = ctk.CTkButton(self.side_frame, width=10, height=50, text='', state='disabled', fg_color='#3a7ebf')
        self.indicador_cadastro.grid(column=0, row=1, padx=(5, 0))

        self.botao_associar = ctk.CTkButton(self.side_frame, text='Associar-se', command=self.clique_associar, font=("Roboto", 20), height=50)
        self.botao_associar.grid(column=1, row=2 ,padx=(10, 25), pady=10, sticky='we')
        self.indicador_associar = ctk.CTkButton(self.side_frame, width=10, height=50, text='', state='disabled', fg_color='transparent')
        self.indicador_associar.grid(column=0, row=2, padx=(5, 0))

        self.botao_comprar_ingresso = ctk.CTkButton(self.side_frame, text='Comprar ingresso', command=self.clique_comprar_ingresso, font=("Roboto", 20), height=50)
        self.botao_comprar_ingresso.grid(column=1, row=3 ,padx=(10, 25), pady=10, sticky='we')
        self.indicador_comprar_ingresso = ctk.CTkButton(self.side_frame, width=10, height=50, text='', state='disabled', fg_color='transparent')
        self.indicador_comprar_ingresso.grid(column=0, row=3, padx=(5, 0))

        self.botao_entrar_funcionario = ctk.CTkButton(self.side_frame, text='Entrar como funcionário', command=self.clique_entrar_funcionario, font=("Roboto", 20), height=50)
        self.botao_entrar_funcionario.grid(column=1, row=4 ,padx=(10, 25), pady=10, sticky='we')
        self.indicador_entrar_funcionario = ctk.CTkButton(self.side_frame, width=10, height=50, text='', state='disabled', fg_color='transparent')
        self.indicador_entrar_funcionario.grid(column=0, row=4, padx=(5, 0))

    def clique_cadastro(self):
        # Mostrar indicador
        self.indicador_cadastro.configure(fg_color='#3a7ebf')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

        # Trocar tela
        self.telas[1].grid_forget()
        self.telas[2].grid_forget()
        self.telas[3].grid_forget()
        self.telas[0].tkraise()
        self.telas[0].grid(row=0, column=1, padx=10, pady=10, sticky='nswe')


    def clique_associar(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='#3a7ebf')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

        # Trocar tela
        self.telas[0].grid_forget()
        self.telas[2].grid_forget()
        self.telas[3].grid_forget()
        self.telas[1].tkraise()
        self.telas[1].grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def clique_comprar_ingresso(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='#3a7ebf')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

        # Trocar tela
        self.telas[0].grid_forget()
        self.telas[1].grid_forget()
        self.telas[3].grid_forget()
        self.telas[2].tkraise()
        self.telas[2].grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def clique_entrar_funcionario(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='#3a7ebf')

        # Trocar tela
        self.telas[0].grid_forget()
        self.telas[1].grid_forget()
        self.telas[2].grid_forget()
        self.telas[3].tkraise()
        self.telas[3].grid(row=0, column=1, padx=10, pady=10, sticky='nswe')


class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(index=(0, 1, 2), weight=1)
        self.grid_rowconfigure(index=(0, 2), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Cadastro", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nswe')
        
        self.label_cpf = ctk.CTkLabel(self, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='se')

        self.input_inserir_cpf = ctk.CTkEntry(self, font=("Roboto", 20))
        self.input_inserir_cpf.grid(row=1, column=1, padx=10, pady=10, sticky='swe')

        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', font=("Roboto", 20), command=self.confirmar)
        self.botao_confirmar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
    
    def confirmar(self):
        socio = db.get_socio_by_id(self.input_inserir_cpf.get())

        if len(self.input_inserir_cpf.get()) != 14:
            messagebox.showerror('Erro!', 'Insira exatamente 14 dígitos!')
            return

        if socio is None:
            top = TelaNovoCadastro(self.input_inserir_cpf.get())
        else:
            top = TelaInfoCadastro(socio)


class TelaAssociacao(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(index=(0, 6), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Associação", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=4, sticky='nswe')

        # Primeira linha
        self.label_cpf = ctk.CTkLabel(self, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.input_cpf = ctk.CTkEntry(self, font=("Roboto", 20))
        self.input_cpf.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        # Segunda linha
        self.label_equipe = ctk.CTkLabel(self, text='Equipe:', font=("Roboto", 20))
        self.label_equipe.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.escolha_equipe = ctk.CTkComboBox(self, font=("Roboto", 20))
        self.escolha_equipe.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Terceira linha
        self.label_plano = ctk.CTkLabel(self, text='Plano:', font=("Roboto", 20))
        self.label_plano.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        planos = ['A', 'B', 'C']
        self.escolha_plano = ctk.CTkSegmentedButton(self, font=("Roboto", 20), values=planos)
        self.escolha_plano.set(planos[0])
        self.escolha_plano.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        self.label_desconto = ctk.CTkLabel(self, text=f'Desconto: {"50%"}', font=("Roboto", 20))
        self.label_desconto.grid(row=3, column=2, padx=10, pady=10, sticky='ew')


        # Quarta linha
        self.label_quantidade_meses = ctk.CTkLabel(self, text='Meses:', font=("Roboto", 20))
        self.label_quantidade_meses.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        n_meses = [str(i) for i in range(1, 25)]
        self.escolha_meses = ctk.CTkComboBox(self, font=("Roboto", 20), values=n_meses)
        self.escolha_meses.set(n_meses[5])
        self.escolha_meses.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Quinta linha
        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', font=("Roboto", 20))
        self.botao_confirmar.grid(row=5, column=2, columnspan=1, padx=10, pady=10, sticky='ew')

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
        

class TelaIngresso(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(index=(0, 4), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Ingresso", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=4, sticky='nswe')

        # Primeira linha
        self.label_cpf = ctk.CTkLabel(self, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.input_cpf = ctk.CTkEntry(self, font=("Roboto", 20))
        self.input_cpf.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        # Segunda linha
        self.label_ingresso = ctk.CTkLabel(self, text='Ingresso:', font=("Roboto", 20))
        self.label_ingresso.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        mandantes = ['Belo F.C.', 'Preá Clube', 'Largatixa E.C.']
        visitantes = ['Time do Norte', 'A+ F.C', 'Time do Sul']
        valores = list()
        for i, m in enumerate(mandantes):
            for j, v in enumerate(visitantes):
                valores.append(f'{m} x {v} - {i+10}/{j+1:02}/2023')

        self.escolha_ingresso = ctk.CTkComboBox(self, font=("Roboto", 20), values=valores)
        self.escolha_ingresso.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Terceira linha
        self.botao_confirmar = ctk.CTkButton(self, text='Continuar', font=("Roboto", 20))
        self.botao_confirmar.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')


class TelaFuncionario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(index=(0, 9), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Funcionário", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=4, sticky='nswe')

        self.label = ctk.CTkLabel(self, text="Escolher tabela:", font=("Roboto", 30))
        self.label.grid(row=1, column=0, columnspan=4, sticky='nswe')

        self.botao_socio = ctk.CTkButton(self, text='Sócio', font=("Roboto", 20), command=self.abrirSocio)
        self.botao_socio.grid(row=2, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_equipe = ctk.CTkButton(self, text='Equipe', font=("Roboto", 20), command=self.abrirEquipe)
        self.botao_equipe.grid(row=3, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_plano = ctk.CTkButton(self, text='Plano', font=("Roboto", 20), command=self.abriPlano)
        self.botao_plano.grid(row=4, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_ingresso = ctk.CTkButton(self, text='Ingresso', font=("Roboto", 20), command=self.abriIngresso)
        self.botao_ingresso.grid(row=5, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_estoque = ctk.CTkButton(self, text='Estoque', font=("Roboto", 20), command=self.abriEstoque)
        self.botao_estoque.grid(row=6, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_relatorios = ctk.CTkButton(self, text='Relatórios', font=("Roboto", 20))
        self.botao_relatorios.grid(row=7, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def abrirSocio(self):
        tabela = TelaTabela(tabela='Socio')

    def abrirEquipe(self):
        tabela = TelaTabela(tabela='Equipe')

    def abriPlano(self):
        tabela = TelaTabela(tabela='Plano')

    def abriIngresso(self):
        tabela = TelaTabela(tabela='Ingresso')

    def abriEstoque(self):
        tabela = TelaTabela(tabela='Estoque')

class TelaInfoCadastro(ctk.CTkToplevel):
    def __init__(self, socio: Socio):
        super().__init__()

        self.socio = socio
        self.attributes('-topmost', 'true')

        self.title(f'Dados cadastrais')
        self.geometry('1280x720')

        self.columnconfigure(index=(0, 1, 2), weight=1)
        self.rowconfigure(index=(1), weight=1)

        self.frame_campos = ctk.CTkFrame(self)
        self.frame_campos.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky='nswe')

        columns = ('partida', 'dt_compra', 'valor', 'forma_pagamento' , 'status_pagamento')
        self.view = ttk.Treeview(self, columns=columns, show='headings')
        self.view.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')
        self.view.heading('partida', text='Partida')
        self.view.heading('dt_compra', text='Data da compra')
        self.view.heading('valor', text='Valor pago')
        self.view.heading('forma_pagamento', text='Forma de pagamento')
        self.view.heading('status_pagamento', text='Status do pagamento')

        self.frame_campos.columnconfigure(index=(0, 1, 2), weight=1)

        self.label_cpf = ctk.CTkLabel(self.frame_campos, text='CPF', font=("Roboto", 20))
        self.label_cpf.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
        self.input_cpf = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.cpf)
        self.input_cpf.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_nome = ctk.CTkLabel(self.frame_campos, text='Nome', font=("Roboto", 20))
        self.label_nome.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
        self.input_nome = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.nome)
        self.input_nome.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_email = ctk.CTkLabel(self.frame_campos, text='Email', font=("Roboto", 20))
        self.label_email.grid(row=0, column=2, padx=5, pady=(10, 0), sticky='')
        self.input_email = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.email)
        self.input_email.grid(row=1, column=2, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_telefone = ctk.CTkLabel(self.frame_campos, text='Telefone', font=("Roboto", 20))
        self.label_telefone.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
        self.input_telefone = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.telefone)
        self.input_telefone.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_dt_nasimento = ctk.CTkLabel(self.frame_campos, text='Data de nascimento', font=("Roboto", 20))
        self.label_dt_nasimento.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
        self.input_dt_nasimento = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.dt_nascimento.strftime("%d/%m/%Y"))
        self.input_dt_nasimento.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_dt_cadastro = ctk.CTkLabel(self.frame_campos, text='Data de cadastro', font=("Roboto", 20))
        self.label_dt_cadastro.grid(row=2, column=2, padx=5, pady=(10, 0), sticky='')
        self.input_dt_cadastro = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.dt_cadastro.strftime("%d/%m/%Y"))
        self.input_dt_cadastro.grid(row=3, column=2, padx=5, pady=10, columnspan=1, sticky='we')

        # Populando tabela
        pedidos = db.get_pedidos_realizdos(socio.cpf)
        for pedido in pedidos:
            self.view.insert('', tk.END, values=(pedido.partida, pedido.dt_compra.strftime("%d/%m/%Y"), pedido.valor, pedido.forma_pagamento, pedido.status_pagamento))


class TelaTabela(ctk.CTkToplevel):
    def __init__(self, tabela='Socio'):
        super().__init__()

        self.tabela = tabela
        self.attributes('-topmost', 'true')

        self.title(f'Editar {tabela}')
        self.geometry('1280x720')

        self.columnconfigure(index=(0, 1, 2), weight=1)
        self.rowconfigure(index=(1), weight=1)

        self.frame_campos = ctk.CTkFrame(self)
        self.frame_campos.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky='nswe')

        self.view = ttk.Treeview(self)
        self.view.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

        self.botao_adicionar = ctk.CTkButton(self, text='Adicionar', font=("Roboto", 20))
        self.botao_adicionar.grid(row=2, column=0, padx=10, pady=10, sticky='we')

        self.botao_editar = ctk.CTkButton(self, text='Editar', font=("Roboto", 20))
        self.botao_editar.grid(row=2, column=1, padx=10, pady=10, sticky='we')

        self.botao_remover = ctk.CTkButton(self, text='Remover', font=("Roboto", 20))
        self.botao_remover.grid(row=2, column=2, padx=10, pady=10, sticky='we')

        if tabela == 'Socio':
            self.frame_campos.columnconfigure(index=(0, 1, 2), weight=1)

            self.label_cpf = ctk.CTkLabel(self.frame_campos, text='CPF', font=("Roboto", 20))
            self.label_cpf.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_cpf = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_cpf.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_nome = ctk.CTkLabel(self.frame_campos, text='Nome', font=("Roboto", 20))
            self.label_nome.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_nome = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_nome.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_email = ctk.CTkLabel(self.frame_campos, text='Email', font=("Roboto", 20))
            self.label_email.grid(row=0, column=2, padx=5, pady=(10, 0), sticky='')
            self.input_email = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_email.grid(row=1, column=2, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_telefone = ctk.CTkLabel(self.frame_campos, text='Telefone', font=("Roboto", 20))
            self.label_telefone.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_telefone = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_telefone.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_dt_nasimento = ctk.CTkLabel(self.frame_campos, text='Data de nascimento', font=("Roboto", 20))
            self.label_dt_nasimento.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_dt_nasimento = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_dt_nasimento.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_dt_cadastro = ctk.CTkLabel(self.frame_campos, text='Data de cadastro', font=("Roboto", 20))
            self.label_dt_cadastro.grid(row=2, column=2, padx=5, pady=(10, 0), sticky='')
            self.input_dt_cadastro = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_dt_cadastro.grid(row=3, column=2, padx=5, pady=10, columnspan=1, sticky='we')

        elif tabela == 'Equipe':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_cnpj = ctk.CTkLabel(self.frame_campos, text='CNPJ', font=("Roboto", 20))
            self.label_cnpj.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_cnpj = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_cnpj.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_nome = ctk.CTkLabel(self.frame_campos, text='Nome', font=("Roboto", 20))
            self.label_nome.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_nome = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_nome.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_endereço = ctk.CTkLabel(self.frame_campos, text='Endereço', font=("Roboto", 20))
            self.label_endereço.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_endereço = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_endereço.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_email = ctk.CTkLabel(self.frame_campos, text='Email', font=("Roboto", 20))
            self.label_email.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_email = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_email.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        elif tabela == 'Plano':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_valor = ctk.CTkLabel(self.frame_campos, text='Valor', font=("Roboto", 20))
            self.label_valor.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_valor = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_valor.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_desconto = ctk.CTkLabel(self.frame_campos, text='Desconto', font=("Roboto", 20))
            self.label_desconto.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_desconto = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_desconto.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        elif tabela == 'Ingresso':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_id_mandante = ctk.CTkLabel(self.frame_campos, text='ID Mandante', font=("Roboto", 20))
            self.label_id_mandante.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_id_mandante = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_id_mandante.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_visitante = ctk.CTkLabel(self.frame_campos, text='Visitante', font=("Roboto", 20))
            self.label_visitante.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_visitante = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_visitante.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_preco = ctk.CTkLabel(self.frame_campos, text='Preço', font=("Roboto", 20))
            self.label_preco.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_preco = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_preco.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_dt_evento = ctk.CTkLabel(self.frame_campos, text='Data do evento', font=("Roboto", 20))
            self.label_dt_evento.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_dt_evento = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_dt_evento.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        elif tabela == 'Estoque':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_id_ingresso = ctk.CTkLabel(self.frame_campos, text='ID Ingresso', font=("Roboto", 20))
            self.label_id_ingresso.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_id_ingresso = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_id_ingresso.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_quantidade = ctk.CTkLabel(self.frame_campos, text='Quantidade', font=("Roboto", 20))
            self.label_quantidade.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_quantidade = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_quantidade.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')
    
    def recarregar_tabela(self):
        pass


class TelaNovoCadastro(ctk.CTkToplevel):
    def __init__(self, cpf):
        super().__init__()

        self.title(f'Novo cadastro')
        self.geometry('500x800')
        self.attributes('-topmost', 'true')

        self.cpf = cpf

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky='news')

        self.main_frame.columnconfigure(index=(0, 3), weight=1)
        self.main_frame.rowconfigure(index=(0, 7), weight=1)

        self.titulo = ctk.CTkLabel(self.main_frame, text='Novo cadastro', font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=4, sticky='news')

        self.label_cpf = ctk.CTkLabel(self.main_frame, text='CPF', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=5, pady=10, sticky='e')
        self.input_cpf = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=self.cpf)
        self.input_cpf.grid(row=1, column=1, padx=5, pady=10, columnspan=2, sticky='we')

        self.label_nome = ctk.CTkLabel(self.main_frame, text='Nome', font=("Roboto", 20))
        self.label_nome.grid(row=2, column=0, padx=5, pady=10, sticky='e')
        self.input_nome = ctk.CTkEntry(self.main_frame, font=("Roboto", 20))
        self.input_nome.grid(row=2, column=1, padx=5, pady=10, columnspan=2, sticky='we')

        self.label_email = ctk.CTkLabel(self.main_frame, text='Email', font=("Roboto", 20))
        self.label_email.grid(row=3, column=0, padx=5, pady=10, sticky='e')
        self.input_email = ctk.CTkEntry(self.main_frame, font=("Roboto", 20))
        self.input_email.grid(row=3, column=1, padx=5, pady=10, columnspan=2, sticky='we')

        self.label_telefone = ctk.CTkLabel(self.main_frame, text='Telefone', font=("Roboto", 20))
        self.label_telefone.grid(row=4, column=0, padx=5, pady=10, sticky='e')
        self.input_telefone = ctk.CTkEntry(self.main_frame, font=("Roboto", 20))
        self.input_telefone.grid(row=4, column=1, padx=5, pady=10, columnspan=2, sticky='we')

        self.label_dt_nasimento = ctk.CTkLabel(self.main_frame, text='Data de nascimento', font=("Roboto", 20))
        self.label_dt_nasimento.grid(row=5, column=0, padx=5, pady=10, sticky='e')
        self.input_dt_nasimento = ctk.CTkEntry(self.main_frame, font=("Roboto", 20))
        self.input_dt_nasimento.grid(row=5, column=1, padx=5, pady=10, columnspan=2, sticky='we')

        self.botao_cadastrar = ctk.CTkButton(self.main_frame, text='Cadastrar', font=("Roboto", 20), command=self.cadastrar)
        self.botao_cadastrar.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky='we')
    
    def cadastrar(self):
        if len(self.input_nome.get()) == 0 or len(self.input_email.get()) == 0 or len(self.input_telefone.get()) == 0:
            messagebox.showerror('Erro!', 'Preencha todos os campos!')

            return

        try:
            novo_socio = Socio(cpf=self.cpf, 
                               nome=self.input_nome.get(), 
                               email=self.input_email.get(), 
                               telefone=self.input_telefone.get(),
                               dt_cadastro=datetime.date.today(),
                               dt_nascimento=datetime.datetime.strptime(self.input_dt_nasimento.get(), "%d/%m/%Y").date()
                               )

            db.create_socio(novo_socio)

            res = messagebox.showinfo('Sucesso!', 'Cadastro criado com sucesso!')
            if res == 'ok':
                self.destroy()
        except:
            messagebox.showerror('Erro!', 'Não foi possível realizar o cadastro, tente novamente!')


app = TelaInicial()
app.mainloop()

