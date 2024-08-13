```
docker exec -it learning-kafka-kafka-1 bash
```

```
$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic pageview
>
$ kafka-topics.sh --list --bootstrap-server localhost:9092
> pageview
```

