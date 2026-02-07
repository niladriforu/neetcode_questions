"""Data processing package."""

from .ingestion import (
    ingest_csv,
    ingest_json,
    ingest_parquet,
    ingest_delta,
    ingest_from_api,
    get_sample_schema,
)
from .transformation import (
    clean_data,
    handle_missing_values,
    standardize_column_names,
    filter_by_condition,
    aggregate_data,
    add_derived_columns,
    transform_pipeline,
)

__all__ = [
    # Ingestion
    "ingest_csv",
    "ingest_json",
    "ingest_parquet",
    "ingest_delta",
    "ingest_from_api",
    "get_sample_schema",
    # Transformation
    "clean_data",
    "handle_missing_values",
    "standardize_column_names",
    "filter_by_condition",
    "aggregate_data",
    "add_derived_columns",
    "transform_pipeline",
]
