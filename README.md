# 🍓 CSV GraphQL CLI

<div align="center">

![CSV GraphQL CLI Logo](docs/assets/logo-banner.png)

**Transform your CSV data into powerful GraphQL APIs in minutes!**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/csv-graphql-cli.svg)](https://badge.fury.io/py/csv-graphql-cli)
[![GitHub issues](https://img.shields.io/github/issues/coryjanowski/csv-graphql-cli.svg)](https://github.com/coryjanowski/csv-graphql-cli/issues)
[![GitHub stars](https://img.shields.io/github/stars/coryjanowski/csv-graphql-cli.svg)](https://github.com/coryjanowski/csv-graphql-cli/stargazers)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[📖 Documentation](docs/) • [🚀 Quick Start](#-quick-start) • [💻 Examples](examples/) • [🤝 Contributing](CONTRIBUTING.md)

</div>

---

## ✨ Features

🔥 **Professional Data Pipeline in Your Terminal**

- 🍓 **Beautiful CLI**: Stunning ASCII art and colorful interface
- 📊 **Smart CSV Ingestion**: Automatic schema detection and type inference
- 🐘 **PostgreSQL Integration**: Seamless database operations
- 🔍 **GraphQL API**: Modern, flexible data querying
- 🚀 **FastAPI Server**: High-performance async web server
- 🎯 **Multiple Entry Points**: 7 different CLI commands for convenience
- 🛠️ **Developer Friendly**: Type hints, comprehensive error handling
- 📦 **Easy Installation**: pip-installable with all dependencies

## 🚀 Quick Start

### Installation

```bash
# From PyPI (recommended)
pip install csv-graphql-cli

# From source
git clone https://github.com/coryjanowski/csv-graphql-cli.git
cd csv-graphql-cli
pip install -e .
```

### Basic Usage

```bash
# 1️⃣ Initialize database connection
csvgql init-db

# 2️⃣ Ingest your CSV data
csvgql ingest -f employees.csv -t employees

# 3️⃣ Preview your data
csvgql preview -t employees

# 4️⃣ Start GraphQL server
csvgql serve

# 5️⃣ Query at http://localhost:8000/graphql
```

## 🎬 Demo

![CLI Demo](docs/assets/demo.gif)

## 📊 Example Workflow

```bash
# Beautiful ASCII art welcome screen
csvgql

# Multiple command aliases available
csv-graphql init-db     # Full command
csvgql init-db          # Short alias  
csv-ingest -f data.csv  # Direct command
csvgql-dev              # Development server
```

## 🔧 CLI Commands

| Command | Alias | Description |
|---------|-------|-------------|
| `csvgql` | `csv-graphql` | Main CLI with beautiful interface |
| `csv-ingest` | - | Direct CSV ingestion |
| `csv-serve` | - | Direct server startup |
| `csv-preview` | - | Direct data preview |
| `csv-tables` | - | Direct table listing |
| `csvgql-dev` | - | Development server with auto-reload |

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

Create `.env` file:

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

## 📁 Project Structure

```
csv-graphql-cli/
├── src/                    # 📦 Main application code
├── tests/                  # 🧪 Test suite
├── examples/               # 📋 Usage examples
├── docs/                   # 📚 Documentation
├── docker/                 # 🐳 Docker configuration
└── .github/               # 🐙 GitHub workflows
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_cli.py
```

## 🐳 Docker Support

```bash
# Build and run with Docker
docker-compose up

# Or use the Dockerfile directly
docker build -t csv-graphql-cli .
docker run -p 8000:8000 csv-graphql-cli
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTE.md](CONTRIBUTE.md) for guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📋 Requirements

- **Python**: 3.8 or higher
- **PostgreSQL**: 12 or higher  
- **Dependencies**: See [requirements.txt](requirements.txt)

## 🏆 Why CSV GraphQL CLI?

✅ **Professional Grade**: Enterprise-ready with comprehensive error handling  
✅ **Beautiful UX**: Stunning CLI interface that developers love  
✅ **Modern Stack**: FastAPI, Strawberry GraphQL, SQLAlchemy 2.0  
✅ **Type Safe**: Full type hints and validation  
✅ **Well Tested**: Comprehensive test suite  
✅ **Great DX**: Multiple installation methods and CLI aliases  
✅ **Production Ready**: Docker support and CI/CD workflows  

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using [FastAPI](https://fastapi.tiangolo.com/), [Strawberry GraphQL](https://strawberry.rocks/), and [Click](https://click.palletsprojects.com/)
- Inspired by the need for rapid CSV-to-API prototyping

---

<div align="center">

**[⭐ Star this repo](https://github.com/coryjanowski/csv-graphql-cli/stargazers)** • **[🐛 Report Bug](https://github.com/coryjanowski/csv-graphql-cli/issues)** • **[💡 Request Feature](https://github.com/coryjanowski/csv-graphql-cli/issues)**

Made with 🍓 by [Cory Janowski](https://github.com/coryjanowski)

</div> 