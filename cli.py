#!/usr/bin/env python3

"""
CSV to PostgreSQL GraphQL CLI

A command-line tool for ingesting CSV files into PostgreSQL 
and serving the data via GraphQL API.
"""

import click
import os
import sys
from pathlib import Path
from database import db_manager
from server import start_server
from config import Config
import logging
from sqlalchemy import text

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ASCII Art Banner
BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ██████╗███████╗██╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗██████║
║  ██╔════╝██╔════╝██║   ██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔═══║
║  ██║     ███████╗██║   ██║    ██║  ███╗██████╔╝███████║██████╔╝███████║██████║
║  ██║     ╚════██║╚██╗ ██╔╝    ██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║██╔═══║
║  ╚██████╗███████║ ╚████╔╝     ╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║██████║
║   ╚═════╝╚══════╝  ╚═══╝       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════║
║                                                                               ║
║           🍓 CSV to PostgreSQL GraphQL CLI Tool v1.0.0 🍓                   ║
║           📊 Ingest → 🐘 Store → 🔍 Query → 🚀 Serve                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

DIVIDER = "═" * 80

def print_banner():
    """Print the CLI banner."""
    click.echo(click.style(BANNER, fg='cyan', bold=True))

def print_divider():
    """Print a visual divider."""
    click.echo(click.style(DIVIDER, fg='blue'))

def print_success(message):
    """Print a success message with style."""
    click.echo(click.style(f"✅ {message}", fg='green', bold=True))

def print_error(message):
    """Print an error message with style."""
    click.echo(click.style(f"❌ {message}", fg='red', bold=True))

def print_warning(message):
    """Print a warning message with style."""
    click.echo(click.style(f"⚠️  {message}", fg='yellow', bold=True))

def print_info(message):
    """Print an info message with style."""
    click.echo(click.style(f"ℹ️  {message}", fg='blue'))

@click.group()
@click.version_option(version="1.0.0", prog_name="CSV GraphQL CLI")
@click.pass_context
def cli(ctx):
    """CSV to PostgreSQL GraphQL CLI
    
    A powerful tool for ingesting CSV files into PostgreSQL and serving data via GraphQL.
    """
    if ctx.invoked_subcommand is None:
        print_banner()
        print_divider()
        
        help_text = """
╔════════════════════════════════════════════════════════════════════╗
║                           🚀 QUICK START 🚀                       ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  1️⃣  Initialize:    python3 cli.py init-db                       ║
║  2️⃣  Ingest CSV:    python3 cli.py ingest -f data.csv -t table   ║
║  3️⃣  Preview:       python3 cli.py preview -t table              ║
║  4️⃣  Start server:  python3 cli.py serve                         ║
║  5️⃣  Query data:    Visit http://localhost:8000/graphql          ║
║                                                                    ║
║  📖 Full help:      python3 cli.py --help                        ║
║  📖 Command help:   python3 cli.py COMMAND --help                ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

Available Commands:
"""
        click.echo(click.style(help_text, fg='cyan'))
        
        commands = [
            ("🔧 init-db", "Test database connection"),
            ("📥 ingest", "Import CSV file to PostgreSQL"),
            ("🔍 preview", "Preview table data"),
            ("📋 tables", "List all database tables"),
            ("🚀 serve", "Start GraphQL API server"),
            ("⚙️  config-info", "Show current configuration")
        ]
        
        for cmd, desc in commands:
            click.echo(f"  {click.style(cmd, fg='green', bold=True):<20} {desc}")
        
        print_divider()
    pass

@cli.command()
def init_db():
    """Initialize database connection and test connectivity."""
    print_banner()
    print_divider()
    print_info("Testing database connection...")
    
    if db_manager.create_database_if_not_exists():
        print_success("Database connection successful!")
        click.echo(f"📍 Connected to: {click.style(Config.DATABASE_URL, fg='green')}")
        print_divider()
        click.echo(click.style("🎉 Ready to ingest CSV files and serve GraphQL!", fg='magenta', bold=True))
    else:
        print_error("Database connection failed!")
        click.echo("Please check your database configuration in the .env file")
        sys.exit(1)

@cli.command()
@click.option('--file', '-f', required=True, type=click.Path(exists=True), 
              help='Path to the CSV file to ingest')
@click.option('--table', '-t', required=True, 
              help='Name of the table to create/insert into')
@click.option('--replace', is_flag=True, 
              help='Replace table if it already exists')
