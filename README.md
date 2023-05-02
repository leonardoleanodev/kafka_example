# kafka_example

para subir o servidor do kafka


`docker-compose up`

para criar um novo topico do kafka

`exec broker   kafka-topics --create     --topic purchases     --bootstrap-server localhost:9092     --replication-factor 1     --partitions 1`

examplo de produção de mensagem
 
`node producer.js getting-started.properties`

examplo de consumidor

`node consumer.js getting-started.properties `