from bd.models import Socio, Equipe, Plano, Ingresso, PedidosRealizados, Associacao, Venda, Estoque
from dateutil.relativedelta import relativedelta
from typing import Optional, Tuple, Union
from sqlite3 import IntegrityError
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

        self.equipes = db.get_equipe_names()
        self.escolha_equipe = ctk.CTkComboBox(self, font=("Roboto", 20), values=self.equipes)
        self.escolha_equipe.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Terceira linha
        self.label_plano = ctk.CTkLabel(self, text='Plano:', font=("Roboto", 20))
        self.label_plano.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.planos_desconto = dict()
        self.planos_valor = dict()
        for p in db.get_planos():
            self.planos_desconto[p.categoria] = p.desconto_ingresso
            self.planos_valor[p.categoria] = p.valor

        self.categorias = list(self.planos_desconto.keys())

        self.escolha_plano = ctk.CTkSegmentedButton(self, font=("Roboto", 20), values=self.categorias, command=self.click_plano)
        self.escolha_plano.set(self.categorias[0])
        self.escolha_plano.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        self.label_desconto = ctk.CTkLabel(self, text='', font=("Roboto", 20))
        self.label_desconto.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        self.click_plano(self.categorias[0])

        # Quarta linha
        self.label_quantidade_meses = ctk.CTkLabel(self, text='Meses:', font=("Roboto", 20))
        self.label_quantidade_meses.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        n_meses = [str(i) for i in range(1, 25)]
        self.escolha_meses = ctk.CTkComboBox(self, font=("Roboto", 20), values=n_meses)
        self.escolha_meses.set(n_meses[5])
        self.escolha_meses.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Quinta linha
        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', font=("Roboto", 20), command=self.confirmar)
        self.botao_confirmar.grid(row=5, column=2, columnspan=1, padx=10, pady=10, sticky='ew')

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
    
    def click_plano(self, label):
        self.label_desconto.configure(text=f'Valor: R${self.planos_valor[label]:.2f} | Desconto no ingresso: {self.planos_desconto[label] * 100}%')
    
    def confirmar(self):
        socio = db.get_socio_by_id(self.input_cpf.get())
        id_equipe = db.get_equipe_by_name(self.escolha_equipe.get())[0].id

        if socio is None:
            messagebox.showerror('Erro!', 'É necessário realizar o cadastro primeiro!')
            return
        
        if db.check_associacao_ativa(self.input_cpf.get(), id_equipe):
            messagebox.showerror('Erro!', f'CPF {self.input_cpf.get()} já é sócio do time {self.escolha_equipe.get()}!')
            return


        top = TelaInfoAssociacao(self.input_cpf.get(), self.escolha_equipe.get(), self.escolha_plano.get(), self.planos_valor[self.escolha_plano.get()], self.escolha_meses.get(), id_equipe)

