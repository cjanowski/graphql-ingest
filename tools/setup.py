#!/usr/bin/env python3
"""
Setup script for CSV to PostgreSQL GraphQL CLI Tool
A beautiful, feature-rich CLI for data ingestion and GraphQL API serving.
"""

import sys
from pathlib import Path
from setuptools import setup, find_packages

# Ensure we're using Python 3.8+
if sys.version_info < (3, 8):
    print("❌ This package requires Python 3.8 or higher!")
    print(f"   You are using Python {sys.version_info.major}.{sys.version_info.minor}")
    sys.exit(1)

# Read long description from README
README_PATH = Path(__file__).parent / "README.md"
LONG_DESCRIPTION = (
    README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
)

# Read requirements from requirements.txt
REQUIREMENTS_PATH = Path(__file__).parent / "requirements.txt"
if REQUIREMENTS_PATH.exists():
    with open(REQUIREMENTS_PATH, "r") as f:
        REQUIREMENTS = [
            line.strip() for line in f if line.strip() and not line.startswith("#")
        ]
else:
    REQUIREMENTS = [
        "click>=8.1.7",
        "pandas>=2.1.4",
        "sqlalchemy>=2.0.23",
        "psycopg2-binary>=2.9.9",
        "strawberry-graphql>=0.216.1",
        "uvicorn>=0.24.0",
        "fastapi>=0.104.1",
        "python-dotenv>=1.0.0",
        "alembic>=1.13.1",
        "requests>=2.31.0",
    ]

# Development dependencies
DEV_REQUIREMENTS = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
    "pre-commit>=3.0.0",
]

# Optional dependencies for enhanced features
EXTRAS_REQUIRE = {
    "dev": DEV_REQUIREMENTS,
    "test": ["pytest>=7.0.0", "pytest-asyncio>=0.21.0"],
    "lint": ["black>=23.0.0", "flake8>=6.0.0", "mypy>=1.0.0"],
    "docs": ["sphinx>=7.0.0", "sphinx-rtd-theme>=1.3.0"],
    "all": DEV_REQUIREMENTS + ["sphinx>=7.0.0", "sphinx-rtd-theme>=1.3.0"],
}

setup(
    # Basic package information
    name="csv-graphql-cli",
    version="1.0.0",
    # Package description
    description="🍓 A beautiful CLI tool for ingesting CSV files into PostgreSQL and serving data via GraphQL",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # Author information
    author="Cory Janowski",
    author_email="cory@example.com",
    maintainer="Cory Janowski",
    maintainer_email="cory@example.com",
    # URLs
    url="https://github.com/coryjanowski/csv-graphql-cli",
    project_urls={
        "Homepage": "https://github.com/coryjanowski/csv-graphql-cli",
        "Documentation": "https://github.com/coryjanowski/csv-graphql-cli#readme",
        "Repository": "https://github.com/coryjanowski/csv-graphql-cli",
        "Bug Tracker": "https://github.com/coryjanowski/csv-graphql-cli/issues",
        "Changelog": "https://github.com/coryjanowski/csv-graphql-cli/releases",
    },
    # Package structure
    packages=find_packages(),
    py_modules=["cli", "config", "database", "graphql_schema", "server"],
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.csv", "*.example", "LICENSE"],
    },
    # Dependencies
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.8",
    # CLI entry points - Multiple ways to access the tool!
    entry_points={
        "console_scripts": [
            # Primary CLI command
            "csv-graphql=cli:cli",
            "csvgql=cli:cli",  # Short alias
            # Individual command aliases for convenience
            "csv-ingest=cli:ingest",
            "csv-serve=cli:serve",
            "csv-preview=cli:preview",
            "csv-tables=cli:tables",
            # Development shortcuts
            "csvgql-dev=server:main",  # Direct server start
        ],
    },
    # Package metadata
    license="MIT",
    license_files=["LICENSE"],
    keywords=[
        "csv",
        "postgresql",
        "graphql",
        "cli",
        "data",
        "ingestion",
        "strawberry",
        "fastapi",
        "database",
        "api",
        "etl",
        "pandas",
    ],
    # PyPI classifiers
    classifiers=[
        # Development Status
        "Development Status :: 4 - Beta",
        # Intended Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Data Scientists",
        "Intended Audience :: System Administrators",
        # License
        "License :: OSI Approved :: MIT License",
        # Programming Language
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        # Topic
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        # Environment
        "Environment :: Console",
        "Environment :: Web Environment",
        # Operating System
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
    # Additional metadata
    zip_safe=False,
    platforms=["any"],
    # Minimum setuptools version
    setup_requires=["setuptools>=45", "wheel"],
)
