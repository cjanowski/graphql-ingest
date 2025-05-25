from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    inspect,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from typing import Dict, List, Any
import logging
from config import Config  # type: ignore

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
engine = create_engine(Config.DATABASE_URL, echo=Config.DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()


class DatabaseManager:
    """Manages database operations including table creation and data
    ingestion."""

    def __init__(self) -> None:
        self.engine = engine
        self.metadata = metadata

    def create_database_if_not_exists(self) -> bool:
        """Create database if it doesn't exist."""
        try:
            # Test connection
            with self.engine.connect():
                logger.info("Database connection successful")
                return True
        except SQLAlchemyError as e:
            logger.error(f"Database connection failed: {e}")
            return False

    def infer_column_type(self, series: pd.Series) -> Any:
        """Infer SQLAlchemy column type from pandas Series."""
        if pd.api.types.is_integer_dtype(series):
            return Integer
        elif pd.api.types.is_float_dtype(series):
            return Float
        elif pd.api.types.is_datetime64_any_dtype(series):
            return DateTime
        else:
            # For strings, use Text for longer content, String for shorter
            max_length = series.astype(str).str.len().max() if not series.empty else 0
            return Text if max_length > 255 else String(255)

    def create_table_from_dataframe(self, df: pd.DataFrame, table_name: str) -> Table:
        """Create a SQLAlchemy table based on DataFrame structure."""
        columns = []

        # Check if DataFrame already has an 'id' column
        has_id_column = "id" in df.columns

        if not has_id_column:
            # Add auto-incrementing id column if CSV doesn't have one
            id_col = Column("id", Integer, primary_key=True, autoincrement=True)
            columns.append(id_col)

        for col_name in df.columns:
            col_type = self.infer_column_type(df[col_name])
            # If this is an existing 'id' column, make it the primary key
            if col_name == "id" and has_id_column:
                pk_col: Column = Column(col_name, col_type, primary_key=True)
                columns.append(pk_col)
            else:
                columns.append(Column(col_name, col_type))

        table = Table(table_name, self.metadata, *columns, extend_existing=True)
        return table

    def ingest_csv(self, file_path: str, table_name: str) -> Dict[str, Any]:
        """Ingest CSV file into PostgreSQL table."""
        try:
            # Read CSV file
            logger.info(f"Reading CSV file: {file_path}")
            df = pd.read_csv(file_path)

            if df.empty:
                raise ValueError("CSV file is empty")

            # Create table schema
            logger.info(f"Creating table: {table_name}")
            table = self.create_table_from_dataframe(df, table_name)

            # Create table in database
            table.create(self.engine, checkfirst=True)

            # Insert data
            logger.info(f"Inserting {len(df)} rows into {table_name}")
            df.to_sql(
                table_name,
                self.engine,
                if_exists="append",
                index=False,
                method="multi",
            )

            return {
                "success": True,
                "table_name": table_name,
                "rows_inserted": len(df),
                "columns": list(df.columns),
            }

        except Exception as e:
            logger.error(f"Error ingesting CSV: {e}")
            return {"success": False, "error": str(e)}

    def get_tables(self) -> List[Dict[str, Any]]:
        """Get list of all tables with their schema information."""
        try:
            inspector = inspect(self.engine)
            tables = []

            for table_name in inspector.get_table_names():
                columns = []
                for column in inspector.get_columns(table_name):
                    columns.append(
                        {
                            "name": column["name"],
                            "type": str(column["type"]),
                            "nullable": column["nullable"],
                        }
                    )

                tables.append({"name": table_name, "columns": columns})

            return tables

        except Exception as e:
            logger.error(f"Error getting tables: {e}")
            return []

    def get_table_data(
        self, table_name: str, limit: int = 100, offset: int = 0
    ) -> Dict[str, Any]:
        """Get data from a specific table."""
        try:
            with self.engine.connect() as conn:
                # Get total count
                count_query = f"SELECT COUNT(*) FROM {table_name}"
                total = conn.execute(text(count_query)).scalar()

                # Get data
                data_query = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
                result = conn.execute(text(data_query))

                # Convert to list of dictionaries
                columns = result.keys()
                data = [dict(zip(columns, row)) for row in result.fetchall()]

                return {
                    "success": True,
                    "data": data,
                    "total": total,
                    "limit": limit,
                    "offset": offset,
                }

        except Exception as e:
            logger.error(f"Error getting table data: {e}")
            return {"success": False, "error": str(e)}


# Create global database manager instance
db_manager = DatabaseManager()
