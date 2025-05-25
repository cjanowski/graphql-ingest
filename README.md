# CSV to PostgreSQL GraphQL CLI

A Python CLI tool that ingests CSV files, loads data into PostgreSQL, and exposes a GraphQL API using Strawberry.

## Features

- 🔄 CSV file ingestion with automatic schema detection
- 🐘 PostgreSQL database integration with SQLAlchemy
- 🍓 GraphQL API powered by Strawberry
- 🖥️ Clean CLI interface with Click
- 🔧 Database migrations with Alembic
- ⚡ Fast API server with Uvicorn

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Initialize the database:
```bash
python cli.py init-db
```

## Usage

### Ingest CSV file
```bash
python cli.py ingest --file data.csv --table my_table
```

### Start GraphQL server
```bash
python cli.py serve --port 8000
```

### View GraphQL playground
Open http://localhost:8000/graphql in your browser

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `DB_HOST`: Database host (default: localhost)
- `DB_PORT`: Database port (default: 5432)
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password

## Example GraphQL Queries

```graphql
query {
  tables {
    name
    columns {
      name
      type
    }
  }
}

query {
  tableData(tableName: "my_table", limit: 10) {
    data
    total
  }
}
``` 