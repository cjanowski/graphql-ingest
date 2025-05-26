from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from graphql_schema import schema
from config import Config  # type: ignore
import uvicorn
from typing import Optional, Dict, Any

# Create FastAPI app
app = FastAPI(
    title="CSV to PostgreSQL GraphQL API",
    description=(
        ("A GraphQL API for querying data ingested from CSV files " "into PostgreSQL")
    ),
    version="1.0.3",
)

# Create GraphQL router
graphql_app = GraphQLRouter(schema)

# Include GraphQL router
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root() -> Dict[str, Any]:
    """Root endpoint with API information."""
    return {
        "message": "CSV to PostgreSQL GraphQL API",
        "version": "1.0.3",
        "endpoints": {
            "graphql": "/graphql",
            "graphql_playground": "/graphql (GraphiQL interface)",
        },
        "status": "running",
    }


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


def start_server(
    host: Optional[str] = None,
    port: Optional[int] = None,
    reload: bool = False,
) -> None:
    """Start the FastAPI server with Uvicorn."""
    host = host or Config.SERVER_HOST
    port = port or Config.SERVER_PORT

    uvicorn.run("server:app", host=host, port=port, reload=reload, log_level="info")


def main() -> None:
    """Main entry point for direct server startup."""
    start_server(reload=True)


if __name__ == "__main__":
    main()
