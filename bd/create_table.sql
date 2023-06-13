-- Criação de tabelas do sistema

DROP TABLE Socio, Equipe, Plano, Associacao, Ingresso, Estoque, Venda CASCADE;

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
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    visitante varchar(30) NOT NULL,
    dt_evento date NOT NULL,
    preco_inteiro float NOT NULL,
    id_mandante INTEGER,
    FOREIGN KEY (id_mandante)
        REFERENCES Equipe(id)
        ON DELETE CASCADE
);

CREATE TABLE Estoque (
    id SERIAL PRIMARY KEY,
    quantidade INTEGER,
    id_ingresso INTEGER,
    UNIQUE (id_ingresso),
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

CREATE OR REPLACE VIEW qtd_socios_ativos AS
    SELECT e.nome as time, COALESCE(COUNT(DISTINCT s.nome), 0) AS socios_ativos
    FROM Equipe AS e
    LEFT JOIN Associacao AS a
    ON a.id_equipe = e.id
    LEFT JOIN Socio AS s
    ON a.cpf_socio = s.cpf
    LEFT JOIN Plano AS p
    ON p.categoria = a.categoria_plano
    WHERE a.dt_expiracao >= CURRENT_DATE
    GROUP BY e.nome;

CREATE OR REPLACE VIEW faturamento_time AS
    SELECT e.nome as time, SUM(valor) as valor_faturado FROM Venda AS v
    INNER JOIN Ingresso AS i
    ON i.id = v.id_ingresso
    INNER JOIN Equipe as e
    ON e.id = i.id_mandante
    WHERE v.status_pagamento = 'APROVADO'
    GROUP BY e.nome;

CREATE OR REPLACE FUNCTION check_associacao_ativa(
    input_cpf VARCHAR,
    input_id_equipe INTEGER
)
RETURNS BOOLEAN AS $$
DECLARE
	assoc_count INTEGER;
    res BOOLEAN;
BEGIN	
	SELECT COUNT(*) INTO assoc_count FROM Associacao
	WHERE (CURRENT_DATE BETWEEN dt_associacao AND dt_expiracao)
		AND cpf_socio = input_cpf
		AND id_equipe = input_id_equipe;
	
    IF assoc_count > 0 THEN
        res := TRUE;
    ELSE
        res := FALSE;
    END IF;

    RETURN res;
END;
$$ LANGUAGE plpgsql;
