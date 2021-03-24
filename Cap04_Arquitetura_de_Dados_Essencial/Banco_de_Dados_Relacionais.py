"""
================================================================================
                        Banos de Dados Relacionais
================================================================================


========================= SGBDR - RDBMS ========================================

Sistema de Banco de Dados Relacionais

É composto por Entidades que agrupom as nossas informações. São chamadas de Tabelas.

Registros ou Tuplas - "linhas"
Atributos - "Colunas"


Chaves Primárias(PK)
Chave que dá unicidade aquele registro, eu não posso ter uma duplicidade dessa informação.
Ela é única.


Chaves Secundárias(FK)
Herança da PK de outra tabela e cria um relacionamento entre nossas tabelas,
entre duas instâncias de informações.



============================ Modelagem ===============================================

1 - Modelo Conceitual - MER

2 - Modelo Lógico - implementação



======================== MER - DER ================================================

DER - Diagrama de Entidade Relacionamento

Entidades Fortes - Entidades que NÃO DEPENDEM de outras para existir.
Não possui FK.

Entidades Fracas - Entidades que DEPENDEM de outras para existir.
Possui FK.

Entidade Associativa - De muitos para muitos (M -> N)


========================== Normalização =========================================

1° .. 5° - Formas normais na teoria
1°, 2° e 3° - Na prática


1° Forma Normal
Garantir a existência de valor único em cada coluna

2° Forma Normal
Evitar a duplicidade de valor

3° Forma Normal
Os valores precisam ser totalmente dependente da PK


Primeiro preciso aplicar a 1° forma normal, depois a 2° forma normal e assim por diante.

























"""