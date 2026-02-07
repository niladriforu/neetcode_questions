"""Databricks App - Flask web application for data visualization."""

from flask import Flask, render_template, jsonify, request
from pyspark.sql import SparkSession
import logging
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Spark session (in Databricks context)
try:
    spark = SparkSession.builder.getOrCreate()
    logger.info("Spark session initialized")
except Exception as e:
    logger.error(f"Failed to initialize Spark: {e}")
    spark = None


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard page with data visualizations."""
    return render_template('dashboard.html')


@app.route('/api/data')
def get_data():
    """
    API endpoint to fetch data from Delta table.
    
    Returns:
        JSON response with data
    """
    try:
        # Get query parameters
        table_name = request.args.get('table', 'default.sample_data')
        limit = int(request.args.get('limit', 100))
        
        if not spark:
            return jsonify({'error': 'Spark session not available'}), 500
        
        # Query Delta table
        logger.info(f"Querying table: {table_name}")
        df = spark.sql(f"SELECT * FROM {table_name} LIMIT {limit}")
        
        # Convert to JSON
        data = [row.asDict() for row in df.collect()]
        
        return jsonify({
            'success': True,
            'count': len(data),
            'data': data
        })
    
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/stats')
def get_stats():
    """
    API endpoint to fetch statistics from data.
    
    Returns:
        JSON response with statistics
    """
    try:
        table_name = request.args.get('table', 'default.sample_data')
        
        if not spark:
            return jsonify({'error': 'Spark session not available'}), 500
        
        # Query for statistics
        logger.info(f"Calculating statistics for: {table_name}")
        stats_df = spark.sql(f"""
            SELECT 
                COUNT(*) as total_records,
                COUNT(DISTINCT category) as unique_categories
            FROM {table_name}
        """)
        
        stats = stats_df.collect()[0].asDict()
        
        return jsonify({
            'success': True,
            'stats': stats
        })
    
    except Exception as e:
        logger.error(f"Error calculating stats: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/aggregated')
def get_aggregated():
    """
    API endpoint to fetch aggregated data.
    
    Returns:
        JSON response with aggregated data
    """
    try:
        table_name = request.args.get('table', 'default.sample_data')
        group_by = request.args.get('group_by', 'category')
        
        if not spark:
            return jsonify({'error': 'Spark session not available'}), 500
        
        # Query for aggregated data
        logger.info(f"Aggregating data by: {group_by}")
        agg_df = spark.sql(f"""
            SELECT 
                {group_by},
                COUNT(*) as count,
                AVG(value) as avg_value,
                SUM(value) as total_value
            FROM {table_name}
            GROUP BY {group_by}
            ORDER BY count DESC
        """)
        
        data = [row.asDict() for row in agg_df.collect()]
        
        return jsonify({
            'success': True,
            'count': len(data),
            'data': data
        })
    
    except Exception as e:
        logger.error(f"Error aggregating data: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'spark_available': spark is not None
    })


if __name__ == '__main__':
    # Run the app
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
