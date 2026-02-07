"""Unit tests for data transformation module."""

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from src.data_processing.transformation import (
    clean_data,
    standardize_column_names,
    handle_missing_values,
    aggregate_data,
)


@pytest.fixture(scope="module")
def spark():
    """Create a Spark session for testing."""
    spark = SparkSession.builder \
        .appName("test") \
        .master("local[2]") \
        .config("spark.sql.shuffle.partitions", "2") \
        .getOrCreate()
    yield spark
    spark.stop()


def test_clean_data(spark):
    """Test data cleaning function."""
    # Create test data with duplicates
    data = [
        (1, "  test  ", 100),
        (1, "  test  ", 100),
        (2, "test2", 200),
    ]
    df = spark.createDataFrame(data, ["id", "name", "value"])
    
    # Clean data
    cleaned_df = clean_data(df)
    
    # Verify duplicates removed
    assert cleaned_df.count() == 2


def test_standardize_column_names(spark):
    """Test column name standardization."""
    # Create test data with non-standard column names
    data = [(1, "test", 100)]
    df = spark.createDataFrame(data, ["Product ID", "Product-Name", "Product Value"])
    
    # Standardize names
    standardized_df = standardize_column_names(df)
    
    # Verify column names
    assert "product_id" in standardized_df.columns
    assert "product_name" in standardized_df.columns
    assert "product_value" in standardized_df.columns


def test_handle_missing_values_drop(spark):
    """Test handling missing values with drop strategy."""
    # Create test data with nulls
    data = [
        (1, "test", 100),
        (2, None, 200),
        (3, "test3", None),
    ]
    df = spark.createDataFrame(data, ["id", "name", "value"])
    
    # Handle missing values
    handled_df = handle_missing_values(df, strategy="drop")
    
    # Verify nulls dropped
    assert handled_df.count() == 1


def test_aggregate_data(spark):
    """Test data aggregation."""
    # Create test data
    data = [
        ("A", 100),
        ("A", 200),
        ("B", 150),
    ]
    df = spark.createDataFrame(data, ["category", "value"])
    
    # Aggregate data
    agg_df = aggregate_data(df, ["category"], {"value": "sum"})
    
    # Verify aggregation
    assert agg_df.count() == 2
    assert "value_sum" in agg_df.columns
    
    # Check specific values
    result = agg_df.filter(col("category") == "A").collect()[0]
    assert result.value_sum == 300
