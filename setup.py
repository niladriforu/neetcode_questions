"""Setup configuration for the Databricks PySpark project."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="databricks-pyspark-project",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A PySpark project for Databricks with Delta Lake and web app integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niladriforu/neetcode_questions",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pyspark>=3.4.0",
        "delta-spark>=2.4.0",
        "pandas>=1.5.3",
        "requests>=2.31.0",
        "flask>=2.3.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "pylint>=2.17.0",
        ],
    },
)
