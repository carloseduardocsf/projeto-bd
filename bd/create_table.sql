-- Criação de tabelas do sistema

CREATE TABLE Socio (
    cpf char(14) NOT NULL,
    nome varchar(60) NOT NULL,
    email varchar(40) NOT NULL,
    telefone varchar(19),
    dt_nascimento date NOT NULL,
    dt_cadastro date DEFAULT CURRENT_DATE,
    PRIMARY KEY (cpf),
    UNIQUE (email)
);

CREATE TABLE Equipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj char(18) NOT NULL,
    nome varchar(30) NOT NULL,
    endereco varchar(100) NOT NULL,
    email varchar(40) NOT NULL,
    UNIQUE (email, nome, cnpj)
);

CREATE TABLE Plano (
    categoria char(1) NOT NULL,
    valor float NOT NULL,
    desconto_ingresso float NOT NULL,
    PRIMARY KEY (categoria),
    UNIQUE (categoria)
);

CREATE TABLE Associacao (
    cpf_socio char(14),
    id_equipe INTEGER,
    categoria_plano char(1),
    dt_associacao date DEFAULT CURRENT_DATE NOT NULL,
    dt_expiracao date NOT NULL,
    PRIMARY KEY (cpf_socio, id_equipe, categoria_plano),
    FOREIGN KEY (cpf_socio)
        REFERENCES Socio(cpf)
        ON DELETE CASCADE,
    FOREIGN KEY (id_equipe)
        REFERENCES Equipe(id)
        ON DELETE CASCADE,
    FOREIGN KEY (categoria_plano)
        REFERENCES Plano(categoria)
        ON DELETE CASCADE
);

CREATE TABLE Ingresso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitante varchar(30) NOT NULL,
    dt_evento date NOT NULL,
    preco_inteiro float NOT NULL,
    id_mandante INTEGER,
    FOREIGN KEY (id_mandante)
        REFERENCES Equipe(id)
        ON DELETE CASCADE
);

CREATE TABLE Estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantidade INTEGER,
    id_ingresso INTEGER,
    FOREIGN KEY (id_ingresso)
        REFERENCES Ingresso(id)
        ON DELETE CASCADE
);

CREATE TABLE Venda (
    cpf_socio char(14),
    id_ingresso INTEGER,
    dt date DEFAULT CURRENT_DATE,
    valor float NOT NULL,
    forma_pagamento varchar(10) NOT NULL,
    status_pagamento varchar(10) NOT NULL,
    PRIMARY KEY (cpf_socio, id_ingresso),
    FOREIGN KEY (cpf_socio)
        REFERENCES Socio(cpf)
        ON DELETE CASCADE,
    FOREIGN KEY (id_ingresso)
        REFERENCES Ingresso(id)
        ON DELETE CASCADE
);
