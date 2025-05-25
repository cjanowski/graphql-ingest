#!/usr/bin/env python3
"""
Basic unit tests for GraphQL CSV Ingest

These tests verify that the core components can be imported and basic
functionality works.
"""

import pytest
import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_imports():
    """Test that core modules can be imported."""
    try:
        import click  # noqa: F401
        import pandas as pd  # noqa: F401
        import sqlalchemy  # noqa: F401
        import strawberry  # noqa: F401
        import fastapi  # noqa: F401
        import requests  # noqa: F401

        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import required modules: {e}")


def test_project_structure():
    """Test that the project has the expected structure."""
    project_root = Path(__file__).parent.parent

    # Check for essential files
    essential_files = [
        "README.md",
        "CONTRIBUTE.md",
        "CHANGELOG.md",
        "LICENSE",
        "pyproject.toml",
        "requirements.txt",
    ]

    for file_name in essential_files:
        file_path = project_root / file_name
        assert file_path.exists(), f"Missing essential file: {file_name}"


def test_project_directories():
    """Test that the project has the expected directory structure."""
    project_root = Path(__file__).parent.parent

    # Check for essential directories
    essential_dirs = ["src", "tests", "docs", "examples", ".github"]

    for dir_name in essential_dirs:
        dir_path = project_root / dir_name
        assert dir_path.exists(), f"Missing essential directory: {dir_name}"
        assert dir_path.is_dir(), f"{dir_name} is not a directory"


def test_github_templates():
    """Test that GitHub templates are present."""
    project_root = Path(__file__).parent.parent
    github_dir = project_root / ".github"

    # Check for GitHub templates
    templates = [
        "PULL_REQUEST_TEMPLATE.md",
        "ISSUE_TEMPLATE/bug_report.md",
        "ISSUE_TEMPLATE/feature_request.md",
    ]

    for template in templates:
        template_path = github_dir / template
        assert template_path.exists(), f"Missing GitHub template: {template}"


def test_documentation_structure():
    """Test that documentation structure is present."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"

    # Check for documentation files
    doc_files = ["README.md", "assets/logo.txt"]

    for doc_file in doc_files:
        doc_path = docs_dir / doc_file
        assert doc_path.exists(), f"Missing documentation file: {doc_file}"


@pytest.mark.parametrize(
    "file_name,expected_content",
    [
        ("README.md", "GraphQL CSV Ingest"),
        ("CONTRIBUTE.md", "Contributing to GraphQL CSV Ingest"),
        ("CHANGELOG.md", "Changelog"),
        ("LICENSE", "MIT"),
    ],
)
def test_file_contents(file_name, expected_content):
    """Test that key files contain expected content."""
    project_root = Path(__file__).parent.parent
    file_path = project_root / file_name

    assert file_path.exists(), f"File {file_name} does not exist"

    content = file_path.read_text(encoding="utf-8")
    assert (
        expected_content in content
    ), f"Expected content '{expected_content}' not found in {file_name}"


def test_sample_data():
    """Test that sample data file exists and is readable."""
    sample_file = Path(__file__).parent.parent / "data" / "sample_data.csv"
    assert sample_file.exists(), "Sample data file is missing"

    # Try to read with pandas
    try:
        import pandas as pd  # noqa: F401

        df = pd.read_csv(sample_file)
        assert len(df) > 0, "Sample data file is empty"
        assert len(df.columns) > 0, "Sample data file has no columns"
    except Exception as e:
        pytest.fail(f"Failed to read sample data file: {e}")


class TestProjectConfiguration:
    """Test class for project configuration validation."""

    def test_pyproject_toml_structure(self):
        """Test that pyproject.toml has the correct structure."""
        project_root = Path(__file__).parent.parent
        pyproject_file = project_root / "pyproject.toml"

        assert pyproject_file.exists(), "pyproject.toml is missing"

        content = pyproject_file.read_text(encoding="utf-8")

        # Check for essential sections
        essential_sections = [
            "[build-system]",
            "[project]",
            "[project.optional-dependencies]",
            "[tool.pytest.ini_options]",
        ]

        for section in essential_sections:
            assert section in content, f"Missing section in pyproject.toml: {section}"

    def test_requirements_file(self):
        """Test that requirements.txt has the expected dependencies."""
        project_root = Path(__file__).parent.parent
        requirements_file = project_root / "requirements.txt"

        assert requirements_file.exists(), "requirements.txt is missing"

        content = requirements_file.read_text(encoding="utf-8")

        # Check for essential dependencies
        essential_deps = [
            "click",
            "pandas",
            "sqlalchemy",
            "strawberry-graphql",
            "fastapi",
            "requests",
        ]

        for dep in essential_deps:
            assert dep in content, f"Missing dependency in requirements.txt: {dep}"


if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])