class TelaInfoAssociacao(ctk.CTkToplevel):
    def __init__(self, cpf, equipe, plano, valor, meses, id_equipe):
        super().__init__()

        self.cpf = cpf
        self.equipe = equipe
        self.plano = plano
        self.valor = valor
        self.meses = int(meses)
        self.id_equipe = id_equipe

        self.geometry('500x800')
        self.attributes('-topmost', 'true')
        self.title('Confirmação')

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky='news')
        self.main_frame.rowconfigure(index=(0, 6), weight=1)
        self.main_frame.columnconfigure(index=(0, 2), weight=1)

        self.titulo = ctk.CTkLabel(self.main_frame, text="Confirmar", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nswe')

        self.label_cpf = ctk.CTkLabel(self.main_frame, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.input_cpf = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=cpf)
        self.input_cpf.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.label_equipe = ctk.CTkLabel(self.main_frame, text='Equipe:', font=("Roboto", 20))
        self.label_equipe.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.escolha_equipe = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=equipe)
        self.escolha_equipe.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        self.label_plano = ctk.CTkLabel(self.main_frame, text='Plano:', font=("Roboto", 20))
        self.label_plano.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.escolha_plano = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=plano)
        self.escolha_plano.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.label_plano = ctk.CTkLabel(self.main_frame, text='Meses:', font=("Roboto", 20))
        self.label_plano.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.escolha_plano = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=meses)
        self.escolha_plano.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.label_valor_esq = ctk.CTkLabel(self.main_frame, text='Valor total:', font=("Roboto", 20))
        self.label_valor_esq.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.label_valor_dir = ctk.CTkLabel(self.main_frame, text=f'R${(valor * self.meses):.2f}', font=("Roboto", 20))
        self.label_valor_dir.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.botao_cancelar = ctk.CTkButton(self.main_frame, text='Cancelar', font=("Roboto", 20), command=self.destroy)
        self.botao_cancelar.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.botao_confirmar = ctk.CTkButton(self.main_frame, font=("Roboto", 20), text='Confirmar', command=self.associar)
        self.botao_confirmar.grid(row=6, column=1, padx=10, pady=10, sticky='ew')

    def associar(self):
        try:
            associacao = Associacao(cpf_socio=self.cpf, id_equipe=self.id_equipe, categoria_plano=self.plano, dt_associacao=datetime.date.today(), dt_expiracao=datetime.date.today() + relativedelta(months=self.meses))

            db.create_associacao(associacao=associacao)

            messagebox.showinfo('Sucesso!', 'Associação feita com sucesso!')

            self.destroy()
    
        except:
            messagebox.showerror('Erro!', 'Não foi possível realizar a associação, tente novamente!')


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

        self.ingressos_disponiveis = db.get_ingressos_disponiveis()
        self.escolha_ingresso = ctk.CTkComboBox(self, font=("Roboto", 20), values=self.ingressos_disponiveis)
        self.escolha_ingresso.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Terceira linha
        self.botao_confirmar = ctk.CTkButton(self, text='Continuar', font=("Roboto", 20), command=self.clique_continuar)
        self.botao_confirmar.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def clique_continuar(self):
        socio = db.get_socio_by_id(self.input_cpf.get())

        if socio is None:
            messagebox.showerror('Erro!', 'É necessário realizar o cadastro primeiro!')
            return
        
        mandante = self.escolha_ingresso.get().split(' x ')[0]
        visitante = self.escolha_ingresso.get().split(' x ')[1].split(' - ')[0]
        data = datetime.datetime.strptime(self.escolha_ingresso.get().split(' x ')[1].split(' - ')[1], "%d/%m/%Y").date()

        id_ingresso = db.get_id_ingresso_by_mandante_visitante_data(mandante, visitante, data)
        id_mandante = db.get_equipe_by_name(mandante)[0].id
        
        top = TelaInfoIngresso(self.input_cpf.get(), id_ingresso, id_mandante, self.escolha_ingresso.get())


