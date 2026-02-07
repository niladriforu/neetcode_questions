"""Batch processing pipeline for data processing."""

from pyspark.sql import SparkSession
import logging
from typing import Optional

from ..utils import (
    get_spark_session,
    write_delta_table,
    read_delta_table,
    setup_logger,
)
from ..data_processing import (
    ingest_csv,
    transform_pipeline,
)
from ..config import config

logger = setup_logger(__name__)


class BatchPipeline:
    """
    Batch processing pipeline for ETL operations.
    """
    
    def __init__(self, spark: Optional[SparkSession] = None):
        """
        Initialize the batch pipeline.
        
        Args:
            spark: Optional SparkSession (creates new if not provided)
        """
        self.spark = spark or get_spark_session()
        self.config = config
    
    def run_ingestion(self, source_path: str, source_format: str = "csv"):
        """
        Run data ingestion step.
        
        Args:
            source_path: Path to source data
            source_format: Format of source data (csv, json, parquet)
            
        Returns:
            DataFrame with ingested data
        """
        logger.info(f"Starting ingestion from {source_path}")
        
        if source_format == "csv":
            df = ingest_csv(self.spark, source_path)
        elif source_format == "json":
            from ..data_processing import ingest_json
            df = ingest_json(self.spark, source_path)
        elif source_format == "parquet":
            from ..data_processing import ingest_parquet
            df = ingest_parquet(self.spark, source_path)
        else:
            raise ValueError(f"Unsupported format: {source_format}")
        
        logger.info(f"Ingested {df.count()} records")
        return df
    
    def run_transformation(self, df, transformation_config: Optional[dict] = None):
        """
        Run data transformation step.
        
        Args:
            df: Input DataFrame
            transformation_config: Optional transformation configuration
            
        Returns:
            Transformed DataFrame
        """
        logger.info("Starting transformation")
        
        transformed_df = transform_pipeline(df, transformation_config)
        
        logger.info(f"Transformed {transformed_df.count()} records")
        return transformed_df
    
    def run_load(
        self,
        df,
        output_path: str,
        mode: str = "overwrite",
        partition_by: list = None
    ):
        """
        Run data loading step.
        
        Args:
            df: DataFrame to load
            output_path: Output path for Delta table
            mode: Write mode
            partition_by: Columns to partition by
        """
        logger.info(f"Starting load to {output_path}")
        
        write_delta_table(
            df,
            output_path,
            mode=mode,
            partition_by=partition_by,
            optimize=True
        )
        
        logger.info("Load completed successfully")
    
    def run_full_pipeline(
        self,
        source_path: str,
        output_path: str,
        source_format: str = "csv",
        transformation_config: Optional[dict] = None,
        partition_by: list = None
    ):
        """
        Run the full ETL pipeline.
        
        Args:
            source_path: Path to source data
            output_path: Output path for Delta table
            source_format: Format of source data
            transformation_config: Transformation configuration
            partition_by: Columns to partition by
        """
        logger.info("Starting full batch pipeline")
        
        # Ingestion
        df = self.run_ingestion(source_path, source_format)
        
        # Transformation
        df = self.run_transformation(df, transformation_config)
        
        # Load
        self.run_load(df, output_path, partition_by=partition_by)
        
        logger.info("Full batch pipeline completed successfully")


def main():
    """Main entry point for the batch pipeline."""
    pipeline = BatchPipeline()
    
    # Example usage
    pipeline.run_full_pipeline(
        source_path="/mnt/data/input/sample.csv",
        output_path="/mnt/data/output/processed_data",
        source_format="csv",
        partition_by=["category"]
    )


if __name__ == "__main__":
    main()
