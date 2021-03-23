"""
============================== Parte 2 - Arquitetura de IoT ==========================

========================= Problema a Resolver ======================================

Um proprietário de uma frota de veículos pretende saber em tempo real qual a localização de
cada um dos seus veículos.

Então ele vai precisar ter um GPS em cada um dos veículos da sua frota.

Esses GPS vão coletar a posição geográfica mais atual e vai ter que transmitir isso para a um Servidor(NUVEM).

E essas posições depois podem ser armazenados e esses dados podem ser utilizados para poder criar uma aplicação
onde exista um mapa e nesse mapa agente consiga visualizar a última posição de cada um desses veículos.



============================ Conectando as coisas ============================================

Considere esses atributos na ESCOLHA

- Baixo consumo de energia
- Rede da dados limitado
- Resiliência (Fazer um buffer)
- Segurança
- Customização
- Baixo Custo



================================== Arduino ===================================================

Plataforma de Prototipagem
Com entradas/saídas
Desenvolvedor escreve em C/C++
Interface serial ou USB
Shields

=================================== Embarcados ===============================================

MCUs
Microcontrolador de chip único
Sistema Operacional Real Time
Embarcado
Uso Industrial, médico, militar, transporte


=================================== Minicomputadores ==========================================

Raspberry Pi

Computador Completo
Hardware integrado em uma única placa
Roda SO Linux ou Windows
Uso doméstico ou comercial


============================ O Protocolo de Comunicação ==================================

Voltando ao Problema

Vamos usar Smartphone ou GPS tracker(embarcado) para nos dar a informação da localização do carro.


================================ O protocolo MQTT =======================================

O importante é que ambos falem a mesma língua.

Por isso a importância de ter um protocolo único e o protocolo MQTT é o mais importante de IoT.



============================== MQTT =================================================

Base na pilha do TCP/IP

Protocolo de mensagem ASSÍNCRONA(M2M)

Criado pela IBM para conectar sensores de pipelines de petróleos a satélites.

Padrão OASIS suportado pelas linguagens de programação mais populares.




========================== Modelo Cliente Servidor =========================

CLIENTE >>>>>>>>>>>>>>> Request >>>>>>>>>>>>>>>>>>>> SERVER
                        HTTP
CLIENTE <<<<<<<<<<<<<<Response <<<<<<<<<<<<<<<<<<<<SERVER

Modelo SÍNCRONO



============================== Modelo Publish/Subscribe ====================

GPS                                                                 Publish


                            MQTT Broker



Acceletomer/Gyroscope                                               Publish
 SENSOR




=========================== Publish =======================================

GPS >>>>>>>>>>>>>>> Publish >>>>>>>>>>>>>>>>>> MQTT Broker









"""