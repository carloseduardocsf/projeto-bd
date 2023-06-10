INSERT INTO Equipe (cnpj, nome, endereco, email)
VALUES
    ('37.167.882/0001-94', 'Belo F.C.', 'Rua Maravilha do Contorno, 2013', 'maiordaparaiba@belo.com'),
    ('42.430.604/0001-18', 'Lagartixa E.C.', 'Rua Vale do Dinossauros, S.N.', 'contato@lagartixa.com'),
    ('08.206.290/0001-36', 'Preá Clube', 'Rua Toca do Préa, 13', 'raposa@cg.com'),
    ('78.091.816/0001-65', 'Doze F.C', 'Rua Doze Mais Um, S.N.', 'contato@doze.com'),
    ('18.919.312/0001-69', 'Volante E.C.', 'Rua Mangabeirão, S.N.', 'clubevolante@macacoautino.com');

INSERT INTO Socio (cpf, nome, email, telefone, dt_nascimento, dt_cadastro)
VALUES
    ('518.717.860-10', 'Yago Roberto Hugo Costa', 'yago_costa@clinicasilhouette.com.br', '+55 (83) 99670-8612', '1980-04-03', '2022-05-10'),
    ('958.174.510-69', 'Filipe Rafael Aragão', 'filipe.rafael.aragao@supracolor.com.br', '+55 (83) 99520-4215', '1998-02-08', '2022-05-12'),
    ('947.048.408-83', 'Luís Filipe Davi Santos', 'luis.filipe.santos@maptec.com.br', '+55 (83) 98874-3690', '2003-04-18', '2022-05-14'),
    ('844.163.368-10', 'Vanessa Ayla Emilly Nascimento', 'vanessa-nascimento79@ceuazul.ind.br', '+55 (83) 99745-2011', '1990-01-14', '2022-05-16'),
    ('950.284.076-30', 'Vitória Fátima Giovana Peixoto', 'vitoria_fatima_peixoto@yahoo.de', '+55 (83) 99644-4832', '1988-01-24', '2022-04-10'),
    ('663.567.940-54', 'Lorenzo Raul Nelson Ramos', 'lorenzoraulramos@igui.com.br', '+55 (84) 98534-2470', '1963-03-13', '2022-03-05'),
    ('251.366.534-18', 'Cláudio Yuri Daniel Campos', 'claudio-campos70@metroquali.com.br', '+55 (84) 98334-2330', '1999-04-22', '2022-03-10'),
    ('432.512.914-67', 'Kamilly Hadassa Drumond', 'kamilly-drumond96@johndeere.com', '+55 (83) 99713-2503', '1997-03-18', '2022-04-11'),
    ('018.147.354-29', 'Melissa Jennifer Dias', 'melissa-dias91@eletroaquila.net', '+55 (83) 98758-3528', '1997-03-17', '2022-03-10'),
    ('541.756.874-08', 'Tiago João Moura', 'tiagojoaomoura@silicotex.net', '+55 (83) 98272-5693', '1997-01-19', '2022-03-22');

INSERT INTO Plano (categoria, valor, desconto_ingresso)
VALUES 
   ('A', 99.90, 0.9),
   ('B', 49.90, 0.6),
   ('C', 19.90, 0.2);

INSERT INTO Ingresso (visitante, preco_inteiro, id_mandante, dt_evento)
VALUES
    ('Mercenários E.C.', 20.00, 1, '2023-06-15'),
    ('Time do Sul F.C.', 30.00, 2, '2023-06-19'),
    ('Newark F.C.', 50.00, 3, '2023-06-23'),
    ('Volante E.C.', 20.00, 4, '2023-06-27'),

INSERT INTO Estoque (quantidade, id_ingresso)
VALUES
    (10, 1),
    (10, 2),
    (10, 3),
    (10, 4);

INSERT INTO Associacao (cpf_socio, id_equipe, categoria_plano, dt_associacao, dt_expiracao)
VALUES
    ('518.717.860-10', 1, 'B', '2023-02-05', '2023-08-05'),
    ('958.174.510-69', 1, 'C', '2022-08-29', '2022-09-29'),
    ('947.048.408-83', 1, 'C', '2022-12-28', '2023-12-28'),
    ('844.163.368-10', 2, 'A', '2023-04-15', '2023-07-15'),
    ('950.284.076-30', 2, 'B', '2022-11-08', '2022-12-08'),
    ('663.567.940-54', 3, 'C', '2023-03-25', '2023-06-25'),
    ('251.366.534-18', 4, 'B', '2023-04-07', '2023-10-07'),
    ('432.512.914-67', 4, 'A', '2022-09-18', '2022-10-18'),
    ('018.147.354-29', 5, 'A', '2022-10-14', '2023-10-14'),
    ('541.756.874-08', 5, 'C', '2023-02-22', '2023-08-22');

INSERT INTO Venda (cpf_socio, id_ingresso, dt, valor, forma_pagamento, status_pagamento)
VALUES
    ('518.717.860-10', 1, '2023-06-14', 8.00, 'PIX', 'APROVADO'),
    ('958.174.510-69', 1, '2023-06-14', 16.00, 'PIX', 'APROVADO'),
    ('947.048.408-83', 1, '2023-06-14', 16.00, 'PIX', 'APROVADO'),
    ('844.163.368-10', 2, '2023-06-18', 3.00, 'PIX', 'APROVADO'),
    ('950.284.076-30', 2, '2023-06-18', 12.00, 'DÉBITO', 'APROVADO'),
    ('663.567.940-54', 3, '2023-06-22', 40.00, 'CRÉDITO', 'APROVADO'),
    ('251.366.534-18', 3, '2023-06-22', 50.00, 'PIX', 'APROVADO'),
    ('432.512.914-67', 4, '2023-06-26', 2.00, 'PIX', 'APROVADO'),
    ('018.147.354-29', 4, '2023-06-26', 20.00, 'CRÉDITO', 'APROVADO'),
    ('541.756.874-08', 4, '2023-06-26', 20.00, 'DÉBITO', 'APROVADO');