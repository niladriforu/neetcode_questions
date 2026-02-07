"""Data ingestion module for reading data from various sources."""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
import logging

logger = logging.getLogger(__name__)


def get_sample_schema() -> StructType:
    """
    Define a sample schema for demo data.
    
    Returns:
        StructType schema definition
    """
    return StructType([
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("category", StringType(), True),
        StructField("value", DoubleType(), True),
        StructField("timestamp", TimestampType(), True),
    ])


def ingest_csv(spark: SparkSession, file_path: str, schema: StructType = None) -> DataFrame:
    """
    Ingest data from CSV file.
    
    Args:
        spark: SparkSession
        file_path: Path to CSV file
        schema: Optional schema definition
        
    Returns:
        DataFrame containing CSV data
    """
    logger.info(f"Ingesting CSV from: {file_path}")
    
    reader = spark.read.format("csv").option("header", "true")
    
    if schema:
        reader = reader.schema(schema)
    else:
        reader = reader.option("inferSchema", "true")
    
    return reader.load(file_path)


def ingest_json(spark: SparkSession, file_path: str, schema: StructType = None) -> DataFrame:
    """
    Ingest data from JSON file.
    
    Args:
        spark: SparkSession
        file_path: Path to JSON file
        schema: Optional schema definition
        
    Returns:
        DataFrame containing JSON data
    """
    logger.info(f"Ingesting JSON from: {file_path}")
    
    reader = spark.read.format("json")
    
    if schema:
        reader = reader.schema(schema)
    
    return reader.load(file_path)


def ingest_parquet(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Ingest data from Parquet file.
    
    Args:
        spark: SparkSession
        file_path: Path to Parquet file
        
    Returns:
        DataFrame containing Parquet data
    """
    logger.info(f"Ingesting Parquet from: {file_path}")
    return spark.read.format("parquet").load(file_path)


def ingest_delta(spark: SparkSession, table_path: str) -> DataFrame:
    """
    Ingest data from Delta table.
    
    Args:
        spark: SparkSession
        table_path: Path to Delta table or table name
        
    Returns:
        DataFrame containing Delta table data
    """
    logger.info(f"Ingesting Delta table from: {table_path}")
    return spark.read.format("delta").load(table_path)


def ingest_from_api(spark: SparkSession, api_data: list) -> DataFrame:
    """
    Ingest data from API response.
    
    Args:
        spark: SparkSession
        api_data: List of dictionaries from API response
        
    Returns:
        DataFrame containing API data
    """
    logger.info(f"Ingesting data from API (records: {len(api_data)})")
    return spark.createDataFrame(api_data)
