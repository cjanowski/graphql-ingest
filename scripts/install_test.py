#!/usr/bin/env python3
"""
Installation Test Script for CSV GraphQL CLI

This script demonstrates all the CLI entry points created by the improved setup.py
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and show the result."""
    print(f"\n🔍 Testing: {description}")
    print(f"Command: {cmd}")
    print("─" * 50)

    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            print("✅ SUCCESS")
            if result.stdout:
                print(
                    result.stdout[:200] + "..."
                    if len(result.stdout) > 200
                    else result.stdout
                )
        else:
            print("❌ FAILED")
            print(result.stderr[:200] if result.stderr else "No error message")
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT (expected for some commands)")
    except Exception as e:
        print(f"💥 ERROR: {e}")


def main():
    """Test all CLI entry points."""
    print(
        """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     🧪 CLI ENTRY POINTS TEST 🧪                              ║
║                                                                               ║
║  This script tests all the awesome CLI entry points from setup.py            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    )

    # Test commands (most will show help since they're not installed yet)
    test_commands = [
        ("csv-graphql --help", "Main CLI command"),
        ("csvgql --help", "Short alias"),
        ("csv-ingest --help", "Direct ingest command"),
        ("csv-serve --help", "Direct serve command"),
        ("csv-preview --help", "Direct preview command"),
        ("csv-tables --help", "Direct tables command"),
        ("python3 setup.py --help", "Setup.py help"),
        ("python3 setup.py check", "Setup.py validation"),
    ]

    for cmd, desc in test_commands:
        run_command(cmd, desc)

    print(
        f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           📦 INSTALLATION GUIDE 📦                           ║
║                                                                               ║
║  To install this package and get all these awesome CLI commands:             ║
║                                                                               ║
║  🔧 Development install:   pip install -e .                                  ║
║  🔧 With dev tools:        pip install -e .[dev]                             ║
║  🔧 Production install:    pip install .                                     ║
║  🔧 From PyPI (future):    pip install csv-graphql-cli                       ║
║                                                                               ║
║  After installation, you can use ANY of these commands:                      ║
║  • csv-graphql           (main command)                                      ║
║  • csvgql                (short alias)                                       ║
║  • csv-ingest            (direct ingestion)                                  ║
║  • csv-serve             (direct server)                                     ║
║  • csv-preview           (direct preview)                                    ║
║  • csv-tables            (direct table listing)                              ║
║  • csvgql-dev            (development server)                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    )


if __name__ == "__main__":
    main()
