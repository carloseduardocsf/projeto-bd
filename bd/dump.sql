INSERT INTO Equipes (cnpj, nome, endereco, email)
VALUES
    ('37.167.882/0001-94', 'Belo F.C.', 'Rua Maravilha do Contorno, 2013', 'maiordaparaiba@belo.com'),
    ('42.430.604/0001-18', 'Lagartixa E.C.', 'Rua Vale do Dinossauros, S.N.', 'contato@lagartixa.com'),
    ('08.206.290/0001-36', 'Preá Clube', 'Rua Toca do Préa, 13', 'raposa@cg.com'),
    ('78.091.816/0001-65', 'Doze F.C', 'Rua Doze Mais Um, S.N.', 'contato@doze.com'),
    ('18.919.312/0001-69', 'Volante E.C.', 'Rua Mangabeirão, S.N.', 'clubevolante@macacoautino.com');

INSERT INTO Socios (cpf, nome, email, telefone, dt_nascimento, dt_cadastro)
VALUES
    ('518.717.860-10', 'Yago Roberto Hugo Costa', 'yago_costa@clinicasilhouette.com.br', '+55 (83) 99670-8612', '1980-04-03', '2022-05-10'),
    ('958.174.510-69', 'Filipe Rafael Aragão', 'filipe.rafael.aragao@supracolor.com.br', '+55 (83) 99520-4215', '1998-02-08', '2022-05-12'),
    ('947.048.408-83', 'Luís Filipe Davi Santos', 'luis.filipe.santos@maptec.com.br', '+55 (83) 98874-3690', '2003-04-18', '2022-05-14'),
    ('844.163.368-10', 'Vanessa Ayla Emilly Nascimento', 'vanessa-nascimento79@ceuazul.ind.br', '+55 (83) 99745-2011', '1990-01-14', '2022-05-16'),
    ('950.284.076-30', 'Vitória Fátima Giovana Peixoto', 'vitoria_fatima_peixoto@yahoo.de', '+55 (83) 99644-4832', '1988-01-24', '2022-04-10'),
    ('663.567.940-54', 'Lorenzo Raul Nelson Ramos', 'lorenzoraulramos@igui.com.br', '+55 (84) 98534-2470', '1963-03-13', '2022-03-05'),
    ('251.366.534-18', 'Cláudio Yuri Daniel Campos', 'claudio-campos70@metroquali.com.br', '+55 (84) 98534-2470', '1999-04-22', '2022-03-10'),
    ('432.512.914-67', 'Kamilly Hadassa Drumond', 'kamilly-drumond96@johndeere.com', '+55 (83) 99713-2503', '1997-03-18', '2022-04-11'),
    ('018.147.354-29', 'Melissa Jennifer Dias', 'melissa-dias91@eletroaquila.net', '+55 (83) 98758-3528', '1997-03-17', '2022-03-10'),
    ('541.756.874-08', 'Tiago João Moura', 'tiagojoaomoura@silicotex.net', '+55 (83) 98272-5693', '1997-01-19', '2022-03-22');

INSERT INTO Planos (categoria, valor)
VALUES 
   ('A', 99.90),
   ('B', 49.90),
   ('C', 19.90);

INSERT INTO Contratos (dt_associacao, dt_expiracao, qtd_meses, categoria_plano)
VALUES 
    ('2023-02-05', '2023-08-05', 6, 'B'),
    ('2022-08-29', '2022-09-29', 1, 'C'),
    ('2022-12-28', '2023-12-28', 12, 'C'),
    ('2023-04-15', '2023-07-15', 3, 'A'),
    ('2022-11-08', '2022-12-08', 1, 'B'),
    ('2023-03-25', '2023-06-25', 3, 'C'),
    ('2023-04-07', '2023-10-07', 6, 'B'),
    ('2022-09-18', '2022-10-18', 1, 'A'),
    ('2022-10-14', '2023-10-14', 12, 'A'),
    ('2023-02-22', '2023-08-22', 6, 'C');

INSERT INTO Beneficios (categoria_plano, beneficio)
VALUES
    ('C', 'Desconto de 20% no Ingresso'),
    ('C', 'Carteirinha de Sócio Contribuinte'),
    ('C', 'Poderá Frequentar no Limite de 30 (trinta) dias as Dependências do Clube'),
    ('C', 'Receber Publicações ou Informações Sociais'),
    ('C', 'Participar de Promoções Promovidos'),
    ('B', 'Ingresso Grátis no Setor Geral'),
    ('B', 'Carteirinha de Sócio Contribuinte'),
    ('B', 'Poderá Frequentar Dependências do Clube'),
    ('B', 'Receber Publicações ou Informações Sociais'),
    ('B', 'Participar de Promoções e Eventos Promovidos'),
    ('A', 'Ingresso Grátis em Qualquer Setor '),
    ('A', 'Carteirinha de Sócio Patrimonial'),
    ('A', 'Poderá Frequentar Sem Restrição as Dependências do Clube'),
    ('A', 'Receber Publicações ou Informações Sociais'),
    ('A', 'Participar de Promoções e Eventos Promovidos'),
    ('A', 'Votar para presidente do clube a partir de 3 (três) anos consecutivos de vida associativa');

INSERT INTO Assossiacoes (id_equipe, cpf_socio, id_contrato)
VALUES
    (1, '518.717.860-10', 1),
    (1, '958.174.510-69', 2),
    (1, '947.048.408-83', 3),
    (2, '844.163.368-10', 4),
    (2, '950.284.076-30', 5),
    (3, '663.567.940-54', 6),
    (4, '251.366.534-18', 7),
    (5, '432.512.914-67', 8),
    (5, '018.147.354-29', 9),
    (5, '541.756.874-08', 10);