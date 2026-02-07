"""Utility functions for Spark operations."""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, current_timestamp
from delta import configure_spark_with_delta_pip
import logging

logger = logging.getLogger(__name__)


def get_spark_session(app_name: str = "DatabricksPySparkProject") -> SparkSession:
    """
    Create or get existing Spark session with Delta Lake support.
    
    Args:
        app_name: Name of the Spark application
        
    Returns:
        SparkSession configured with Delta Lake
    """
    try:
        # In Databricks, just get the existing session
        spark = SparkSession.builder.getOrCreate()
        logger.info(f"Retrieved existing Spark session: {app_name}")
    except Exception as e:
        logger.warning(f"Creating new Spark session: {e}")
        builder = (
            SparkSession.builder
            .appName(app_name)
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .config("spark.sql.adaptive.enabled", "true")
        )
        spark = configure_spark_with_delta_pip(builder).getOrCreate()
        logger.info(f"Created new Spark session: {app_name}")
    
    return spark


def add_metadata_columns(df: DataFrame) -> DataFrame:
    """
    Add standard metadata columns to a DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with added metadata columns
    """
    return df.withColumn("processed_timestamp", current_timestamp())


def optimize_dataframe(df: DataFrame, num_partitions: int = 200) -> DataFrame:
    """
    Optimize DataFrame by repartitioning.
    
    Args:
        df: Input DataFrame
        num_partitions: Number of partitions
        
    Returns:
        Optimized DataFrame
    """
    return df.repartition(num_partitions)


def read_delta_table(spark: SparkSession, table_path: str) -> DataFrame:
    """
    Read a Delta table.
    
    Args:
        spark: SparkSession
        table_path: Path to Delta table
        
    Returns:
        DataFrame containing table data
    """
    logger.info(f"Reading Delta table: {table_path}")
    return spark.read.format("delta").load(table_path)


def write_delta_table(
    df: DataFrame,
    table_path: str,
    mode: str = "overwrite",
    partition_by: list = None,
    optimize: bool = True
) -> None:
    """
    Write DataFrame to Delta table.
    
    Args:
        df: Input DataFrame
        table_path: Path to Delta table
        mode: Write mode (overwrite, append, etc.)
        partition_by: List of columns to partition by
        optimize: Whether to optimize the table after writing
    """
    logger.info(f"Writing Delta table: {table_path} with mode: {mode}")
    
    writer = df.write.format("delta").mode(mode)
    
    if partition_by:
        writer = writer.partitionBy(*partition_by)
    
    writer.save(table_path)
    
    if optimize:
        logger.info(f"Optimizing Delta table: {table_path}")
        spark = df.sparkSession
        spark.sql(f"OPTIMIZE delta.`{table_path}`")


def create_or_replace_table(
    df: DataFrame,
    catalog: str,
    schema: str,
    table_name: str,
    partition_by: list = None
) -> None:
    """
    Create or replace a table in Unity Catalog.
    
    Args:
        df: Input DataFrame
        catalog: Catalog name
        schema: Schema name
        table_name: Table name
        partition_by: List of columns to partition by
    """
    full_table_name = f"{catalog}.{schema}.{table_name}"
    logger.info(f"Creating/replacing table: {full_table_name}")
    
    writer = df.write.format("delta").mode("overwrite").option("overwriteSchema", "true")
    
    if partition_by:
        writer = writer.partitionBy(*partition_by)
    
    writer.saveAsTable(full_table_name)
