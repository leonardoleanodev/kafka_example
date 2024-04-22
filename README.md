# kafka_example

para subir o servidor do kafka


`docker-compose up`

para criar um novo topico do kafka

`exec broker   kafka-topics --create     --topic purchases     --bootstrap-server localhost:9092     --replication-factor 1     --partitions 1`

examplo de produção de mensagem
 
`node producer.js getting-started.properties`

examplo de consumidor

`node consumer.js getting-started.properties`

create the network:

`docker network create kafka-network`

UI

`docker run -it -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui`

referencias

https://developer.confluent.io/get-started/nodejs/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.dsa_mt.dsa_rgn.latam_lng.eng_dv.all_con.confluent-developer&utm_term=&creative=&device=c&placement=&gad=1&gclid=CjwKCAjwjMiiBhA4EiwAZe6jQ_5SBbbdgWZWVE7Rj_2nxk0BMLJMQE7sWDPbae-PilMW3z8RmeXYQxoC27kQAvD_BwE#introduction


using docker for producer:

`docker compose -f docker-compose-producer.yml up`

using docker for consumer:

`docker compose -f docker-compose-consumer.yml up`
