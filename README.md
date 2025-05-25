# 🍓 GraphQL CSV Ingest

<div align="center">

**Transform your CSV data into powerful GraphQL APIs in minutes!**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[📖 Documentation](docs/) • [🚀 Quick Start](#-quick-start) • [💻 Examples](examples/) • [🤝 Contributing](CONTRIBUTE.md)

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
# From PyPI (when published)
pip install graphql-csv-ingest

# From source
git clone https://github.com/yourusername/graphql-csv-ingest.git
cd graphql-csv-ingest
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

_Demo GIF coming soon - showing the beautiful CLI interface in action!_

## 📊 Example Workflow

```bash
# Beautiful ASCII art welcome screen
csvgql

# Complete workflow example
csvgql init-db                    # Initialize database
csvgql ingest -f data.csv -t users # Ingest CSV data
csvgql preview -t users           # Preview the data
csvgql serve                      # Start GraphQL server
```

## 🔧 CLI Commands

| Command | Description |
|---------|-------------|
| `csvgql` | Main CLI with beautiful interface |
| `csvgql init-db` | Initialize database connection |
| `csvgql ingest` | Ingest CSV files into database |
| `csvgql serve` | Start GraphQL server |
| `csvgql preview` | Preview table data |
| `csvgql tables` | List available tables |

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
graphql-csv-ingest/
├── src/                    # 📦 Main application code
├── tests/                  # 🧪 Test suite
├── examples/               # 📋 Usage examples
├── docs/                   # 📚 Documentation
├── docker/                 # 🐳 Docker configuration
├── .github/                # 🐙 GitHub workflows
├── CONTRIBUTE.md           # 🤝 Contribution guidelines
├── CHANGELOG.md            # 📋 Change log
└── README.md               # 📖 Project overview
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
```

## 🐳 Docker Support

```bash
# Build and run with Docker
docker-compose up

# Or use the Dockerfile directly
docker build -t graphql-csv-ingest .
docker run -p 8000:8000 graphql-csv-ingest
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

## 🏆 Why GraphQL CSV Ingest?

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

**[⭐ Star this repo](#)** • **[🐛 Report Bug](../../issues)** • **[💡 Request Feature](../../issues)**

Made with 🍓 and ❤️ for the developer community

</div> 