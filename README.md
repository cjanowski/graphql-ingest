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

[![PyPI version](https://img.shields.io/pypi/v/csv-graphql-cli.svg)](https://pypi.org/project/csv-graphql-cli/)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org/downloads/)
[![PyPI downloads](https://img.shields.io/pypi/dm/csv-graphql-cli.svg)](https://pypi.org/project/csv-graphql-cli/)
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
- 📦 **Easy Installation**: Available on PyPI with all dependencies

## 🚀 Quick Start

### Installation

```bash
# 🎉 Install from PyPI (Recommended)
pip install csv-graphql-cli

# 🔧 Or install in a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install csv-graphql-cli

# 🛠️ Development installation from source
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e ".[dev]"
```

### Quick Start - Method 1: Using Installed Commands (Recommended)

After running `pip install csv-graphql-cli`:

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

_Demo video coming soon - showing the CLI interface in action!_

<img width="603" alt="Screenshot 2025-05-26 at 7 56 13 AM" src="https://github.com/user-attachments/assets/40354b0b-a234-49f0-86b7-1e70c0cd855d" />
<img width="604" alt="Screenshot 2025-05-26 at 8 19 37 AM" src="https://github.com/user-attachments/assets/979fffdf-6180-4a22-bafb-822642a418e2" />
<img width="586" alt="Screenshot 2025-05-25 at 9 33 31 PM" src="https://github.com/user-attachments/assets/7d24e284-02b1-4797-96f2-b06fbd6b100d" />
<img width="586" alt="Screenshot 2025-05-25 at 9 33 41 PM" src="https://github.com/user-attachments/assets/61f7df72-867c-4970-858e-8f9acd0a6923" />
<img width="583" alt="Screenshot 2025-05-25 at 9 33 58 PM" src="https://github.com/user-attachments/assets/d47ced3c-0ec2-4aa1-8cdf-e97f10948372" />
<img width="563" alt="Screenshot 2025-05-25 at 9 34 21 PM" src="https://github.com/user-attachments/assets/ac607c4b-c6d1-46dc-bb54-aa2c4abcdbcb" />
<img width="582" alt="Screenshot 2025-05-25 at 9 34 44 PM" src="https://github.com/user-attachments/assets/5ffdce9a-9901-4c74-a557-d0ed887216b7" />


## 📊 Example Workflow

```bash
# Using installed package (after pip install csv-graphql-cli)
csvgql                                    # Show main interface
csvgql init-db                           # Initialize database
csvgql ingest -f data.csv -t users       # Ingest CSV data
csvgql preview -t users                  # Preview the data
csvgql serve                             # Start GraphQL server

# OR using wrapper script (development)
python csvgql.py                         # Show main interface
python csvgql.py init-db                 # Initialize database
python csvgql.py ingest -f data.csv -t users  # Ingest CSV data
python csvgql.py preview -t users        # Preview the data
python csvgql.py serve                   # Start GraphQL server
```

## 🔧 CLI Commands

### Method 1: Using Installed Package (Recommended)

After running `pip install csv-graphql-cli`:

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
| **PyPI Package** | `csvgql` | Main CLI interface (shows all commands) |
| **PyPI Package** | `csvgql init-db` | Initialize database |
| **PyPI Package** | `csvgql ingest` | Ingest CSV files |
| **PyPI Package** | `csvgql serve` | Start GraphQL server |
| **PyPI Package** | `csvgql preview` | Preview table data |
| **PyPI Package** | `csvgql tables` | List available tables |
| **PyPI Package** | `csvgql config-info` | Show current configuration |
| **Development** | `python csvgql.py` | Main CLI interface |
| **Development** | `python csvgql.py init-db` | Initialize database |
| **Development** | `python -m src.cli` | Main CLI interface |
| **Development** | `python -m src.cli init-db` | Initialize database |

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

### Option 1: Install from PyPI (Recommended) 🎉
```bash
pip install csv-graphql-cli
```

### Option 2: Install in Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install csv-graphql-cli
```

### Option 3: Development Setup
```bash
git clone https://github.com/cjanowski/graphql-ingest.git
cd graphql-ingest
pip install -e ".[dev]"
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

*Made with ❤️ and lots of 🍓🍓🍓!* 
