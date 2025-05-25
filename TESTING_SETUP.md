# Testing Setup Guide

This document explains the testing setup for GraphQL CSV Ingest and how to resolve common issues.

## 🐛 Issue Resolved: ModuleNotFoundError

### Problem
When running `pytest`, you encountered:
```
ModuleNotFoundError: No module named 'requests'
```

### Root Cause
The issue occurred because:
1. **Environment Management**: The system uses an externally managed Python environment
2. **Missing Virtual Environment**: Tests were running without proper dependency isolation
3. **Integration vs Unit Tests**: The original `test_examples.py` was an integration test requiring a running server

### ✅ Solution Applied

#### 1. **Created Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. **Installed Development Dependencies**
```bash
pip install -e ".[dev]"
```

#### 3. **Restructured Tests**
- **Renamed**: `tests/test_examples.py` → `tests/integration_test_examples.py`
  - This prevents pytest from automatically running integration tests
  - Integration tests can be run manually when needed
- **Created**: `tests/test_basic.py` - Proper unit tests for project validation

#### 4. **Fixed Pytest Configuration**
- Added `asyncio_default_fixture_loop_scope = "function"` to `pyproject.toml`
- Eliminated the pytest warning about asyncio configuration

## 🧪 Current Test Structure

```
tests/
├── test_basic.py                    # ✅ Unit tests (runs with pytest)
├── integration_test_examples.py     # 🔧 Integration tests (manual)
└── sample_data.csv                  # 📊 Test data
```

### Unit Tests (`test_basic.py`)
- **Dependency Validation**: Verifies all required packages can be imported
- **Project Structure**: Validates directory and file structure
- **Documentation**: Checks that all documentation files exist
- **Configuration**: Validates `pyproject.toml` and `requirements.txt`

### Integration Tests (`integration_test_examples.py`)
- **GraphQL API Testing**: Real API calls to running server
- **Manual Execution**: Run when server is available
- **Example Queries**: Demonstrates API usage patterns

## 🚀 Running Tests

### Unit Tests (Recommended)
```bash
# Activate virtual environment
source venv/bin/activate

# Run all unit tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=src
```

### Integration Tests (Manual)
```bash
# 1. Start the server first
csvgql serve

# 2. In another terminal, run integration tests
python tests/integration_test_examples.py
```

## 📦 Dependencies

### Production Dependencies
All listed in `pyproject.toml` under `[project]` dependencies:
- `click` - CLI framework
- `pandas` - Data processing
- `sqlalchemy` - Database ORM
- `strawberry-graphql` - GraphQL framework
- `fastapi` - Web framework
- `requests` - HTTP client
- And more...

### Development Dependencies
Listed under `[project.optional-dependencies]`:
- `pytest` - Testing framework
- `pytest-asyncio` - Async testing support
- `black` - Code formatting
- `flake8` - Linting
- `mypy` - Type checking

## 🔧 Best Practices

### Environment Setup
1. **Always use virtual environments** for Python projects
2. **Install with `[dev]` extras** for development work:
   ```bash
   pip install -e ".[dev]"
   ```

### Test Organization
1. **Unit Tests**: Fast, isolated, no external dependencies
2. **Integration Tests**: Slower, require running services
3. **Separate concerns**: Keep unit and integration tests separate

### Continuous Integration
The project includes `.github/workflows/ci.yml` for automated testing in CI/CD pipelines.

## 🎯 Test Results

After applying the fixes:
```
============================================ 12 passed in 6.48s ============================================
```

✅ **All 12 unit tests pass successfully**
✅ **No dependency errors**
✅ **No pytest warnings**
✅ **Clean test output**

## 📚 Next Steps

To extend the test suite:

1. **Add Application Tests**: Test actual CLI commands and functions
2. **Add Database Tests**: Test database operations with test databases
3. **Add GraphQL Tests**: Test GraphQL schema and resolvers
4. **Add Performance Tests**: Test with large CSV files

## 🛠️ Troubleshooting

### Common Issues

**Virtual Environment Not Activated**
```bash
source venv/bin/activate
```

**Dependencies Not Installed**
```bash
pip install -e ".[dev]"
```

**Integration Tests Failing**
```bash
# Make sure server is running first
csvgql serve
```

---

**The testing environment is now fully functional!** ✅ 