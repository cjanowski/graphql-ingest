# 🍓 GraphQL CSV Ingest

<div align="center">

```
  ____                 _      ____  _        ____ ______     __  ___                 _   
 / ___|_ __ __ _ _ __ | |__  / __ \| |      / ___/ ___\ \   / / |_ _|_ __   __ _  __| |_ 
| |  _| '__/ _` | '_ \| '_ \| |  | | |     | |   \___ \\ \ / /   | || '_ \ / _` |/ _` (_)
| |_| | | | (_| | |_) | | | | |__| | |___  | |___ ___) |\ V /    | || | | | (_| | (_| |_ 
 \____|_|  \__,_| .__/|_| |_|\___\_\_____|  \____|____/  \_/    |___|_| |_|\__, |\__,_(_)
                |_|                                                         |___/        
```

**Transform your CSV data into powerful GraphQL APIs in minutes!**

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[📖 Documentation](docs/) • [🚀 Quick Start](#-quick-start) • [💻 Examples](examples/) • [🤝 Contributing](CONTRIBUTE.md)

</div>

---

## ✨ Features

🔥 **Professional Data Pipeline in Your Terminal**

- 🍓 **Beautiful CLI**: Fun ASCII art and colorful interface
- 📊 **Smart CSV Ingestion**: Automatic schema detection and type inference
- 🐘 **PostgreSQL Integration**: Seamless database operations
- 🔍 **GraphQL API**: Modern, flexible data querying
- 🚀 **FastAPI Server**: High-performance async web server
- 🎯 **Multiple Entry Points**: Multiple CLI commands for convenience
- 🛠️ **Developer Friendly**: Type hints, comprehensive error handling
- 📦 **Easy Installation**: pip-installable with all dependencies

## 🚀 Quick Start

### Installation

```bash
# From source (recommended - package not yet on PyPI)
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e .

# For development with all dev dependencies
pip install -e ".[dev]"

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Quick Start - Method 1: Using Installed Commands (Recommended)

After running `pip install -e .`:

```bash
# 1️⃣ Show the main interface and available commands
csvgql

# 2️⃣ Initialize database connection
csvgql init-db

# 3️⃣ Ingest your CSV data
csvgql ingest -f data/sample_data.csv -t employees

# 4️⃣ Preview your data
csvgql preview -t employees

# 5️⃣ Start GraphQL server
csvgql serve

# 6️⃣ Query at http://localhost:8000/graphql
```

### Quick Start - Method 2: Using Wrapper Script

Use the convenient wrapper script (`csvgql.py`) if you prefer not to install:

```bash
# Navigate to project directory
cd graphql-ingest

# 1️⃣ Show the main interface and available commands
python csvgql.py

# 2️⃣ Initialize database connection
python csvgql.py init-db

# 3️⃣ Ingest your CSV data
python csvgql.py ingest -f data/sample_data.csv -t employees

# 4️⃣ Preview your data
python csvgql.py preview -t employees

# 5️⃣ Start GraphQL server
python csvgql.py serve

# 6️⃣ Query at http://localhost:8000/graphql
```

### Quick Start - Method 3: Direct Module Usage

For development, you can also run directly from source:

```bash
# Navigate to project directory
cd graphql-ingest

# Run CLI directly from source
python -m src.cli

# Or individual commands
python -m src.cli init-db
python -m src.cli ingest -f data/sample_data.csv -t employees
python -m src.cli serve
```

## 🎬 Demo

_Demo GIF coming soon - showing the beautiful CLI interface in action!_

## 📊 Example Workflow

```bash
# Using installed commands (after pip install -e .)
csvgql                                    # Show main interface
csvgql init-db                           # Initialize database
csvgql ingest -f data.csv -t users       # Ingest CSV data
csvgql preview -t users                  # Preview the data
csvgql serve                             # Start GraphQL server

# OR using wrapper script
python csvgql.py                         # Show main interface
python csvgql.py init-db                 # Initialize database
python csvgql.py ingest -f data.csv -t users  # Ingest CSV data
python csvgql.py preview -t users        # Preview the data
python csvgql.py serve                   # Start GraphQL server
```

## 🔧 CLI Commands

### Method 1: Using Installed Commands (Recommended)

After running `pip install -e .`:

```bash
csvgql                               # Show main interface
csvgql init-db                       # Initialize database
csvgql ingest -f data.csv -t table   # Ingest CSV
csvgql serve                         # Start GraphQL server
csvgql preview -t table              # Preview table data
csvgql tables                        # List tables
csvgql config-info                   # Show configuration
```

### Method 2: Using the Wrapper Script

If you prefer not to install the package:

```bash
# Navigate to project directory
cd graphql-ingest

# Use the wrapper script
python csvgql.py                    # Show main interface
python csvgql.py init-db            # Initialize database
python csvgql.py ingest -f data.csv -t table  # Ingest CSV
python csvgql.py serve              # Start GraphQL server
python csvgql.py preview -t table   # Preview table data
python csvgql.py tables             # List tables
python csvgql.py config-info        # Show configuration
```

### Method 3: Direct Module Execution (Development)

| Command | Description |
|---------|-------------|
| `python -m src.cli` | Main CLI interface |
| `python -m src.cli init-db` | Initialize database |
| `python -m src.cli ingest` | Ingest CSV files |
| `python -m src.cli serve` | Start GraphQL server |
| `python -m src.cli preview` | Preview table data |
| `python -m src.cli tables` | List available tables |
| `python -m src.cli config-info` | Show current configuration |

### All Available Commands Summary

| Method | Command | Description |
|--------|---------|-------------|
| **Installed** | `csvgql` | Main CLI interface (shows all commands) |
| **Installed** | `csvgql init-db` | Initialize database |
| **Installed** | `csvgql ingest` | Ingest CSV files |
| **Installed** | `csvgql serve` | Start GraphQL server |
| **Installed** | `csvgql preview` | Preview table data |
| **Installed** | `csvgql tables` | List available tables |
| **Installed** | `csvgql config-info` | Show current configuration |
| **Wrapper** | `python csvgql.py` | Main CLI interface |
| **Wrapper** | `python csvgql.py init-db` | Initialize database |
| **Direct** | `python -m src.cli` | Main CLI interface |
| **Direct** | `python -m src.cli init-db` | Initialize database |

## 🔍 GraphQL Queries

### List Tables
```graphql
{
  tables {
    name
    columns {
      name
      type
    }
  }
}
```

### Query Data
```graphql
{
  tableData(tableName: "employees", limit: 10) {
    data
    total
  }
}
```

### Ingest CSV via API
```graphql
mutation {
  ingestCsv(file: "new_data.csv", tableName: "products") {
    success
    message
    rowsInserted
  }
}
```

## 🛠️ Configuration

Create `.env` file in the project root:

```bash
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password

# Server Configuration  
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
DEBUG=false
```

You can also copy the example configuration:
```bash
cp config/env.example .env
```

## 📁 Project Structure

```
graphql-ingest/
├── 📦 src/                    # Main application code
│   ├── cli.py                 # Command-line interface
│   ├── config.py              # Configuration management
│   ├── database.py            # Database operations
│   ├── graphql_schema.py      # GraphQL schema definition
│   └── server.py              # FastAPI server
├── 🧪 tests/                  # Test suite
│   ├── test_basic.py          # Basic functionality tests
│   └── integration_test_examples.py
├── 📋 examples/               # Usage examples
├── 📚 docs/                   # Documentation
├── 🐳 docker/                 # Docker configuration
├── 📊 data/                   # Sample data files
│   ├── sample_data.csv        # Test data
│   └── test_data_large.csv    # Larger test dataset
├── ⚙️ config/                 # Configuration files
│   ├── env.example            # Environment template
│   ├── setup.cfg              # Setup configuration
│   └── MANIFEST.in            # Package manifest
├── 🛠️ tools/                  # Build and development tools
│   ├── setup.py               # Package setup script
│   └── coverage.xml           # Coverage reports
├── 🐙 .github/                # GitHub workflows
├── 📋 requirements/           # Dependency management
├── 📄 CONTRIBUTE.md           # Contribution guidelines
├── 📋 CHANGELOG.md            # Change log
├── 🚀 QUICKSTART.md           # Quick start guide
└── 📖 README.md               # Project overview
```

## 🧪 Testing

### Setup Testing Environment
```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install with development dependencies
pip install -e ".[dev]"
```

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_basic.py
```

## 🐳 Docker Support

```bash
# Build and run with Docker
docker-compose up

# Or use the Dockerfile directly
docker build -t csv-graphql-cli .
docker run -p 8000:8000 csv-graphql-cli
```

## 🚀 Installation Options

### Option 1: Install from Source (Recommended)
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e .
```

### Option 2: Development Setup
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e ".[dev]"
```

### Option 3: Using Virtual Environment (Recommended)
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

## 📋 Requirements

- Python 3.9 or higher
- PostgreSQL database
- Modern terminal with Unicode support

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTE.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Built with [Strawberry GraphQL](https://strawberry.rocks/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- CLI beauty by [Click](https://click.palletsprojects.com/)
- Data processing by [Pandas](https://pandas.pydata.org/)

---

*Made with ❤️ and lots of beautiful ASCII art! 🎨* 