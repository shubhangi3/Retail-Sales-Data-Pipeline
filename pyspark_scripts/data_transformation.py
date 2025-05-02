from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Import df_clean from the data_cleaning.py file
from data_cleaning import df_clean  # Make sure it's defined as df_clean in data_cleaning.py

# Perform transformations on df_clean
df_transformed = df_clean.withColumn("total", expr("quantity * price"))

# Example of a transformation: Top 3 selling products
top_products = df_transformed.groupBy("product").sum("total").orderBy("sum(total)", ascending=False)
top_products.show()

