# Databricks notebook source
# MAGIC %md
# MAGIC # ETL Pipeline - Data Ingestion and Processing
# MAGIC 
# MAGIC This notebook demonstrates a complete ETL pipeline using PySpark and Delta Lake on Databricks.
# MAGIC 
# MAGIC ## Pipeline Steps:
# MAGIC 1. **Extract**: Read data from various sources
# MAGIC 2. **Transform**: Clean and process the data
# MAGIC 3. **Load**: Write to Delta Lake tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Setup and Configuration

# COMMAND ----------

# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from delta.tables import DeltaTable
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
CATALOG = "main"
SCHEMA = "default"
SOURCE_PATH = "/mnt/data/raw"
OUTPUT_PATH = "/mnt/data/processed"

print("Configuration loaded successfully")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Data Ingestion

# COMMAND ----------

# Read sample data (CSV)
df_raw = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(f"{SOURCE_PATH}/sample_data.csv")

# Display sample records
display(df_raw.limit(10))

print(f"Total records ingested: {df_raw.count()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Data Transformation

# COMMAND ----------

# Clean and transform data
df_transformed = df_raw \
    .dropDuplicates() \
    .na.drop() \
    .withColumn("processing_timestamp", current_timestamp()) \
    .withColumn("year", year(col("timestamp"))) \
    .withColumn("month", month(col("timestamp")))

# Add data quality checks
df_transformed = df_transformed \
    .withColumn("quality_flag", 
                when(col("value").isNull(), "missing")
                .when(col("value") < 0, "invalid")
                .otherwise("valid"))

# Display transformed data
display(df_transformed.limit(10))

print(f"Records after transformation: {df_transformed.count()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Data Aggregation

# COMMAND ----------

# Create aggregated view
df_aggregated = df_transformed \
    .groupBy("category", "year", "month") \
    .agg(
        count("*").alias("record_count"),
        sum("value").alias("total_value"),
        avg("value").alias("avg_value"),
        min("value").alias("min_value"),
        max("value").alias("max_value")
    ) \
    .orderBy("year", "month", "category")

display(df_aggregated)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Write to Delta Lake

# COMMAND ----------

# Write raw data to Bronze table
df_raw.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .save(f"{OUTPUT_PATH}/bronze_data")

print("Bronze table created successfully")

# COMMAND ----------

# Write transformed data to Silver table
df_transformed.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .partitionBy("year", "month") \
    .save(f"{OUTPUT_PATH}/silver_data")

print("Silver table created successfully")

# COMMAND ----------

# Write aggregated data to Gold table
df_aggregated.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(f"{CATALOG}.{SCHEMA}.gold_aggregated_data")

print("Gold table created successfully")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Optimize Delta Tables

# COMMAND ----------

# Optimize Silver table
spark.sql(f"OPTIMIZE delta.`{OUTPUT_PATH}/silver_data`")

# Optimize Gold table
spark.sql(f"OPTIMIZE {CATALOG}.{SCHEMA}.gold_aggregated_data")

print("Tables optimized successfully")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Verify Results

# COMMAND ----------

# Query Gold table
gold_df = spark.table(f"{CATALOG}.{SCHEMA}.gold_aggregated_data")
display(gold_df)

print("Pipeline completed successfully!")
