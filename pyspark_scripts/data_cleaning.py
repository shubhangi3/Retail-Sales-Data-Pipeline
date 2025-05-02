from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesDataCleaning").getOrCreate()

# Load CSV from HDFS
df = spark.read.csv("hdfs://localhost:9000/user/sales_data/sales_data.csv", header=True, inferSchema=True)

# Drop nulls
df_clean = df.dropna()

# Cast types
df_clean = df_clean.withColumn("quantity", col("quantity").cast("int")) \
                   .withColumn("price", col("price").cast("float"))

df_clean.show()
