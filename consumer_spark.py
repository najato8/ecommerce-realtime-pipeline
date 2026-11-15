import sys
import json
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
sc = SparkContext("local[2]", "EcommerceConsumer")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 5)

stream = KafkaUtils.createStream(
    ssc,
    "localhost:2181",
    "spark-consumer",
    {"ecommerce-orders": 1}
)
orders = stream.map(lambda x: json.loads(x[1]))

def save_to_hdfs(rdd):
    if not rdd.isEmpty():
        rdd.map(lambda order: str(order)).saveAsTextFile(
            "hdfs:///ecommerce/orders/" + str(int(time.time()))
        )

orders.foreachRDD(save_to_hdfs)

ssc.start()
ssc.awaitTermination()
