from typing import Optional, Tuple, Union
import customtkinter as ctk

# Tela de cadastro
#     Inserir cpf
#         Se não existir, tela de cadastro
#         Se existir Tela com o(s) time(s) associado(s) e ingressos comprados

# Se associar
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

        # Frame da direita (principal), que ocupa toda a primeira coluna que tem peso 4, começa no cadastro
        # self.main_frame = ctk.CTkFrame(self)
        self.main_frame = TelaAssociacao(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

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
        self.indicador_cadastro.configure(fg_color='#3a7ebf')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

    def clique_associar(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='#3a7ebf')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

    def clique_comprar_ingresso(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='#3a7ebf')
        self.indicador_entrar_funcionario.configure(fg_color='transparent')

    def clique_entrar_funcionario(self):
        self.indicador_cadastro.configure(fg_color='transparent')
        self.indicador_associar.configure(fg_color='transparent')
        self.indicador_comprar_ingresso.configure(fg_color='transparent')
        self.indicador_entrar_funcionario.configure(fg_color='#3a7ebf')


class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(index=(0, 1, 2), weight=1)
        self.grid_rowconfigure(index=(0, 2), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Cadastro", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nswe')
        
        self.label_cpf = ctk.CTkLabel(self, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='se')

        self.input_inserir_cpf = ctk.CTkEntry(self, font=("Roboto", 20))
        self.input_inserir_cpf.grid(row=1, column=1, padx=10, pady=10, sticky='swe')

        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', font=("Roboto", 20))
        self.botao_confirmar.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')


class TelaAssociacao(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(index=(0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(index=(0, 6), weight=1)

        self.titulo = ctk.CTkLabel(self, text="Associação", font=("Roboto", 50))
        self.titulo.grid(row=0, column=0, columnspan=5, sticky='nswe')

        # Primeira linha
        self.label_cpf = ctk.CTkLabel(self, text='CPF:', font=("Roboto", 20))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.input_cpf = ctk.CTkEntry(self, font=("Roboto", 20))
        self.input_cpf.grid(row=1, column=1, padx=10, pady=10, columnspan=3, sticky='ew')

        # Segunda linha
        self.label_equipe = ctk.CTkLabel(self, text='Equipe:', font=("Roboto", 20))
        self.label_equipe.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.escolha_equipe = ctk.CTkComboBox(self, font=("Roboto", 20))
        self.escolha_equipe.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky='ew')

        # Terceira linha
        self.label_plano = ctk.CTkLabel(self, text='Plano:', font=("Roboto", 20))
        self.label_plano.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        planos = ['A', 'B', 'C']
        self.escolha_plano = ctk.CTkSegmentedButton(self, font=("Roboto", 20), values=planos)
        self.escolha_plano.set(planos[0])
        self.escolha_plano.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        self.label_desconto = ctk.CTkLabel(self, text='Desconto: ', font=("Roboto", 20))
        self.label_desconto.grid(row=3, column=2, padx=10, pady=10, sticky='e')

        self.saida_desconto = ctk.CTkLabel(self, text='50%', font=("Roboto", 20))
        self.saida_desconto.grid(row=3, column=3, padx=10, pady=10, sticky='w')

        # Quarta linha
        self.label_quantidade_meses = ctk.CTkLabel(self, text='Meses:', font=("Roboto", 20))
        self.label_quantidade_meses.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        n_meses = [str(i) for i in range(1, 25)]
        self.escolha_meses = ctk.CTkComboBox(self, font=("Roboto", 20), values=n_meses)
        self.escolha_meses.set(n_meses[5])
        self.escolha_meses.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky='ew')

        # Quinta linha
        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', font=("Roboto", 20))
        self.botao_confirmar.grid(row=5, column=2, columnspan=2, padx=10, pady=10, sticky='ew')
        

app = TelaInicial()
app.mainloop()
