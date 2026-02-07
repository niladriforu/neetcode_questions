# API Documentation

## Overview

This document describes the REST API endpoints available in the Databricks App.

Base URL (local): `http://localhost:8080`
Base URL (Databricks Apps): `https://your-workspace.cloud.databricks.com/apps/<app-id>`

## Authentication

Currently, the API uses the Databricks session authentication. For production use, consider implementing:
- API keys
- OAuth 2.0
- JWT tokens

## Endpoints

### Health Check

Check if the API is running and Spark session is available.

**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "spark_available": true
}
```

**Status Codes**:
- `200 OK`: Service is healthy

---

### Get Data

Fetch data from a Delta table.

**Endpoint**: `GET /api/data`

**Query Parameters**:
- `table` (string, optional): Table name in format `catalog.schema.table`. Default: `default.sample_data`
- `limit` (integer, optional): Maximum number of records to return. Default: `100`

**Example Request**:
```bash
curl "http://localhost:8080/api/data?table=main.default.sample_data&limit=50"
```

**Response**:
```json
{
  "success": true,
  "count": 50,
  "data": [
    {
      "id": 1,
      "name": "Product A",
      "category": "Electronics",
      "value": 299.99,
      "timestamp": "2024-01-15T10:30:00"
    },
    ...
  ]
}
```

**Status Codes**:
- `200 OK`: Success
- `500 Internal Server Error`: Error fetching data

---

### Get Statistics

Fetch statistics from a Delta table.

**Endpoint**: `GET /api/stats`

**Query Parameters**:
- `table` (string, optional): Table name. Default: `default.sample_data`

**Example Request**:
```bash
curl "http://localhost:8080/api/stats?table=main.default.sample_data"
```

**Response**:
```json
{
  "success": true,
  "stats": {
    "total_records": 1500,
    "unique_categories": 5
  }
}
```

**Status Codes**:
- `200 OK`: Success
- `500 Internal Server Error`: Error calculating stats

---

### Get Aggregated Data

Fetch aggregated data grouped by a specified column.

**Endpoint**: `GET /api/aggregated`

**Query Parameters**:
- `table` (string, optional): Table name. Default: `default.sample_data`
- `group_by` (string, optional): Column to group by. Default: `category`

**Example Request**:
```bash
curl "http://localhost:8080/api/aggregated?table=main.default.sample_data&group_by=category"
```

**Response**:
```json
{
  "success": true,
  "count": 5,
  "data": [
    {
      "category": "Electronics",
      "count": 450,
      "avg_value": 549.99,
      "total_value": 247495.50
    },
    {
      "category": "Clothing",
      "count": 320,
      "avg_value": 65.50,
      "total_value": 20960.00
    },
    ...
  ]
}
```

**Status Codes**:
- `200 OK`: Success
- `500 Internal Server Error`: Error aggregating data

---

## Error Handling

All error responses follow this format:

```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

Common error scenarios:
- Table not found
- Invalid table name format
- Spark session not available
- Invalid query parameters
- Database connection issues

## Rate Limiting

Currently, no rate limiting is implemented. For production deployments, consider:
- Implementing rate limiting per user/IP
- Using Databricks SQL Warehouse for better resource management
- Caching frequently accessed data

## Usage Examples

### Python

```python
import requests

# Base URL
base_url = "http://localhost:8080"

# Get data
response = requests.get(f"{base_url}/api/data", params={
    "table": "main.default.sample_data",
    "limit": 100
})
data = response.json()

if data["success"]:
    print(f"Retrieved {data['count']} records")
    for record in data["data"]:
        print(record)
```

### JavaScript

```javascript
// Fetch data
fetch('/api/data?table=main.default.sample_data&limit=100')
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log(`Retrieved ${data.count} records`);
      data.data.forEach(record => console.log(record));
    }
  })
  .catch(error => console.error('Error:', error));
```

### cURL

```bash
# Get statistics
curl -X GET "http://localhost:8080/api/stats?table=main.default.sample_data"

# Get aggregated data
curl -X GET "http://localhost:8080/api/aggregated?table=main.default.sample_data&group_by=category"
```

## Extending the API

To add new endpoints, edit `databricks_app/app.py`:

```python
@app.route('/api/custom-endpoint')
def custom_endpoint():
    """Custom endpoint description."""
    try:
        # Your logic here
        result = {"success": True, "data": "..."}
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500
```

## Best Practices

1. **Use appropriate limits**: Don't fetch all data at once
2. **Handle errors gracefully**: Always check the `success` field
3. **Cache results**: Cache data that doesn't change frequently
4. **Use pagination**: Implement pagination for large datasets
5. **Monitor performance**: Track API response times
6. **Secure sensitive data**: Don't expose internal table structures

## Future Enhancements

Planned improvements:
- [ ] Authentication and authorization
- [ ] Pagination support
- [ ] Filtering capabilities
- [ ] Sorting options
- [ ] Field selection (partial responses)
- [ ] WebSocket support for real-time updates
- [ ] GraphQL endpoint
- [ ] API versioning
