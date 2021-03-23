""""

================================================================
                        WSDL e XSD
================================================================




====================== Objetivos da Aula ===================================

1 - O que é WSDL?

2 - O que é XSD?

3 - SOAP na prática



========================== WSDL ============================================

WSDL - Web Services Description Language

Usado para descrever Web Services, funciona com um CONTRATO do serviço.

A descrição é feito em um documento XML, onde é descrito o serviço, especificações de acesso,
operações e métodos.



========================== XSD ==============================================

XSD - XML Schema Definition

É um SCHEMA no formato XML usado para definir a ESTRUTURA DE DADOS que será validada no XML.

O XSD funciona como uma "DOCUMENTAÇÃO" de como deve ser montado o SOAP Message(XML) que será
enviado através de WebServives.


Exemplo:  http://www.soapclient.com/xml/soapresponder.wsdl



"""


### Para integrar a aplicação com o Serviço SOAP, usar a biblioteca zeep do Python
###  https://docs.python-zeep.org/en/master/
### Essa biblioteca transforma todas as operações que estão no WSDL em funções Python



import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
result = client.service.Method1('oi!', 'tchau!')
print(result)
