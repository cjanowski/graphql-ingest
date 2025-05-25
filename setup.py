from setuptools import setup, find_packages

setup(
    name="csv-graphql-cli",
    version="1.0.0",
    description="A CLI tool for ingesting CSV files into PostgreSQL and serving data via GraphQL",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    py_modules=["cli", "config", "database", "graphql_schema", "server"],
    install_requires=[
        "click==8.1.7",
        "pandas==2.1.4",
        "sqlalchemy==2.0.23",
        "psycopg2-binary==2.9.9",
        "strawberry-graphql==0.216.1",
        "uvicorn==0.24.0",
        "fastapi==0.104.1",
        "python-dotenv==1.0.0",
        "alembic==1.13.1",
        "requests==2.31.0"
    ],
    entry_points={
        "console_scripts": [
            "csv-graphql=cli:cli",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 