# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("yarn") \
      .appName("JOB DF SPARK") \
      .getOrCreate() 


# local data

from datetime import datetime, date

df = spark.createDataFrame([
    (1, 2., 'string1', date(2025, 1, 1), datetime(2025, 1, 1, 12, 0), 'red'),
    (2, 3., 'string2', date(2025, 2, 1), datetime(2025, 1, 2, 12, 0), 'yellow'),
    (3, 4., 'string3', date(2025, 3, 1), datetime(2025, 1, 3, 12, 0), 'red'),
    (4, 10.2, 'string3', date(2025, 4, 1), datetime(2025, 1, 4, 12, 0), 'red'),
], schema='a long, b double, c string, d date, e timestamp, color string')

df.printSchema()

df.show()

df.filter(df.a == 1).select("a","b","color").show()

# CSV data from HDFS

df2 = spark.read.option("header", "true").csv("/tmp/quincaillerie/*.csv")
df2.createOrReplaceTempView("my_csv_table");
df3=spark.sql("select * from my_csv_table");
df3.show()


# HIVE DATA

# terminal

#spark-submit2 /home/hadoop/data_code/first.py

#spark-submit2 --driver-memory 1g --executor-memory 1g --executor-cores 1 /home/hadoop/data_code/first.py

#spark-submit2 \
#--conf "spark.sql.catalogImplementation=hive" \
#--driver-java-options "-Dhive.metastore.uris=thrift://localhost:9083" \
#--conf spark.sql.crossJoin.enabled=true \
#--conf spark.sql.hive.convertMetastoreParquet=false \
#--conf spark.sql.parquet.writeLegacyFormat=true \
#--conf spark.mapreduce.input.fileinputformat.input.dir.recursive=true \
#--conf spark.hive.mapred.supports.subdirectories=true \
#--conf spark.mapred.input.dir.recursive=true \
#--conf spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive=true \
#/home/hadoop/data_code/first.py


spark.stop()