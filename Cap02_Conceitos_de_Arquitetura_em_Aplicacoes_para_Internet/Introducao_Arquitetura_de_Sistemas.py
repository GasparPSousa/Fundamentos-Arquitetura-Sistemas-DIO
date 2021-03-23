""""
================================================================================
Introdução a Arquitetura de Sistemas
================================================================================


=============================== Objetivos da Aula ================================

1 - Tipos de Arquitetura

2 - Comparativo entre os tipos de Arquiteturas

3 - Gerenciamento de erros e volume de acesso.



=========================== Requisitos Básicos ==================================

- Conhecimento Básico sobre protocolo HTTP e proxy

- Entendimento de RESTAPI

- Conhecimento sobre Docker

- Saber programar



============================= Tipos de Arquiterura ================================

- Monolito

- Microserviços #1 (Vários Monolitos Interligados entre si diretamente)
Se a aplicação crescer muito, isso pode ficar caótico.

- Microserviços #2 (Varios Monolitos interligados por um "Message Broker")
Se o Message Broker cair, o sistema todo cai.

- Microserviços #3 (Vários Monolitos interligados por um Gerenciador de pipeline)
Se o pipeline cair, o sistema todo cai.













"""