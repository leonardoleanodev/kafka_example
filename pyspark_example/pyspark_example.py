from pyspark.sql.functions import explode, col
from pyspark.sql.types import StringType, StructField, StructType, ArrayType, LongType
from pyspark import SparkContext
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.streaming.query import StreamingQuery
from pyspark.sql.functions import from_json

import os

# add argument to spark get the pakages it needs
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2 pyspark-shell'

# initialize the SparkContext
sc = SparkContext().setLogLevel("ERROR")

# Create SparkSession
spark = (
    SparkSession
    .builder
    .appName("Streaming from Kafka")
    .config("spark.streaming.stopGracefullyOnShutdown", True)
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2')
    .config("spark.sql.shuffle.partitions", 4)
    .master("local[*]")
    .getOrCreate()
)

spark

# Create the streaming_df to read from kafka
streaming_df = spark.readStream\
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "pageview") \
    .option("startingOffsets", "earliest") \
    .load()

data_string = streaming_df.selectExpr(
    "CAST(key AS STRING)", "CAST(value AS STRING)")

grouped: DataFrame = data_string.groupBy("key","value").count()

query: StreamingQuery = (
    grouped
    .writeStream
    .outputMode("complete")
    .format("console")
    .start()
)

query.awaitTermination()
