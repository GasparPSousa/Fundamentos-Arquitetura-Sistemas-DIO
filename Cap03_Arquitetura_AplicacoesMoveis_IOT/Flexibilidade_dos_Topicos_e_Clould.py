"""
================================= Flexibilidade dos Tópicos =================================================


   mqtt       ://    broker.io      /    a6g319          /    gps        /      position
PROTOCOLO            BROKER             USER IDENTIFIER     SENSOR              INFORMATION TYPE


mqtt://broker/user/accelerometer
mqtt://broker/user/gps/position
mqtt://broker/user/gps/velocity




carro1   pub matt://broker/user1/gps/position
carro2   pub matt://broker/user2/gps/position
carro3   pub matt://broker/user3/gps/position
carro4   pub matt://broker/user4/gps/position
carro5   pub matt://broker/user5/gps/position


================================= Subscribe =================================================================


MQTT Broker <<<<<<<<<<<<<<<<<<<<<< Subscribe <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Smartphone
MQTT Broker >>>>>>>>>>>>>>>>>>>>>> Publish >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Smartphone

sub mqtt://broker/user/gps/position




mqtt://broker/user/gps/position
mqtt://broker/user/gps/velocity
mqtt://broker/user/gps/accelerometer
mqtt://broker/user/gps/position
mqtt://broker/+/gps/position ( visualizar TODOS os usuários)
mqtt://broker/user/gps/+ (Todas que vem do GPS...posição e velocidade)
mqtt://broker/+/# (TODAS as mensagens dos tópicos internos de TODOS os usuários e TODOS os sensores)



================================= QoS 0 ===================================================
Níveis diferentes de qualidade de serviço

MQTT Cliente >>>>>>>>>>>>>>>>>>> Publish >>>>>>>>>>>>>>>>>>> MQTT Broker


Nível minimo de menor esforço
Sem garantia de entrega
Mensagem não é restransmitida

Mais barato


====================================  QoS 1 ============================================

MQTT Cliente >>>>>>>>>>>>>>>>>>> Publish >>>>>>>>>>>>>>>>>>> MQTT Broker
MQTT Cliente <<<<<<<<<<<<<<<<<<< Puback <<<<<<<<<<<<<<<<<<<< MQTT Broker

Garante que a mensagem foi entregue no mínimo uma vez ao recebedor
Mensagem pode ser restransmitida se não houver confirmação de entrega




=============================== QoS 2 ==================================================


Melhor que o QoS 1




============================ Cloud ================================================

Grande e cada vez maior o número de devices conectados

TBs ou PBs de informações

Potencial de escala global


BROKER >>>>>>>>>> WORKER >>>>>>>>>>>>> DATA STORE

Armazena cada posição geográfica recebida identificando o usuário, data, hora permitindo reconstruir rotas inteiras.



BROKER >>>>>>>>>>> WORKER >>>>>>>>>>>>> CACHE >>>>>>>>>>>>>>>>

Apresenta em tempo real a última posição de cada usuário no mapa e a quantidade de usuários por hora.




"""