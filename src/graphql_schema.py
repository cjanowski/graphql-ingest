import strawberry
from typing import List, Optional
from database import db_manager
import json


@strawberry.type
class ColumnInfo:
    """GraphQL type for database column information."""

    name: str
    type: str
    nullable: bool


@strawberry.type
class TableInfo:
    """GraphQL type for database table information."""

    name: str
    columns: List[ColumnInfo]


@strawberry.type
class TableDataResponse:
    """GraphQL type for table data response."""

    success: bool
    data: Optional[str] = None  # JSON string of the data
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    error: Optional[str] = None


@strawberry.type
class IngestionResult:
    """GraphQL type for CSV ingestion result."""

    success: bool
    table_name: Optional[str] = None
    rows_inserted: Optional[int] = None
    columns: Optional[List[str]] = None
    error: Optional[str] = None


@strawberry.type
class Query:
    """GraphQL Query root type."""

    @strawberry.field
    def tables(self) -> List[TableInfo]:
        """Get all database tables with their schema information."""
        tables_data = db_manager.get_tables()

        tables = []
        for table_data in tables_data:
            columns = [
                ColumnInfo(
                    name=col["name"],
                    type=col["type"],
                    nullable=col["nullable"],
                )
                for col in table_data["columns"]
            ]

            tables.append(TableInfo(name=table_data["name"], columns=columns))

        return tables

    @strawberry.field
    def table_data(
        self,
        table_name: str,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
    ) -> TableDataResponse:
        """Get data from a specific table."""
        result = db_manager.get_table_data(table_name, limit or 100, offset or 0)

        if result["success"]:
            return TableDataResponse(
                success=True,
                data=json.dumps(result["data"], default=str),
                total=result["total"],
                limit=result["limit"],
                offset=result["offset"],
            )
        else:
            return TableDataResponse(success=False, error=result["error"])

    @strawberry.field
    def table_schema(self, table_name: str) -> Optional[TableInfo]:
        """Get schema information for a specific table."""
        tables_data = db_manager.get_tables()

        for table_data in tables_data:
            if table_data["name"] == table_name:
                columns = [
                    ColumnInfo(
                        name=col["name"],
                        type=col["type"],
                        nullable=col["nullable"],
                    )
                    for col in table_data["columns"]
                ]
                return TableInfo(name=table_data["name"], columns=columns)
        return None


@strawberry.type
class Mutation:
    """GraphQL Mutation root type."""

    @strawberry.field
    def ingest_csv(self, file_path: str, table_name: str) -> IngestionResult:
        """Ingest a CSV file into the database."""
        result = db_manager.ingest_csv(file_path, table_name)

        if result["success"]:
            return IngestionResult(
                success=True,
                table_name=result["table_name"],
                rows_inserted=result["rows_inserted"],
                columns=result["columns"],
            )
        else:
            return IngestionResult(success=False, error=result["error"])


# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
