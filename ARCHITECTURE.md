# Project Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATABRICKS WORKSPACE                      │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌──────────────────┐ │
│  │   Unity        │  │   Databricks   │  │   Databricks     │ │
│  │   Catalog      │  │   Notebooks    │  │   Jobs           │ │
│  └────────────────┘  └────────────────┘  └──────────────────┘ │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Delta Live Tables Pipeline                  │  │
│  │                                                          │  │
│  │   Bronze Layer → Silver Layer → Gold Layer              │  │
│  │   (Raw Data)     (Cleaned)      (Business Metrics)      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                  Databricks App                          │  │
│  │         ┌─────────────────────────────┐                 │  │
│  │         │    Flask Web Application    │                 │  │
│  │         │  - Dashboard                │                 │  │
│  │         │  - REST API                 │                 │  │
│  │         │  - Data Visualization       │                 │  │
│  │         └─────────────────────────────┘                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
         ┌──────────────────────────────────────┐
         │         Delta Lake Storage            │
         │  - ACID Transactions                  │
         │  - Time Travel                        │
         │  - Schema Evolution                   │
         └──────────────────────────────────────┘
                            ▲
                            │
         ┌──────────────────┴──────────────────┐
         │                                      │
    ┌────┴────┐                           ┌────┴────┐
    │ External│                           │  Cloud  │
    │  APIs   │                           │ Storage │
    │         │                           │ (S3/    │
    │         │                           │ ADLS/   │
    │         │                           │ GCS)    │
    └─────────┘                           └─────────┘
```

## Data Flow

### ETL Pipeline Flow

```
1. INGESTION
   ├── CSV Files ──────────┐
   ├── JSON Files ─────────┤
   ├── API Endpoints ──────┤──▶ Bronze Tables (Raw Data)
   ├── Parquet Files ──────┤
   └── Streaming Sources ──┘

2. TRANSFORMATION
   Bronze Tables ──▶ [Data Cleaning] ──▶ Silver Tables (Cleaned)
                     │
                     ├── Remove Duplicates
                     ├── Handle Missing Values
                     ├── Standardize Formats
                     └── Quality Checks

3. AGGREGATION
   Silver Tables ──▶ [Business Logic] ──▶ Gold Tables (Analytics)
                     │
                     ├── Aggregations
                     ├── Metrics Calculation
                     ├── Joins
                     └── Business Rules

4. CONSUMPTION
   Gold Tables ──▶ ├── Databricks App Dashboard
                   ├── REST API Endpoints
                   ├── Business Intelligence Tools
                   └── Data Science Workflows
```

## Component Architecture

### Source Code Structure

```
src/
├── api/                    # External API Integration
│   ├── client.py          # HTTP client with retry logic
│   └── __init__.py
│
├── config/                 # Configuration Management
│   └── __init__.py        # Pydantic config models
│
├── data_processing/        # Core ETL Logic
│   ├── ingestion.py       # Data ingestion from sources
│   ├── transformation.py  # Data transformation logic
│   └── __init__.py
│
├── pipelines/              # Pipeline Orchestration
│   ├── batch_pipeline.py  # Batch processing workflow
│   ├── delta_live_tables.py # DLT definitions
│   └── __init__.py
│
└── utils/                  # Shared Utilities
    ├── spark_utils.py     # Spark helper functions
    ├── logger.py          # Logging configuration
    └── __init__.py
```

### Web Application Architecture

```
databricks_app/
├── app.py                  # Flask application
│   ├── Route: /           # Home page
│   ├── Route: /dashboard  # Interactive dashboard
│   ├── Route: /api/data   # Data retrieval endpoint
│   ├── Route: /api/stats  # Statistics endpoint
│   └── Route: /api/aggregated # Aggregated data endpoint
│
├── templates/              # HTML templates
│   ├── index.html         # Landing page
│   └── dashboard.html     # Dashboard with Chart.js
│
└── static/                 # Static assets
    └── (CSS, JS, images)
```

### Testing Architecture

```
tests/
├── unit/                   # Unit Tests
│   ├── test_ingestion.py  # Test data ingestion
│   ├── test_transformation.py # Test transformations
│   └── test_api_client.py # Test API client
│
└── integration/            # Integration Tests
    └── (End-to-end tests)
```

## Deployment Architecture

### Development Environment

```
Developer Workstation
       │
       │ git push
       ▼
GitHub Repository
       │
       │ databricks bundle deploy --target dev
       ▼
Databricks Development Workspace
       │
       ├── Dev Catalog (main_dev.default)
       ├── Dev Cluster
       └── Dev Jobs
