# Deployment Guide

This guide covers deploying the PySpark project to Databricks.

## Prerequisites

1. **Databricks Workspace**: Access to a Databricks workspace
2. **Databricks CLI**: Installed and configured
3. **Python 3.9+**: For local development
4. **Git**: For version control

## Deployment Steps

### 1. Setup Databricks CLI

Install the Databricks CLI:
```bash
pip install databricks-cli
```

Configure with your workspace:
```bash
databricks configure --token
```

You'll be prompted for:
- Databricks Host (e.g., `https://your-workspace.cloud.databricks.com`)
- Token (generate from User Settings > Access Tokens)

### 2. Create Required Resources

#### Unity Catalog Setup (if using Unity Catalog)

```sql
-- Create catalog
CREATE CATALOG IF NOT EXISTS main;

-- Create schema
CREATE SCHEMA IF NOT EXISTS main.default;

-- Grant permissions
GRANT USE CATALOG ON CATALOG main TO `your_user_or_group`;
GRANT USE SCHEMA ON SCHEMA main.default TO `your_user_or_group`;
```

#### Mount Storage (if not using Unity Catalog)

For Azure:
```python
dbutils.fs.mount(
    source = "wasbs://container@storage.blob.core.windows.net",
    mount_point = "/mnt/data",
    extra_configs = {
        "fs.azure.account.key.storage.blob.core.windows.net": 
        dbutils.secrets.get(scope="storage-scope", key="storage-key")
    }
)
```

For AWS S3:
```python
dbutils.fs.mount(
    source = "s3a://bucket-name",
    mount_point = "/mnt/data",
    extra_configs = {
        "fs.s3a.access.key": dbutils.secrets.get(scope="aws-scope", key="access-key"),
        "fs.s3a.secret.key": dbutils.secrets.get(scope="aws-scope", key="secret-key")
    }
)
```

### 3. Deploy Using Databricks Asset Bundles

#### Initialize Bundle (if not already done)

The project already includes `databricks.yml`. Review and update it:

```yaml
bundle:
  name: databricks-pyspark-project

workspace:
  host: https://your-workspace.cloud.databricks.com
```

#### Validate Configuration

```bash
databricks bundle validate
```

#### Deploy to Development

```bash
databricks bundle deploy --target development
```

#### Deploy to Production

```bash
databricks bundle deploy --target production
```

### 4. Upload Notebooks

#### Using Databricks CLI

```bash
# Upload all notebooks
databricks workspace import_dir notebooks /Workspace/Users/your.email@example.com/notebooks --overwrite
```

#### Using Web UI

1. Go to Databricks workspace
2. Navigate to Workspace
3. Right-click > Import
4. Select the notebook files

### 5. Create and Configure Jobs

#### Using Databricks UI

1. Go to Workflows > Jobs
2. Click "Create Job"
3. Configure tasks:
   - Task 1: ETL Pipeline (notebook: `01_etl_pipeline.py`)
   - Task 2: API Integration (notebook: `02_api_integration.py`)
   - Task 3: Data Analysis (notebook: `data_analysis.py`)
4. Set dependencies between tasks
5. Configure schedule (e.g., daily at 2 AM)

#### Using Configuration File

```bash
databricks jobs create --json-file resources/jobs.yml
```

### 6. Setup Delta Live Tables Pipeline

#### Using Databricks UI

1. Go to Workflows > Delta Live Tables
2. Click "Create Pipeline"
3. Configure:
   - Name: `data_processing_pipeline`
   - Notebook: `notebooks/etl/01_etl_pipeline.py`
   - Target: `main.default`
   - Cluster settings: Auto-scaling (1-5 workers)

#### Using Configuration File

```bash
databricks pipelines create --json-file resources/dlt_pipeline.yml
```

### 7. Deploy Databricks App

#### Prepare the App

1. Ensure all dependencies are in `requirements.txt`
2. Test locally first:
   ```bash
   cd databricks_app
   python app.py
   ```

#### Deploy to Databricks Apps

1. Go to Apps in Databricks workspace
2. Click "Create App"
3. Select "Python Web App"
4. Upload the `databricks_app` directory
5. Configure:
   - Name: Data Dashboard App
   - Compute: Select or create a cluster
   - Environment variables (from `.env`)
6. Click "Deploy"

### 8. Configure Secrets

Store sensitive data in Databricks Secrets:

```bash
# Create secret scope
databricks secrets create-scope --scope api-scope

# Add secrets
databricks secrets put --scope api-scope --key api-key
databricks secrets put --scope storage-scope --key storage-key
```

Usage in code:
```python
api_key = dbutils.secrets.get(scope="api-scope", key="api-key")
```

### 9. Setup Monitoring

#### Configure Job Notifications

In the job configuration, add email notifications:
```yaml
email_notifications:
  on_start:
    - "data-team@example.com"
  on_success:
    - "data-team@example.com"
  on_failure:
    - "data-team@example.com"
    - "alerts@example.com"
```

#### Enable Logging

Configure cluster to send logs to cloud storage:
```json
{
  "cluster_log_conf": {
    "s3": {
      "destination": "s3://bucket/logs",
      "region": "us-east-1"
    }
  }
}
```

## Verification

### Test the Deployment

1. **Run a test job**:
   ```bash
   databricks jobs run-now --job-id <job-id>
   ```

2. **Check job status**:
   ```bash
   databricks jobs get-run --run-id <run-id>
   ```

3. **Access the web app**:
   - Navigate to the Databricks Apps URL
   - Verify data is loading correctly

4. **Query Delta tables**:
   ```sql
   SELECT * FROM main.default.gold_aggregated_data LIMIT 10;
   ```

## Troubleshooting

### Common Issues

1. **Import errors in notebooks**:
   - Ensure all dependencies are installed on the cluster
   - Check Python version compatibility

2. **Permission errors**:
   - Verify Unity Catalog permissions
   - Check cluster access controls

3. **Delta table not found**:
   - Verify table paths are correct
   - Ensure tables were created successfully

4. **App connection issues**:
   - Check cluster is running
   - Verify network configuration
   - Review app logs

## Rollback

If you need to rollback:

1. **Revert notebooks**:
   ```bash
   databricks workspace import_dir notebooks-backup /Workspace/Users/your.email@example.com/notebooks --overwrite
   ```

2. **Delete current job**:
   ```bash
   databricks jobs delete --job-id <job-id>
   ```

3. **Restore previous job**:
   ```bash
   databricks jobs create --json-file resources/jobs-backup.yml
   ```

## Production Checklist

- [ ] All tests passing
- [ ] Secrets configured
- [ ] Monitoring and alerts set up
- [ ] Job schedules configured
- [ ] Access controls reviewed
- [ ] Data retention policies configured
- [ ] Backup strategy in place
- [ ] Documentation updated
- [ ] Team trained on new workflows

## Next Steps

After deployment:
1. Monitor initial runs closely
2. Optimize based on performance metrics
3. Set up data quality monitoring
4. Plan for scaling as data grows
5. Schedule regular reviews and updates
