# Retail Sales Data Pipeline using PySpark and Hadoop

## Tech Stack
- **Python**
- **PySpark**
- **Hadoop (HDFS)**
- **GitHub**

## 📁 Project Structure

Retail-Sales-Data-Pipeline/
│
├── data/
│ └── sales_data.csv # Sample dataset
├── hdfs_upload.sh # Script to upload CSV to HDFS
├── pyspark_scripts/
│ ├── data_cleaning.py # Cleans raw sales data
│ ├── data_transformation.py # Adds "total" column
│ └── data_output.py # Writes result to HDFS
└── README.md # Project documentation

## Dataset Columns
- `id`
- `customer_name`
- `product`
- `category`
- `quantity`
- `price`
- `date`
- `total` (derived)

## Pipeline Steps

1. **Upload CSV to HDFS**  
   `hdfs dfs -put sales_data.csv /user/sales_data/`

2. **Data Cleaning** (`data_cleaning.py`)  
   - Drops nulls
   - Casts `quantity` to int and `price` to float

3. **Transformation** (`data_transformation.py`)  
   - Adds a new column `total = quantity * price`
   - Aggregates top products

4. **Save to HDFS** (`data_output.py`)  
   - Final data written to: `/user/output/top_products`

## Sample Output

```text
id,customer_name,product,category,quantity,price,date,total
101,John Doe,Laptop,Electronics,1,60000.0,2024-12-01,60000.0
...


## How to run:--
spark-submit pyspark_scripts/data_cleaning.py
spark-submit pyspark_scripts/data_transformation.py
spark-submit pyspark_scripts/data_output.py
