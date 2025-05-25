# 🍓 Quick Start Guide

This guide will help you get the **CSV to PostgreSQL GraphQL CLI** up and running quickly with beautiful ASCII art and colorful output!

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database (local or remote)
- Basic familiarity with command line

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Database Connection

Copy the example environment file and configure your database:

```bash
cp env.example .env
```

Edit `.env` with your database credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=csv_graphql_db
DB_USER=postgres
DB_PASSWORD=your_password
```

### 3. Test Database Connection

```bash
python3 cli.py init-db
```

You should see a beautiful ASCII art banner followed by:
```
╔═══════════════════════════════════════════════════════════════════════════════╗
║           🍓 CSV to PostgreSQL GraphQL CLI Tool v1.0.0 🍓                   ║
║           📊 Ingest → 🐘 Store → 🔍 Query → 🚀 Serve                        ║
╚═══════════════════════════════════════════════════════════════════════════════╝

ℹ️  Testing database connection...
✅ Database connection successful!
📍 Connected to: postgresql://postgres:***@localhost:5432/csv_graphql_db
🎉 Ready to ingest CSV files and serve GraphQL!
```

## 🚀 Basic Usage

### 1. See the Beautiful Interface

```bash
python3 cli.py
```

This shows the main banner and quick start guide with colorful styling!

### 2. Ingest Sample Data

```bash
python3 cli.py ingest --file sample_data.csv --table employees
```

You'll see a beautiful progress display with success celebration box!

### 3. View Tables

```bash
python3 cli.py tables
```

### 4. Preview Data

```bash
python3 cli.py preview --table employees --limit 5
```

### 5. Start GraphQL Server

```bash
python3 cli.py serve
```

You'll see a beautiful server ready box with all endpoints and example queries!
The server will start at http://localhost:8000

### 6. Access GraphQL Playground

Open your browser and go to: http://localhost:8000/graphql

## ✨ New Visual Features

- **🎨 ASCII Art Banner**: Beautiful "CSV GRAPH" logo with box drawing
- **🌈 Colorful Output**: Success (green), errors (red), warnings (yellow), info (blue)
- **📦 Information Boxes**: Styled borders and organized information display
- **🎯 Progress Bars**: Visual feedback during CSV processing
- **🎉 Success Celebrations**: Beautiful completion messages with emojis
- **📋 Quick Start Guide**: Interactive help when running `python3 cli.py`

## Sample GraphQL Queries

### Get all tables:
```graphql
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
```

### Get table data:
```graphql
query {
  tableData(tableName: "employees", limit: 5) {
    success
    data
    total
  }
}
```

### Get table schema:
```graphql
query {
  tableSchema(tableName: "employees") {
    name
    columns {
      name
      type
    }
  }
}
```

## Troubleshooting

### Database Connection Issues

1. **Connection refused**: Make sure PostgreSQL is running
2. **Authentication failed**: Check username/password in `.env`
3. **Database doesn't exist**: Create the database manually or use an existing one

### CLI Issues

1. **Permission denied**: Make sure the CLI script is executable: `chmod +x cli.py`
2. **Module not found**: Make sure you're in the correct directory and dependencies are installed

### Server Issues

1. **Port already in use**: Use a different port: `python3 cli.py serve --port 8001`
2. **Module errors**: Make sure all dependencies are installed correctly

## 🎯 Next Steps

- **🎨 Enjoy the beautiful interface** - Run `python3 cli.py` to see the main banner
- **📊 Try ingesting your own CSV files** - Use different data sources
- **🔍 Explore the GraphQL API** with different queries in the playground
- **🚀 Build something awesome** with your CSV data
- **📖 Check out the full documentation** in `README.md`

---

*Made with ❤️ and lots of ASCII art! 🎨* 