```

### Production Environment

```
GitHub Repository
       │
       │ databricks bundle deploy --target prod
       ▼
Databricks Production Workspace
       │
       ├── Prod Catalog (main.default)
       ├── Prod Cluster (Auto-scaling)
       ├── Scheduled Jobs
       └── Monitoring & Alerts
```

## Data Architecture (Medallion)

### Bronze Layer
- **Purpose**: Raw data ingestion
- **Characteristics**:
  - Minimal transformation
  - All source data preserved
  - Append-only
  - Full audit trail

### Silver Layer
- **Purpose**: Cleaned and validated data
- **Characteristics**:
  - Deduplicated
  - Standardized formats
  - Quality checks applied
  - Type conversions

### Gold Layer
- **Purpose**: Business-level aggregations
- **Characteristics**:
  - Aggregated metrics
  - Business logic applied
  - Optimized for queries
  - Ready for analytics

## Technology Stack

```
┌─────────────────────────────────────────────┐
│           Presentation Layer                 │
│  ┌────────────┐  ┌──────────────────────┐  │
│  │   Flask    │  │    Chart.js          │  │
│  │   HTML/CSS │  │    (Visualization)   │  │
│  └────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────────┐
│           Application Layer                  │
│  ┌────────────┐  ┌──────────────────────┐  │
│  │  Python    │  │    PySpark           │  │
│  │  3.9+      │  │    (Processing)      │  │
│  └────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────────┐
│            Data Layer                        │
│  ┌────────────┐  ┌──────────────────────┐  │
│  │ Delta Lake │  │  Unity Catalog       │  │
│  │ (Storage)  │  │  (Governance)        │  │
│  └────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────┘
                    │
┌─────────────────────────────────────────────┐
│         Infrastructure Layer                 │
│  ┌────────────┐  ┌──────────────────────┐  │
│  │ Databricks │  │  Cloud Storage       │  │
│  │ Runtime    │  │  (S3/ADLS/GCS)      │  │
│  └────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────┘
```

## Security Architecture

```
┌──────────────────────────────────────────────────┐
│              Security Layers                      │
│                                                   │
│  Authentication                                   │
│  ├── Databricks Token                           │
│  ├── Service Principal                          │
│  └── SSO Integration                            │
│                                                   │
│  Authorization                                    │
│  ├── Unity Catalog ACLs                         │
│  ├── Table Permissions                          │
│  └── Cluster Access Controls                    │
│                                                   │
│  Secrets Management                               │
│  ├── Databricks Secrets                         │
│  ├── Key Vault Integration                      │
│  └── Environment Variables                      │
│                                                   │
│  Network Security                                 │
│  ├── VPC/VNet Peering                           │
│  ├── Private Link                                │
│  └── IP Whitelisting                            │
└──────────────────────────────────────────────────┘
```

## Monitoring & Observability

```
┌──────────────────────────────────────────────────┐
│            Monitoring Stack                       │
│                                                   │
│  Application Logs                                 │
│  ├── Python logging                              │
│  ├── Spark logs                                  │
│  └── Flask logs                                  │
│                                                   │
│  Job Monitoring                                   │
│  ├── Job run history                             │
│  ├── Task success/failure                        │
│  └── Email notifications                         │
│                                                   │
│  Performance Metrics                              │
│  ├── Spark UI                                    │
│  ├── Query execution plans                       │
│  └── Resource utilization                        │
│                                                   │
│  Data Quality                                     │
│  ├── DLT expectations                            │
│  ├── Row counts                                  │
│  └── Schema validation                           │
└──────────────────────────────────────────────────┘
```

## Scalability Considerations

### Horizontal Scaling
- Auto-scaling clusters
- Distributed processing with Spark
- Partition strategies for large datasets

### Vertical Scaling
- Configurable cluster sizes
- Memory optimization
- Shuffle partition tuning

### Storage Optimization
- Delta Lake optimization
- Z-ordering for queries
- Data partitioning
- Vacuum old versions

## Best Practices Implemented

1. **Code Organization**: Modular, maintainable structure
2. **Error Handling**: Comprehensive try-catch blocks
3. **Logging**: Consistent logging throughout
4. **Testing**: Unit and integration tests
5. **Documentation**: Extensive inline and external docs
6. **Configuration**: Externalized configuration
7. **Security**: No hardcoded credentials
8. **Performance**: Optimized for large-scale data

## Future Enhancements

- Real-time streaming with Structured Streaming
- Machine learning pipelines with MLflow
- Advanced monitoring with Grafana
- CI/CD with GitHub Actions
- Data lineage tracking
- Advanced data quality framework
