""""
====================================================================
                        REST API JSON
====================================================================


===================== Objetivos da Aula ============================

1 - O que é REST?

2 - Vantagens de se utilizar REST.

3 - O que é uma API?

4 - Entendendo os métodos utilizados pelo REST.

5 - Estrutura de um REST.

6 - Estrutura de um JSON.


======================== REST =======================================

REST - Representation State Transfer.
(uma analogia que o pessoal faz é: "não importa com é, importa é COMO está" no momento da chamada)

É um ESTILO DE ARQUITERUTA de software que define implementação de um serviço web.

Podem trabalhar com formatos XML, JSON ou outros.



======================== Vantagens do REST ============================

Permite integrações entre aplicações e também entre cliente e servidor em páginas web e aplicações.

Utiliza dos métodos HTTP para definir a operação que está sendo efetuada.

Arquitetura de fácil compreensão.



======================== Estrutura do REST ==============================



CLIENTE >>>>>>>>>>>>>>> Requisição HTTP(GET, POST, PUT, DELETE,...)>>>>>>>>>>>>> SERVIDOR

CLIENTE <<<<<<<<<<<<<<< Retorna um código da operação <<<<<<<<<<<<<<<<<<<<<<<<<< SERVIDOR
                        Retorna mensagem(Texto, JSON, XML,...)


Quando um aplicação web disponibiliza um conjunto de rotinas e padrões através de
serviços web podemos chamar esse conjunto de API.



================================ API =======================================

API - Application Programming Interface

São conjuntos de rotinas documentados e disponibilizados por uma aplicação para que outras aplicações possam consumir
suas funcionalidades.

Ficou popular com o aumento de serviços web.

As maiores plataformad de tecnologia disponibilizam API para acessos de suas funcionalidades, algumas delas são:
Facebook, Twitter, Telegram, Whatsapp, Github..


================================== Principais Métodos HTTP =======================

GET - Solicita a representação de um recurso.

POST - Solicita a criação de um recurso.

DELETE - Solicita a exclusão de um recurso.

PUT - Solicita a atualização de um recurso.


Esses são os principais, existem outros.
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

https://developer.twitter.com/en/docs/api-reference-index

Para ser REST tem que usar esses métodos HTTP.


================================ JSON ===================================================

JSON - JavaScript Object Notaion (não só para JavaScript, mas para qualquer linguagem)

Formatação leve utilizada para troca de mensagens entre sistemas.

Usa-se de uma estrutura de CHAVE e VALOR e também de LISTAS ORDENADAS.

Um dos formatos mais populares e mais utilizados para troca de mensagens entre sistemas.







"""