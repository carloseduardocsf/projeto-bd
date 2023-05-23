-- Criação de tabelas do sistema

CREATE TABLE Socios (
    cpf char(14) NOT NULL,
    nome varchar(60) NOT NULL,
    email varchar(40) NOT NULL,
    telefone varchar(19),
    dt_nascimento date NOT NULL,
    dt_cadastro date DEFAULT CURRENT_DATE,
    PRIMARY KEY (cpf),
    UNIQUE (email)
);

CREATE TABLE Equipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj char(18) NOT NULL,
    nome varchar(30) NOT NULL,
    endereco varchar(100) NOT NULL,
    email varchar(40) NOT NULL,
    UNIQUE (email)
);

CREATE TABLE Planos (
    categoria char(1) NOT NULL,
    valor float NOT NULL,
    PRIMARY KEY (categoria)
);

CREATE TABLE Contratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dt_associacao date NOT NULL,
    dt_expiracao date NOT NULL,
    qtd_meses INTEGER NOT NULL,
    categoria_plano char(1) NOT NULL,
    FOREIGN KEY (categoria_plano)
        REFERENCES Planos(categoria)
        ON DELETE CASCADE
);

CREATE TABLE Beneficios (
    categoria_plano char(1),
    beneficio varchar(100),
    PRIMARY KEY (categoria_plano, beneficio),
    FOREIGN KEY (categoria_plano)
        REFERENCES Planos(categoria)
        ON DELETE CASCADE
);

CREATE TABLE Assossiacoes (
    cpf_socio char(14),
    id_equipe INTEGER,
    id_contrato INTEGER,
    PRIMARY KEY (cpf_socio, id_equipe, id_contrato),
    FOREIGN KEY (cpf_socio)
        REFERENCES Socios(cpf)
        ON DELETE CASCADE,
    FOREIGN KEY (id_equipe)
        REFERENCES Equipes(id)
        ON DELETE CASCADE,
    FOREIGN KEY (id_contrato)
        REFERENCES Contratos(id)
        ON DELETE CASCADE
);
