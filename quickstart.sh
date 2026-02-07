#!/bin/bash
# Quick Start Script for Databricks PySpark Project

echo "=================================="
echo "Databricks PySpark Project Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed"
    exit 1
fi

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Install package in development mode
echo ""
echo "Installing package in development mode..."
pip install -e .

# Create .env file from template
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file with your configuration"
fi

echo ""
echo "=================================="
echo "Setup completed successfully!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run tests: pytest tests/"
echo "3. Start the web app: cd databricks_app && python app.py"
echo "4. Deploy to Databricks: databricks bundle deploy --target development"
echo ""
echo "For more information, see README.md"
