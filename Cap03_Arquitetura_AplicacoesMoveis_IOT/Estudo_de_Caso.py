"""
================================================================================
Parte  3: Estudo de Caso
================================================================================



============================= Arquiterura é Escolha =============================



GPS >>>>>>>>>mqtt>>>>>>> BROKER >>>>>>>mqtt>>>>>>>> WORKER >>>>>>>>>>>>>>> Data Store





=========================== Prova de Conceito ===================================

Testar esse conceito com tecnologias simples sem se preocupar com Escalabilidade.



App Android >>>>>>>>>>>> Eclipse Mosquito >>>>>>>>>>>>> Node.js >>>>>>>>>>>> MySQL



Aqui já é um exemplo de como resolvo aquele problema arquitetural utilizando tecnologias.
Estou dando nome as tecnologias que vc pode usar para resolver aquele problema.
Aqui a Arquitetura já está chegando ao nível de apontar a solução para cada uma das etapas



============================== Mínimo Produto Viável ================================

Solução um pouco mais robusta.



GPS Embarcado >>>>>>>>>>>>> HiveMQ >>>>>>>>>>>>>>>>> AKKA SCALA JVM >>>>>>>>>>> MongoDB



Substituindo os componentes anteriores por outros mais apropriados para uma carga maior de dados,
já pensando em Escalabilidade.


======================================== Solução ================================================

Solução Cloud Native - Usando componentes, utilizando recursos totalmente gerenciados pelo
Cloud Server Provide, pela Amazon nesse caso.



GPS Embarcado >>>>>>>>>>>>> AWS >>>>>>>>>>>>>>>>>>>>> AWS >>>>>>>>>>>>>>>>>>>>> AWS
                            IoT Core                  Kinesis                   S3
                                                      Firehose


Com isso eu ganho  em tudo que uma nuvem tem a me oferecer em relação a ter um ambiente Estável,
ter um ambiente interoperável e um ambiente Escalável!

Essa solução funciona para 10, para 1000, para 1000000 e para 500000000.

A única preocupação vai ser o custo, isso vai ser cobrado de vc de alguma forma.




================================== IoT na Prática - Arquitetura ==========================================

GPS >>>>>>>mqtt>>>>>>>> BROKER >>>>>>>mqtt>>>>>>> WORKER >>>>tcp>>>>> CACHE >>>>socket.io >>>>>>>> App com Mapa(visualizar os veículos)



GPS Embarcado >>>>>>>>> AWS >>>>>>>>>>>>>>>>>> AWS >>>>>>>>>>>>>>>>>AWS >>>>>>>>>>>>>>>>>>>>>>> AWS
                      IoT Core               Data Stream          Lambda                    ELasticCache Redis



============================= Entregar para o consumidor uma aplicação Web =================================

AWS >>>>>>>>>>>>>>> AWS EC2 >>>>>>>>>>>>>>>> FeatherJS >>>>>>>>>>>>>>>>>>>>>>> Dashboard
ElasticCache                                 Backend
Redis



"""