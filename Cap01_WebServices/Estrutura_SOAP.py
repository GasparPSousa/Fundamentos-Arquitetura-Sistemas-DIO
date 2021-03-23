"""

====================================================
Estrutura SOAP
====================================================



==================== Objetivos da Aula ============================

1 - O que é SOAP?

2 - As Vantagens de se utilizar SOAP.

3 - O que é XML?

4 - Entender a estrutura de uma mensagem SOAP.



===================== SOAP =========================================

SOAP - Simples Object Acess Protocol

É um protocolo baseado em XML para acessar serciços web principalment por HTTP.

Pode-se dizer que SOAP é uma definição de como serviços web se comunicam.

Foi desenvolvido para facilitar integrações entre aplicações.


====================== Vantagens ====================================

Permite integrações entre aplicações, independente da linguagem, pois usa como
linguagem comum o XML.

É independente de plataforma e software.

Meio de transporte genérico, ou seja, pode ser usado por outros protocolos além de HTTP.



========================= XML =======================================

XML - Extensible Markup Language

É uma linguagem de marcação criada na década de 90 pela W3C.

Facilita a separação de conteúdo.

Não tem limitação de criação de tags.

Linguagem comum para integrações entre aplicações


====================== Estrutura do SOAP ===========================

O "SOAP Message" possui uma estrutura única que deve sempre se seguida.

       ------------------------------------------
        |                                       |
        |      SOAP Envelope                    |
        |                                       |
        |   ------------------                  |
        |   |   SOAP Header  |                  |
        |   |                |                  |
        |   ------------------                  |
        |                                       |
        | -----------------------------         |
        | |                           |         |
        | |   SOAP Body               |         |
        | |                           |         |
        | |                           |         |
        | |                           |         |
        | |----------------------------         |
        |----------------------------------------


SOAP Envelope é o primeiro elemento do documento e é usado para ENCAPSULAR toda a mensagem SOAP.

SOAP Header é o elemento que possui informações de ATRIBUTOS e METADADOS da requisição.

SOAP Body é o elemento que contém os DETALHES da mensagem.





"""