class TelaInfoIngresso(ctk.CTkToplevel):
    def __init__(self, cpf, id_ingresso, id_mandante, ingresso):
        super().__init__()

        self.cpf = cpf
        self.id_ingresso = id_ingresso
        self.id_mandante = id_mandante
        self.ingresso = ingresso

        self.geometry('800x800')
        self.attributes('-topmost', 'true')
        self.title('Confirmação')

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky='news')
        self.main_frame.rowconfigure(index=(0, 8), weight=1)
        self.main_frame.columnconfigure(index=(0, 2), weight=1)

        self.titulo = ctk.CTkLabel(self.main_frame, text="Confirmar", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nswe')

        self.label_cpf = ctk.CTkLabel(self.main_frame, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.input_cpf = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=cpf)
        self.input_cpf.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

        self.label_ingresso = ctk.CTkLabel(self.main_frame, text='Ingresso:', font=("Roboto", 20))
        self.label_ingresso.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.escolha_ingresso = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=self.ingresso)
        self.escolha_ingresso.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        # Contas
        self.desconto = db.get_desconto_from_cpf_equipe(self.cpf, self.id_mandante)
        self.valor_inteiro = db.get_valor_inteiro_by_ingresso_id(self.id_ingresso)
        self.valor_a_pagar = self.valor_inteiro * (1 - self.desconto)

        self.label_valor = ctk.CTkLabel(self.main_frame, text='Valor inteiro:', font=("Roboto", 20))
        self.label_valor.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.escolha_valor = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=f'R${self.valor_inteiro:.2f}')
        self.escolha_valor.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        self.label_desconto = ctk.CTkLabel(self.main_frame, text='Desconto do plano:', font=("Roboto", 20))
        self.label_desconto.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.escolha_desconto = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=f'{self.desconto * 100}%')
        self.escolha_desconto.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        self.label_valor_a_pagar = ctk.CTkLabel(self.main_frame, text='Valor a pagar:', font=("Roboto", 20))
        self.label_valor_a_pagar.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.escolha_valor_a_pagar = ctk.CTkLabel(self.main_frame, font=("Roboto", 20), text=f'R${self.valor_a_pagar:.2f}')
        self.escolha_valor_a_pagar.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        self.label_forma_pagamento = ctk.CTkLabel(self.main_frame, text='Forma de pagamento:', font=("Roboto", 20))
        self.label_forma_pagamento.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.escolha_forma_pagamento = ctk.CTkComboBox(self.main_frame, font=("Roboto", 20), values=['PIX', 'CRÉDITO', 'DÉBITO'])
        self.escolha_forma_pagamento.grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

        self.botao_cancelar = ctk.CTkButton(self.main_frame, text='Cancelar', font=("Roboto", 20), command=self.destroy)
        self.botao_cancelar.grid(row=7, column=0, padx=10, pady=10, sticky='e')
        self.botao_confirmar = ctk.CTkButton(self.main_frame, font=("Roboto", 20), text='Confirmar', command=self.comprar)
        self.botao_confirmar.grid(row=7, column=1, columnspan=2, padx=10, pady=10, sticky='ew')
        
    def comprar(self):
        try:
            if db.get_quantidade_by_id_ingresso(self.id_ingresso) < 1:
                messagebox.showerror('Erro!', 'Sem estoque')
                return
            
            venda = Venda(cpf_socio=self.cpf, id_ingresso=self.id_ingresso, dt=datetime.date.today(), valor=self.valor_a_pagar, forma_pagamento=self.escolha_forma_pagamento.get(), status_pagamento='APROVADO')

            db.vender_ingresso(venda=venda)

            messagebox.showinfo('Sucesso!', 'Sucesso!')

            self.destroy()
    
        except IntegrityError:
            messagebox.showerror('Erro!', 'Só é possível comprar 1 ingresso por CPF!')
        except:
            messagebox.showerror('Erro!', 'Não foi possível realizar a compra, tente novamente!')


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

        self.botao_plano = ctk.CTkButton(self, text='Plano', font=("Roboto", 20), command=self.abrirPlano)
        self.botao_plano.grid(row=4, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_ingresso = ctk.CTkButton(self, text='Ingresso', font=("Roboto", 20), command=self.abrirIngresso)
        self.botao_ingresso.grid(row=5, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_estoque = ctk.CTkButton(self, text='Estoque', font=("Roboto", 20), command=self.abrirEstoque)
        self.botao_estoque.grid(row=6, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.botao_relatorios = ctk.CTkButton(self, text='Relatórios', font=("Roboto", 20))
        self.botao_relatorios.grid(row=7, column=1, columnspan=2, sticky='nswe', padx=10, pady=10)

        self.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

    def abrirSocio(self):
        tabela = TelaTabela(tabela='Socio')

    def abrirEquipe(self):
        tabela = TelaTabela(tabela='Equipe')

    def abrirPlano(self):
        tabela = TelaTabela(tabela='Plano')

    def abrirIngresso(self):
        tabela = TelaTabela(tabela='Ingresso')

    def abrirEstoque(self):
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

        self.label_cpf = ctk.CTkLabel(self.frame_campos, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
        self.input_cpf = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.cpf)
        self.input_cpf.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_nome = ctk.CTkLabel(self.frame_campos, text='Nome:', font=("Roboto", 20))
        self.label_nome.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
        self.input_nome = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.nome)
        self.input_nome.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_email = ctk.CTkLabel(self.frame_campos, text='Email:', font=("Roboto", 20))
        self.label_email.grid(row=0, column=2, padx=5, pady=(10, 0), sticky='')
        self.input_email = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.email)
        self.input_email.grid(row=1, column=2, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_telefone = ctk.CTkLabel(self.frame_campos, text='Telefone:', font=("Roboto", 20))
        self.label_telefone.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
        self.input_telefone = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.telefone)
        self.input_telefone.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_dt_nasimento = ctk.CTkLabel(self.frame_campos, text='Data de nascimento:', font=("Roboto", 20))
        self.label_dt_nasimento.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
        self.input_dt_nasimento = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.dt_nascimento.strftime("%d/%m/%Y"))
        self.input_dt_nasimento.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

        self.label_dt_cadastro = ctk.CTkLabel(self.frame_campos, text='Data de cadastro:', font=("Roboto", 20))
        self.label_dt_cadastro.grid(row=2, column=2, padx=5, pady=(10, 0), sticky='')
        self.input_dt_cadastro = ctk.CTkLabel(self.frame_campos, font=("Roboto", 20), text=self.socio.dt_cadastro.strftime("%d/%m/%Y"))
        self.input_dt_cadastro.grid(row=3, column=2, padx=5, pady=10, columnspan=1, sticky='we')

        times = db.get_times_associados_by_cpf(socio.cpf)
        self.label_times_associados = ctk.CTkLabel(self.frame_campos, text='Time(s):', font=("Roboto", 20))
        self.label_times_associados.grid(row=4, column=0, columnspan=3, sticky='we', padx=5, pady=10)
        self.times_associados = ctk.CTkLabel(self.frame_campos, text=', '.join(times), font=("Roboto", 20))
        self.times_associados.grid(row=5, column=0, columnspan=3, sticky='we', padx=5, pady=10)

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

        self.index_selecionado = None

        column_dict = {
            'Socio': ('cpf', 'nome', 'email', 'telefone', 'dt_nascimento', 'dt_cadastro'),
            'Equipe': ('id', 'cnpj', 'nome', 'endereco', 'email'),
            'Plano': ('categoria', 'valor', 'desconto_ingresso'),
            'Ingresso': ('id', 'visitante', 'dt_evento', 'preco_inteiro', 'id_mandante'),
            'Estoque': ('id', 'quantidade', 'id_ingresso')
        }

        self.view = ttk.Treeview(self, columns=column_dict[self.tabela], show='headings')
        self.view.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')
        self.view.bind("<<TreeviewSelect>>", self.selecionar_item)

        self.recarregar_tabela_completa()

        self.botao_adicionar = ctk.CTkButton(self, text='Adicionar', font=("Roboto", 20), command=self.adicionar)
        self.botao_adicionar.grid(row=2, column=0, padx=10, pady=10, sticky='we')

        self.botao_editar = ctk.CTkButton(self, text='Editar', font=("Roboto", 20))
        self.botao_editar.grid(row=2, column=1, padx=10, pady=10, sticky='we')

        self.botao_remover = ctk.CTkButton(self, text='Remover', font=("Roboto", 20))
        self.botao_remover.grid(row=2, column=2, padx=10, pady=10, sticky='we')

        if self.tabela == 'Socio':
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

            self.view.heading('cpf', text='CPF')
            self.view.heading('nome', text='Nome')
            self.view.heading('email', text='Email')
            self.view.heading('telefone', text='Telefone')
            self.view.heading('dt_nascimento', text='Nascimento')
            self.view.heading('dt_cadastro', text='Data de cadastro')

            self.view.column('cpf', anchor=tk.CENTER)
            self.view.column('nome', anchor=tk.CENTER)
            self.view.column('email', anchor=tk.CENTER)
            self.view.column('telefone', anchor=tk.CENTER)
            self.view.column('dt_nascimento', anchor=tk.CENTER)
            self.view.column('dt_cadastro', anchor=tk.CENTER)

        elif self.tabela == 'Equipe':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_cnpj = ctk.CTkLabel(self.frame_campos, text='CNPJ', font=("Roboto", 20))
            self.label_cnpj.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_cnpj = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_cnpj.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_nome = ctk.CTkLabel(self.frame_campos, text='Nome', font=("Roboto", 20))
            self.label_nome.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_nome = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_nome.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_endereco = ctk.CTkLabel(self.frame_campos, text='Endereço', font=("Roboto", 20))
            self.label_endereco.grid(row=2, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_endereco = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_endereco.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_email = ctk.CTkLabel(self.frame_campos, text='Email', font=("Roboto", 20))
            self.label_email.grid(row=2, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_email = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_email.grid(row=3, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.view.heading('id', text='ID')
            self.view.heading('cnpj', text='CNPJ')
            self.view.heading('nome', text='Nome')
            self.view.heading('endereco', text='Endereço')
            self.view.heading('email', text='Email')

            self.view.column('id', anchor=tk.CENTER)
            self.view.column('cnpj', anchor=tk.CENTER)
            self.view.column('nome', anchor=tk.CENTER)
            self.view.column('endereco', anchor=tk.CENTER)
            self.view.column('email', anchor=tk.CENTER)

        elif self.tabela == 'Plano':
            self.frame_campos.columnconfigure(index=(0, 1, 2), weight=1)

            self.label_categoria = ctk.CTkLabel(self.frame_campos, text='Categoria', font=("Roboto", 20))
            self.label_categoria.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_categoria = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_categoria.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_valor = ctk.CTkLabel(self.frame_campos, text='Valor', font=("Roboto", 20))
            self.label_valor.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_valor = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_valor.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_desconto = ctk.CTkLabel(self.frame_campos, text='Desconto', font=("Roboto", 20))
            self.label_desconto.grid(row=0, column=2, padx=5, pady=(10, 0), sticky='')
            self.input_desconto = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_desconto.grid(row=1, column=2, padx=5, pady=10, columnspan=1, sticky='we')

            self.view.heading('categoria', text='Categoria')
            self.view.heading('valor', text='Valor')
            self.view.heading('desconto_ingresso', text='Desconto no ingresso')

            self.view.column('categoria', anchor=tk.CENTER)
            self.view.column('valor', anchor=tk.CENTER)
            self.view.column('desconto_ingresso', anchor=tk.CENTER)

        elif self.tabela == 'Ingresso':
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

            self.view.heading('id', text='ID')
            self.view.heading('visitante', text='Visitante')
            self.view.heading('dt_evento', text='Data do evento')
            self.view.heading('preco_inteiro', text='Preço inteiro')
            self.view.heading('id_mandante', text='ID Mandante')

            self.view.column('id', anchor=tk.CENTER)
            self.view.column('visitante', anchor=tk.CENTER)
            self.view.column('dt_evento', anchor=tk.CENTER)
            self.view.column('preco_inteiro', anchor=tk.CENTER)
            self.view.column('id_mandante', anchor=tk.CENTER)

        elif self.tabela == 'Estoque':
            self.frame_campos.columnconfigure(index=(0, 1), weight=1)

            self.label_id_ingresso = ctk.CTkLabel(self.frame_campos, text='ID Ingresso', font=("Roboto", 20))
            self.label_id_ingresso.grid(row=0, column=0, padx=5, pady=(10, 0), sticky='')
            self.input_id_ingresso = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_id_ingresso.grid(row=1, column=0, padx=5, pady=10, columnspan=1, sticky='we')

            self.label_quantidade = ctk.CTkLabel(self.frame_campos, text='Quantidade', font=("Roboto", 20))
            self.label_quantidade.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='')
            self.input_quantidade = ctk.CTkEntry(self.frame_campos, font=("Roboto", 20))
            self.input_quantidade.grid(row=1, column=1, padx=5, pady=10, columnspan=1, sticky='we')

            self.view.heading('id', text='ID')
            self.view.heading('quantidade', text='Quantidade')
            self.view.heading('id_ingresso', text='id_ingresso')

            self.view.column('id', anchor=tk.CENTER)
            self.view.column('quantidade', anchor=tk.CENTER)
            self.view.column('id_ingresso', anchor=tk.CENTER)
    
    def limpa_tabela(self):
        for item in self.view.get_children():
            self.view.delete(item)

    def recarregar_tabela_completa(self):
        self.limpa_tabela()

        if self.tabela == 'Socio':
            socios = db.get_socios()
            for socio in socios:
                self.view.insert('', tk.END, values=(socio.cpf, socio.nome, socio.email, socio.telefone, socio.dt_nascimento.strftime("%d/%m/%Y"), socio.dt_cadastro.strftime("%d/%m/%Y")))

        elif self.tabela == 'Equipe':
            equipes = db.get_equipes()
            for eq in equipes:
                self.view.insert('', tk.END, values=(eq.id, eq.cnpj, eq.nome, eq.endereco, eq.email))
        elif self.tabela == 'Plano':
            planos = db.get_planos()
            for p in planos:
                self.view.insert('', tk.END, values=(p.categoria, p.valor, p.desconto_ingresso))
        elif self.tabela == 'Ingresso':
            ingressos = db.get_ingresso()
            for i in ingressos:
                self.view.insert('', tk.END, values=(i.id, i.visitante, i.dt_evento.strftime("%d/%m/%Y"), i.preco_inteiro, i.id_mandante))
        elif self.tabela == 'Estoque':
            estoques = db.get_estoque()
            for e in estoques:
                self.view.insert('', tk.END, values=(e.id, e.quantidade, e.id_ingresso)) 
    
    def selecionar_item(self, a):
        self.index_selecionado = self.view.focus()
        v = self.view.item(self.index_selecionado, 'values')

        if self.tabela == 'Socio':
            try:
                self.input_cpf.delete(0, tk.END)
                self.input_nome.delete(0, tk.END)
                self.input_email.delete(0, tk.END)
                self.input_telefone.delete(0, tk.END)
                self.input_dt_nasimento.delete(0, tk.END)
                self.input_dt_cadastro.delete(0, tk.END)

                self.input_cpf.insert(0, v[0])
                self.input_nome.insert(0, v[1])
                self.input_email.insert(0, v[2])
                self.input_telefone.insert(0, v[3])
                self.input_dt_nasimento.insert(0, v[4])
                self.input_dt_cadastro.insert(0, v[5])
            except:
                self.input_cpf.delete(0, tk.END)
                self.input_nome.delete(0, tk.END)
                self.input_email.delete(0, tk.END)
                self.input_telefone.delete(0, tk.END)
                self.input_dt_nasimento.delete(0, tk.END)
                self.input_dt_cadastro.delete(0, tk.END)

            
        elif self.tabela == 'Equipe':
                try:
                    self.input_cnpj.delete(0, tk.END)
                    self.input_nome.delete(0, tk.END)
                    self.input_endereco.delete(0, tk.END)
                    self.input_email.delete(0, tk.END)

                    self.input_cnpj.insert(0, v[1])
                    self.input_nome.insert(0, v[2])
                    self.input_endereco.insert(0, v[3])
                    self.input_email.insert(0, v[4])
                except:
                    self.input_cnpj.delete(0, tk.END)
                    self.input_nome.delete(0, tk.END)
                    self.input_endereco.delete(0, tk.END)
                    self.input_email.delete(0, tk.END)
            
        elif self.tabela == 'Plano':
            try:
                self.input_categoria.delete(0, tk.END)
                self.input_valor.delete(0, tk.END)
                self.input_desconto.delete(0, tk.END)

                self.input_categoria.insert(0, v[0])
                self.input_valor.insert(0, v[1])
                self.input_desconto.insert(0, v[2])
            except:
                self.input_categoria.delete(0, tk.END)
                self.input_valor.delete(0, tk.END)
                self.input_desconto.delete(0, tk.END)

        elif self.tabela == 'Ingresso':
            try:
                self.input_id_mandante.delete(0, tk.END)
                self.input_visitante.delete(0, tk.END)
                self.input_preco.delete(0, tk.END)
                self.input_dt_evento.delete(0, tk.END)

                self.input_id_mandante.insert(0, v[4])
                self.input_visitante.insert(0, v[1])
                self.input_preco.insert(0, v[3])
                self.input_dt_evento.insert(0, v[2])
            except:
                self.input_id_mandante.delete(0, tk.END)
                self.input_visitante.delete(0, tk.END)
                self.input_preco.delete(0, tk.END)
                self.input_dt_evento.delete(0, tk.END)

        elif self.tabela == 'Estoque':
            try:
                self.input_id_ingresso.delete(0, tk.END)
                self.input_quantidade.delete(0, tk.END)

                self.input_id_ingresso.insert(0, v[2])
                self.input_quantidade.insert(0, v[1])
            except:
                self.input_id_ingresso.delete(0, tk.END)
                self.input_quantidade.delete(0, tk.END)

    def adicionar(self):
        if self.tabela == 'Socio':
            if len(self.input_cpf.get()) == 0 or len(self.input_nome.get()) == 0 or len(self.input_email.get()) == 0 or len(self.input_telefone.get()) == 0 or len(self.input_dt_nasimento.get()) == 0 or len(self.input_dt_cadastro.get()) == 0:
                messagebox.showerror('Erro!', 'Todos os campos precisam ser preenchidos!')
                return

            try:
                socio = Socio(cpf=self.input_cpf.get(), 
                                nome=self.input_nome.get(), 
                                email=self.input_email.get(), 
                                telefone=self.input_telefone.get(), 
                                dt_nascimento=datetime.datetime.strptime(self.input_dt_nasimento.get(), "%d/%m/%Y"),
                                dt_cadastro=datetime.datetime.strptime(self.input_dt_cadastro.get(), "%d/%m/%Y"))
                
                db.create_socio(socio=socio)

                messagebox.showinfo('Sucesso!', 'Sócio adicionado!')
            except IntegrityError:
                messagebox.showerror('Erro!' , 'CPF e Email precisam ser únicos!')
            except:
                messagebox.showerror('Erro!' , 'Não foi possível adicionar!')

        elif self.tabela == 'Equipe':
            if len(self.input_cnpj.get()) == 0 or len(self.input_nome.get()) == 0 or len(self.input_endereco.get()) == 0 or len(self.input_email.get()) == 0:
                messagebox.showerror('Erro!', 'Todos os campos precisam ser preenchidos!')
                return

            try:
                equipe = Equipe(
                    id=0,
                    cnpj=self.input_cnpj.get(),
                    nome=self.input_nome.get(),
                    endereco=self.input_endereco.get(),
                    email=self.input_email.get()
                )
                
                db.create_equipe(equipe=equipe)

                messagebox.showinfo('Sucesso!', 'Equipe adicionada!')
            except IntegrityError:
                messagebox.showerror('Erro!' , 'Email, nome e CNPJ precisam ser únicos!')
            except:
                messagebox.showerror('Erro!' , 'Não foi possível adicionar!')
        elif self.tabela == 'Plano':
            if len(self.input_categoria.get()) == 0 or len(self.input_valor.get()) == 0 or len(self.input_desconto.get()) == 0:
                messagebox.showerror('Erro!', 'Todos os campos precisam ser preenchidos!')
                return

            try:
                plano = Plano(
                    categoria=self.input_categoria.get(),
                    valor=float(self.input_valor.get()),
                    desconto_ingresso=float(self.input_desconto.get())
                )
                
                db.create_plano(plano=plano)

                messagebox.showinfo('Sucesso!', 'Plano adicionado!')
            except IntegrityError:
                messagebox.showerror('Erro!' , 'Categoria já existe')
            except:
                messagebox.showerror('Erro!' , 'Não foi possível adicionar!')

        elif self.tabela == 'Ingresso':
            if len(self.input_visitante.get()) == 0 or len(self.input_preco.get()) == 0 or len(self.input_id_mandante.get()) == 0 or len(self.input_dt_evento.get()) == 0:
                messagebox.showerror('Erro!', 'Todos os campos precisam ser preenchidos!')
                return

            try:
                ingresso = Ingresso(
                    id=0,
                    visitante=self.input_visitante.get(),
                    preco_inteiro=float(self.input_preco.get()),
                    id_mandante=int(self.input_id_mandante.get()),
                    dt_evento=datetime.datetime.strptime(self.input_dt_evento.get(), "%d/%m/%Y")
                )
                
                db.create_ingresso(ingresso=ingresso)

                messagebox.showinfo('Sucesso!', 'Ingresso adicionado!')
            except IntegrityError:
                messagebox.showerror('Erro!' , 'Erro de integridade!')
            except:
                messagebox.showerror('Erro!' , 'Não foi possível adicionar!')

        elif self.tabela == 'Estoque':
            if len(self.input_quantidade.get()) == 0 or len(self.input_id_ingresso.get()) == 0:
                messagebox.showerror('Erro!', 'Todos os campos precisam ser preenchidos!')
                return

            try:
                estoque = Estoque(
                    id=0,
                    quantidade=int(self.input_quantidade.get()),
                    id_ingresso=int(self.input_id_ingresso.get())
                )
                
                db.create_estoque(estoque=estoque)

                messagebox.showinfo('Sucesso!', 'Estoque adicionado!')
            except IntegrityError:
                messagebox.showerror('Erro!' , 'Erro de integridade!')
            except:
                messagebox.showerror('Erro!' , 'Não foi possível adicionar!')
        
        self.recarregar_tabela_completa()

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

