"""Configuration module for the Databricks project."""

import os
from typing import Optional
from pydantic import BaseModel, Field


class SparkConfig(BaseModel):
    """Spark configuration settings."""
    
    app_name: str = Field(default="DatabricksPySparkProject")
    shuffle_partitions: int = Field(default=200)
    adaptive_enabled: bool = Field(default=True)
    dynamic_allocation_enabled: bool = Field(default=True)


class DeltaConfig(BaseModel):
    """Delta Lake configuration settings."""
    
    catalog: str = Field(default="main")
    schema: str = Field(default="default")
    checkpoint_location: str = Field(default="/tmp/checkpoints")
    auto_optimize: bool = Field(default=True)
    auto_compact: bool = Field(default=True)


class APIConfig(BaseModel):
    """API configuration settings."""
    
    base_url: Optional[str] = Field(default=None)
    timeout: int = Field(default=30)
    max_retries: int = Field(default=3)
    api_key: Optional[str] = Field(default=None)


class AppConfig(BaseModel):
    """Main application configuration."""
    
    environment: str = Field(default="development")
    debug: bool = Field(default=True)
    spark: SparkConfig = Field(default_factory=SparkConfig)
    delta: DeltaConfig = Field(default_factory=DeltaConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables."""
        return cls(
            environment=os.getenv("ENVIRONMENT", "development"),
            debug=os.getenv("DEBUG", "true").lower() == "true",
            spark=SparkConfig(
                app_name=os.getenv("SPARK_APP_NAME", "DatabricksPySparkProject"),
                shuffle_partitions=int(os.getenv("SPARK_SHUFFLE_PARTITIONS", "200")),
            ),
            delta=DeltaConfig(
                catalog=os.getenv("DELTA_CATALOG", "main"),
                schema=os.getenv("DELTA_SCHEMA", "default"),
                checkpoint_location=os.getenv("CHECKPOINT_LOCATION", "/tmp/checkpoints"),
            ),
            api=APIConfig(
                base_url=os.getenv("API_BASE_URL"),
                timeout=int(os.getenv("API_TIMEOUT", "30")),
                api_key=os.getenv("API_KEY"),
            ),
        )


# Global configuration instance
config = AppConfig.from_env()
