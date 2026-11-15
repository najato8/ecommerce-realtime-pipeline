# Real-Time E-Commerce Pipeline

A real-time data pipeline that simulates e-commerce transactions and processes them using Big Data tools.

## Architecture
Python Producer --> Apache Kafka --> Spark Streaming --> HDFS --> Matplotlib


## Tech Stack

| Component | Technology |
|-----------|-----------|
| Environment | Cloudera QuickStart VM (CDH 5.13) |
| Message Broker | Apache Kafka 0.10.2.2 |
| Stream Processing | Apache Spark Streaming 1.6.0 |
| Storage | Hadoop HDFS 2.6.0 |
| Visualization | Matplotlib 2.2.5 |
| Language | Python 2.7 |

## Project Structure
producer.py # Simulates e-commerce orders and sends to Kafka
consumer_spark.py # Reads from Kafka, processes and saves to HDFS
visualize.py # Reads from HDFS and generates charts
ecommerce_stats.png # Output visualization
## Author

Najat Oudaoud Ouhmou
SDBDIA - ENSIASD Taroudant
