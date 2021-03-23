"""
===============================================================================
                    Integração com REST e Métodos HTTP
===============================================================================


============================ Objetivos da Aula ================================

1 - integração com serviços REST

2 - Métodos HTTP na prática

3 - Código de estado HTTP



=========================== Código de Estddo ====================================

Usado pelo servidor para avisar o cliente sobre o estado da operação solicitada.

1xx - Informativo

2xx - Sucesso

3xx - Redirecionamento

4xx - Erro do Cliente

5xx - Erro do Servidor



https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


=============================== Prática ==================================================

O professor utilizou o POSTMAN.

O legal do REST é ter uma URI só para fazer tudo. Você só precisa mudar o método HTTP.
Não precisa mudar a mensagem e nem o URI.

No SOAP vc também muda o método, mas muda o método no "soap message", ou seja, na mensagem que você envia.




"""

# Como funciona no código?
# Utilizar o biblioteca Resquest: HTTP for Humans
# https://requests.readthedocs.io/en/master/


import requests

def consulta():
    response = requests.get('http://127.0.0.1:5000/pessoa/')
    print(response.status_code)
    print(response.json())
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'], pessoa['idade'])

def insere():
    nome = 'Rafael'
    idade = 31
    pessoa = {"nome": nome, "idade": idade}
    response = requests.post('http://127.0.0.1:5000/pessoa/', json=pessoa)
    print(response.status_code)
    print(response.json())


consulta()
insere()


# Exemplo utilizando uma URI na máquina LOCAL do professor.
