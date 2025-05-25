#!/usr/bin/env python3
"""
Test examples for the CSV GraphQL CLI

This script demonstrates various GraphQL queries you can run against the API.
"""

import requests
import json

# GraphQL endpoint
GRAPHQL_URL = "http://localhost:8000/graphql"


def run_query(query, variables=None):
    """Run a GraphQL query against the API."""
    payload = {"query": query, "variables": variables or {}}

    try:
        response = requests.post(GRAPHQL_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def test_get_tables():
    """Test getting all tables."""
    query = """
    query {
        tables {
            name
            columns {
                name
                type
                nullable
            }
        }
    }
    """

    print("🔍 Getting all tables...")
    result = run_query(query)
    if result:
        print(json.dumps(result, indent=2))
    print("-" * 50)


def test_get_table_data(table_name="employees"):
    """Test getting data from a specific table."""
    query = """
    query GetTableData($tableName: String!, $limit: Int, $offset: Int) {
        tableData(tableName: $tableName, limit: $limit, offset: $offset) {
            success
            data
            total
            limit
            offset
            error
        }
    }
    """

    variables = {"tableName": table_name, "limit": 5, "offset": 0}

    print(f"📊 Getting data from table: {table_name}")
    result = run_query(query, variables)
    if result:
        print(json.dumps(result, indent=2))
    print("-" * 50)


def test_get_table_schema(table_name="employees"):
    """Test getting schema for a specific table."""
    query = """
    query GetTableSchema($tableName: String!) {
        tableSchema(tableName: $tableName) {
            name
            columns {
                name
                type
                nullable
            }
        }
    }
    """

    variables = {"tableName": table_name}

    print(f"🏗️  Getting schema for table: {table_name}")
    result = run_query(query, variables)
    if result:
        print(json.dumps(result, indent=2))
    print("-" * 50)


def test_ingest_csv():
    """Test CSV ingestion via GraphQL mutation."""
    mutation = """
    mutation IngestCSV($filePath: String!, $tableName: String!) {
        ingestCsv(filePath: $filePath, tableName: $tableName) {
            success
            tableName
            rowsInserted
            columns
            error
        }
    }
    """

    variables = {"filePath": "sample_data.csv", "tableName": "employees"}

    print("📥 Testing CSV ingestion...")
    result = run_query(mutation, variables)
    if result:
        print(json.dumps(result, indent=2))
    print("-" * 50)


if __name__ == "__main__":
    print("🧪 Testing GraphQL API")
    print("Make sure the server is running: python cli.py serve")
    print("=" * 50)

    # Run tests
    test_get_tables()
    test_get_table_data()
    test_get_table_schema()
    # test_ingest_csv()  # Uncomment to test CSV ingestion via GraphQL