def ingest(file, table, replace):
    """Ingest a CSV file into PostgreSQL."""
    file_path = Path(file).resolve()
    
    print_banner()
    print_divider()
    
    click.echo(click.style("📊 CSV INGESTION STARTED", fg='cyan', bold=True))
    print_divider()
    
    click.echo(f"📁 File: {click.style(str(file_path), fg='yellow')}")
    click.echo(f"🎯 Target table: {click.style(table, fg='green', bold=True)}")
    
    # Test database connection first
    if not db_manager.create_database_if_not_exists():
        print_error("Database connection failed!")
        sys.exit(1)
    
    # Check if table exists and handle replace option
    existing_tables = [t["name"] for t in db_manager.get_tables()]
    if table in existing_tables:
        if replace:
            print_warning(f"Table '{table}' exists and will be replaced")
            # Drop and recreate table
            with db_manager.engine.connect() as conn:
                conn.execute(text(f"DROP TABLE IF EXISTS {table}"))
                conn.commit()
        else:
            print_warning(f"Table '{table}' already exists. Data will be appended.")
            print_info("Use --replace flag to replace the table instead.")
    
    print_divider()
    
    # Perform ingestion
    with click.progressbar(length=1, label=click.style('Processing CSV', fg='cyan')) as bar:
        result = db_manager.ingest_csv(str(file_path), table)
        bar.update(1)
    
    print_divider()
    
    if result["success"]:
        success_box = f"""
╔══════════════════════════════════════════════════════════════╗
║                    🎉 INGESTION SUCCESSFUL! 🎉              ║
╠══════════════════════════════════════════════════════════════╣
║  📊 Table:        {result['table_name']:<40} ║
║  📈 Rows inserted: {result['rows_inserted']:<39} ║
║  📋 Columns:      {len(result['columns']):<40} ║
║                                                              ║
║  Columns: {', '.join(result['columns']):<48} ║
╚══════════════════════════════════════════════════════════════╝
"""
        click.echo(click.style(success_box, fg='green', bold=True))
        print_info(f"Ready to query! Try: python3 cli.py preview -t {table}")
    else:
        print_error(f"Ingestion failed: {result['error']}")
        sys.exit(1)

@cli.command()
@click.option('--host', '-h', default=None, 
              help=f'Host to bind the server (default: {Config.SERVER_HOST})')
@click.option('--port', '-p', default=None, type=int,
              help=f'Port to bind the server (default: {Config.SERVER_PORT})')
@click.option('--reload', is_flag=True, 
              help='Enable auto-reload for development')
def serve(host, port, reload):
    """Start the GraphQL API server."""
    host = host or Config.SERVER_HOST
    port = port or Config.SERVER_PORT
    
    print_banner()
    print_divider()
    
    # Test database connection first
    if not db_manager.create_database_if_not_exists():
        print_error("Database connection failed!")
        sys.exit(1)
    
    click.echo(click.style("🚀 Starting GraphQL API server...", fg='cyan', bold=True))
    print_divider()
    
    # Server info box
    server_info = f"""
╔════════════════════════════════════════════════════════════════════╗
║                         🍓 SERVER READY 🍓                        ║
╠════════════════════════════════════════════════════════════════════╣
║  🌐 Server URL:      http://{host}:{port:<30} ║
║  🔍 GraphQL Playground: http://{host}:{port}/graphql{' ' * 19} ║
║  📊 API Docs:        http://{host}:{port}/docs{' ' * 23} ║
║                                                                    ║
║  💡 Try some queries:                                              ║
║     • List tables:     {{ tables {{ name }} }}                    ║
║     • Get table data:  {{ tableData(tableName: "employees") }}    ║
║                                                                    ║
║  🛑 Press Ctrl+C to stop the server                               ║
╚════════════════════════════════════════════════════════════════════╝
"""
    click.echo(click.style(server_info, fg='green'))
    
    try:
        start_server(host=host, port=port, reload=reload)
    except KeyboardInterrupt:
        print_divider()
        click.echo(click.style("\n👋 Server stopped gracefully", fg='yellow', bold=True))
        print_divider()

@cli.command()
def tables():
    """List all tables in the database."""
    click.echo("📋 Database Tables:")
    
    # Test database connection first
    if not db_manager.create_database_if_not_exists():
        click.echo("❌ Database connection failed!")
        sys.exit(1)
    
    tables_list = db_manager.get_tables()
    
    if not tables_list:
        click.echo("📭 No tables found in the database")
        return
    
    for table in tables_list:
        click.echo(f"\n🔧 Table: {table['name']}")
        click.echo("   Columns:")
        for col in table['columns']:
            nullable = "NULL" if col['nullable'] else "NOT NULL"
            click.echo(f"     • {col['name']} ({col['type']}) {nullable}")

@cli.command()
@click.option('--table', '-t', required=True, help='Table name to query')
@click.option('--limit', '-l', default=10, help='Number of rows to display')
def preview(table, limit):
    """Preview data from a table."""
    click.echo(f"👀 Previewing table: {table} (limit: {limit})")
    
    # Test database connection first
    if not db_manager.create_database_if_not_exists():
        click.echo("❌ Database connection failed!")
        sys.exit(1)
    
    result = db_manager.get_table_data(table, limit=limit)
    
    if result["success"]:
        click.echo(f"📊 Total rows: {result['total']}")
        click.echo(f"📄 Showing {len(result['data'])} rows:")
        
        if result['data']:
            # Display data in a simple table format
            data = result['data']
            headers = list(data[0].keys()) if data else []
            
            # Print headers
            click.echo("\n" + " | ".join(f"{h:<15}" for h in headers))
            click.echo("-" * (len(headers) * 17))
            
            # Print rows
            for row in data:
                values = [str(row.get(h, ""))[:15] for h in headers]
                click.echo(" | ".join(f"{v:<15}" for v in values))
        else:
            click.echo("📭 No data found")
    else:
        click.echo(f"❌ Error: {result['error']}")

@cli.command()
def config_info():
    """Display current configuration."""
    click.echo("⚙️  Current Configuration:")
    click.echo(f"🗄️  Database URL: {Config.DATABASE_URL}")
    click.echo(f"🌐 Server Host: {Config.SERVER_HOST}")
    click.echo(f"🔌 Server Port: {Config.SERVER_PORT}")
    click.echo(f"🐛 Debug Mode: {Config.DEBUG}")

if __name__ == '__main__':
    cli() 