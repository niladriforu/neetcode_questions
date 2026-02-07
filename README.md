# Databricks PySpark Project

A comprehensive PySpark-based data processing project designed to run on Databricks, featuring Delta Lake integration, ETL pipelines, and a web application interface.

## 🚀 Features

- **PySpark Data Processing**: Scalable data processing with Apache Spark
- **Delta Lake Integration**: ACID transactions and time travel for data lakes
- **Delta Live Tables**: Declarative ETL pipeline definitions
- **Batch Processing**: Scheduled ETL jobs for data ingestion and transformation
- **API Integration**: Client for fetching data from external APIs
- **Databricks App**: Flask-based web application for data visualization
- **Unity Catalog Support**: Integration with Databricks Unity Catalog
- **Comprehensive Testing**: Unit and integration tests included

## 📁 Project Structure

```
.
├── databricks_app/          # Flask web application
│   ├── app.py              # Main application file
│   ├── templates/          # HTML templates
│   └── static/             # Static assets (CSS, JS)
├── notebooks/               # Databricks notebooks
│   ├── etl/                # ETL pipeline notebooks
│   └── analysis/           # Data analysis notebooks
├── src/                     # Source code
│   ├── api/                # API client modules
│   ├── config/             # Configuration management
│   ├── data_processing/    # Data ingestion and transformation
│   ├── pipelines/          # Pipeline definitions
│   └── utils/              # Utility functions
├── resources/               # Databricks resource configurations
│   ├── dlt_pipeline.yml    # Delta Live Tables config
│   └── jobs.yml            # Jobs configuration
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── data/                    # Data files
│   ├── raw/                # Raw input data
│   └── processed/          # Processed output data
├── databricks.yml          # Databricks Asset Bundle config
├── requirements.txt        # Python dependencies
└── setup.py               # Package setup configuration
```

## 🛠️ Technologies

- **Apache Spark / PySpark**: Distributed data processing
- **Delta Lake**: Reliable data lake storage layer
- **Databricks**: Unified analytics platform
- **Flask**: Web application framework
- **Python 3.9+**: Programming language
- **pytest**: Testing framework
- **Chart.js**: Data visualization

## 📦 Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/niladriforu/neetcode_questions.git
cd neetcode_questions
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

### Databricks Setup

1. Install Databricks CLI:
```bash
pip install databricks-cli
```

2. Configure Databricks CLI:
```bash
databricks configure --token
```

3. Deploy using Databricks Asset Bundles:
```bash
databricks bundle deploy --target development
```

## 🚦 Quick Start

### Running the ETL Pipeline

#### Using Python Script:
```python
from src.pipelines import BatchPipeline

pipeline = BatchPipeline()
pipeline.run_full_pipeline(
    source_path="/mnt/data/input/sample.csv",
    output_path="/mnt/data/output/processed_data",
    source_format="csv"
)
```

#### Using Databricks Notebook:
1. Upload notebooks from `notebooks/etl/` to Databricks workspace
2. Run `01_etl_pipeline.py` notebook
3. Results will be written to Delta Lake tables

### Running the Web Application

#### Locally:
```bash
cd databricks_app
python app.py
```
Access the app at `http://localhost:8080`

#### On Databricks Apps:
1. Deploy the app using Databricks Apps feature
2. Configure the app to use your Databricks cluster
3. Access via the generated Databricks Apps URL

### Using the API Client

```python
from src.api import APIClient

# Initialize client
client = APIClient(
    base_url="https://api.example.com",
    api_key="your-api-key"
)

# Fetch data
data = client.get("/endpoint")

# Fetch paginated data
all_data = client.fetch_paginated_data("/endpoint", max_pages=10)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Environment
ENVIRONMENT=development
DEBUG=true

# Spark Configuration
SPARK_APP_NAME=DatabricksPySparkProject
SPARK_SHUFFLE_PARTITIONS=200

# Delta Lake
DELTA_CATALOG=main
DELTA_SCHEMA=default
CHECKPOINT_LOCATION=/tmp/checkpoints

# API Configuration
API_BASE_URL=https://api.example.com
API_KEY=your-api-key
API_TIMEOUT=30

# Flask App
SECRET_KEY=your-secret-key
PORT=8080
```

### Databricks Configuration

Edit `databricks.yml` to configure:
- Workspace settings
- Catalog and schema names
- Environment-specific configurations

## 📊 Data Processing Workflow

### Bronze Layer (Raw Data)
- Ingest data from various sources (CSV, JSON, API)
- Minimal transformations
- Store in Delta Lake bronze tables

### Silver Layer (Cleaned Data)
- Data validation and quality checks
- Remove duplicates
- Handle missing values
- Standardize formats

### Gold Layer (Business-Level Data)
- Aggregations and metrics
- Business logic applied
- Optimized for analytics and reporting

## 🧪 Testing

Run unit tests:
```bash
pytest tests/unit/
```

Run all tests with coverage:
```bash
pytest --cov=src tests/
```

Run specific test file:
```bash
pytest tests/unit/test_ingestion.py -v
```

## 📝 Notebooks

### ETL Notebooks
- `01_etl_pipeline.py`: Complete ETL pipeline with Bronze/Silver/Gold layers
- `02_api_integration.py`: Example of fetching data from external APIs

### Analysis Notebooks
- `data_analysis.py`: Data exploration and visualization examples

## 🔐 Security Best Practices

1. **Secrets Management**: Use Databricks Secrets for sensitive data
   ```python
   api_key = dbutils.secrets.get(scope="api-scope", key="api-key")
   ```

2. **Unity Catalog**: Use Unity Catalog for data governance

3. **Access Control**: Configure proper workspace and table permissions

4. **Network Security**: Use VPC peering or Private Link when needed

## 📈 Monitoring and Optimization

### Delta Table Optimization
```sql
-- Optimize table
OPTIMIZE delta.`/path/to/table`

-- Vacuum old files
VACUUM delta.`/path/to/table` RETAIN 168 HOURS
```

### Performance Tuning
- Use appropriate partitioning strategies
- Enable auto-optimize for Delta tables
- Monitor Spark UI for job performance
- Use Z-ordering for frequently queried columns

## 🚀 Deployment

### Deploy to Databricks

1. **Using Databricks Asset Bundles**:
```bash
# Deploy to development
databricks bundle deploy --target development

# Deploy to production
databricks bundle deploy --target production
```

2. **Using Databricks CLI**:
```bash
# Upload notebooks
databricks workspace import_dir notebooks /Workspace/notebooks

# Create job
databricks jobs create --json-file resources/jobs.yml
```

### Schedule Jobs

Jobs can be scheduled using:
- Databricks Jobs UI
- Databricks Asset Bundles (see `resources/jobs.yml`)
- Databricks REST API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Create an issue in the GitHub repository
- Check Databricks documentation: https://docs.databricks.com/
- PySpark documentation: https://spark.apache.org/docs/latest/api/python/

## 📚 Additional Resources

- [Databricks Best Practices](https://docs.databricks.com/best-practices/index.html)
- [Delta Lake Guide](https://docs.delta.io/latest/index.html)
- [PySpark API Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Delta Live Tables](https://docs.databricks.com/delta-live-tables/index.html)
- [Databricks Apps](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)

## ✨ Features Coming Soon

- [ ] Real-time streaming pipelines
- [ ] Machine learning model integration
- [ ] Advanced data quality checks
- [ ] Automated data lineage tracking
- [ ] Enhanced monitoring dashboards