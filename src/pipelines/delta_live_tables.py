"""Delta Live Tables pipeline definition."""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, current_timestamp
import dlt
import logging

logger = logging.getLogger(__name__)


# Bronze Layer: Raw data ingestion
@dlt.table(
    name="bronze_raw_data",
    comment="Raw data ingested from source",
    table_properties={
        "quality": "bronze",
        "pipelines.autoOptimize.managed": "true"
    }
)
def bronze_raw_data():
    """
    Bronze table: Ingest raw data from source.
    
    Returns:
        DataFrame with raw data
    """
    # This is a placeholder - in real implementation, this would read from your source
    # For example: spark.readStream.format("cloudFiles")...
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation", "/mnt/data/schema")
        .load("/mnt/data/raw")
        .withColumn("ingestion_timestamp", current_timestamp())
    )


# Silver Layer: Cleaned and validated data
@dlt.table(
    name="silver_cleaned_data",
    comment="Cleaned and validated data",
    table_properties={
        "quality": "silver",
        "pipelines.autoOptimize.managed": "true"
    }
)
@dlt.expect_or_drop("valid_id", "id IS NOT NULL")
@dlt.expect_or_drop("valid_value", "value >= 0")
def silver_cleaned_data():
    """
    Silver table: Clean and validate bronze data.
    
    Returns:
        DataFrame with cleaned data
    """
    return (
        dlt.read_stream("bronze_raw_data")
        .dropDuplicates(["id"])
        .withColumn("processing_timestamp", current_timestamp())
    )


# Gold Layer: Aggregated business-level data
@dlt.table(
    name="gold_aggregated_data",
    comment="Aggregated data for business analytics",
    table_properties={
        "quality": "gold",
        "pipelines.autoOptimize.managed": "true"
    }
)
def gold_aggregated_data():
    """
    Gold table: Aggregate data for analytics.
    
    Returns:
        DataFrame with aggregated data
    """
    from pyspark.sql.functions import sum, avg, count
    
    return (
        dlt.read("silver_cleaned_data")
        .groupBy("category")
        .agg(
            count("*").alias("record_count"),
            sum("value").alias("total_value"),
            avg("value").alias("average_value")
        )
        .withColumn("aggregation_timestamp", current_timestamp())
    )
