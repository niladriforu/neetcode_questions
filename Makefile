.PHONY: help install test lint format clean run deploy

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -e ".[dev]"

test: ## Run tests
	pytest tests/ -v

test-cov: ## Run tests with coverage
	pytest --cov=src tests/ --cov-report=html --cov-report=term

lint: ## Run linters
	flake8 src/ tests/
	pylint src/

format: ## Format code with black
	black src/ tests/ databricks_app/

format-check: ## Check code formatting
	black --check src/ tests/ databricks_app/

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run-app: ## Run the Databricks app locally
	cd databricks_app && python app.py

deploy-dev: ## Deploy to Databricks development environment
	databricks bundle deploy --target development

deploy-prod: ## Deploy to Databricks production environment
	databricks bundle deploy --target production

validate: ## Validate Databricks bundle configuration
	databricks bundle validate

setup: ## Initial setup (create venv and install)
	python -m venv venv
	. venv/bin/activate && make install
	cp .env.example .env
	@echo "Setup complete! Edit .env file with your configuration"

docs: ## Generate documentation
	sphinx-build -b html docs/ docs/_build/

notebook-upload: ## Upload notebooks to Databricks
	databricks workspace import_dir notebooks /Workspace/notebooks --overwrite

all: format lint test ## Run format, lint, and test
