# Databricks notebook source
# MAGIC %md
# MAGIC # API Integration Example
# MAGIC 
# MAGIC This notebook demonstrates how to fetch data from external APIs and process it with PySpark.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Setup

# COMMAND ----------

import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json

# API Configuration
API_BASE_URL = "https://api.example.com/v1"
API_KEY = dbutils.secrets.get(scope="api-scope", key="api-key")  # Store securely in Databricks secrets

print("API client configured")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Fetch Data from API

# COMMAND ----------

def fetch_api_data(endpoint, params=None):
    """
    Fetch data from API with error handling.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/{endpoint}",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

# Example: Fetch data
api_data = fetch_api_data("data", params={"limit": 100})

if api_data:
    print(f"Fetched {len(api_data)} records from API")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Convert to DataFrame

# COMMAND ----------

# Create DataFrame from API response
if api_data:
    df = spark.createDataFrame(api_data)
    display(df.limit(10))
    
    # Save to Delta Lake
    df.write \
        .format("delta") \
        .mode("overwrite") \
        .save("/mnt/data/api_data")
    
    print("API data saved to Delta Lake")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Schedule and Monitor
# MAGIC 
# MAGIC This notebook can be scheduled as a Databricks Job to run periodically and fetch fresh data from the API.
