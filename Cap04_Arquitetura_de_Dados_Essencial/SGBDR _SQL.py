"""
================================================================================================
                                        SGDBR - SQL
================================================================================================


====================================== SQL =====================================================

DDL - Data Definition Language

DML - Data Manipulation Language

DQL - Data Query Languagem


====================================== DDL =====================================================

CREATE TABLE Cliente
    (
        codigo number(10) NOT NULL PRIMARY KEY,
        nome varchar(50) NOT NULL,
        telefone varchar(15)
    );


======================================= DML ===================================================

INSERT into Cliente(codigo, nome, telefone)
    VALUES(1, "João", "21-9999 9999");

DELETE FROM Cliente
WHERE coluna = 1;

UPDATE Cliente
SET nome = "João"
WHERE codigo = 1;


MUITA ATENÇÃO quando for executar os comandos DELETE E UPDATE...Sempre tem que especicar o WHERE para filtrar
onde vc quer fazer as alterações, do contrário, vai aplicar as alterações na TABELA inteira!


===================================== DQL =========================================================

SELECT codigo, nome FROM Cliente
    WHERE codigo = 1
        AND/OR GROUPBY profissao
        AND/OR HAVING count(1) > 0
        AND/OR ORDERBY nome, codigo;


=================================== Algebra Relacional ============================================

AUB
AintersãoB
A-B


=================================== Query =======================================================

SELECT codigo, nome FROM Cliente WHERE cogigo = 2
UNION
SELECT codigo, nome FROM Cliente WHERE nome = "João";


Vc precisa ter equivalência das colunas


============================== Funções de Conjunto =======================================

SELECT SUM(ven.quantidade) as QTotal, SUM(ven.valor) as VTotal
FROM item_venda ven  (Aqui não coloca a palavra as)
WHERE ven.valor > 5;


SELECT SUM(ven.quantidade) as QTotal, SUM(ven.valor) as VTotal, pro.descricao
FROM item_venda ven  (Aqui não coloca a palavra as)
JOIN produto pro
ON pro.codigo = ven.cod_produto
WHERE ven.valor > 5
GROUPBY pro.descricao
HAVING SUM(ven.valor) >= 10;


============================ Index ======================================================














"""