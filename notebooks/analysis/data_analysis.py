# Databricks notebook source
# MAGIC %md
# MAGIC # Data Analysis and Visualization
# MAGIC 
# MAGIC This notebook provides examples of data analysis and visualization using processed data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Load Data

# COMMAND ----------

from pyspark.sql.functions import *
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_style("whitegrid")

# Load data from Gold table
df = spark.table("main.default.gold_aggregated_data")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Summary Statistics

# COMMAND ----------

# Calculate summary statistics
summary = df.select(
    count("*").alias("total_records"),
    sum("total_value").alias("grand_total"),
    avg("avg_value").alias("overall_average")
).collect()[0]

print(f"Total Records: {summary.total_records}")
print(f"Grand Total Value: {summary.grand_total:,.2f}")
print(f"Overall Average: {summary.overall_average:,.2f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Category Analysis

# COMMAND ----------

# Analyze by category
category_stats = df.groupBy("category") \
    .agg(
        sum("record_count").alias("total_records"),
        sum("total_value").alias("total_value"),
        avg("avg_value").alias("average_value")
    ) \
    .orderBy(desc("total_value"))

display(category_stats)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Trend Analysis

# COMMAND ----------

# Analyze trends over time
trend_df = df.groupBy("year", "month") \
    .agg(
        sum("record_count").alias("monthly_records"),
        sum("total_value").alias("monthly_total")
    ) \
    .orderBy("year", "month")

display(trend_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Create Visualizations

# COMMAND ----------

# Convert to Pandas for visualization
pandas_df = category_stats.toPandas()

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(pandas_df['category'], pandas_df['total_value'])
plt.xlabel('Category')
plt.ylabel('Total Value')
plt.title('Total Value by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Export Results

# COMMAND ----------

# Export top insights to CSV
category_stats.coalesce(1) \
    .write \
    .format("csv") \
    .mode("overwrite") \
    .option("header", "true") \
    .save("/mnt/data/exports/category_analysis")

print("Analysis results exported successfully")
