"""
CSV to PostgreSQL GraphQL CLI

A beautiful command-line tool for ingesting CSV files into PostgreSQL
and serving the data via GraphQL API.
"""

__version__ = "1.0.0"
__author__ = "Cory Janowski"
__email__ = "cory@example.com"
__description__ = (
    "🍓 A beautiful CLI tool for ingesting CSV files into PostgreSQL "
    "and serving data via GraphQL"
)

# Import main components for easy access
from .cli import cli
from .config import Config
from .database import db_manager
from .server import start_server

__all__ = ["cli", "Config", "db_manager", "start_server"]
