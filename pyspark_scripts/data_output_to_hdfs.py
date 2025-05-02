from data_transformation import df_transformed  # Import df_transformed from the other script

# Save final transformed data to HDFS in CSV format
df_transformed.write.mode("overwrite").csv("hdfs://localhost:9000/user/output/top_products")

