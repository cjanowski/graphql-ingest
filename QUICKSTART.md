# 🍓 Quick Start Guide

This guide will help you get the **CSV to PostgreSQL GraphQL CLI** up and running quickly with beautiful ASCII art and colorful output!

## Prerequisites

- Python 3.9 or higher
- PostgreSQL database (local or remote)
- Basic familiarity with command line

## Setup

### 1. Install the Package

#### Option A: Install from Source (Recommended)
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e .
```

#### Option B: Development Setup (with all dependencies)
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e ".[dev]"
```

#### Option C: Using Virtual Environment (Recommended)
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### 2. Configure Database Connection

Copy the example environment file and configure your database:

```bash
cp config/env.example .env
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

#### Using Installed Commands (Recommended)
```bash
csvgql init-db
```

#### Alternative: Using Wrapper Script
```bash
python csvgql.py init-db
```

#### Alternative: Direct Module
```bash
python -m src.cli init-db
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

### Method 1: Using Installed Commands (Recommended)

After running `pip install -e .`:

#### 1. See the Beautiful Interface

```bash
csvgql
```

This shows the main banner and quick start guide with colorful styling!

#### 2. Ingest Sample Data

```bash
csvgql ingest --file data/sample_data.csv --table employees
```

#### 3. View Tables

```bash
csvgql tables
```

#### 4. Preview Data

```bash
csvgql preview --table employees --limit 5
```

#### 5. Start GraphQL Server

```bash
csvgql serve
```

### Method 2: Using Wrapper Script

#### 1. See the Beautiful Interface

```bash
python csvgql.py
```

This shows the main banner and quick start guide with colorful styling!

#### 2. Ingest Sample Data

```bash
python csvgql.py ingest --file data/sample_data.csv --table employees
```

#### 3. View Tables

```bash
python csvgql.py tables
```

#### 4. Preview Data

```bash
python csvgql.py preview --table employees --limit 5
```

#### 5. Start GraphQL Server

```bash
python csvgql.py serve
```

### Method 3: Development Commands (Direct Module)

#### 1. See the Beautiful Interface

```bash
python -m src.cli
```

#### 2. Ingest Sample Data

```bash
python -m src.cli ingest --file data/sample_data.csv --table employees
```

#### 3. View Tables

```bash
python -m src.cli tables
```

#### 4. Preview Data

```bash
python -m src.cli preview --table employees --limit 5
```

#### 5. Start GraphQL Server

```bash
python -m src.cli serve
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
- **📋 Quick Start Guide**: Interactive help when running main command

## 📁 Sample Data Location

Sample data files are now organized in the `data/` directory:

- `data/sample_data.csv` - Basic test data
- `data/test_data_large.csv` - Larger test dataset

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

## 🔧 Configuration Files

Configuration files are now organized in the `config/` directory:

- `config/env.example` - Environment template
- `config/setup.cfg` - Setup configuration
- `config/MANIFEST.in` - Package manifest

## Troubleshooting

### Database Connection Issues

1. **Connection refused**: Make sure PostgreSQL is running
2. **Authentication failed**: Check username/password in `.env`
3. **Database doesn't exist**: Create the database manually or use an existing one

### CLI Issues

1. **Command not found**: 
   - If using installed version: Make sure you installed with `pip install -e .`
   - If using development: Use `python -m src.cli` instead

2. **Module not found**: Make sure you're in the correct directory and dependencies are installed

### Server Issues

1. **Port already in use**: Use a different port: `csvgql-serve --port 8001`
2. **Module errors**: Make sure all dependencies are installed correctly

## 🎯 Command Quick Reference

### Installed Commands (after pip install -e .)
```bash
csvgql                       # Show main interface
csvgql init-db              # Initialize database
csvgql ingest               # Ingest CSV files
csvgql serve                # Start GraphQL server
csvgql preview              # Preview table data
csvgql tables               # List available tables
csvgql config-info          # Show current configuration
```

### Wrapper Script Commands
```bash
python csvgql.py             # Show main interface
python csvgql.py init-db     # Initialize database
python csvgql.py ingest      # Ingest CSV files
python csvgql.py serve       # Start GraphQL server
python csvgql.py preview     # Preview table data
python csvgql.py tables      # List available tables
python csvgql.py config-info # Show current configuration
```

### Direct Module Commands (Development)
```bash
python -m src.cli            # Main interface
python -m src.cli init-db    # Initialize database
python -m src.cli ingest     # Ingest CSV files
python -m src.cli serve      # Start GraphQL server
python -m src.cli preview    # Preview table data
python -m src.cli tables     # List available tables
python -m src.cli config-info # Show current configuration
```

## 🎯 Next Steps

- **🎨 Enjoy the beautiful interface** - Run `csvgql` to see the main banner
- **📊 Try ingesting your own CSV files** - Use different data sources
- **🔍 Explore the GraphQL API** with different queries in the playground
- **🚀 Build something awesome** with your CSV data
- **📖 Check out the full documentation** in `README.md`

---

*Made with ❤️ and lots of ASCII art! 🎨* 