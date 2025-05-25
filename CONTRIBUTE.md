# Contributing to GraphQL CSV Ingest

Thank you for your interest in contributing to GraphQL CSV Ingest! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Git
- Virtual environment tool (venv, virtualenv, conda, etc.)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/graphql-csv-ingest.git
   cd graphql-csv-ingest
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Set Up Environment**
   ```bash
   cp env.example .env
   # Edit .env with your database credentials
   ```

5. **Run Tests**
   ```bash
   pytest
   ```

## 🛠️ Development Workflow

### Branch Strategy

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/xyz` - Feature branches
- `bugfix/xyz` - Bug fix branches
- `hotfix/xyz` - Critical fixes

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write Code**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run Quality Checks**
   ```bash
   # Run tests
   pytest

   # Check code formatting
   black --check .
   isort --check-only .

   # Run linting
   flake8 .

   # Type checking
   mypy src/
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(cli): add support for JSON output format
fix(database): resolve connection timeout issues
docs: update API documentation
test(core): add unit tests for CSV parser
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_csv_parser.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Mirror the source code structure
- Use descriptive test names
- Include both unit and integration tests
- Test edge cases and error conditions

**Example:**
```python
def test_csv_parser_handles_empty_file():
    """Test that CSV parser gracefully handles empty files."""
    # Test implementation
```

## 📝 Documentation

### Code Documentation

- Use docstrings for all public functions and classes
- Follow [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) docstrings
- Include type hints
- Document complex algorithms and business logic

### User Documentation

- Update README.md for user-facing changes
- Add examples in `examples/` directory
- Update QUICKSTART.md for setup changes
- Add API documentation for new endpoints

## 🎨 Code Style

We use the following tools to maintain code quality:

### Formatting
- **Black** for code formatting
- **isort** for import sorting

### Linting
- **flake8** for style guide enforcement
- **mypy** for static type checking

### Configuration

All tools are configured in `pyproject.toml`. Run formatting before committing:

```bash
# Format code
black .
isort .

# Check everything
pre-commit run --all-files
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment Information**
   - Python version
   - Operating system
   - Package versions (`pip freeze`)

2. **Reproduction Steps**
   - Minimal code example
   - Expected vs actual behavior
   - Error messages and stack traces

3. **Context**
   - Use case description
   - Data samples (anonymized)

## 💡 Feature Requests

For new features:

1. **Check Existing Issues** - Avoid duplicates
2. **Describe the Problem** - What are you trying to solve?
3. **Propose a Solution** - How should it work?
4. **Consider Alternatives** - What other approaches exist?
5. **Implementation Details** - Technical considerations

## 📋 Pull Request Process

1. **Pre-submission Checklist**
   - [ ] Tests pass locally
   - [ ] Code is formatted and linted
   - [ ] Documentation is updated
   - [ ] CHANGELOG.md is updated (if applicable)
   - [ ] Branch is up to date with main

2. **PR Description**
   - Clear title and description
   - Link to related issues
   - Screenshots for UI changes
   - Breaking changes highlighted

3. **Review Process**
   - All PRs require at least one review
   - Address feedback promptly
   - Keep discussions focused and constructive
   - Maintainers may request changes

## 🏗️ Project Structure

```
graphql-csv-ingest/
├── src/
│   └── graphql_csv_ingest/     # Main package
├── tests/                      # Test files
├── docs/                       # Documentation
├── examples/                   # Usage examples
├── scripts/                    # Utility scripts
├── docker/                     # Docker configurations
├── .github/                    # GitHub templates and workflows
├── requirements/               # Dependency files
└── README.md                   # Project overview
```

## 🤝 Community Guidelines

- **Be Respectful** - Treat everyone with respect
- **Be Constructive** - Provide helpful feedback
- **Be Patient** - Reviews and responses take time
- **Be Collaborative** - Work together towards solutions

## 📞 Getting Help

- **GitHub Issues** - Bug reports and feature requests
- **Discussions** - Questions and general discussion
- **Email** - For security issues: security@example.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to GraphQL CSV Ingest!** 🎉 