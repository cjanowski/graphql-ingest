from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from graphql_schema import schema
from config import Config
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="CSV to PostgreSQL GraphQL API",
    description="A GraphQL API for querying data ingested from CSV files into PostgreSQL",
    version="1.0.0"
)

# Create GraphQL router
graphql_app = GraphQLRouter(schema)

# Include GraphQL router
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "CSV to PostgreSQL GraphQL API",
        "version": "1.0.0",
        "endpoints": {
            "graphql": "/graphql",
            "graphql_playground": "/graphql (GraphiQL interface)"
        },
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

def start_server(host: str = None, port: int = None, reload: bool = False):
    """Start the FastAPI server with Uvicorn."""
    host = host or Config.SERVER_HOST
    port = port or Config.SERVER_PORT
    
    uvicorn.run(
        "server:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

if __name__ == "__main__":
    start_server(reload=True) 