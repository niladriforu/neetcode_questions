# Data Directory

This directory contains sample data files for the project.

## Structure

- `raw/` - Raw input data files
  - `sample_data.csv` - Sample CSV data for testing

- `processed/` - Processed output data (Delta Lake tables)
  - This directory will be populated by the ETL pipelines

## Usage

The sample data in `raw/sample_data.csv` can be used to test the ETL pipeline and data processing modules.

In a production Databricks environment, you would typically mount cloud storage (S3, ADLS, GCS) to these paths using:

```python
# Mount Azure Data Lake Storage
dbutils.fs.mount(
    source = "wasbs://container@storage.blob.core.windows.net",
    mount_point = "/mnt/data",
    extra_configs = {"fs.azure.account.key.storage.blob.core.windows.net": dbutils.secrets.get(scope="storage-scope", key="storage-key")}
)
```

Or use Unity Catalog volumes for managed storage.
