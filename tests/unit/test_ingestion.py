"""Unit tests for data ingestion module."""

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from src.data_processing.ingestion import (
    get_sample_schema,
    ingest_csv,
    ingest_json,
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


def test_get_sample_schema():
    """Test sample schema generation."""
    schema = get_sample_schema()
    assert isinstance(schema, StructType)
    assert len(schema.fields) == 5
    assert schema.fields[0].name == "id"


def test_ingest_csv(spark, tmp_path):
    """Test CSV ingestion."""
    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("id,name,value\n1,test,100\n2,test2,200\n")
    
    # Ingest CSV
    df = ingest_csv(spark, str(csv_file))
    
    # Verify
    assert df.count() == 2
    assert "id" in df.columns
    assert "name" in df.columns
    assert "value" in df.columns


def test_ingest_json(spark, tmp_path):
    """Test JSON ingestion."""
    # Create a temporary JSON file
    json_file = tmp_path / "test.json"
    json_file.write_text('{"id": 1, "name": "test", "value": 100}\n{"id": 2, "name": "test2", "value": 200}\n')
    
    # Ingest JSON
    df = ingest_json(spark, str(json_file))
    
    # Verify
    assert df.count() == 2
    assert "id" in df.columns


def test_ingest_from_api(spark):
    """Test API data ingestion."""
    from src.data_processing.ingestion import ingest_from_api
    
    # Sample API data
    api_data = [
        {"id": 1, "name": "item1", "value": 100},
        {"id": 2, "name": "item2", "value": 200},
    ]
    
    # Ingest API data
    df = ingest_from_api(spark, api_data)
    
    # Verify
    assert df.count() == 2
    assert "id" in df.columns
