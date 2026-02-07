"""Data transformation module for processing and cleaning data."""

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col, when, lower, trim, regexp_replace,
    to_timestamp, current_timestamp, lit,
    count, sum as _sum, avg, max as _max, min as _min
)
from pyspark.sql.window import Window
import logging

logger = logging.getLogger(__name__)


def clean_data(df: DataFrame) -> DataFrame:
    """
    Apply basic data cleaning operations.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    logger.info("Cleaning data...")
    
    # Remove duplicates
    df = df.dropDuplicates()
    
    # Trim string columns
    string_cols = [field.name for field in df.schema.fields if str(field.dataType) == "StringType()"]
    for col_name in string_cols:
        df = df.withColumn(col_name, trim(col(col_name)))
    
    return df


def handle_missing_values(df: DataFrame, strategy: str = "drop") -> DataFrame:
    """
    Handle missing values in the DataFrame.
    
    Args:
        df: Input DataFrame
        strategy: Strategy for handling missing values ('drop', 'fill_zero', 'fill_mean')
        
    Returns:
        DataFrame with handled missing values
    """
    logger.info(f"Handling missing values with strategy: {strategy}")
    
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill_zero":
        return df.fillna(0)
    elif strategy == "fill_mean":
        # Calculate mean for numeric columns
        numeric_cols = [field.name for field in df.schema.fields 
                       if str(field.dataType) in ["IntegerType()", "DoubleType()", "FloatType()"]]
        
        fill_values = {}
        for col_name in numeric_cols:
            mean_val = df.select(avg(col(col_name))).first()[0]
            if mean_val is not None:
                fill_values[col_name] = mean_val
        
        return df.fillna(fill_values)
    else:
        logger.warning(f"Unknown strategy: {strategy}, returning original DataFrame")
        return df


def standardize_column_names(df: DataFrame) -> DataFrame:
    """
    Standardize column names to lowercase with underscores.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with standardized column names
    """
    logger.info("Standardizing column names...")
    
    for col_name in df.columns:
        new_col_name = col_name.lower().replace(" ", "_").replace("-", "_")
        df = df.withColumnRenamed(col_name, new_col_name)
    
    return df


def filter_by_condition(df: DataFrame, condition: str) -> DataFrame:
    """
    Filter DataFrame by a condition.
    
    Args:
        df: Input DataFrame
        condition: SQL-like condition string
        
    Returns:
        Filtered DataFrame
    """
    logger.info(f"Filtering data with condition: {condition}")
    return df.filter(condition)


def aggregate_data(df: DataFrame, group_by_cols: list, agg_cols: dict) -> DataFrame:
    """
    Aggregate data by grouping columns.
    
    Args:
        df: Input DataFrame
        group_by_cols: List of columns to group by
        agg_cols: Dictionary mapping column names to aggregation functions
                  e.g., {'value': 'sum', 'count': 'count'}
        
    Returns:
        Aggregated DataFrame
    """
    logger.info(f"Aggregating data by: {group_by_cols}")
    
    agg_exprs = []
    for col_name, agg_func in agg_cols.items():
        if agg_func == "sum":
            agg_exprs.append(_sum(col(col_name)).alias(f"{col_name}_sum"))
        elif agg_func == "avg":
            agg_exprs.append(avg(col(col_name)).alias(f"{col_name}_avg"))
        elif agg_func == "count":
            agg_exprs.append(count(col(col_name)).alias(f"{col_name}_count"))
        elif agg_func == "max":
            agg_exprs.append(_max(col(col_name)).alias(f"{col_name}_max"))
        elif agg_func == "min":
            agg_exprs.append(_min(col(col_name)).alias(f"{col_name}_min"))
    
    return df.groupBy(*group_by_cols).agg(*agg_exprs)


def add_derived_columns(df: DataFrame) -> DataFrame:
    """
    Add derived columns to the DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with derived columns
    """
    logger.info("Adding derived columns...")
    
    # Add processing timestamp
    df = df.withColumn("processing_timestamp", current_timestamp())
    
    # Add data quality flag (example)
    if "value" in df.columns:
        df = df.withColumn(
            "quality_flag",
            when(col("value").isNull(), "missing")
            .when(col("value") < 0, "invalid")
            .otherwise("valid")
        )
    
    return df


def transform_pipeline(df: DataFrame, config: dict = None) -> DataFrame:
    """
    Execute a complete transformation pipeline.
    
    Args:
        df: Input DataFrame
        config: Optional configuration dictionary
        
    Returns:
        Transformed DataFrame
    """
    logger.info("Starting transformation pipeline...")
    
    # Default configuration
    if config is None:
        config = {
            "standardize_names": True,
            "clean_data": True,
            "missing_strategy": "drop",
            "add_derived": True,
        }
    
    # Apply transformations
    if config.get("standardize_names", True):
        df = standardize_column_names(df)
    
    if config.get("clean_data", True):
        df = clean_data(df)
    
    if config.get("missing_strategy"):
        df = handle_missing_values(df, config["missing_strategy"])
    
    if config.get("add_derived", True):
        df = add_derived_columns(df)
    
    logger.info("Transformation pipeline completed")
    return df
